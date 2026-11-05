#!/usr/bin/env python3
"""Reels: 'Bir kağıdı 42 kez katla' - 1080x1920, 30 fps."""
import math, os, random, subprocess, sys
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
BOLD = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
MED = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"
INK = (14, 19, 48); NAVY2 = (28, 36, 84); CREAM = (246, 239, 217); CREAM2 = (226, 217, 190)
YEL = (255, 197, 61); CORAL = (232, 72, 60); WHITE = (255, 255, 255); LINE = (196, 186, 156)

SCENES = [("s1", 0.0, 4.5), ("s2", 4.5, 9.0), ("s3", 9.0, 24.0), ("s4", 24.0, 28.5), ("s5", 28.5, 33.5)]
XF = 0.25
DUR = SCENES[-1][2]

# climb keyframes: local time, fold
KF = [(0, 5), (1.0, 11), (2.0, 11), (2.7, 15), (3.7, 15), (5.0, 23), (6.2, 23), (6.9, 27), (8.0, 27),
      (8.7, 32), (9.8, 32), (11.6, 42), (15.0, 42)]
FOLDS_S1 = [("y", .25), ("x", .95), ("y", 1.65)]
DOUBLES_S2 = [.7 + .65 * i for i in range(5)]
COUNT_S4 = (.75, 2.3)
warnings = set()

clamp = lambda v, a=0., b=1.: max(a, min(b, v))
def ease(p):
    p = clamp(p); return p * p * (3 - 2 * p)
def eout(p):
    p = clamp(p); return 1 - (1 - p) ** 3
def back(p):
    p = clamp(p); c = 1.70158; return 1 + (c + 1) * (p - 1) ** 3 + c * (p - 1) ** 2
mix = lambda a, b, p: tuple(int(round(x + (y - x) * p)) for x, y in zip(a, b))

def fold_at(t):
    for (a, fa), (b, fb) in zip(KF, KF[1:]):
        if t <= b:
            return fa if fa == fb else fa + (fb - fa) * ease((t - a) / (b - a))
    return KF[-1][1]

def fmt(meters):
    def num(v, d=0):
        s = f"{v:,.{d}f}"
        return s.replace(",", "X").replace(".", ",").replace("X", ".")
    if meters < .01: return num(meters * 1000, 1) + " mm"
    if meters < 1: return num(meters * 100, 1) + " cm"
    if meters < 10: return num(meters, 1) + " m"
    if meters < 1000: return num(meters) + " m"
    km = meters / 1000
    if km < 100: return num(km, 1) + " km"
    return num(km) + " km"

@lru_cache(None)
def font(path, size): return ImageFont.truetype(path, size)

@lru_cache(4096)
def text_mask(s, size, path):
    f = font(path, size); b = f.getbbox(s); pad = 8
    m = Image.new("L", (b[2] - b[0] + 2 * pad, b[3] - b[1] + 2 * pad), 0)
    ImageDraw.Draw(m).text((pad - b[0], pad - b[1]), s, font=f, fill=255)
    return m

def T(img, s, x, y, size, color=WHITE, path=BOLD, a=1., scale=1.):
    """Text centered on (x, y)."""
    if a <= 0: return
    m = text_mask(s, size, path)
    if scale != 1:
        m = m.resize((max(1, int(m.width * scale)), max(1, int(m.height * scale))), Image.BILINEAR)
    if a < 1: m = m.point(lambda v: int(v * a))
    px, py = int(x - m.width / 2), int(y - m.height / 2)
    if scale >= 1 and a >= 1 and (px < 60 or px + m.width > W - 60): warnings.add((s, px, px + m.width))
    img.paste(color, (px, py), m)

def _ss(img, box, drawer, color, a):
    x0, y0, x1, y1 = [int(v) for v in box]
    x0, y0 = max(x0 - 2, -40), max(y0 - 2, -40); x1, y1 = min(x1 + 3, W + 40), min(y1 + 3, H + 40)
    if x1 <= x0 or y1 <= y0: return
    S = 3; m = Image.new("L", ((x1 - x0) * S, (y1 - y0) * S), 0)
    drawer(ImageDraw.Draw(m), lambda v, o: (v - o) * S, x0, y0)
    m = m.reduce(S)
    if a < 1: m = m.point(lambda v: int(v * a))
    img.paste(color, (x0, y0), m)

