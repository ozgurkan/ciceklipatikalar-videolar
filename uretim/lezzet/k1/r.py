#!/usr/bin/env python3
import os; os.chdir('/home/claude/lezzet/k1')
_h = open('/home/claude/lezzet/f1/r.py').read().split('# ---------- sahneler')[0].replace("os.chdir('/home/claude/lezzet/f1')", "")
exec(_h)
SER = "Trakya Lezzet Rotası · Ek Bölüm"
LUL = P['lul']; KIR = P['kir']; BAB = PT(41.4325, 27.093)
SS_ = art.SS
RIND = (38, 96, 52); RIND2 = (92, 150, 70); FLESH = (222, 58, 62)

@lru_cache(None)
def melon(w=420):
    h = int(w * .8); c = C(w + 24, h + 24); o = 12
    m = c.fill(lambda d: d.ellipse(S(o, o, o + w, o + h), fill=255), RIND, top=1.3, bot=.62, noise=5, ink=3)
    rs = random.Random(w)
    def stripes(d):
        for i in range(9):
            x = o + w * (i + .5) / 9; bow = (i - 4) / 4 * w * .16; pts = []
            for j in range(31):
                u = j / 30; y = o + h * u; pts.append((x + bow * math.sin(u * math.pi) + rs.uniform(-5, 5), y))
            d.line(SP(pts), fill=(126, 178, 92, 235), width=int(w * .034 * SS_), joint='curve')
            d.line(SP([(px + w * .012, py) for px, py in pts]), fill=(160, 204, 120, 150), width=int(w * .01 * SS_), joint='curve')
    c.over(stripes, m)
    c.over(lambda d: d.ellipse(S(o + w * .16, o + h * .1, o + w * .46, o + h * .26), fill=(255, 255, 255, 60)), m)
    c.over(lambda d: d.line(S(o + w * .5, o + 4, o + w * .54, o - 8), fill=(110, 84, 40, 255), width=6 * SS_))
    return c.done()
@lru_cache(None)
def half(w=420):
    c = C(w + 24, w + 24); o = 12
    c.fill(lambda d: d.ellipse(S(o, o, o + w, o + w), fill=255), RIND, top=1.15, bot=.8, ink=3)
    c.over(lambda d: d.ellipse(S(o + w * .035, o + w * .035, o + w * .965, o + w * .965), fill=(214, 232, 176, 255)))
    m = c.fill(lambda d: d.ellipse(S(o + w * .075, o + w * .075, o + w * .925, o + w * .925), fill=255), FLESH, top=1.12, bot=.9, noise=8, ink=0)
    rs = random.Random(3)
    def seeds(d):
        for i in range(22):
            a = rs.uniform(0, 2 * math.pi); r = rs.uniform(.16, .34) * w; x, y = o + w / 2 + math.cos(a) * r, o + w / 2 + math.sin(a) * r; s = w * .018
            pts = [(x + math.cos(a) * s * 1.7, y + math.sin(a) * s * 1.7), (x + math.cos(a + 2.3) * s, y + math.sin(a + 2.3) * s), (x + math.cos(a - 2.3) * s, y + math.sin(a - 2.3) * s)]
            d.polygon(SP(pts), fill=(46, 28, 22, 255))
        d.ellipse(S(o + w * .22, o + w * .18, o + w * .5, o + w * .34), fill=(255, 190, 190, 70))
    c.over(seeds, m); return c.done()
