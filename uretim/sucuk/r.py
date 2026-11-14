#!/usr/bin/env python3
import os; os.chdir('/home/claude/lezzet/s1')
_k = open('/home/claude/lezzet/k1/r.py').read().split('\n# ---------- sahneler')[0].replace("os.chdir('/home/claude/lezzet/k1')", "")
exec(_k)
SER = "Trakya Lezzet Rotası · Ek Bölüm"
KIR = P['kir']; TEKC = P['tek']; LULC = P['lul']
SUC = (150, 38, 34); SUCD = (92, 22, 20); FAT = (250, 230, 216); EGGW = (252, 250, 244); YOLK = (250, 176, 30)
ROWS = [("Kızılcıkdere", "Kırklareli · 1960'lardan beri", RUST), ("İnecik", "Tekirdağ · kör bağırsakta dev sucuk", GREEN), ("Hamitabat", "Lüleburgaz · köy kooperatifi", CLAY)]
ALL = [("Kızılcıkdere", "Kırklareli Merkez", "Kırklareli", RUST), ("Hamitabat", "Lüleburgaz", "Kırklareli", CLAY), ("Yenice", "Pınarhisar", "Kırklareli", GOLD), ("Sergen", "Vize", "Kırklareli", DKBLUE), ("Osmanlı", "Havsa", "Edirne", (120, 60, 110)), ("İnecik", "Süleymanpaşa", "Tekirdağ", GREEN)]
ILC = {"Kırklareli": RUST, "Edirne": (120, 60, 110), "Tekirdağ": GREEN}

# ---------- sucuk çizimleri ----------
def _mottle(im, cx, cy, r, seed, dens=1.):
    d = ImageDraw.Draw(im); rs = random.Random(seed)
    for i in range(int(46 * dens * (r / 60) ** 2) + 6):
        a = rs.uniform(0, 2 * math.pi); rr = r * math.sqrt(rs.random()) * .86; x, y = cx + math.cos(a) * rr, cy + math.sin(a) * rr; s = r * rs.uniform(.04, .1)
        d.ellipse([x - s, y - s * rs.uniform(.6, 1), x + s, y + s], fill=FAT + (235,))
    for i in range(int(30 * dens * (r / 60) ** 2) + 4):
        a = rs.uniform(0, 2 * math.pi); rr = r * math.sqrt(rs.random()) * .86; x, y = cx + math.cos(a) * rr, cy + math.sin(a) * rr; s = r * rs.uniform(.015, .035)
        d.ellipse([x - s, y - s, x + s, y + s], fill=(60, 16, 12, 255))
@lru_cache(None)
def sl(r=60, seed=1):
    n = int(2 * r + 12); c = C(n, n); o = 6
    c.fill(lambda d: d.ellipse(S(o, o, o + 2 * r, o + 2 * r), fill=255), SUCD, top=1.1, bot=.8, ink=2)
    c.over(lambda d: d.ellipse(S(o + r * .09, o + r * .09, o + 2 * r - r * .09, o + 2 * r - r * .09), fill=(178, 58, 48, 255)))
    im = c.done(); _mottle(im, n / 2, n / 2, r * .9, seed)
    gl = Image.new('L', (n, n), 0); ImageDraw.Draw(gl).ellipse([n * .2, n * .16, n * .55, n * .36], fill=60); g = Image.new('RGBA', (n, n), (255, 255, 255, 0)); g.putalpha(gl.filter(ImageFilter.GaussianBlur(r * .08))); im.alpha_composite(g)
    return im
def _tube(pts, th, w, h, col, seed=2, shine=True):
    c = C(w, h)
    def body(d):
        for x, y in pts: d.ellipse(S(x - th / 2, y - th / 2, x + th / 2, y + th / 2), fill=255)
    c.fill(body, col, top=1.22, bot=.72, noise=7, seed=seed, ink=2.5, inkc=(50, 12, 10))
    im = c.done(); d = ImageDraw.Draw(im); rs = random.Random(seed)
    for i in range(0, len(pts), 3):
        x, y = pts[i]
        for j in range(2):
            ox, oy = rs.uniform(-th * .32, th * .32), rs.uniform(-th * .32, th * .32); s = th * rs.uniform(.03, .06)
            d.ellipse([x + ox - s, y + oy - s, x + ox + s, y + oy + s], fill=(214, 150, 130, 150))
    if shine:
        sh = Image.new('L', im.size, 0); dd = ImageDraw.Draw(sh)
        for (x0, y0), (x1, y1) in zip(pts[:-1], pts[1:]): dd.line([(x0 - th * .14, y0 - th * .22), (x1 - th * .14, y1 - th * .22)], fill=120, width=max(2, int(th * .1)))
        g = Image.new('RGBA', im.size, (255, 240, 230, 0)); g.putalpha(sh.filter(ImageFilter.GaussianBlur(th * .05))); im.alpha_composite(g)
    return im