def poly(img, pts, color, a=1.):
    xs, ys = zip(*pts)
    _ss(img, (min(xs), min(ys), max(xs), max(ys)),
        lambda d, f, x0, y0: d.polygon([(f(x, x0), f(y, y0)) for x, y in pts], fill=255), color, a)

def circle(img, cx, cy, r, color, a=1.):
    _ss(img, (cx - r, cy - r, cx + r, cy + r),
        lambda d, f, x0, y0: d.ellipse([f(cx - r, x0), f(cy - r, y0), f(cx + r, x0), f(cy + r, y0)], fill=255), color, a)

def rrect(img, x0, y0, x1, y1, r, color, a=1.):
    _ss(img, (x0, y0, x1, y1),
        lambda d, f, ox, oy: d.rounded_rectangle([f(x0, ox), f(y0, oy), f(x1, ox), f(y1, oy)], r * 3, fill=255), color, a)

def grad(top, bot):
    r = np.linspace(0, 1, H)[:, None]
    a = (np.array(top)[None] * (1 - r) + np.array(bot)[None] * r).astype(np.uint8)
    return Image.fromarray(a[:, None, :], "RGB").resize((W, H), Image.NEAREST)

rng = random.Random(42)
STARS = [(rng.randrange(W), rng.randrange(H), rng.choice([1, 1, 2, 2, 3]), rng.random() * 6.28) for _ in range(170)]
def stars(img, t, alpha=1., shift=0.):
    if alpha <= 0: return
    d = ImageDraw.Draw(img)
    for x, y, r, ph in STARS:
        b = (.55 + .45 * math.sin(t * 2 + ph)) * alpha
        px = img.getpixel((x, int((y + shift) % H)))
        c = mix(px, WHITE, b)
        yy = (y + shift) % H
        d.ellipse([x - r, yy - r, x + r, yy + r], fill=c)

def moon(img, cx, cy, r):
    if r < 2: return
    circle(img, cx, cy, r + 22, WHITE, .10)
    circle(img, cx, cy, r, (235, 232, 220))
    for dx, dy, cr in [(-.35, -.3, .2), (.32, -.42, .12), (.08, .1, .28), (-.48, .36, .13), (.5, .32, .16), (-.1, -.62, .08)]:
        circle(img, cx + dx * r, cy + dy * r, cr * r, (204, 200, 186))

# ---------- Scene 1 ----------
def paper_fold(img, cx, cy, w, h, axis, p, layers):
    th = math.pi * ease(p)
    c, s = math.cos(th), math.sin(th)
    def tr(u, v):  # u along hinge, v perpendicular
        return (cx + u, cy + v) if axis == "y" else (cx + v, cy + u)
    span, wide = (h, w) if axis == "y" else (w, h)
    hinge = -span / 4 * ease(p)
    for i in range(layers, 0, -1):
        o = i * 5
        poly(img, [tr(-wide/2 + o, hinge + o), tr(wide/2 + o, hinge + o), tr(wide/2 + o, hinge + span/2 + o), tr(-wide/2 + o, hinge + span/2 + o)], CREAM2)
    poly(img, [tr(-wide/2, hinge), tr(wide/2, hinge), tr(wide/2, hinge + span/2), tr(-wide/2, hinge + span/2)], CREAM)
    free = hinge - span / 2 * c
    flare = 28 * s
    poly(img, [tr(-wide/2, hinge), tr(wide/2, hinge), tr(wide/2 + flare, free), tr(-wide/2 - flare, free)], CREAM if c > 0 else mix(CREAM, CREAM2, .55))

def scene1(t):
    img = grad(INK, NAVY2); stars(img, t)
    w, h = 560., 760.; cy = 1000.; layers = 0; drawn = False
    if t > 2.25: cy += (1465 - 1000) * eout((t - 2.25) / .4)
    for ax, st in FOLDS_S1:
        if t < st:
            break
        if t < st + .6:
            paper_fold(img, 540, cy, w, h, ax, (t - st) / .6, layers); drawn = True; break
        if ax == "y": h /= 2
        else: w /= 2
        layers = layers * 2 + 1
    if not drawn:
        for i in range(min(layers, 5), 0, -1):
            o = i * 5; poly(img, [(540-w/2+o, cy-h/2+o), (540+w/2+o, cy-h/2+o), (540+w/2+o, cy+h/2+o), (540-w/2+o, cy+h/2+o)], CREAM2)
        poly(img, [(540-w/2, cy-h/2), (540+w/2, cy-h/2), (540+w/2, cy+h/2), (540-w/2, cy+h/2)], CREAM)
    if t > 2.45: moon(img, 540, 840, 250 * back((t - 2.45) / .4))
    T(img, "Bir kâğıdı", 540, 270, 92)
    T(img, "42 kez katla", 540, 400, 128, YEL)
    if t > 2.75:
        T(img, "Ay'a ulaşır!", 540, 1240, 132, WHITE, scale=back((t - 2.75) / .3))
    return img

