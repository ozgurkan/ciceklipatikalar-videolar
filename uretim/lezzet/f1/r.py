#!/usr/bin/env python3
import os; os.chdir('/home/claude/lezzet/f1')
exec(open('/home/claude/lezzet/head.py').read())
from functools import lru_cache
import art
from art import put, C, S, SP
SER = "Trakya Lezzet Rotası · 1"
WARM = Image.new('RGB', (W, H), (58, 38, 24)); MUTE = (158, 136, 104)
TEK = P['tek']

# ---------- yerel sprite'lar ----------
@lru_cache(None)
def clockface(r):
    c = C(2 * r + 20, 2 * r + 20); o = 10
    c.fill(lambda d: d.ellipse(S(o, o, o + 2 * r, o + 2 * r), fill=255), (168, 72, 40), top=1.15, bot=.8, ink=3)
    c.over(lambda d: d.ellipse(S(o + 16, o + 16, o + 2 * r - 16, o + 2 * r - 16), fill=(252, 245, 226, 255)))
    def ticks(d):
        for i in range(60):
            a = i / 60 * 2 * math.pi; big = i % 5 == 0; r0 = r - 26; r1 = r - (52 if big else 38)
            d.line(S(o + r + math.sin(a) * r0, o + r - math.cos(a) * r0, o + r + math.sin(a) * r1, o + r - math.cos(a) * r1), fill=INK + (255,) if big else (150, 120, 90, 255), width=int((5 if big else 2) * art.SS))
    c.over(ticks); return c.done()
@lru_cache(None)
def hand(L, w, col):
    c = C(w + 12, 2 * L + 12)
    c.fill(lambda d: d.rounded_rectangle(S(6, 6, 6 + w, 6 + L + w / 2), int(w * art.SS / 2), fill=255), col, top=1.05, bot=.95, ink=1.2); return c.done()
@lru_cache(None)
def board(w=700, h=120):
    c = C(w + 20, h + 20)
    m = c.fill(lambda d: d.rounded_rectangle(S(10, 10, 10 + w, 10 + h), 26 * art.SS, fill=255), (196, 146, 92), top=1.1, bot=.84, noise=4)
    rs = random.Random(5)
    def grain(d):
        for i in range(9):
            y = 22 + i * (h - 20) / 9; d.arc(S(-200 + rs.uniform(0, 200), y - 30, w + 200, y + 30 + rs.uniform(0, 30)), 200, 340, fill=(160, 112, 66, 150), width=2 * art.SS)
    c.over(grain, m); return c.done()
@lru_cache(None)
def fridge(w=720, h=520):
    c = C(w + 20, h + 20)
    c.fill(lambda d: d.rounded_rectangle(S(10, 10, 10 + w, 10 + h), 34 * art.SS, fill=255), (196, 212, 222), top=1.08, bot=.86, ink=3)
    m = c.fill(lambda d: d.rounded_rectangle(S(34, 34, w - 14, h - 14), 18 * art.SS, fill=255), (226, 240, 247), top=1.05, bot=.9, ink=1.5, inkc=(110, 136, 150))
    def inner(d):
        d.rectangle(S(34, 34, w - 14, 62), fill=(255, 255, 240, 200))
        for y in (h * .36, h * .74):
            d.rectangle(S(34, y, w - 14, y + 12), fill=(170, 196, 208, 255)); d.rectangle(S(34, y + 12, w - 14, y + 20), fill=(150, 176, 190, 120))
    c.over(inner, m); return c.done()
@lru_cache(None)
def tray(w=440, h=150):
    c = C(w + 20, h + 20)
    m = c.fill(lambda d: (d.ellipse(S(40, 10, w - 20, h + 60), fill=255),), (204, 110, 96), top=1.2, bot=.85, noise=10, ink=2.5)
    c.over(lambda d: (d.arc(S(70, 26, w - 60, h + 40), 200, 300, fill=(255, 255, 255, 150), width=5 * art.SS), d.arc(S(120, 46, w - 150, h + 60), 210, 280, fill=(255, 255, 255, 90), width=4 * art.SS)), m)
    c.fill(lambda d: d.rounded_rectangle(S(10, h - 44, 10 + w, h + 10), 16 * art.SS, fill=255), (176, 182, 190), top=1.15, bot=.8, ink=2.5)
    return c.done()