@lru_cache(None)
def kangal(w=520):
    th = w * .2; R = w * .36; cx, cy = w / 2 + 8, w * .42 + 8; pts = []
    for i in range(80):
        a = math.pi * .08 + (math.pi * 1.84) * i / 79; pts.append((cx + math.cos(a + math.pi / 2) * R * 1.05, cy + math.sin(a + math.pi / 2) * R * .9))
    im = _tube(pts, th, int(w + 16), int(w * .9 + 16), SUC, 3)
    d = ImageDraw.Draw(im)
    for x, y in (pts[0], pts[-1]):
        d.ellipse([x - th * .18, y - th * .62, x + th * .18, y - th * .3], fill=(232, 220, 196)); d.line([(x, y - th * .5), (cx, cy - R * 1.25)], fill=(232, 220, 196), width=max(2, int(w / 110)))
    return im
@lru_cache(None)
def stick(L=420, th=70, seed=4):
    pts = [(th / 2 + 10 + i * (L - th) / 59, th / 2 + 10 + 3 * math.sin(i / 59 * math.pi)) for i in range(60)]
    im = _tube(pts, th, int(L + 20), int(th + 26), SUC, seed); d = ImageDraw.Draw(im)
    for x in (pts[0][0] - th * .35, pts[-1][0] + th * .35): d.line([(x, th / 2 + 2), (x, th / 2 + 18)], fill=(232, 220, 196), width=max(2, int(th / 14)))
    return im
@lru_cache(None)
def sahan(w=420):
    n = w + 150; c = C(n, int(w * .78 + 30)); o = 75; cy = w * .39 + 15
    c.fill(lambda d: (d.rounded_rectangle(S(4, cy - 16, o + 10, cy + 16), 14 * SS_, fill=255), d.rounded_rectangle(S(n - o - 10, cy - 16, n - 4, cy + 16), 14 * SS_, fill=255)), (150, 84, 40), ink=2.5)
    c.fill(lambda d: d.ellipse(S(o, 15, o + w, 15 + w * .78), fill=255), (186, 98, 52), top=1.3, bot=.7, ink=3)
    c.over(lambda d: d.ellipse(S(o + w * .07, 15 + w * .06, o + w * .93, 15 + w * .72), fill=(70, 40, 26, 255)))
    im = c.done(); d = ImageDraw.Draw(im); rs = random.Random(5)
    for ex, ey in ((o + w * .34, cy - 6), (o + w * .64, cy + 14)):
        pts = [(ex + math.cos(a) * w * .17 * rs.uniform(.82, 1.1), ey + math.sin(a) * w * .12 * rs.uniform(.82, 1.1)) for a in np.linspace(0, 2 * math.pi, 14, endpoint=False)]
        d.polygon(pts, fill=EGGW); circle(im, ex + 4, ey - 2, w * .06, YOLK); circle(im, ex - 2, ey - 8, w * .018, (255, 236, 160))
    for i, (x, y) in enumerate(((o + w * .2, cy + 40), (o + w * .5, cy - 50), (o + w * .8, cy - 10), (o + w * .48, cy + 58), (o + w * .78, cy + 52))):
        put(im, sl(int(w * .075), i + 2), x, y)
    return im
@lru_cache(None)
def grill(w=520):
    im = Image.new('RGBA', (w + 40, 330), (0, 0, 0, 0)); put(im, art.brazier(w, 150), (w + 40) / 2, 250)
    d = ImageDraw.Draw(im)
    for i in range(9): x = 40 + i * (w - 40) / 8; d.line([(x, 150), (x, 196)], fill=(60, 56, 54), width=5)
    d.line([(30, 170), (w + 10, 170)], fill=(70, 66, 62), width=6)
    for i in range(5):
        x = 80 + i * (w - 120) / 4; s = sl(36, 10 + i); s2 = s.copy(); dd = ImageDraw.Draw(s2)
        for j in range(3): dd.line([(10 + j * 22, 8), (30 + j * 22, s2.height - 8)], fill=(40, 14, 10, 230), width=5)
        put(im, s2, x, 150, rot=8 * (i - 2))
    return im
@lru_cache(None)
def flame(h=90, seed=0):
    c = C(int(h * .7) + 10, h + 10); rs = random.Random(seed); w = h * .7
    c.fill(lambda d: d.polygon(SP([(5 + w / 2, 5), (5 + w * .95, 5 + h * .72), (5 + w / 2, 5 + h), (5 + w * .05, 5 + h * .72)]), fill=255), (250, 140, 40), top=1.3, bot=.9, ink=0)
    c.over(lambda d: d.polygon(SP([(5 + w / 2, 5 + h * .38), (5 + w * .75, 5 + h * .8), (5 + w / 2, 5 + h * .97), (5 + w * .25, 5 + h * .8)]), fill=(255, 226, 120, 255)))
    return c.done()
@lru_cache(None)
def bigsucuk():
    return stick(760, 150, 9)
