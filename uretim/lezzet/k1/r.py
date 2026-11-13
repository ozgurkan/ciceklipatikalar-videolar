#!/usr/bin/env python3
import os; os.chdir('/home/claude/lezzet/k1')
_h = open('/home/claude/lezzet/f1/r.py').read().split('# ---------- sahneler')[0].replace("os.chdir('/home/claude/lezzet/f1')", "")
exec(_h)
from PIL import ImageFilter, ImageChops
SER = "Trakya Lezzet Rotası · Ek Bölüm"
LUL = P['lul']; SS_ = art.SS
DARKG = (28, 82, 44); LIGHTG = (112, 166, 78); FLESH = (226, 54, 60)
ROWS = [("Çeşmekolu", "Lüleburgaz · Kırklareli", RUST), ("Kavakdere", "Kırklareli · 1970'lerden beri", GREEN), ("Erikleryurdu", "Babaeski · kumlu toprak", CLAY), ("Üsküpdere", "Kırklareli · kışın da tezgâhta", DKBLUE), ("Marmaraereğlisi", "Tekirdağ · karpuz festivali", GOLD)]

# ---------- ışık ve doku ----------
def sphere(im, cx, cy, rx, ry, amb=.55, dif=.62, spec=.5):
    a = np.asarray(im).astype(np.float32); h, w = a.shape[:2]; y, x = np.mgrid[0:h, 0:w]
    nx, ny = (x - cx) / rx, (y - cy) / ry; r2 = np.clip(nx * nx + ny * ny, 0, 1); nz = np.sqrt(1 - r2)
    l = np.array([-.45, -.6, .66]); l /= np.linalg.norm(l); d = np.clip(nx * l[0] + ny * l[1] + nz * l[2], 0, 1)
    sh = amb + dif * d; sp = np.clip(d, 0, 1) ** 26 * spec * 255
    a[..., :3] = np.clip(a[..., :3] * sh[..., None] + sp[..., None], 0, 255)
    return Image.fromarray(a.astype(np.uint8), 'RGBA')