@lru_cache(None)
def slice_(w=300):
    h = int(w * .56); c = C(w + 24, h + 24); o = 12; box = S(o, o - h, o + w, o + h)
    c.fill(lambda d: d.chord(box, 0, 180, fill=255), RIND, top=1.1, bot=.8, ink=3)
    c.over(lambda d: d.chord(S(o + w * .03, o - h + w * .03, o + w * .97, o + h - w * .03), 0, 180, fill=(214, 232, 176, 255)))
    m = c.fill(lambda d: d.chord(S(o + w * .075, o - h + w * .075, o + w * .925, o + h - w * .075), 0, 180, fill=255), FLESH, top=1.1, bot=.92, noise=7, ink=0)
    rs = random.Random(5)
    def seeds(d):
        for i in range(7):
            x = o + w * (.2 + .6 * i / 6); y = o + h * rs.uniform(.18, .48); s = w * .02
            d.polygon(SP([(x, y + s * 1.7), (x - s, y - s), (x + s, y - s)]), fill=(46, 28, 22, 255))
    c.over(seeds, m); c.over(lambda d: d.line(S(o, o, o + w, o), fill=art.INKC + (255,), width=3 * SS_)); return c.done()
@lru_cache(None)
def sunflower(r=120):
    n = 2 * r + 40; c = C(n, n + int(r * 1.5)); cx = cy = n / 2
    c.fill(lambda d: d.rectangle(S(cx - 9, cy, cx + 9, cy + r * 2.3), fill=255), (86, 128, 58), top=1.1, bot=.85, ink=2)
    c.fill(lambda d: d.ellipse(S(cx + 6, cy + r * 1.1, cx + r * .9, cy + r * 1.5), fill=255), (98, 142, 62), top=1.1, bot=.85, ink=2)
    def petals(d):
        for i in range(18):
            a = i / 18 * 2 * math.pi; x, y = cx + math.cos(a) * r * .7, cy + math.sin(a) * r * .7; pr = r * .34
            d.ellipse(S(x - pr, y - pr, x + pr, y + pr), fill=255)
    c.fill(petals, (244, 190, 44), top=1.12, bot=.86, ink=2.5)
    m = c.fill(lambda d: d.ellipse(S(cx - r * .52, cy - r * .52, cx + r * .52, cy + r * .52), fill=255), (104, 66, 34), top=1.2, bot=.8, noise=12, ink=2)
    return c.done()
@lru_cache(None)
def drop(w=120):
    c = C(w + 20, int(w * 1.5) + 20); o = 10
    m = c.fill(lambda d: (d.ellipse(S(o, o + w * .5, o + w, o + w * 1.5), fill=255), d.polygon(SP([(o + w * .5, o), (o + w * .93, o + w * .78), (o + w * .07, o + w * .78)]), fill=255)), (86, 156, 198), top=1.25, bot=.8, ink=3)
    c.over(lambda d: d.ellipse(S(o + w * .2, o + w * .8, o + w * .42, o + w * 1.1), fill=(255, 255, 255, 110)), m); return c.done()
@lru_cache(None)
def coin(w=130):
    c = C(w + 20, w + 20); o = 10
    c.fill(lambda d: d.ellipse(S(o, o, o + w, o + w), fill=255), (214, 158, 48), top=1.2, bot=.8, ink=3)
    c.over(lambda d: d.ellipse(S(o + w * .12, o + w * .12, o + w * .88, o + w * .88), outline=(150, 100, 24, 255), width=3 * SS_))
    im = c.done(); T(im, "₺", im.width / 2, im.height / 2 - 2, int(w * .56), (110, 70, 14), M.BOLD); return im
@lru_cache(None)
def worker(w=130):
    c = C(w + 20, int(w * 1.3) + 20); o = 10
    c.fill(lambda d: d.chord(S(o, o + w * .62, o + w, o + w * 1.9), 180, 360, fill=255), (92, 114, 58), top=1.15, bot=.85, ink=3)
    c.fill(lambda d: d.ellipse(S(o + w * .27, o + w * .12, o + w * .73, o + w * .58), fill=255), (232, 190, 150), top=1.08, bot=.9, ink=3)
    c.fill(lambda d: (d.ellipse(S(o + w * .08, o + w * .2, o + w * .92, o + w * .36), fill=255), d.chord(S(o + w * .26, o, o + w * .74, o + w * .5), 180, 360, fill=255)), (226, 196, 120), top=1.1, bot=.85, ink=2.5)
    return c.done()