@lru_cache(None)
def coop():
    c = C(520, 330)
    c.fill(lambda d: d.rectangle(S(40, 120, 480, 310), fill=255), (236, 222, 196), top=1.08, bot=.86, noise=5, ink=3)
    c.fill(lambda d: d.polygon(SP([(20, 128), (260, 20), (500, 128)]), fill=255), (176, 70, 46), top=1.25, bot=.8, ink=3)
    c.fill(lambda d: d.rectangle(S(220, 210, 300, 310), fill=255), (120, 80, 50), ink=2.5)
    for x in (90, 360): c.fill(lambda d, x=x: d.rectangle(S(x, 180, x + 70, 240), fill=255), (176, 210, 228), ink=2.5)
    c.fill(lambda d: d.rounded_rectangle(S(130, 132, 390, 170), 8 * SS_, fill=255), (60, 98, 60), ink=2)
    im = c.done(); T(im, "KÖY KOOPERATİFİ", 260, 151, 22, (250, 244, 226), M.BOLD); return im
@lru_cache(None)
def hills(w=872, h=500):
    a = np.zeros((h, w, 3), np.float32); t = np.linspace(0, 1, h)[:, None, None]
    a[:] = np.array([176, 212, 228]) * (1 - t) + np.array([246, 236, 206]) * t; im = Image.fromarray(a.astype(np.uint8)).convert('RGBA')
    c = C(w, h)
    c.fill(lambda d: d.ellipse(S(-260, 150, 520, 640), fill=255), (78, 118, 72), top=1.1, bot=.9, ink=0)
    c.fill(lambda d: d.ellipse(S(300, 120, 1160, 660), fill=255), (66, 104, 64), top=1.1, bot=.9, ink=0)
    def trees(d):
        rs = random.Random(7)
        for i in range(60):
            x = rs.uniform(0, w); y = rs.uniform(200, 330) + (abs(x - 420) * .1); r = rs.uniform(14, 24)
            d.ellipse(S(x - r, y - r * 1.2, x + r, y + r), fill=(44, 82, 46, 255))
    c.over(trees)
    c.fill(lambda d: d.rectangle(S(0, 360, w, h), fill=255), (138, 170, 90), top=1.08, bot=.86, ink=0)
    im.alpha_composite(c.done()); return im.convert('RGB')
@lru_cache(None)
def cow(w=150, col=(250, 246, 236)):
    c = C(w + 20, int(w * .8)); o = 10
    c.fill(lambda d: (d.rounded_rectangle(S(o + w * .12, o + w * .14, o + w * .82, o + w * .46), w * .14 * SS_, fill=255), d.ellipse(S(o + w * .72, o + w * .06, o + w, o + w * .3), fill=255),
                      *[d.rectangle(S(x, o + w * .4, x + w * .07, o + w * .66), fill=255) for x in (o + w * .18, o + w * .3, o + w * .6, o + w * .7)]), col, top=1.1, bot=.85, ink=2.5)
    c.over(lambda d: (d.ellipse(S(o + w * .3, o + w * .18, o + w * .5, o + w * .32), fill=(60, 44, 36, 255)), d.ellipse(S(o + w * .58, o + w * .28, o + w * .72, o + w * .4), fill=(60, 44, 36, 255))))
    return c.done()
@lru_cache(None)
def mince(w=360):
    c = C(w + 20, int(w * .5) + 20); o = 10
    m = c.fill(lambda d: d.ellipse(S(o, o, o + w, o + w * .5), fill=255), (206, 92, 92), top=1.2, bot=.8, noise=10, ink=2)
    rs = random.Random(3)
    def g(d):
        for i in range(140):
            x, y = o + rs.uniform(.08, .92) * w, o + rs.uniform(.1, .45) * w; d.arc(S(x, y, x + 10, y + 6), 0, 180, fill=(150, 50, 52, 200), width=2 * SS_)
    c.over(g, m); return c.done()

# ---------- sahneler ----------
def TS(im, txt, x, y, size, col, font=None, scale=1., a=1., off=5):
    if scale <= .02 or a <= 0: return
    T(im, txt, x + off, y + off, size, (30, 18, 10), font or M.BOLD, a=a * .55, scale=scale); T(im, txt, x, y, size, col, font or M.BOLD, a=a, scale=scale)
DARK = Image.new('RGB', (W, H), (40, 22, 16))
_gy, _gx = np.mgrid[0:H, 0:W]; _gl = np.clip(1 - np.sqrt(((_gx - 540) / 760) ** 2 + ((_gy - 1000) / 900) ** 2), 0, 1) ** 1.4
GLOW = Image.fromarray((_gl * 120).astype(np.uint8), 'L'); GLOWC = Image.new('RGB', (W, H), (255, 196, 130))
def darkbg(t):
    im, m = cam(TEK[0], TEK[1], .5 + .012 * t); im = Image.blend(im, DARK, .58); im = Image.composite(GLOWC, im, GLOW); return vig(im)