@lru_cache(None)
def coalbed(w=840, h=380):
    c = C(w + 20, h + 20)
    m = c.fill(lambda d: d.rounded_rectangle(S(10, 10, 10 + w, 10 + h), 36 * art.SS, fill=255), (62, 52, 50), top=1.2, bot=.75, ink=3)
    rs = random.Random(8)
    def coals(d):
        for i in range(150):
            x, y, r = rs.uniform(24, w - 4), rs.uniform(24, h - 4), rs.uniform(10, 19); g = rs.choice([(34, 28, 28), (48, 38, 36), (28, 24, 26)])
            d.ellipse(S(x - r, y - r * .8, x + r, y + r * .8), fill=g + (255,))
    c.over(coals, m); return c.done()
@lru_cache(None)
def badge(n):
    c = C(56, 56); c.fill(lambda d: d.ellipse(S(5, 5, 51, 51), fill=255), (206, 148, 44), top=1.15, bot=.85, ink=2)
    im = c.done(); T(im, str(n), 28, 27, 28, (60, 38, 20), M.BOLD); return im
@lru_cache(None)
def sunsp(night):
    c = C(84, 84)
    if night:
        c.fill(lambda d: d.ellipse(S(12, 12, 72, 72), fill=255), (230, 232, 240), top=1.05, bot=.9, ink=2)
        c.over(lambda d: d.ellipse(S(30, 6, 82, 58), fill=(72, 84, 112, 255)))
    else:
        c.over(lambda d: [d.line(S(42 + math.cos(a) * 30, 42 + math.sin(a) * 30, 42 + math.cos(a) * 40, 42 + math.sin(a) * 40), fill=(206, 148, 44, 255), width=4 * art.SS) for a in [i * math.pi / 4 for i in range(8)]])
        c.fill(lambda d: d.ellipse(S(18, 18, 66, 66), fill=255), (244, 190, 70), top=1.1, bot=.9, ink=2)
    return c.done()

# ---------- ortak ----------
def stage(z=.5, t=0, h=800, cy=985, dim=.2):
    im, m = cam(TEK[0], TEK[1], z + .006 * t); im = Image.blend(im, WARM, dim)
    put(im, art.panel(920, h), 540, cy, sh=18); return im
def wt(k, i, word):
    a, b, txt = TM[k]['chunks'][i]; j = txt.lower().find(word.lower()); return a + (b - a - .2) * max(j, 0) / len(txt)
def pop(t, t0, d=.28): return back((t - t0) / d) if t >= t0 else 0
def steam(im, x, y, t, n=6, spread=60, rise=240, sz=1.):
    for i in range(n):
        ph = (t * .42 + i / n) % 1
        put(im, art.puff(), x + spread * math.sin(ph * 5 + i * 2.1), y - ph * rise, s=(.5 + ph * 1.1) * sz, a=(1 - ph) * min(1, ph * 6) * .8)