# ---------- Scene 2 ----------
def scene2(t):
    img = grad(NAVY2, (38, 48, 108))
    T(img, "Bir kâğıt sadece", 540, 270, 66)
    T(img, "0,1 mm", 540, 410, 172, YEL, scale=back(t / .35))
    n, last = 1, None
    for i, d in enumerate(DOUBLES_S2):
        if t >= d: n = 2 ** (i + 1); last = d
    prev = n // 2 if last is not None else 1
    p = eout((t - last) / .3) if last is not None else 1
    stack_h = (prev + (n - prev) * p) * 14
    base = 1320; x0, x1 = 240, 840
    top = base - stack_h
    img.paste(CREAM, (x0, int(top), x1, base))
    d = ImageDraw.Draw(img)
    if n > 1:
        for i in range(1, n):
            y = base - stack_h * i / n
            d.line([(x0, y), (x1, y)], fill=LINE, width=2)
    T(img, f"{n} kat", 540, top - 62, 72, WHITE)
    if last is not None and t - last < .5:
        T(img, "×2", 925, top + 15, 70, YEL, scale=back((t - last) / .18), a=1 - clamp((t - last - .3) / .2))
    T(img, "Her katlamada kalınlık", 540, 1440, 60)
    T(img, "2 katına çıkar", 540, 1525, 76, YEL)
    return img

# ---------- Scene 3 ----------
TOP, PX = 880, 260
L = lambda meters: math.log2(meters / 1e-4)
MARKS = [
    (11, L(.15), "Telefon", "≈15 cm", "Telefonunu geçti"),
    (15, L(1.75), "İnsan", "≈1,75 m", "Bir insanı geçti"),
    (23, L(828), "Burj Khalifa", "828 m", "Burj Khalifa'yı geçti"),
    (27, L(8849), "Everest", "8.849 m", "Everest'i geçti"),
    (32, L(400e3), "Uzay İstasyonu", "≈400 km", "Uzay İstasyonu'nu geçti"),
    (42, L(384400e3), "Ay", "ort. 384.400 km", "AY'I DA GEÇTİ!"),
]
SKY = [(9, (44, 32, 92), (84, 60, 128)), (16, (32, 58, 128), (58, 100, 178)), (22, (24, 88, 170), (54, 138, 214)),
       (27, (16, 44, 112), (30, 84, 160)), (32, (6, 10, 34), (14, 24, 70)), (42, (4, 6, 22), (10, 14, 44))]

def sky(f):
    if f <= SKY[0][0]: return SKY[0][1:]
    for (a, t0, b0), (c, t1, b1) in zip(SKY, SKY[1:]):
        if f <= c:
            p = ease((f - a) / (c - a)); return mix(t0, t1, p), mix(b0, b1, p)
    return SKY[-1][1:]

def icon(img, kind, cx, y):
    dk = (16, 22, 58)
    if kind == "Telefon":
        rrect(img, cx - 75, y, cx + 75, y + 250, 26, dk); rrect(img, cx - 62, y + 16, cx + 62, y + 234, 12, (110, 190, 240))
    elif kind == "İnsan":
        circle(img, cx, y + 42, 42, CREAM); rrect(img, cx - 58, y + 96, cx + 58, y + 250, 42, CORAL)
    elif kind == "Burj Khalifa":
        c = (232, 238, 248)
        poly(img, [(cx - 4, y), (cx + 4, y), (cx + 12, y + 80), (cx + 26, y + 150), (cx + 42, y + 250), (cx - 42, y + 250), (cx - 26, y + 150), (cx - 12, y + 80)], c)
        poly(img, [(cx - 4, y), (cx, y), (cx, y + 250), (cx - 42, y + 250), (cx - 26, y + 150), (cx - 12, y + 80)], (190, 202, 224))
    elif kind == "Everest":
        poly(img, [(cx, y), (cx + 190, y + 250), (cx - 190, y + 250)], (62, 74, 112))
        poly(img, [(cx, y), (cx + 62, y + 82), (cx + 24, y + 66), (cx - 4, y + 92), (cx - 30, y + 62), (cx - 62, y + 82)], WHITE)
    elif kind == "Uzay İstasyonu":
        rrect(img, cx - 62, y + 96, cx + 62, y + 142, 14, (216, 220, 228))
        for sx in (-1, 1):
            poly(img, [(cx + sx * 70, y + 40), (cx + sx * 180, y + 40), (cx + sx * 180, y + 200), (cx + sx * 70, y + 200)], (44, 104, 190))
            for k in (1, 2):
                img.paste((120, 170, 235), (min(cx + sx * 70, cx + sx * 180), y + 40 + k * 53, max(cx + sx * 70, cx + sx * 180), y + 43 + k * 53))
        rrect(img, cx - 76, y + 112, cx + 76, y + 126, 6, (160, 168, 182))