def s_hook(t):
    k = 'hook'; im = darkbg(t)
    chip(im, SER, 540, 300, 34, 1, fill=PAPER, tc=INK)
    c1 = ct(k, 1) - .05; u = t - c1; cx, cy = 540, 1050
    if u < .1:
        steam(im, cx, cy - 170, t, n=6, spread=150, rise=260, sz=1.1)
        k_ = 1 + .03 * math.sin(t * 6) + (.12 * clamp(u / .1 + 1) if u > -.1 else 0)
        put(im, kangal(560), cx, cy + 8 * math.sin(t * 2.4), s=k_, rot=4 * math.sin(t * 1.7), sh=26)
        opts = [(a[0], a[3]) for a in ALL] + [("Senin köyün?", GOLD)]
        for i, (name, col) in enumerate(opts):
            a = -math.pi / 2 + i / len(opts) * 2 * math.pi + t * .3; x, y = cx + math.cos(a) * 320, cy + math.sin(a) * 320
            chip(im, name, x, y + 5 * math.sin(t * 3 + i), 36, 1 + .05 * math.sin(t * 5 + i * 1.3), fill=col)
        w1 = wt(k, 0, "hangi") - .12
        TS(im, "EN İYİ SUCUK", 540, 470, 108, (252, 244, 222))
        TS(im, "HANGİ KÖYÜN?", 540, 600, 112, (255, 206, 84), scale=(1 + .06 * math.sin(clamp((t - w1) / .35) * math.pi)) * (1 + .02 * math.sin(t * 7)))
    else:
        tt = u - .1; rs = random.Random(5)
        if tt < .22: im = Image.blend(im, Image.new('RGB', (W, H), (255, 236, 214)), .5 * (1 - tt / .22))
        if tt < .3:
            d = ImageDraw.Draw(im); p = tt / .3; d.line([(120 + 900 * p - 300, 880 + 200 * p - 60), (120 + 900 * p, 880 + 200 * p)], fill=(255, 250, 236), width=10)
        for i in range(16):
            a = rs.uniform(-math.pi * .95, -math.pi * .05); v = rs.uniform(380, 900)
            x, y = cx + math.cos(a) * v * tt, cy - 40 + math.sin(a) * v * tt + 900 * tt * tt
            if tt < 1.6 and y < 1750: put(im, sl(rs.choice([34, 44, 52]), i), x, y, rot=tt * rs.uniform(-400, 400), a=clamp(1.8 - tt))
        put(im, kangal(560), cx, cy + 10 + 120 * eout(clamp(tt / .6)), s=1 - .25 * eout(clamp(tt / .6)), a=1, sh=20)
        g = pop(t, c1 + .38, .32)
        TS(im, "BİZİM BİRİNCİMİZ", 540, 470, 70, (252, 244, 222), a=clamp((u - .2) / .25))
        if g > 0:
            sparkle(im, 540, 640, t, n=10, R=430, seed=2)
            put(im, badge(1), 540, 770, s=1.9 * g, sh=6); TS(im, "KIZILCIKDERE", 540, 612, 112, (255, 206, 84), scale=g)
    T(im, "Çizim temsilidir", 540, 1690, 24, (230, 214, 184), LORAI, a=.9); return im
def s_yer(t):
    k = 'yer'; p = ease(t / 1.6); im, m = cam(KIR[0], KIR[1] + 40 * (1 - p), .42 + .5 * p + .012 * t); im = vig(im)
    banner(im, "Kızılcıkdere", "Kırklareli · merkeze bağlı köy", y=320, sz=90)
    sx, sy = m(*KIR); gpin(im, sx, sy, t, .45, "Kırklareli")
    c1 = ct(k, 1) - .05
    if t >= c1:
        g = pop(t, c1, .3); put(im, kangal(300), 330, 1260 + 4 * math.sin(t * 3), s=g, rot=-6, sh=12)
        put(im, sl(56, 3), 560, 1300, s=pop(t, c1 + .15, .25), sh=6); put(im, sl(48, 4), 640, 1250, s=pop(t, c1 + .25, .25), sh=6)
        chip(im, "1960'lardan beri", 780, 1160, 46, pop(t, wt(k, 1, "altmışlı") - .1, .25), fill=RUST)
    chip(im, "İğne il merkezini gösterir · Çizim temsilidir", 540, 1560, 24, 1, fill=PAPER, tc=INK)
    T(im, "Kaynak: Anadolu Ajansı, 2011", 540, 1610, 24, (60, 44, 30), LORAI); return im