@lru_cache(None)
def melon(w=420):
    h = int(w * .84); c = C(w + 28, h + 28); o = 14
    m = c.fill(lambda d: d.ellipse(S(o, o, o + w, o + h), fill=255), LIGHTG, top=1., bot=1., noise=6, ink=0)
    rs = random.Random(w + 3)
    def stripes(d):
        n = 8
        for i in range(n):
            x0 = o + w * (i + .5) / n; bow = (i - (n - 1) / 2) / ((n - 1) / 2) * w * .2; L, R = [], []
            for j in range(41):
                u = j / 40; y = o + h * u; cx = x0 + bow * math.sin(u * math.pi) * .9; hw = w * .034 * (.55 + .7 * math.sin(u * math.pi))
                jag = w * .022; L.append((cx - hw - rs.uniform(0, jag) * (1 if j % 2 else .2), y)); R.append((cx + hw + rs.uniform(0, jag) * (1 if j % 2 == 0 else .2), y))
            d.polygon(SP(L + R[::-1]), fill=DARKG + (255,))
            for j in range(6):
                u = rs.uniform(.1, .9); y = o + h * u; cx = x0 + bow * math.sin(u * math.pi) * .9 + rs.choice([-1, 1]) * w * .07; r = w * rs.uniform(.008, .016)
                d.ellipse(S(cx - r, y - r * 2.4, cx + r, y + r * 2.4), fill=DARKG + (210,))
    c.over(stripes, m)
    im = c.done(); im = sphere(im, im.width / 2, im.height / 2, w / 2, h / 2)
    ring = Image.new('L', im.size, 0); ImageDraw.Draw(ring).ellipse([o - 2, o - 2, o + w + 2, o + h + 2], outline=255, width=4)
    edge = Image.new('RGBA', im.size, (24, 54, 30, 0)); edge.putalpha(ring.filter(ImageFilter.GaussianBlur(.8))); im.alpha_composite(edge)
    d = ImageDraw.Draw(im); d.line([(im.width / 2, o + 3), (im.width / 2 + w * .05, o - 9)], fill=(96, 74, 36), width=max(3, w // 60))
    return im
@lru_cache(None)
def half(w=420):
    n = w + 28; o = 14; c = C(n, n)
    c.fill(lambda d: d.ellipse(S(o, o, o + w, o + w), fill=255), DARKG, top=1.2, bot=.75, ink=0)
    c.over(lambda d: d.ellipse(S(o + w * .028, o + w * .028, o + w * .972, o + w * .972), fill=(168, 206, 120, 255)))
    c.over(lambda d: d.ellipse(S(o + w * .05, o + w * .05, o + w * .95, o + w * .95), fill=(236, 244, 208, 255)))
    im = c.done(); a = np.asarray(im).astype(np.float32); y, x = np.mgrid[0:n, 0:n]; r = np.sqrt((x - n / 2) ** 2 + (y - n / 2) ** 2) / (w / 2)
    rng = np.random.default_rng(4); grain = rng.normal(0, 7, (n, n))
    inner = np.clip((.885 - r) / .045, 0, 1); t_ = np.clip(r / .86, 0, 1)
    col = np.stack([238 - 22 * t_ ** 2, 78 - 34 * t_ ** 1.5, 84 - 30 * t_ ** 1.5], -1) + grain[..., None]
    fade = np.clip((r - .74) / .14, 0, 1)[..., None]; col = col * (1 - fade * .55) + np.array([250, 196, 190]) * fade * .55
    a[..., :3] = a[..., :3] * (1 - inner[..., None]) + np.clip(col, 0, 255) * inner[..., None]
    im = Image.fromarray(a.astype(np.uint8), 'RGBA'); big = Image.new('RGBA', (n * 3, n * 3), (0, 0, 0, 0)); d = ImageDraw.Draw(big); rs = random.Random(8)
    for ring_r, cnt, ph in ((.3, 7, .2), (.52, 12, .5)):
        for i in range(cnt):
            an = (i + ph + rs.uniform(-.18, .18)) / cnt * 2 * math.pi; rr = (ring_r + rs.uniform(-.03, .03)) * w / 2; x0, y0 = (n / 2 + math.cos(an) * rr) * 3, (n / 2 + math.sin(an) * rr) * 3; s_ = w * .03 * 3
            tip = (x0 - math.cos(an) * s_ * 1.5, y0 - math.sin(an) * s_ * 1.5); px, py = -math.sin(an), math.cos(an)
            d.polygon([tip, (x0 + px * s_ * .62, y0 + py * s_ * .62), (x0 - px * s_ * .62, y0 - py * s_ * .62)], fill=(38, 22, 18, 255)); d.ellipse([x0 - s_ * .64, y0 - s_ * .64, x0 + s_ * .64, y0 + s_ * .64], fill=(38, 22, 18, 255))
            d.ellipse([x0 - s_ * .3, y0 - s_ * .42, x0 + s_ * .02, y0 - s_ * .1], fill=(120, 96, 88, 255))
    im.alpha_composite(big.resize((n, n), Image.LANCZOS))
    gl = Image.new('L', (n, n), 0); ImageDraw.Draw(gl).ellipse([n * .22, n * .16, n * .56, n * .34], fill=70); glo = Image.new('RGBA', (n, n), (255, 255, 255, 0)); glo.putalpha(gl.filter(ImageFilter.GaussianBlur(w * .03))); im.alpha_composite(glo)
    ring = Image.new('L', (n, n), 0); ImageDraw.Draw(ring).ellipse([o - 1, o - 1, o + w + 1, o + w + 1], outline=255, width=3); e = Image.new('RGBA', (n, n), (24, 54, 30, 0)); e.putalpha(ring); im.alpha_composite(e)
    return im
@lru_cache(None)
def slice_(w=300):
    hf = half(w * 2); n = hf.width; im = hf.crop((0, n // 2, n, n)).resize((w + 14, (w + 14) // 2), Image.LANCZOS); return im
@lru_cache(None)
def star(r=40, col=(255, 226, 120)):
    c = C(2 * r + 8, 2 * r + 8); cx = cy = r + 4
    pts = []
    for i in range(8):
        a = i * math.pi / 4; rr = r if i % 2 == 0 else r * .26; pts.append((cx + math.cos(a) * rr, cy + math.sin(a) * rr))
    c.fill(lambda d: d.polygon(SP(pts), fill=255), col, top=1.1, bot=.95, ink=0); return c.done()
@lru_cache(None)
def dropr(r=14, col=(226, 54, 60)):
    c = C(2 * r + 8, 3 * r + 8); o = 4
    c.fill(lambda d: (d.ellipse(S(o, o + r, o + 2 * r, o + 3 * r), fill=255), d.polygon(SP([(o + r, o), (o + 1.9 * r, o + 1.6 * r), (o + .1 * r, o + 1.6 * r)]), fill=255)), col, top=1.25, bot=.85, ink=0); return c.done()
@lru_cache(None)
def coin(w=110):
    c = C(w + 16, w + 16); o = 8
    c.fill(lambda d: d.ellipse(S(o, o, o + w, o + w), fill=255), (222, 166, 52), top=1.25, bot=.78, ink=2.5)
    c.over(lambda d: d.ellipse(S(o + w * .12, o + w * .12, o + w * .88, o + w * .88), outline=(150, 100, 24, 255), width=3 * SS_))
    im = c.done(); T(im, "TL", im.width / 2, im.height / 2 - 1, int(w * .36), (110, 70, 14), M.BOLD); return im
@lru_cache(None)
def scenery(w=872, h=500):
    a = np.zeros((h, w, 3), np.float32); t = np.linspace(0, 1, h)[:, None, None]
    a[:] = np.array([170, 208, 226]) * (1 - t) + np.array([250, 236, 200]) * t; im = Image.fromarray(a.astype(np.uint8)).convert('RGBA')
    c = C(w, h)
    c.fill(lambda d: d.ellipse(S(-200, 250, 520, 620), fill=255), (126, 158, 96), top=1.1, bot=.9, ink=0)
    c.fill(lambda d: d.ellipse(S(380, 270, 1100, 640), fill=255), (104, 142, 82), top=1.1, bot=.9, ink=0)
    c.fill(lambda d: d.rectangle(S(0, 340, w, h), fill=255), (150, 172, 92), top=1.08, bot=.86, ink=0)
    def rows(d):
        for i in range(9):
            y = 350 + i * i * 1.3 + i * 3; d.line(S(0, y, w, y + 4), fill=(110, 138, 70, 160), width=int((1.5 + i * .4) * SS_))
        rs = random.Random(3)
        for i in range(26):
            x, y = rs.uniform(0, w), rs.uniform(356, 400); r = rs.uniform(5, 9); d.ellipse(S(x - r, y - r * .8, x + r, y + r * .8), fill=DARKG + (255,))
    c.over(rows)
    c.fill(lambda d: d.rectangle(S(0, 408, w, 492), fill=255), (112, 104, 98), top=1.1, bot=.86, ink=0)
    c.over(lambda d: (d.line(S(0, 408, w, 408), fill=INK + (255,), width=3 * SS_), d.line(S(0, 492, w, 492), fill=INK + (255,), width=3 * SS_)))
    im.alpha_composite(c.done()); return im.convert('RGB')
@lru_cache(None)
def truck():
    c = C(520, 300)
    c.fill(lambda d: d.rounded_rectangle(S(20, 120, 362, 230), 10 * SS_, fill=255), (186, 134, 80), top=1.14, bot=.78, noise=4, ink=3)
    c.over(lambda d: [d.line(S(20 + x, 124, 20 + x, 228), fill=(120, 80, 44, 255), width=3 * SS_) for x in range(48, 340, 48)])
    c.over(lambda d: d.rectangle(S(22, 122, 360, 136), fill=(214, 168, 112, 255)))
    c.fill(lambda d: d.polygon(SP([(362, 230), (362, 92), (434, 92), (490, 156), (504, 230)]), fill=255), (176, 62, 40), top=1.3, bot=.74, ink=3)
    c.over(lambda d: d.polygon(SP([(382, 110), (428, 110), (464, 154), (382, 154)]), fill=(206, 230, 240, 255)))
    c.over(lambda d: d.polygon(SP([(392, 116), (410, 116), (396, 150), (384, 150)]), fill=(255, 255, 255, 120)))
    c.over(lambda d: d.ellipse(S(486, 186, 502, 204), fill=(255, 226, 130, 255)))
    c.fill(lambda d: d.rectangle(S(20, 226, 504, 246), fill=255), (64, 56, 54), top=1.1, bot=.8, ink=2)
    im = c.done(); rs = random.Random(1)
    for row, n in enumerate((6, 5, 4, 2)):
        for i in range(n):
            put(im, melon(80), 62 + row * 26 + i * 52 + rs.uniform(-3, 3), 114 - row * 32, rot=rs.uniform(-25, 25))
    return im
@lru_cache(None)
def wheel():
    c = C(88, 88); c.fill(lambda d: d.ellipse(S(6, 6, 82, 82), fill=255), (40, 36, 36), top=1.3, bot=.75, ink=2)
    c.over(lambda d: (d.ellipse(S(26, 26, 62, 62), fill=(180, 176, 170, 255)), d.line(S(44, 14, 44, 74), fill=(110, 106, 100, 255), width=4 * SS_), d.line(S(14, 44, 74, 44), fill=(110, 106, 100, 255), width=4 * SS_), d.ellipse(S(38, 38, 50, 50), fill=(70, 66, 62, 255)))); return c.done()
@lru_cache(None)
def basin(w=300, h=170):
    c = C(w + 16, h + 16)
    m = c.fill(lambda d: d.ellipse(S(8, 8, 8 + w, 8 + h), fill=255), (168, 128, 84), top=1.15, bot=.8, noise=9, ink=3)
    rs = random.Random(6)
    def cracks(d):
        for i in range(11):
            a = rs.uniform(0, 2 * math.pi); r0, r1 = rs.uniform(.25, .5), rs.uniform(.7, .95); x0, y0 = 8 + w / 2 + math.cos(a) * w / 2 * r0, 8 + h / 2 + math.sin(a) * h / 2 * r0; x1, y1 = 8 + w / 2 + math.cos(a + .2) * w / 2 * r1, 8 + h / 2 + math.sin(a + .2) * h / 2 * r1
            d.line(S(x0, y0, (x0 + x1) / 2 + rs.uniform(-12, 12), (y0 + y1) / 2 + rs.uniform(-8, 8), x1, y1), fill=(104, 70, 40, 255), width=int(2.4 * SS_), joint='curve')
    c.over(cracks, m); return c.done()
@lru_cache(None)
def pond(w=260, h=130):
    c = C(w + 12, h + 12); m = c.fill(lambda d: d.ellipse(S(6, 6, 6 + w, 6 + h), fill=255), (92, 160, 198), top=1.2, bot=.84, ink=2, inkc=(46, 96, 130))
    c.over(lambda d: (d.arc(S(40, 30, w - 60, h - 10), 190, 300, fill=(255, 255, 255, 150), width=4 * SS_), d.arc(S(90, 60, w - 20, h + 30), 200, 280, fill=(255, 255, 255, 90), width=3 * SS_)), m); return c.done()
@lru_cache(None)
def podium():
    c = C(760, 250)
    for x0, x1, top, col in ((20, 260, 100, (226, 212, 180)), (500, 740, 140, (214, 190, 150)), (260, 500, 20, (236, 196, 96))):
        c.fill(lambda d, x0=x0, x1=x1, top=top: d.rounded_rectangle(S(x0, top, x1, 240), 12 * SS_, fill=255), col, top=1.12, bot=.8, ink=3)
        c.over(lambda d, x0=x0, x1=x1, top=top: d.rectangle(S(x0 + 3, top + 3, x1 - 3, top + 16), fill=(255, 255, 255, 90)))
    im = c.done(); T(im, "1", 380, 150, 110, (120, 76, 14), LORA); T(im, "2", 140, 180, 76, (120, 100, 70), LORA); T(im, "3", 620, 196, 64, (120, 100, 70), LORA); return im

# ---------- ortak ----------
_vy, _vx = np.mgrid[0:H, 0:W]; _vr = np.sqrt(((_vx - W / 2) / (W * .78)) ** 2 + ((_vy - 960) / (H * .62)) ** 2)
VMASK = Image.fromarray((np.clip((_vr - .55) / .6, 0, 1) ** 1.6 * 150).astype(np.uint8), 'L'); VDARK = Image.new('RGB', (W, H), (34, 22, 14))
def vig(im): return Image.composite(VDARK, im, VMASK)
def stage(z=.5, t=0, h=800, cy=985, dim=.24):
    im, m = cam(TEK[0], TEK[1], z + .006 * t); im = vig(Image.blend(im, WARM, dim))
    put(im, art.panel(920, h), 540, cy, sh=22); return im
def src(im, txt, a=1.): T(im, txt, 540, 1352, 25, (128, 100, 70), LORAI, a=a)
def sparkle(im, x, y, t, n=7, R=150, seed=0):
    rs = random.Random(seed)
    for i in range(n):
        a = rs.uniform(0, 2 * math.pi); r = R * rs.uniform(.6, 1.1); ph = (t * rs.uniform(.9, 1.5) + rs.random()) % 1; s = math.sin(ph * math.pi)
        put(im, star(34), x + math.cos(a) * r, y + math.sin(a) * r * .7, s=.25 + .75 * s, rot=t * 60 + i * 20, a=s)
def title(im, txt, y, size, col, t, t0=0., font=None):
    g = eout((t - t0) / .35)
    if g > 0: T(im, txt, 540, y + 26 * (1 - g), size, col, font or LORA, a=g)
def gpin(im, sx, sy, t, t0, lab, col=RUST):
    q = clamp((t - t0) / .45)
    if q <= 0: return
    if q >= 1:
        for j in range(2):
            ph = ((t - t0) * .8 + j * .5) % 1; rr = 26 + ph * 80; ImageDraw.Draw(im).ellipse([sx - rr, sy - rr * .5, sx + rr, sy + rr * .5], outline=col, width=max(1, int(6 * (1 - ph))))
    b = 18 * math.sin(clamp((t - t0 - .45) / .4) * math.pi) if q >= 1 else 0
    put(im, art.pinsp(), sx, sy - 82 - (1 - eout(q)) * 460 - b, s=1.2, sh=8)
    if q >= 1: chip(im, lab, sx, sy - 215, 40, pop(t, t0 + .45, .22), fill=col)

# ---------- sahneler ----------
def s_hook(t):
    k = 'hook'; im = stage(.5, t, h=820, cy=995); banner(im, "En iyi karpuz hangi köyün?", SER, y=320, sz=70)
    c1 = ct(k, 1) - .05; u = t - c1; cx, cy = 540, 985
    if u < .12:
        k_ = 1 + .03 * math.sin(t * 6) + (.12 * clamp(u / .12 + 1) if u > -.12 else 0)
        put(im, melon(350), cx, cy + 6 * math.sin(t * 2.4), s=k_, rot=5 * math.sin(t * 1.7), sh=18)
        s = 1 + .1 * math.sin(t * 7); circle(im, cx, cy - 6, 70 * s, (252, 244, 222)); ImageDraw.Draw(im).ellipse([cx - 70 * s, cy - 6 - 70 * s, cx + 70 * s, cy - 6 + 70 * s], outline=INK, width=4); T(im, "?", cx, cy - 10, 104, RUST, LORA, scale=s)
        for i, (name, sub, col) in enumerate(ROWS):
            a = -math.pi / 2 + i / 5 * 2 * math.pi + t * .3; x, y = cx + math.cos(a) * 285, cy + math.sin(a) * 300
            chip(im, name, x, y + 5 * math.sin(t * 3 + i), 38 if len(name) < 13 else 32, 1 + .05 * math.sin(t * 5 + i * 1.3), fill=col)
    else:
        q = eout((u - .12) / .5); rs = random.Random(5)
        for i in range(22):
            a = rs.uniform(-math.pi, 0) if i % 3 else rs.uniform(0, 2 * math.pi); v = rs.uniform(260, 620); tt = u - .12
            x, y = cx + math.cos(a) * v * tt, cy - 130 + math.sin(a) * v * tt + 620 * tt * tt
            if tt < 1.1 and 590 < y < 1380: put(im, dropr(rs.choice([9, 12, 15])), x, y, rot=math.degrees(math.atan2(-(math.cos(a) * v), math.sin(a) * v + 1240 * tt)), a=clamp(1.3 - tt))
        put(im, half(330), cx - 175 * q, cy - 120 + 10 * math.sin(t * 2.2), rot=18 * q + 3 * math.sin(t * 2), sh=16)
        put(im, half(330), cx + 175 * q, cy - 120 + 10 * math.sin(t * 2.2 + 1), rot=-18 * q - 3 * math.sin(t * 2), sh=16)
        g = pop(t, c1 + .45, .32)
        if g > 0:
            sparkle(im, 540, 1215, t, n=9, R=330, seed=2)
            put(im, badge(1), 250, 1215, s=2.1 * g, sh=5); T(im, "Çeşmekolu", 600, 1205, 96, RUST, LORA, scale=g)
            T(im, "bizim birincimiz", 600, 1292, 36, (110, 84, 56), LORAI, a=clamp((u - .9) / .3))
    mark(im); return im
def s_yer(t):
    k = 'yer'; p = ease(t / 1.6); im, m = cam(LUL[0], LUL[1] + 40 * (1 - p), .42 + .5 * p + .012 * t); im = vig(im)
    banner(im, "Çeşmekolu", "Lüleburgaz · Kırklareli", y=320, sz=90)
    sx, sy = m(*LUL); gpin(im, sx, sy, t, .45, "Lüleburgaz")
    if t >= 1.0:
        put(im, melon(270), 420, 1235 + 4 * math.sin(t * 3), s=pop(t, 1.0, .3), rot=-6, sh=12); put(im, slice_(260), 700, 1262, s=pop(t, 1.15, .3), rot=8, sh=10)
    chip(im, "İğne ilçe merkezini gösterir · Çizim temsilidir", 540, 1610, 24, 1, fill=PAPER, tc=INK); return im
WIN = (104, 720, 976, 1220)
WMASK = Image.new('L', (W, H), 0); ImageDraw.Draw(WMASK).rounded_rectangle(WIN, 30, fill=255)
def s_kamyon(t):
    k = 'kamyon'; base = stage(.46, t); banner(base, "Köylünün anlattığı", None, y=320, sz=84)
    im = base.copy(); im.paste(scenery(), (WIN[0], WIN[1])); d = ImageDraw.Draw(im)
    put(im, sunsp(False), 820, 800, s=1.5)
    for i in range(2): put(im, art.puff(110, (255, 255, 255), 200), (160 + i * 420 + t * 14) % 1100, 790 + i * 34, s=1.2 - i * .3, a=.85)
    for x in range(int(104 - (t * 300) % 120), 980, 120): d.line([(x, 1170), (x + 60, 1170)], fill=(240, 232, 210), width=6)
    for i in range(3):
        x = -300 + (t * 290 + i * 560) % 1680; y = 1052 + 3 * math.sin(t * 17 + i)
        for j in range(4):
            ph = (t * 1.6 + j / 4 + i * .3) % 1; put(im, art.puff(60, (226, 208, 172), 170), x - 260 - ph * 130, 1160 - ph * 36, s=.5 + ph * 1.1, a=(1 - ph) * .85)
        put(im, truck(), x, y, sh=6)
        for wx in (-150, 152): put(im, wheel(), x + wx, y + 106, rot=-(t * 480 + i * 40) % 360)
    im = Image.composite(im, base, WMASK); ImageDraw.Draw(im).rounded_rectangle(WIN, 30, outline=INK, width=4)
    title(im, "Her gün kamyonlarla karpuz", 660, 54, RUST, t, .25)
    chip(im, "Eskiden", 540, 1290, 44, pop(t, wt(k, 0, "eskiden") - .1), fill=CLAY)
    src(im, "Köylülerin anlatımına göre"); return im
def s_azal(t):
    k = 'azal'; im = stage(.46, t); banner(im, "Bugün", None, y=320, sz=90)
    c1 = ct(k, 1) - .05; mv = ease(clamp((t - c1) / .4))
    ng = sum(1 for i in range(3, 10) if t > .9 + (9 - i) * .16); n = 10 - ng
    T(im, "3–5 çiftçi" if ng == 7 else f"{n} çiftçi", 540, 705 - 22 * mv, 100 - 22 * mv, RUST, LORA, scale=(pop(t, .15, .3) or .01) * (1 + (.05 * math.sin(t * 22) if .9 < t < 2.05 else 0)))
    T(im, "ticari üretim yapan · söyleniyor", 540, 790 - 38 * mv, 32, (110, 84, 56), LORAI, a=clamp((t - .5) / .3))
    for i in range(10):
        gone = i >= 3 and t > .9 + (9 - i) * .16; y = 905 - 66 * mv
        put(im, melon(86), 198 + i * 76, y + (0 if gone else 3 * math.sin(t * 4 + i)), s=pop(t, .3 + i * .04, .2), a=.18 if gone else 1, sh=0 if gone else 4)
    if t >= c1:
        t0 = wt(k, 1, "masraf") - .12
        for j in range(3):
            g = eout((t - t0 - j * .14) / .4)
            if g <= 0: continue
            hh = (60 + j * 62) * g; x = 230 + j * 96; rrect(im, x - 36, 1180 - hh, x + 36, 1180, 8, (214, 150, 60)); ImageDraw.Draw(im).rounded_rectangle([x - 36, 1180 - hh, x + 36, 1180], 8, outline=INK, width=3)
            if j == 2 and g > .9: put(im, coin(96), x, 1180 - hh - 56 + 4 * math.sin(t * 4), s=pop(t, t0 + .6, .25), sh=4)
        chip(im, "Masraf arttı", 326, 1245, 38, pop(t, t0 + .25, .22), fill=RUST)
        t1 = wt(k, 1, "gölet") - .12
        if t >= t1:
            g = pop(t, t1, .3); dry = ease(clamp((t - t1 - .3) / 1.3)); put(im, basin(), 760, 1090, s=g, sh=6); put(im, pond(), 760, 1090, s=g * (1 - .82 * dry), a=1 - .3 * dry)
            chip(im, "Gölette su kalmadı", 760, 1245, 38, pop(t, t1 + .25, .22), fill=DKBLUE)
    src(im, "Kaynak: Görünüm Gazetesi, 30 Nisan 2026"); return im
def s_diger(t):
    k = 'diger'; im = stage(.46, t, h=840, cy=1000); banner(im, "Rakipleri güçlü", None, y=320, sz=84)
    ts = [.12] + [ct(k, i) - .05 for i in range(1, 5)]; act = max(j for j in range(5) if t >= ts[j]) if t >= ts[0] else -1
    for i, (name, sub, col) in enumerate(ROWS):
        if t < ts[i]: continue
        g = eout((t - ts[i]) / .38); y = 672 + i * 132; x0 = 150 + (1 - g) * 140; cur = i == act
        if i == 0: rrect(im, 122, y - 58, 958, y + 58, 20, (238, 212, 140), .95 * g)
        elif cur: rrect(im, 122, y - 58, 958, y + 58, 20, (236, 226, 200), .95 * g)
        if i == 0 or cur: ImageDraw.Draw(im).rounded_rectangle([122, y - 58, 958, y + 58], 20, outline=(150, 110, 60) if i == 0 else (196, 170, 124), width=3)
        put(im, badge(i + 1), x0 + 26, y, s=1.45 * g * (1 + (.08 * math.sin(t * 6) if cur else 0)), rot=(1 - g) * 200, a=g)
        tw = text_mask(name, 52, LORA).width; T(im, name, x0 + 86 + tw / 2, y - 18, 52, col if i else RUST, LORA, a=g)
        sw = text_mask(sub, 28, LORAI).width; T(im, sub, x0 + 86 + sw / 2, y + 31, 28, (104, 80, 54), LORAI, a=g)
        put(im, half(96) if i == 0 else melon(96), 882, y, s=pop(t, ts[i] + .15, .25), rot=6 * math.sin(t * 2 + i), sh=4)
    if t > .4: sparkle(im, 882, 672, t, n=4, R=70, seed=4)
    T(im, "Kaynaklar: Görünüm, AA, İHA, Yeşilyurt, Trakya Gazetesi", 540, 1384, 23, (128, 100, 70), LORAI); return im
def s_cta(t):
    k = 'cta'; im = stage(.44, t, h=820, cy=995); banner(im, "Sence birinci kim?", None, y=320, sz=86)
    g = eout(t / .45); put(im, podium(), 540, 930 + 200 * (1 - g), a=g, sh=10)
    put(im, half(200), 540, 706 + 6 * math.sin(t * 2.6) - 260 * (1 - eout((t - .25) / .45)), s=1 if t > .25 else .01, rot=-8 + 4 * math.sin(t * 2), sh=10)
    if t > .7: sparkle(im, 540, 700, t, n=6, R=170, seed=7)
    for x, y in ((300, 770), (780, 812)):
        s = pop(t, .5, .25) * (1 + .08 * math.sin(t * 5 + x))
        if s > 0:
            yy = y + 4 * math.sin(t * 3 + x); circle(im, x, yy, 44 * s, (252, 244, 222)); ImageDraw.Draw(im).ellipse([x - 44 * s, yy - 44 * s, x + 44 * s, yy + 44 * s], outline=INK, width=3); T(im, "?", x, yy - 3, 62, RUST, LORA, scale=s)
    chip(im, "Çeşmekolu", 540, 1095, 44, pop(t, .55, .25), fill=RUST)
    for i, (name, sub, col) in enumerate(ROWS[1:]):
        chip(im, name, 330 + (i % 2) * 420, 1172 + (i // 2) * 66, 30, pop(t, .7 + i * .1, .22), fill=col)
    c1 = ct(k, 1) - .05
    if t >= c1:
        chip(im, "Köyünü yaz · arkadaşını etiketle", 540, 1320, 40, pop(t, c1) * (1 + .03 * math.sin(t * 5)), fill=(60, 44, 30))
        if t > c1 + .9: chip(im, "Takip et · @ciceklipatikalar", 540, 1612, 36, pop(t, c1 + .9, .25), fill=PAPER, tc=INK)
    T(im, "Müzik özgündür · Çizim temsilidir", 540, 1690, 24, (92, 70, 44), LORAI, a=.9); return im
F = {'hook': s_hook, 'yer': s_yer, 'kamyon': s_kamyon, 'azal': s_azal, 'diger': s_diger, 'cta': s_cta}
exec(open('/home/claude/masal4/common.py').read())