@lru_cache(None)
def soil(w=820, h=210):
    c = C(w + 16, h + 16)
    m = c.fill(lambda d: d.rounded_rectangle(S(8, 8, 8 + w, 8 + h), 26 * SS_, fill=255), (132, 88, 54), top=1.18, bot=.72, noise=12, ink=3)
    rs = random.Random(2)
    def bits(d):
        for i in range(120):
            x, y, r = rs.uniform(14, w), rs.uniform(30, h), rs.uniform(3, 8); d.ellipse(S(x - r, y - r * .6, x + r, y + r * .6), fill=rs.choice([(104, 66, 38, 200), (168, 122, 78, 190), (90, 56, 32, 200)]))
        d.rectangle(S(8, 8, 8 + w, 30), fill=(108, 142, 66, 255))
    c.over(bits, m); return c.done()

def src(im, txt, a=1.): T(im, txt, 540, 1352, 25, (128, 100, 70), LORAI, a=a)
def gpin(im, sx, sy, t, t0, lab, col=RUST, dy=0, dx=0):
    q = clamp((t - t0) / .45)
    if q <= 0: return
    drop_ = (1 - eout(q)) * 420
    if q >= 1:
        ph = ((t - t0) * .8) % 1; rr = 26 + ph * 70; ImageDraw.Draw(im).ellipse([sx - rr, sy - rr * .5, sx + rr, sy + rr * .5], outline=col, width=max(1, int(6 * (1 - ph))))
    put(im, art.pinsp(), sx, sy - 70 - drop_, s=1.0, sh=6)
    if q >= 1: chip(im, lab, sx + dx, sy - 190 + dy, 36, pop(t, t0 + .45, .22), fill=col)

# ---------- sahneler ----------
def s_hook(t):
    k = 'hook'; im = stage(.5, t, h=820, cy=995); banner(im, "Çeşmekolu Karpuzu", SER, y=320, sz=84)
    c1 = ct(k, 1) - .05; mv = ease(clamp((t - c1) / .45))
    put(im, melon(470), 440 - 40 * mv, 860 + 6 * math.sin(t * 2.2) - 60 * mv, s=1 - .22 * mv, rot=4 * math.sin(t * 1.4), sh=16)
    put(im, half(300), 740 - 20 * mv, 990 - 110 * mv, s=1 - .2 * mv, rot=-14 + 5 * math.sin(t * 1.8), sh=12)
    if t < c1: T(im, "Trakya denince akla gelen lezzet", 540, 1250, 46, INK, LORA, a=clamp(t / .3 + 1) * (1 - mv))
    else:
        T(im, "3–5 çiftçi", 540, 1085, 92, RUST, LORA, scale=pop(t, c1 + .1, .3) or .01); T(im, "ticari üretim yapan · söyleniyor", 540, 1170, 34, (110, 84, 56), LORAI, a=clamp((t - c1 - .4) / .3))
        for i in range(10):
            gone = i >= 3 and t > c1 + .5 + (i - 3) * .09
            put(im, melon(84), 196 + i * 76, 1272, s=pop(t, c1 + .2 + i * .03, .2), a=.22 if gone else 1, sh=0 if gone else 3)
    src(im, "Kaynak: Görünüm Gazetesi, 30 Nisan 2026"); mark(im); return im
def s_yer(t):
    k = 'yer'; p = ease(t / 1.8); im, m = cam(LUL[0], LUL[1] + 40 * (1 - p), .42 + .46 * p + .01 * t)
    banner(im, "Çeşmekolu", "Lüleburgaz · Kırklareli", y=320, sz=90)
    sx, sy = m(*LUL); gpin(im, sx, sy, t, .6, "Lüleburgaz")
    c1 = ct(k, 1) - .05
    if t >= c1:
        s = pop(t, c1, .3); put(im, melon(260), 430, 1240, s=s, rot=-6, sh=10); put(im, slice_(240), 690, 1270, s=pop(t, c1 + .15, .3), rot=8, sh=8)
    chip(im, "İğne ilçe merkezini gösterir · Çizim temsilidir", 540, 1610, 24, 1, fill=PAPER, tc=INK); return im