WIN = (104, 700, 976, 1180)
WMASK = Image.new('L', (W, H), 0); ImageDraw.Draw(WMASK).rounded_rectangle(WIN, 30, fill=255)
def s_ad(t):
    k = 'ad'; base = stage(.46, t); c1 = ct(k, 1) - .05
    if t < c1:
        banner(base, "Adı köyle anılır", None, y=320, sz=84); im = base
        sw = 7 * math.sin(t * 2.6); put(im, kangal(420), 540, 900 + 6 * math.sin(t * 2), rot=sw * .4, s=pop(t, .05, .3) or .01, sh=14)
        g = pop(t, .35, .3)
        if g > 0:
            d = ImageDraw.Draw(im); tx, ty = 540 + 150 * math.sin(math.radians(sw)), 1120
            d.line([(540, 760), (tx, ty - 60)], fill=(120, 96, 70), width=3)
            rrect(im, tx - 300, ty - 60, tx + 300, ty + 60, 18, (244, 232, 204)); d.rounded_rectangle([tx - 300, ty - 60, tx + 300, ty + 60], 18, outline=INK, width=3); circle(im, tx - 262, ty, 10, (120, 96, 70))
            T(im, "KIZILCIKDERE SUCUĞU", tx + 14, ty, 46, RUST, M.BOLD, scale=g)
        chip(im, "Kim yaparsa yapsın", 540, 1270, 40, pop(t, wt(k, 0, "yaparsa") - .1, .25), fill=CLAY)
    else:
        banner(base, "Lezzetin sırrı", None, y=320, sz=84)
        im = base.copy(); im.paste(hills(), (WIN[0], WIN[1] - 0))
        for i, (x, y, s_) in enumerate(((300, 1080, 1), (560, 1110, 1.15), (800, 1070, .9))):
            put(im, cow(150, (250, 246, 236) if i != 1 else (176, 120, 80)), x + 6 * math.sin(t * .8 + i), y, s=s_ * (pop(t, c1 + .1 + i * .12, .3) or .01), sh=4)
        put(im, sunsp(False), 830, 790, s=1.3)
        im = Image.composite(im, base, WMASK); ImageDraw.Draw(im).rounded_rectangle(WIN, 30, outline=INK, width=4)
        chip(im, "Istranca'da beslenen hayvanlar", 540, 1250, 38, pop(t, wt(k, 1, "beslenen") - .15, .25), fill=GREEN); chip(im, "+ baharat", 540, 1310, 36, pop(t, wt(k, 1, "baharat") - .1, .25), fill=CLAY)
    src(im, "Kaynak: AA, 2011 · Trakya Gezi Rehberi", a=1) if t < c1 else T(im, "Kaynak: AA, 2011", 540, 1384, 25, (128, 100, 70), LORAI); return im
def s_harc(t):
    k = 'harc'; im = stage(.46, t); banner(im, "Harç", None, y=320, sz=90); c1 = ct(k, 1) - .05
    if t < c1:
        put(im, art.bowl(460), 540, 980, sh=12); put(im, mince(330), 540, 930, s=pop(t, .1, .3) or .01)
        items = [(art.cumin(), 330, "Kimyon", wt(k, 0, "kimyonlu") - .1), (art.garlic(), 750, "Sarımsak", wt(k, 0, "sarımsaklı") - .1)]
        for sp, x, lab, t0 in items:
            if t < t0: continue
            q = clamp((t - t0) / .5); put(im, sp, x + (540 - x) * .35 * eout(q), 640 + 260 * eout(q), s=.75, rot=30 * q, a=1 if q < .9 else 1 - (q - .9) * 6 + .4, sh=6)
            chip(im, lab, x, 1180, 40, pop(t, t0, .22), fill=RUST if x < 540 else CLAY)
        t2 = wt(k, 0, "gece") - .15
        if t >= t2:
            g = pop(t, t2, .3); put(im, sunsp(True), 830, 720, s=1.3 * g)
            chip(im, "Bir gece dinlenir · yerel tarif", 540, 1270, 40, g, fill=DKBLUE)
    else:
        u = t - c1; L = 120 + 640 * eout(clamp(u / 1.3))
        put(im, stick(int(L), 96, 5), 170 + L / 2, 1030, sh=10)
        d = ImageDraw.Draw(im); d.polygon([(250, 980), (330, 1004), (330, 1056), (250, 1080)], fill=(180, 180, 186)); d.polygon([(250, 980), (330, 1004), (330, 1056), (250, 1080)], outline=INK)
        chip(im, "Bağırsağa doldurulur", 540, 1230, 44, pop(t, c1 + .1, .25), fill=RUST)
    src(im, "Kaynak: Ali Çakır, Kırklareli Mutfağı · Kırklareli Gazetesi"); return im