def scene3(t):
    f = fold_at(t); top, bot = sky(f); img = grad(top, bot)
    n = int(f + 1e-6); meters = 1e-4 * 2 ** n
    vel = (fold_at(t + .03) - fold_at(t - .03)) / .06
    stars(img, t, ease((f - 25) / 7), shift=f * 34)
    # clouds
    for lv, cx, s in [(18.2, 760, 1.0), (21.0, 850, .8), (24.4, 860, 1.0)]:
        y = TOP + (f - lv) * PX
        if -150 < y < H + 150:
            for dx, dy, r in [(-85, 12, 52), (0, -8, 76), (88, 14, 54)]:
                circle(img, cx + dx * s, y + dy * s, r * s, (226, 236, 248))
    # speed lines
    if vel > 2:
        d = ImageDraw.Draw(img)
        rs = random.Random(int(t * FPS))
        for _ in range(int(min(vel, 8) * 2)):
            x, y, ln = rs.randrange(420, 1000), rs.randrange(500, 1800), rs.randrange(70, 240)
            c = mix(bot, WHITE, .28); d.line([(x, y), (x, y + ln)], fill=c, width=3)
    # column
    x0, x1 = 120, 330
    img.paste(CREAM, (x0, TOP, x1, H))
    d = ImageDraw.Draw(img)
    off = (f * PX) % 32
    y = TOP + off
    while y < H:
        d.line([(x0, y), (x1, y)], fill=LINE, width=2); y += 32
    img.paste(YEL, (x0 - 8, TOP - 8, x1 + 8, TOP + 8))
    # landmarks
    for reach, lv, name, hgt, banner in MARKS:
        y = TOP + (f - lv) * PX
        if y < -420 or y > H + 20: continue
        ix = 690
        for dx in range(345, 500, 34):
            d.line([(dx, y), (dx + 18, y)], fill=WHITE, width=3)
        if name == "Ay":
            moon(img, ix, y + 225, 225)
            T(img, hgt, ix, y + 500, 44, WHITE, MED)
        else:
            icon(img, name, ix, int(y))
            T(img, name, ix, y + 292, 46, WHITE)
            T(img, hgt, ix, y + 345, 40, WHITE, MED)
    # HUD
    rrect(img, 90, 230, 990, 470, 36, (8, 10, 30), .95)
    T(img, f"{n}. KATLAMA", 540, 288, 50, YEL)
    T(img, fmt(meters), 540, 385, 116 if meters < 1e8 else 112, WHITE)
    # banner
    for i, (reach, lv, name, hgt, banner) in enumerate(MARKS):
        hold_start = next(a for a, fa in KF if fa == reach)
        hold_end = max(a for a, fa in KF if fa == reach)
        if hold_start <= t <= hold_end + .02:
            age = t - hold_start
            s = back(age / .22)
            c = YEL if name != "Ay" else CORAL
            tc = INK if name != "Ay" else WHITE
            sz = 60 if name != "Ay" else 76
            tw = text_mask(banner, sz, BOLD).width
            hw = (tw / 2 + 46) * s; hh = (sz * .95) * s
            rrect(img, 540 - hw, 570 - hh, 540 + hw, 570 + hh, hh, c)
            T(img, banner, 540, 570, sz, tc, scale=s)
    return img