def s_tat(t):
    k = 'tat'; im = stage(.46, t); banner(im, "Tadı toprağından", None, y=320, sz=86)
    d = ImageDraw.Draw(im); sp_ = ease(clamp(t / 6)); ang = math.pi * (.82 - .64 * sp_); sx, sy = 540 + math.cos(ang) * 330, 900 - math.sin(ang) * 250
    for i in range(12):
        a = i / 12 * 2 * math.pi + t * .5; d.line([(sx + math.cos(a) * 62, sy + math.sin(a) * 62), (sx + math.cos(a) * (88 + 8 * math.sin(t * 4 + i)), sy + math.sin(a) * (88 + 8 * math.sin(t * 4 + i)))], fill=(226, 170, 50), width=7)
    put(im, sunsp(False), sx, sy, s=1.5, sh=4)
    put(im, soil(), 540, 1175, sh=10)
    pts = [(170 + i * 12, 1066 + 14 * math.sin(i * .5)) for i in range(62)]; d = ImageDraw.Draw(im); d.line(pts, fill=(70, 112, 52), width=8, joint='curve')
    for i in range(0, 60, 6):
        x, y = pts[i]; put(im, leaf(), x, y - 22, s=.9, rot=20 * math.sin(i) + 6 * math.sin(t * 2 + i))
    for i, (x, w_) in enumerate(((300, 190), (545, 240), (790, 170))):
        g = pop(t, .15 + i * .18, .35); put(im, melon(w_), x, 1050 - w_ * .28, s=g * (1 + .02 * math.sin(t * 3 + i)), rot=(-5, 3, 6)[i], sh=6)
    c1 = ct(k, 1) - .05
    chip(im, "Toprak", 300, 1262, 40, pop(t, wt(k, 0, "toprağı") - .1), fill=CLAY)
    if t >= c1: chip(im, "Dalında · güneşte", 730, 1262, 40, pop(t, c1), fill=GOLD)
    src(im, "Kaynak: Görünüm Gazetesi, 30 Nisan 2026"); return im
@lru_cache(None)
def leaf():
    c = C(70, 60); c.fill(lambda d: d.polygon(SP([(35, 54), (6, 30), (16, 10), (35, 20), (54, 8), (64, 30)]), fill=255), (92, 140, 62), top=1.15, bot=.85, ink=2); return c.done()
def s_azal(t):
    k = 'azal'; im = stage(.46, t); banner(im, "Neden azaldı?", None, y=320, sz=86)
    c1 = ct(k, 1) - .05; fade = 1 - ease(clamp((t - c1) / .35)); d = ImageDraw.Draw(im)
    items = [("masraf", coin, "Masraf arttı", RUST, 1), ("gölet", drop, "Gölette su kalmadı", DKBLUE, -1)]
    if fade > 0:
        for i, (wd, sp, lab, col, arrow) in enumerate(items):
            t0 = wt(k, 0, wd) - .12; x = 330 + i * 420
            if t < t0: continue
            g = pop(t, t0, .28); put(im, sp(), x, 840 + 5 * math.sin(t * 3 + i), s=g * 1.5, a=fade, sh=8)
            if arrow and g > .9 and fade > .9:
                ay = 700 - arrow * 6 * math.sin(t * 5); pts = [(x + 96, ay + 34 * arrow), (x + 96, ay - 20 * arrow)]
                d.line(pts, fill=col, width=12); d.polygon([(x + 76, ay - 16 * arrow), (x + 116, ay - 16 * arrow), (x + 96, ay - 48 * arrow)], fill=col)
            if fade > .9: chip(im, lab, x, 1040, 40, pop(t, t0 + .2, .22), fill=col)
    if t >= c1:
        a = 1 - fade; q = ease(clamp((t - c1 - .5) / .8))
        put(im, melon(300), 300, 880, s=1, a=a * (1 - .6 * q), rot=-4, sh=8)
        if q > 0:
            d = ImageDraw.Draw(im); d.line([(250, 780), (350, 980)], fill=RUST, width=int(14 * q) + 1); d.line([(350, 780), (250, 980)], fill=RUST, width=int(14 * q) + 1)
        d = ImageDraw.Draw(im); ax = 470 + 70 * clamp((t - c1 - .4) / .5)
        if t > c1 + .4: d.line([(470, 880), (ax, 880)], fill=INK, width=10); d.polygon([(ax, 856), (ax, 904), (ax + 36, 880)], fill=INK)
        put(im, sunflower(120), 780, 920, s=pop(t, wt(k, 1, "ayçiçeği") - .15, .35), rot=5 * math.sin(t * 2), sh=8)
        chip(im, "Karpuz yerine ayçiçeği", 540, 1210, 44, pop(t, c1 + 1.0), fill=GOLD, tc=INK)
    src(im, "Kaynak: Görünüm Gazetesi, 30 Nisan 2026"); return im