def s_diger(t):
    k = 'diger'; im = stage(.46, t, h=860, cy=1000); banner(im, "Rakipleri güçlü", None, y=320, sz=84)
    ts = [.12, ct(k, 1) - .05]; act = 1 if t >= ts[1] else 0
    for i, (name, sub, col) in enumerate(ROWS[:2]):
        if t < ts[i]: continue
        g = eout((t - ts[i]) / .38); y = 640 + i * 118; x0 = 150 + (1 - g) * 140; cur = i == act
        if i == 0: rrect(im, 122, y - 52, 958, y + 52, 20, (238, 212, 140), .95 * g)
        elif cur: rrect(im, 122, y - 52, 958, y + 52, 20, (236, 226, 200), .95 * g)
        if i == 0 or cur: ImageDraw.Draw(im).rounded_rectangle([122, y - 52, 958, y + 52], 20, outline=(150, 110, 60) if i == 0 else (196, 170, 124), width=3)
        put(im, badge(i + 1), x0 + 26, y, s=1.35 * g * (1 + (.08 * math.sin(t * 6) if cur else 0)), rot=(1 - g) * 200, a=g)
        tw = text_mask(name, 50, LORA).width; T(im, name, x0 + 86 + tw / 2, y - 16, 50, col if i else RUST, LORA, a=g)
        sw = text_mask(sub, 27, LORAI).width; T(im, sub, x0 + 86 + sw / 2, y + 29, 27, (104, 80, 54), LORAI, a=g)
    if t < ts[1]:
        put(im, kangal(300), 540, 1020 + 6 * math.sin(t * 2), s=pop(t, .3, .3) or .01, sh=10)
        for j, x in enumerate((260, 820)):
            s = pop(t, .5, .25) * (1 + .08 * math.sin(t * 5 + j))
            if s > 0: circle(im, x, 1000, 46 * s, (252, 244, 222)); ImageDraw.Draw(im).ellipse([x - 46 * s, 1000 - 46 * s, x + 46 * s, 1000 + 46 * s], outline=INK, width=3); T(im, "VS" if j else "?", x, 997, 46, RUST, M.BOLD, scale=s)
    else:
        g = pop(t, ts[1] + .2, .3); put(im, bigsucuk(), 540, 1050, s=(g or .01) * .95, rot=-3 + 2 * math.sin(t * 2), sh=12)
        t2 = ct(k, 2) - .05
        if t >= t2:
            chip(im, "15 kiloya kadar · DHA, 2010", 540, 1210, 42, pop(t, t2 + .1, .25) * (1 + .03 * math.sin(t * 6)), fill=GREEN)
    T(im, "Kaynaklar: AA (2012), DHA (2010), Trakya Gezi Rehberi", 540, 1384, 23, (128, 100, 70), LORAI); return im
@lru_cache(None)
def shop(awn=(186, 40, 40)):
    c = C(560, 380)
    c.fill(lambda d: d.rectangle(S(40, 110, 520, 370), fill=255), (236, 222, 196), top=1.08, bot=.86, noise=5, ink=3)
    c.fill(lambda d: d.rectangle(S(80, 170, 480, 330), fill=255), (70, 50, 40), ink=2.5)
    def awning(d):
        for i in range(8):
            x0 = 20 + i * 65; d.polygon(SP([(x0, 60), (x0 + 65, 60), (x0 + 65, 120), (x0 + 32, 140), (x0, 120)]), fill=(awn if i % 2 == 0 else (250, 244, 230)) + (255,))
    c.over(awning)
    c.over(lambda d: (d.line(S(20, 60, 540, 60), fill=INK + (255,), width=3 * SS_), d.line(S(90, 186, 470, 186), fill=(180, 170, 160, 255), width=4 * SS_)))
    im = c.done()
    for i in range(6):
        x = 120 + i * 62; put(im, stick(120, 30, 20 + i).rotate(90, expand=True), x, 250)
    return im
@lru_cache(None)
def cleaver(L=260):
    c = C(int(L * .62) + 40, L + 40); o = 20
    c.fill(lambda d: d.polygon(SP([(o, o), (o + L * .6, o), (o + L * .6, o + L * .5), (o, o + L * .56)]), fill=255), (196, 200, 206), top=1.25, bot=.8, ink=3)
    c.over(lambda d: d.ellipse(S(o + L * .44, o + L * .08, o + L * .53, o + L * .17), fill=(90, 90, 96, 255)))
    c.fill(lambda d: d.rounded_rectangle(S(o + L * .2, o + L * .52, o + L * .38, o + L), 8 * SS_, fill=255), (120, 74, 40), top=1.15, bot=.8, ink=3)
    return c.done()
@lru_cache(None)
def barn():
    c = C(560, 360)
    c.fill(lambda d: d.rectangle(S(60, 140, 500, 350), fill=255), (176, 62, 44), top=1.15, bot=.8, noise=5, ink=3)
    c.fill(lambda d: d.polygon(SP([(40, 150), (280, 30), (520, 150)]), fill=255), (110, 70, 50), top=1.2, bot=.8, ink=3)
    c.fill(lambda d: d.rectangle(S(210, 210, 350, 350), fill=255), (236, 222, 196), ink=2.5)
    c.over(lambda d: (d.line(S(210, 210, 350, 350), fill=(176, 62, 44, 255), width=6 * SS_), d.line(S(350, 210, 210, 350), fill=(176, 62, 44, 255), width=6 * SS_)))
    return c.done()
def rakip(t, k, title, sub, pos, pinlab, illus, chips, srctxt, note="İğne ilçe merkezini gösterir · Çizim temsilidir"):
    p = ease(t / 1.4); im, m = cam(pos[0], pos[1] + 40 * (1 - p), .42 + .45 * p + .012 * t); im = vig(im)
    banner(im, title, sub, y=320, sz=90)
    sx, sy = m(*pos); gpin(im, sx, sy, t, .35, pinlab)
    rrect(im, 150, 920, 930, 1300, 30, PAPER, .96 * clamp((t - .5) / .3)); ImageDraw.Draw(im).rounded_rectangle([150, 920, 930, 1300], 30, outline=INK, width=4) if t > .6 else None
    if t > .6: illus(im, t)
    for j, (txt, t0, col) in enumerate(chips):
        if t >= t0: chip(im, txt, 540, 1250 - (len(chips) - 1 - j) * 64, 40, pop(t, t0, .25) * (1 + .03 * math.sin(t * 5)), fill=col)
    chip(im, note, 540, 1650, 24, 1, fill=PAPER, tc=INK)
    T(im, srctxt, 540, 1700, 24, (60, 44, 30), LORAI); return im