# ---------- Scene 4 ----------
def scene4(t):
    img = Image.new("RGB", (W, H), CREAM)
    T(img, "Peki gerçekte?", 540, 285, 104, INK, scale=back(t / .3))
    k = 1 + int(11 * ease((t - COUNT_S4[0]) / (COUNT_S4[1] - COUNT_S4[0])))
    T(img, str(k), 540, 610, 300, CORAL)
    T(img, "katlama", 540, 810, 72, INK)
    # 1.2 km strip growing
    p = eout((t - .9) / 1.5)
    x0, x1 = 130, 130 + 820 * p
    img.paste(INK, (x0, 980, int(x1), 1006))
    T(img, "1,2 km", 540, 1065, 72, CORAL, a=clamp((t - 1.8) / .3))
    T(img, "uzunluğunda kâğıt gerekti", 540, 1145, 56, INK, a=clamp((t - 1.8) / .3))
    a = clamp((t - 2.7) / .3)
    if a > 0:
        rrect(img, 110, 1270, 970, 1490, 36, INK, a)
        T(img, "42 katlama sadece", 540, 1335, 62, WHITE, a=a)
        T(img, "matematikte mümkün", 540, 1425, 62, YEL, a=a)
    return img

# ---------- Scene 5 ----------
def scene5(t):
    img = grad(INK, NAVY2); stars(img, t)
    T(img, "Üstel büyüme", 540, 275, 110, YEL)
    T(img, "işte böyle bir şey", 540, 395, 70)
    x0, x1, y0, y1 = 150, 930, 1130, 510
    d = ImageDraw.Draw(img)
    d.line([(x0, y1), (x0, y0), (x1 + 15, y0)], fill=(110, 120, 170), width=5)
    p = ease(t / 2.0)
    pts = []
    for i in range(int(180 * p) + 1):
        u = i / 180
        v = (2 ** (u * 12) - 1) / (2 ** 12 - 1)
        pts.append((x0 + (x1 - x0) * u, y0 + (y1 - y0) * v))
    if len(pts) > 1:
        d.line(pts, fill=YEL, width=12, joint="curve")
        cx, cy = pts[-1]; circle(img, cx, cy, 20, WHITE)
    T(img, "kat sayısı", 540, 1178, 42, (190, 196, 225), MED)
    a = clamp((t - 1.5) / .35)
    T(img, "103 katlamada", 540, 1290, 64, YEL, a=a)
    T(img, "gözlemlenebilir evreni aşar", 540, 1375, 58, WHITE, a=a)
    if t > 2.8:
        s = back((t - 2.8) / .28)
        pl = 1 + .025 * math.sin((t - 3) * 5) if t > 3.2 else 1
        hw, hh = 430 * s * pl, 72 * s * pl
        rrect(img, 540 - hw, 1515 - hh, 540 + hw, 1515 + hh, hh, YEL)
        T(img, "Bunu bilmeyen birine gönder", 540, 1515, 50, INK, scale=s * pl)
    return img

FUNCS = {"s1": scene1, "s2": scene2, "s3": scene3, "s4": scene4, "s5": scene5}

def frame(T_):
    for i, (name, a, b) in enumerate(SCENES):
        if T_ < b or i == len(SCENES) - 1:
            im = FUNCS[name](T_ - a)
            if i and T_ - a < XF:
                pname, pa, _ = SCENES[i - 1]
                im = Image.blend(FUNCS[pname](T_ - pa), im, ease((T_ - a) / XF))
            return im

def render_scene(name):
    _, a, b = next(s for s in SCENES if s[0] == name)
    tmp, out = f"parts/{name}.tmp.mp4", f"parts/{name}.mp4"
    n0, n1 = round(a * FPS), round(b * FPS)
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "18", "-preset", "veryfast",
                          "-pix_fmt", "yuv420p", tmp], stdin=subprocess.PIPE)
    for i in range(n0, n1):
        p.stdin.write(frame(i / FPS).tobytes())
    p.stdin.close()
    if p.wait() == 0:
        os.replace(tmp, out); print("done", name, flush=True)
    else:
        sys.exit(1)

if __name__ == "__main__":
    if sys.argv[1] == "still":
        os.makedirs("stills", exist_ok=True)
        for t in map(float, sys.argv[2:]):
            frame(t).save(f"stills/t{t:05.2f}.jpg", quality=88)
        print("warnings", warnings)
    else:
        os.makedirs("parts", exist_ok=True)
        render_scene(sys.argv[2])
        if warnings: print("warnings", warnings)