@lru_cache(4096)
def tw_(s, sz): return text_mask(s, sz, M.BOLD).width
def _cap(img, now):
    for k in ORDER:
        s = TM[k]['start']
        for a, b, txt in TM[k]['chunks']:
            if s + a <= now < s + b:
                if now < .2: return
                sz = 50; lines = [txt]
                if tw_(txt, sz) > 860:
                    wds = txt.split(); best = None
                    for i in range(1, len(wds)):
                        l1, l2 = ' '.join(wds[:i]), ' '.join(wds[i:]); w_ = max(tw_(l1, sz), tw_(l2, sz))
                        if best is None or w_ < best[0]: best = (w_, [l1, l2])
                    lines = best[1]
                    while max(tw_(l, sz) for l in lines) > 860 and sz > 36: sz -= 2
                tw = max(tw_(l, sz) for l in lines); lh = sz * 1.28; h = lh * len(lines) / 2 + 24; box = [540 - tw / 2 - 30, 1490 - h, 540 + tw / 2 + 30, 1490 + h]
                rrect(img, box[0] + 5, box[1] + 9, box[2] + 5, box[3] + 9, 18, (40, 26, 14), .28)
                rrect(img, *box, 18, (252, 244, 222), .98); ImageDraw.Draw(img).rounded_rectangle(box, 18, outline=INK, width=3)
                cut = (now - s - a) / max(.2, b - a - .28) * len(txt); pos = 0
                for i, l in enumerate(lines):
                    y = 1490 + (i - (len(lines) - 1) / 2) * lh; x0 = 540 - tw_(l, sz) / 2; ws = l.split()
                    for j, wd in enumerate(ws):
                        right = tw_(' '.join(ws[:j + 1]), sz); w_ = tw_(wd, sz); e = pos + len(wd)
                        col = INK if e <= cut else RUST if pos <= cut else MUTE
                        T(img, wd, x0 + right - w_ / 2, y, sz, col, M.BOLD); pos = e + 1
                return
M.caption = _cap

# ---------- sahneler ----------
def s_hook(t):
    k = 'hook'; im = stage(.5, t, h=820, cy=995); banner(im, "Tekirdağ Köftesi", SER, y=320, sz=86)
    T(im, "18–24 saat", 540, 690, 96, RUST, LORA, scale=1 + .04 * math.sin(t * 3))
    cx, cy, r = 540, 950, 170; put(im, clockface(r), cx, cy, sh=12)
    p = clamp(t / 3.4); d = ImageDraw.Draw(im)
    d.arc([cx - r + 34, cy - r + 34, cx + r - 34, cy + r - 34], -90, -90 + 360 * ease(p) * .92, fill=GOLD, width=12)
    a = 40 + t * 520; put(im, hand(84, 16, INK), cx, cy, rot=-(a / 12 + 20)); put(im, hand(122, 10, (168, 72, 40)), cx, cy, rot=-a)
    circle(im, cx, cy, 13, INK); circle(im, cx, cy, 5, GOLD)
    put(im, board(), 540, 1275, sh=12)
    for i in range(5):
        put(im, art.kofte(118, 0), 300 + i * 120, 1262 + 3 * math.sin(t * 4 + i), rot=6 * math.sin(t * 2 + i * 1.7), sh=5)
    if t >= ct(k, 1) - .05:
        s = pop(t, ct(k, 1) - .05, .25); circle(im, 880, 690, 62 * s, RUST); T(im, "?", 880, 688, 96, (252, 244, 222), LORA, scale=s)
    mark(im); return im
def s_yer(t):
    k = 'yer'; p = ease(t / 2.0); im, m = cam(TEK[0], TEK[1] + 60 * (1 - p), .42 + .5 * p + .01 * t)
    banner(im, "Tekirdağ", "Marmara kıyısı", y=320, sz=90)
    sx, sy = m(*TEK); q = clamp((t - .7) / .5)
    if q > 0:
        drop = (1 - eout(q)) * 520; bounce = 22 * math.sin(clamp((t - 1.2) / .5) * math.pi) * (1 if t > 1.2 else 0)
        if q >= 1:
            for i in range(2):
                ph = ((t - 1.2) * .8 + i * .5) % 1; rr = 30 + ph * 90
                ImageDraw.Draw(im).ellipse([sx - rr, sy - rr * .5, sx + rr, sy + rr * .5], outline=RUST, width=max(1, int(7 * (1 - ph))))
        put(im, art.pinsp(), sx, sy - 82 - drop - bounce, s=1.25, sh=8)
    if t >= ct(k, 1) - .05:
        t0 = ct(k, 1) - .05; s = pop(t, t0, .3); put(im, art.plate(520), 540, 1235, s=s, sh=12)
        for i in range(5):
            s2 = pop(t, t0 + .15 + i * .09, .25); put(im, art.kofte(118, 6), 540 + (i - 2) * 86, 1225 - (i % 2) * 26, s=s2, rot=8 - i * 4, sh=4)
        if s > .9: steam(im, 540, 1180, t, n=4, spread=50, rise=150, sz=.7)
        chip(im, "Bütün Türkiye'de bilinir", 540, 1345, 44, pop(t, t0 + .5), fill=GREEN)
    mark(im); return im