def s_hamit(t):
    k = 'hamit'
    def il(im, t): put(im, coop(), 540, 1070, s=(pop(t, .6, .3) or .01) * .85, sh=10); put(im, sl(40, 7), 830, 1140, s=pop(t, .9, .25), sh=6)
    return rakip(t, k, "Hamitabat", "Lüleburgaz · Kırklareli", LULC, "Lüleburgaz", il, [("Köy kooperatifinin bile sucuğu var", wt(k, 0, "kooperatifinin") - .1, CLAY)], "Kaynak: Hamitabat Köy-Koop")
def s_yenice(t):
    k = 'yenice'
    def il(im, t): put(im, shop(), 540, 1065, s=(pop(t, .6, .3) or .01) * .8, sh=10)
    return rakip(t, k, "Yenice", "Pınarhisar · Kırklareli", PT(41.62, 27.52), "Pınarhisar", il, [("Köy kasapçılığı · sucuk ve kavurma", wt(k, 0, "kavurması") - .1, GOLD)], "Kaynak: Trakya Gezi Rehberi (2011) · Jorko Yollarda (2019)")
def s_osmanli(t):
    k = 'osmanli'; c1 = ct(k, 1) - .05
    def il(im, t):
        put(im, barn(), 540, 1040, s=(pop(t, .6, .3) or .01) * .78, sh=10)
        for j in range(2): put(im, cow(120, (250, 246, 236) if j else (176, 120, 80)), 300 + j * 480, 1110, s=pop(t, .8 + j * .1, .25), sh=4)
    return rakip(t, k, "Osmanlı köyü", "Havsa · Edirne", PT(41.55, 26.82), "Havsa", il,
                 [("Adı bile iddialı", wt(k, 0, "iddialı") - .1, (120, 60, 110)), ("1971'den beri · üretici beyanı", c1 + .4, RUST)], "Kaynak: Trakya Gezi Rehberi · üretici beyanı")
def s_sergen(t):
    k = 'sergen'
    def il(im, t):
        put(im, shop((40, 70, 130)), 470, 1065, s=(pop(t, .6, .3) or .01) * .72, sh=10)
        put(im, cleaver(200), 790, 1050, s=pop(t, .8, .25), rot=-20 + 6 * math.sin(t * 4), sh=8)
    return rakip(t, k, "Sergen", "Vize · Kırklareli", PT(41.57, 27.76), "Vize", il, [("Kasaplarıyla anılıyor", wt(k, 0, "kasaplarıyla") - .1, DKBLUE)], "Kaynak: Trakya Gezi Rehberi")
def s_tablo(t):
    k = 'tablo'; im = stage(.46, t, h=900, cy=1010); banner(im, "Adaylar", None, y=320, sz=84)
    c1 = ct(k, 1) - .05; c2 = ct(k, 2) - .05
    for i, (name, ilce, il, col) in enumerate(ALL):
        t0 = .1 + i * .12
        if t < t0: continue
        g = eout((t - t0) / .35); y = 610 + i * 100; hl = (il == "Kırklareli" and t < c1) or (il != "Kırklareli" and c1 <= t < c2)
        rrect(im, 140 + (1 - g) * 120, y - 42, 940, y + 42, 18, (238, 212, 140) if hl else (244, 236, 216), .95 * g)
        put(im, badge(i + 1), 186 + (1 - g) * 120, y, s=1.15 * g, a=g)
        tw = text_mask(name, 44, LORA).width; T(im, name, 236 + tw / 2 + (1 - g) * 120, y - 12, 44, col, LORA, a=g)
        sw = text_mask(ilce, 25, LORAI).width; T(im, ilce, 236 + sw / 2 + (1 - g) * 120, y + 24, 25, (104, 80, 54), LORAI, a=g)
        chip(im, il, 830, y, 30, g, fill=ILC[il])
    if t >= c2:
        chip(im, "Hangi il kazanır?", 540, 1270, 48, pop(t, c2, .25) * (1 + .04 * math.sin(t * 6)), fill=(60, 44, 30)); sparkle(im, 540, 1270, t, n=5, R=260, seed=3)
    return im