@lru_cache(None)
def truck():
    c = C(520, 300)
    c.fill(lambda d: d.rounded_rectangle(S(20, 120, 360, 230), 10 * SS_, fill=255), (176, 126, 76), top=1.1, bot=.82, noise=4, ink=3)
    c.over(lambda d: [d.line(S(20 + x, 122, 20 + x, 228), fill=(120, 80, 44, 255), width=3 * SS_) for x in range(48, 340, 48)])
    c.fill(lambda d: d.polygon(SP([(360, 230), (360, 96), (432, 96), (486, 156), (500, 230)]), fill=255), (168, 72, 40), top=1.2, bot=.8, ink=3)
    c.over(lambda d: d.polygon(SP([(380, 112), (426, 112), (462, 156), (380, 156)]), fill=(206, 228, 236, 255)))
    c.fill(lambda d: d.rectangle(S(20, 226, 500, 244), fill=255), (70, 60, 56), top=1.1, bot=.8, ink=2)
    im = c.done()
    rs = random.Random(1)
    for row, n in enumerate((6, 5, 4)):
        for i in range(n):
            put(im, melon(78), 62 + row * 26 + i * 52 + rs.uniform(-3, 3), 112 - row * 34, rot=rs.uniform(-25, 25))
    return im
@lru_cache(None)
def wheel():
    c = C(84, 84); c.fill(lambda d: d.ellipse(S(6, 6, 78, 78), fill=255), (44, 40, 40), top=1.2, bot=.8, ink=2)
    c.over(lambda d: (d.ellipse(S(26, 26, 58, 58), fill=(170, 166, 160, 255)), d.line(S(42, 12, 42, 72), fill=(120, 116, 110, 255), width=4 * SS_), d.line(S(12, 42, 72, 42), fill=(120, 116, 110, 255), width=4 * SS_))); return c.done()
def s_kamyon(t):
    k = 'kamyon'; im = stage(.46, t); banner(im, "Köylünün anlattığı", None, y=320, sz=84)
    d = ImageDraw.Draw(im); d.rounded_rectangle([110, 1010, 970, 1090], 14, fill=(120, 110, 100), outline=INK, width=3)
    for x in range(int(130 - (t * 260) % 120), 960, 120):
        if x > 120: d.line([(x, 1050), (min(x + 60, 960), 1050)], fill=(236, 226, 200), width=6)
    crop = im.crop((104, 600, 976, 1100))
    for i in range(3):
        x = -260 + (t * 250 + i * 560) % 1680 - 120; y = 900 + 3 * math.sin(t * 16 + i)
        if -300 < x < 1400:
            for j in range(3):
                ph = (t * 1.5 + j / 3 + i * .3) % 1; put(im, art.puff(60, (214, 196, 160), 150), x - 250 - ph * 110, 1000 - ph * 30, s=.5 + ph, a=(1 - ph) * .8)
            put(im, truck(), x, y, sh=8)
            for wx in (-150, 150): put(im, wheel(), x + wx, y + 104, rot=-(t * 420 + i * 40) % 360)
    edge = Image.new('L', im.size, 0); ImageDraw.Draw(edge).rounded_rectangle([104, 600, 976, 1100], 30, fill=255)
    base = stage(.46, t); banner(base, "Köylünün anlattığı", None, y=320, sz=84); im = Image.composite(im, base, edge)
    T(im, "Her gün kamyonlarla karpuz", 540, 690, 54, RUST, LORA, a=clamp((t - .3) / .3))
    chip(im, "Eskiden", 540, 1200, 46, pop(t, wt(k, 0, "eskiden") - .1), fill=CLAY)
    src(im, "Köylülerin anlatımına göre"); return im