ING = [("bayat", "Bayat ekmek", art.bread, 225, 730, CLAY), ("soğan", "Soğan", art.onion, 855, 730, RUST), ("sarımsak", "Sarımsak", art.garlic, 225, 1010, GREEN), ("kimyon", "Kimyon", art.cumin, 855, 1010, GOLD)]
def s_et(t):
    k = 'et'; im = stage(.46, t); banner(im, "Ne giriyor?", None, y=320, sz=86)
    s = pop(t, .12, .35); put(im, art.bowl(), 540, 1020 + 6 * math.sin(t * 2), s=s * .84, sh=14)
    if t < ct(k, 1) - .1 or True:
        a = clamp((t - .5) / .3); T(im, "Tekirdağ'da yetişen", 540, 1205, 44, INK, LORA, a=a); T(im, "genç dana eti", 540, 1275, 62, RUST, LORA, a=a)
    for wd, lab, sp, x, y, col in ING:
        t0 = wt(k, 1, wd) - .1
        if t >= t0:
            q = eout((t - t0) / .4); sx = -160 if x < 540 else 1240
            put(im, sp(), sx + (x - sx) * q, y - 70 * math.sin(q * math.pi), s=.8, rot=(1 - q) * (40 if x < 540 else -40), sh=8)
            if q >= 1:
                chip(im, lab, x, y + 128, 36, pop(t, t0 + .4, .22), fill=col)
                ph = clamp((t - t0 - .4) / .5)
                if ph < 1:
                    for j in range(3): circle(im, x + (540 - x) * ph + 12 * math.sin(j * 2 + ph * 6), y + (960 - y) * ph - 80 * math.sin(ph * math.pi) + j * 9, 9 - j * 2, col, 1 - ph * .5)
    return im
def flake(d, x, y, r, col):
    for i in range(3):
        a = i * math.pi / 3; d.line([(x - math.cos(a) * r, y - math.sin(a) * r), (x + math.cos(a) * r, y + math.sin(a) * r)], fill=col, width=3)
def s_dinlen(t):
    k = 'dinlen'; im = stage(.46, t); banner(im, "Soğukta dinleniyor", None, y=320, sz=80)
    put(im, fridge(), 540, 880, sh=14); put(im, tray(), 540, 955, sh=6)
    d = ImageDraw.Draw(im); rs = random.Random(3)
    for i in range(16):
        x = rs.uniform(220, 860); sp = rs.uniform(.12, .22); ph = (t * sp + rs.random()) % 1; y = 660 + ph * 440
        flake(d, x + 14 * math.sin(t * 1.3 + i), y, 9 + 5 * (i % 3), (130, 176, 204) if i % 2 else (255, 255, 255))
    chip(im, "0–4 °C", 778, 700, 40, pop(t, .35), fill=DKBLUE)
    p = ease(clamp((t - .3) / 3.3)); hrs = int(round(18 * p))
    T(im, f"{hrs} saat", 540, 1210, 92, RUST, LORA, scale=1 + (.06 * math.sin(t * 9) if 0 < p < 1 else 0))
    c1 = ct(k, 1) - .05
    if t < c1:
        x0, x1, y = 250, 830, 1315; d.line([(x0, y), (x1, y)], fill=(196, 170, 124), width=8); d.line([(x0, y), (x0 + (x1 - x0) * p, y)], fill=RUST, width=8)
        for i in range(4): circle(im, x0 + (x1 - x0) * i / 3, y, 9, RUST if p >= i / 3 else (196, 170, 124))
        put(im, sunsp(.28 < p < .8), x0 + (x1 - x0) * p, y - 4, s=1.05, sh=4)
    else:
        chip(im, "Lezzetin sırlarından biri", 540, 1315, 46, pop(t, c1), fill=GREEN)
    return im