def s_kavga(t):
    k = 'kavga'; im = darkbg(t); im = Image.blend(im, DARK, .35); c1 = ct(k, 1) - .05
    TS(im, "ASIL KAVGA", 540, 400, 110, (255, 206, 84), scale=pop(t, .05, .3) * (1 + .03 * math.sin(t * 8)))
    if t >= c1:
        gL = pop(t, wt(k, 1, "sahanda") - .12, .3); gR = pop(t, wt(k, 1, "ızgarada") - .12, .3)
        if gL > 0:
            put(im, sahan(400), 285, 880 + 6 * math.sin(t * 2.4), s=gL * .95, rot=-4, sh=16); steam(im, 290, 800, t, n=4, spread=90, rise=200)
            chip(im, "Sahanda yumurtalı", 290, 1140, 40, gL, fill=GOLD, tc=INK)
        if gR > 0:
            put(im, grill(440), 795, 880 + 6 * math.sin(t * 2.4 + 1), s=gR * .95, rot=3, sh=16)
            for j in range(5): put(im, flame(70, j), 640 + j * 75, 960 + 6 * math.sin(t * 13 + j), s=(.8 + .2 * math.sin(t * 11 + j * 2)) * gR, a=.85)
            chip(im, "Izgarada", 790, 1140, 40, gR, fill=RUST)
        if gL > 0 and gR > 0:
            g = pop(t, wt(k, 1, "ızgarada") + .25, .3)
            circle(im, 540, 900, 70 * g * (1 + .06 * math.sin(t * 9)), (255, 206, 84)); ImageDraw.Draw(im).ellipse([540 - 70 * g, 900 - 70 * g, 540 + 70 * g, 900 + 70 * g], outline=INK, width=4)
            T(im, "VS", 540, 897, 60, INK, M.BOLD, scale=g); sparkle(im, 540, 900, t, n=6, R=140, seed=9)
            chip(im, "Sen hangisisin? Yorumda yaz", 540, 1300, 42, pop(t, wt(k, 1, "ızgarada") + .5, .25) * (1 + .03 * math.sin(t * 5)), fill=(60, 44, 30))
    T(im, "Çizim temsilidir", 540, 1690, 24, (230, 214, 184), LORAI, a=.9); return im
def s_cta(t):
    k = 'cta'; im = stage(.44, t, h=820, cy=995); banner(im, "Sence birinci kim?", None, y=320, sz=86)
    g = eout(t / .45); put(im, podium(), 540, 930 + 200 * (1 - g), a=g, sh=10)
    put(im, kangal(230), 540, 716 + 6 * math.sin(t * 2.6) - 260 * (1 - eout((t - .25) / .45)), s=1 if t > .25 else .01, rot=-6 + 4 * math.sin(t * 2), sh=10)
    if t > .7: sparkle(im, 540, 700, t, n=6, R=170, seed=7)
    for x, y in ((300, 770), (780, 812)):
        s = pop(t, .5, .25) * (1 + .08 * math.sin(t * 5 + x))
        if s > 0:
            yy = y + 4 * math.sin(t * 3 + x); circle(im, x, yy, 44 * s, (252, 244, 222)); ImageDraw.Draw(im).ellipse([x - 44 * s, yy - 44 * s, x + 44 * s, yy + 44 * s], outline=INK, width=3); T(im, "?", x, yy - 3, 62, RUST, LORA, scale=s)
    chip(im, "Kızılcıkdere", 540, 1095, 44, pop(t, .55, .25), fill=RUST)
    for i, (name, ilce, il, col) in enumerate(ALL[1:]):
        chip(im, name, 200 + (i % 3) * 340 if i < 3 else 370 + (i - 3) * 340, 1165 + (i // 3) * 62, 32, pop(t, .7 + i * .08, .22), fill=col)
    c1 = ct(k, 1) - .05
    if t >= c1:
        chip(im, "Köyünü yaz · köylüne gönder", 540, 1300, 42, pop(t, c1) * (1 + .03 * math.sin(t * 5)), fill=(60, 44, 30))
        if t > c1 + .9: chip(im, "Takip et · @ciceklipatikalar", 540, 1612, 36, pop(t, c1 + .9, .25), fill=PAPER, tc=INK)
    T(im, "Müzik özgündür · Çizim temsilidir", 540, 1690, 24, (92, 70, 44), LORAI, a=.9); return im
F = {'hook': s_hook, 'yer': s_yer, 'ad': s_ad, 'harc': s_harc, 'diger': s_diger, 'hamit': s_hamit, 'yenice': s_yenice, 'osmanli': s_osmanli, 'sergen': s_sergen, 'tablo': s_tablo, 'kavga': s_kavga, 'cta': s_cta}
_c = open('/home/claude/masal4/common.py').read(); exec(_c.split("if __name__")[0])
def frame(now):
    for i, k in enumerate(ORDER):
        a, b = TM[k]['start'], TM[k]['end']
        if now < b or i == len(ORDER) - 1:
            im = F[k](now - a)
            if i and now - a < .42:
                p = ease((now - a) / .42); prev = F[ORDER[i - 1]](now - TM[ORDER[i - 1]]['start']); r = 40 + p * 1250
                mk = Image.new('L', (W, H), 0); d = ImageDraw.Draw(mk); d.ellipse([540 - r, 960 - r, 540 + r, 960 + r], fill=255)
                im = Image.composite(im, prev, mk); d = ImageDraw.Draw(im)
                d.ellipse([540 - r - 26, 960 - r - 26, 540 + r + 26, 960 + r + 26], outline=SUCD, width=26); d.ellipse([540 - r, 960 - r, 540 + r, 960 + r], outline=FAT, width=12)
            M.caption(im, now); return im
exec("if __name__" + _c.split("if __name__")[1])