ROWS = [("Çeşmekolu", "Lüleburgaz · Kırklareli", RUST), ("Kavakdere", "Kırklareli · 1970'lerden beri", GREEN), ("Erikleryurdu", "Babaeski · kumlu toprak", CLAY), ("Üsküpdere", "Kırklareli · kışın da tezgâhta", DKBLUE), ("Marmaraereğlisi", "Tekirdağ · karpuz festivali", GOLD)]
def s_diger(t):
    k = 'diger'; im = stage(.46, t, h=840, cy=1000); banner(im, "Trakya'nın karpuz durakları", None, y=320, sz=70)
    ts = [.15] + [ct(k, i) - .05 for i in range(1, 5)]
    for i, (name, sub, col) in enumerate(ROWS):
        if t < ts[i]: continue
        g = eout((t - ts[i]) / .35); y = 672 + i * 132; x0 = 150 + (1 - g) * 80
        cur = i == max(j for j in range(5) if t >= ts[j])
        if i == 0 or cur: rrect(im, 122, y - 58, 958, y + 58, 20, (236, 214, 150) if i == 0 else (240, 230, 204), .9 * g)
        put(im, badge(i + 1), x0 + 26, y, s=1.4 * g, a=g)
        tw = text_mask(name, 50, LORA).width; T(im, name, x0 + 84 + tw / 2, y - 18, 50, col if i else RUST, LORA, a=g)
        sw = text_mask(sub, 28, LORAI).width; T(im, sub, x0 + 84 + sw / 2, y + 30, 28, (104, 80, 54), LORAI, a=g)
        put(im, half(92) if i == 0 else melon(92), 880, y, s=pop(t, ts[i] + .15, .25), sh=3)
    T(im, "Kaynaklar: Görünüm, AA, İHA, Yeşilyurt, Trakya Gazetesi", 540, 1380, 23, (128, 100, 70), LORAI); return im
def s_cta(t):
    k = 'cta'; im = stage(.44, t); banner(im, "Sence hangisi?", None, y=320, sz=90)
    put(im, half(210), 300, 740 + 5 * math.sin(t * 2.5), s=pop(t, .05, .3), rot=-8, sh=8); chip(im, "Çeşmekolu", 640, 740, 56, pop(t, .2, .25), fill=RUST)
    for i, (name, sub, col) in enumerate(ROWS[1:]):
        chip(im, name, 320 + (i % 2) * 440, 915 + (i // 2) * 110, 36, pop(t, .4 + i * .12, .22), fill=col)
    c1 = ct(k, 1) - .05
    if t >= c1:
        chip(im, "Yorumlara yaz", 540, 1170, 50, pop(t, c1)); T(im, "Takip et · @ciceklipatikalar", 540, 1290, 44, INK, LORA, a=clamp((t - c1 - .6) / .4))
    mark(im, "Müzik özgündür · Çizim temsilidir"); return im
F = {'hook': s_hook, 'yer': s_yer, 'kamyon': s_kamyon, 'tat': s_tat, 'azal': s_azal, 'diger': s_diger, 'cta': s_cta}
exec(open('/home/claude/masal4/common.py').read())