def s_sekil(t):
    k = 'sekil'; im = stage(.46, t); banner(im, "Ölçüsü belli", None, y=320, sz=86)
    s = pop(t, .05, .3); put(im, art.scale_sp(), 540, 850 + 40 * (1 - min(s, 1)), s=.9, sh=12)
    q = clamp((t - .25) / .3); dy = (1 - eout(q)) * 300
    if q > 0: put(im, art.kofte(250, 0), 540, 695 - dy + (5 * math.sin(clamp((t - .55) / .3) * math.pi) if t > .55 else 0), sh=5)
    g = int(round(15 * ease(clamp((t - .5) / .7)))); T(im, f"{g} g", 540, 902, 62, (40, 60, 34), M.BOLD)
    c1 = ct(k, 1) - .05
    if t >= c1:
        p = eout((t - c1) / .45); put(im, art.ruler(7, 80), 540 + 15 + (1 - p) * 900, 1290, sh=8)
        put(im, art.kofte(520, 0), 535, 1178, s=1, a=clamp((t - c1) / .25), sh=6)
        if p >= 1:
            pp = clamp((t - c1 - .45) / .35); d = ImageDraw.Draw(im); xa, xb = 275, 795
            d.line([(xa, 1062), (xa + (xb - xa) * pp, 1062)], fill=RUST, width=6); d.line([(xa, 1045), (xa, 1079)], fill=RUST, width=6)
            if pp >= 1: d.line([(xb, 1045), (xb, 1079)], fill=RUST, width=6)
            chip(im, "6,5 cm", 535, 1062, 46, pop(t, c1 + .6, .25))
    return im
KPOS = [(540 + (i % 5 - 2) * 148, 855 + (i // 5) * 110) for i in range(10)]
def s_izgara(t):
    k = 'izgara'; im = stage(.46, t); banner(im, "Mangalda, sacın üstünde", None, y=320, sz=70)
    put(im, coalbed(), 540, 910, sh=14); rs = random.Random(6)
    for i in range(34):
        e = i % 4; u = rs.random()
        x, y = ((140 + u * 800, 742 if e == 0 else 1078) if e < 2 else (142 if e == 2 else 938, 750 + u * 320))
        g = .55 + .45 * math.sin(t * (3 + rs.random() * 4) + i); put(im, art.puff(60, (255, 136, 36), 210), x, y, s=.75 + .35 * g, a=.45 + .5 * g)
        put(im, art.puff(30, (255, 226, 130), 230), x, y, s=.6 + .3 * g, a=g)
    put(im, art.sac(), 540, 910, sh=8)
    q = min(6, int(clamp(t / 3.4) * 6.99))
    for i, (x, y) in enumerate(KPOS):
        put(im, art.kofte(128, q), x, y + 1.5 * math.sin(t * 14 + i * 1.3), rot=(-3, 2, -1, 3, -2)[i % 5], sh=4)
    steam(im, 540, 800, t, n=8, spread=260, rise=250, sz=.95)
    c1 = ct(k, 1) - .05
    if t < c1:
        chip(im, "Mangal kömürü", 330, 665, 38, pop(t, .3), fill=(70, 58, 54)); chip(im, "Oluklu sac", 770, 665, 38, pop(t, wt(k, 0, "oluklu") - .1), fill=CLAY)
    else:
        for i, (x, y) in enumerate(KPOS):
            put(im, badge(i + 1), x, y - 34, s=pop(t, c1 + i * .07, .2))
        chip(im, "Porsiyon: 10 köfte", 540, 1250, 52, pop(t, c1 + .15))
    return im
def s_tescil(t):
    k = 'tescil'; im = stage(.5, t); banner(im, "Coğrafi işaretli", None, y=320, sz=84)
    c1 = ct(k, 1) - .05; mv = ease(clamp((t - c1) / .5)); q = clamp((t - .15) / .28)
    if q > 0:
        s = (1.9 - .9 * eout(q)) * (1 - .3 * mv) + (.05 * math.sin(clamp((t - .43) / .25) * math.pi) if t > .43 else 0)
        put(im, art.seal(), 540 - 220 * mv, 930 - 80 * mv, s=s, rot=-8, a=min(1, q * 2), sh=12)
        if .4 < t < .9:
            ph = (t - .4) / .5; d = ImageDraw.Draw(im); rr = 210 + ph * 120; d.ellipse([540 - rr, 870 - rr, 540 + rr, 870 + rr], outline=GOLD, width=max(1, int(8 * (1 - ph))))
    a0 = clamp((t - .7) / .3)
    T(im, "Tescil No: 517", 540 - 220 * mv, 1245 - 115 * mv, 40 - 4 * mv, INK, LORAI, a=a0)
    if t >= c1:
        a = clamp((t - c1 - .25) / .3); T(im, "≈ 100 yıl", 735, 790, 88, RUST, LORA, scale=pop(t, c1 + .2, .3) or .01, a=a)
        T(im, "önce bir ustayla", 735, 880, 40, INK, LORA, a=a); T(im, "başladığı anlatılır", 735, 936, 38, (110, 84, 56), LORAI, a=a)
        p = ease(clamp((t - c1 - .6) / 1.2)); d = ImageDraw.Draw(im); x0, x1, y = 220, 860, 1255
        d.line([(x0, y), (x1, y)], fill=(196, 170, 124), width=8); d.line([(x0, y), (x0 + (x1 - x0) * p, y)], fill=RUST, width=8)
        circle(im, x0, y, 14, RUST); T(im, "Usta", x0 + 10, y + 52, 36, INK, LORA, a=a); T(im, "≈ 100 yıl önce", x0 + 70, y - 46, 30, (110, 84, 56), LORAI, a=a)
        if p > .97: circle(im, x1, y, 16 * pop(t, c1 + 1.75, .2), GOLD); T(im, "2020 · Tescil", x1 - 60, y + 52, 36, INK, LORA, a=clamp((t - c1 - 1.75) / .25))
    return im
PYR = [(540 + (j - (n - 1) / 2) * 138, 838 + r * 36) for r, n in enumerate((1, 2, 3, 4)) for j in range(n)]
def s_cta(t):
    k = 'cta'; im = stage(.44, t); banner(im, "Sen yedin mi?", None, y=320, sz=90)
    put(im, art.plate(720), 540, 935, s=pop(t, .0, .3) if t < .3 else 1, sh=14)
    for i, (x, y) in enumerate(PYR):
        put(im, art.kofte(128, 6), x, y, s=pop(t, .12 + i * .05, .22), rot=(-2, 3, -3, 1, 2, -1, 2, -2, 1, 3)[i], sh=4)
    steam(im, 540, 800, t, n=5, spread=110, rise=170, sz=.8)
    c1 = ct(k, 1) - .05
    if t >= c1: chip(im, "Yorumlara yaz", 540, 1150, 50, pop(t, c1))
    c2 = ct(k, 2) - .05
    if t >= c2:
        chip(im, "Yarın: Edirne", 540, 1250, 44, pop(t, c2), fill=GREEN); T(im, "Takip et · @ciceklipatikalar", 540, 1335, 42, INK, LORA, a=clamp((t - c2 - .9) / .4))
    mark(im, "Müzik özgündür · Çizim temsilidir"); return im
F = {'hook': s_hook, 'yer': s_yer, 'et': s_et, 'dinlen': s_dinlen, 'sekil': s_sekil, 'izgara': s_izgara, 'tescil': s_tescil, 'cta': s_cta}
exec(open('/home/claude/masal4/common.py').read())
