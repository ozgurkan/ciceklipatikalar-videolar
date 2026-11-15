#!/usr/bin/env python3
import os; os.chdir('/home/claude/lezzet/bz')
_s = open('/home/claude/lezzet/tt/r.py').read().replace("/home/claude/lezzet/tt", "/home/claude/lezzet/bz")
exec(_s.split("\nF = {")[0])
SER = "Trakya Lezzet Rotası · İçecekler"
VELC = PT(41.19, 27.70)
BOZ = (236, 214, 150); HRD = (96, 24, 48)

@lru_cache(None)
def glass(w=180, col=BOZ, top=None, foam=False):
    h = int(w * 1.5); c = C(w + 20, h + 20); o = 10
    c.fill(lambda d: d.polygon(SP([(o, o), (o + w, o), (o + w * .88, o + h), (o + w * .12, o + h)]), fill=255), (236, 240, 244), top=1.1, bot=.95, ink=3)
    c.over(lambda d: d.polygon(SP([(o + w * .06, o + h * .14), (o + w * .94, o + h * .14), (o + w * .86, o + h * .95), (o + w * .14, o + h * .95)]), fill=col + (255,)))
    im = c.done(); d = ImageDraw.Draw(im)
    d.line([(o + w * .2, o + h * .25), (o + w * .26, o + h * .8)], fill=(255, 255, 255, 120), width=6)
    if top == 'leblebi':
        for i in range(6): x = o + w * (.2 + i * .12); circle(im, x, o + h * .14, w * .07, (226, 196, 120)); ImageDraw.Draw(im).ellipse([x - w * .07, o + h * .14 - w * .07, x + w * .07, o + h * .14 + w * .07], outline=(150, 110, 60), width=2)
    elif top == 'tarcin':
        rs = random.Random(3)
        for i in range(70): x, y = o + w * rs.uniform(.12, .88), o + h * rs.uniform(.13, .2); d.ellipse([x - 3, y - 2, x + 3, y + 2], fill=(140, 80, 40))
    return im
@lru_cache(None)
def train():
    c = C(780, 260)
    c.fill(lambda d: (d.rounded_rectangle(S(20, 70, 230, 200), 16 * SS_, fill=255), d.rectangle(S(60, 30, 110, 70), fill=255)), (40, 70, 110), top=1.2, bot=.8, ink=3)
    for i in range(2):
        x0 = 260 + i * 260; c.fill(lambda d, x0=x0: d.rounded_rectangle(S(x0, 80, x0 + 240, 200), 14 * SS_, fill=255), (176, 60, 44), top=1.15, bot=.85, ink=3)
        c.over(lambda d, x0=x0: [d.rectangle(S(x0 + 18 + j * 56, 100, x0 + 58 + j * 56, 140), fill=(236, 226, 196, 255)) for j in range(4)])
    def wheels(d):
        for x in (60, 170, 300, 440, 560, 700): d.ellipse(S(x - 26, 186, x + 26, 238), fill=(30, 30, 34, 255))
    c.over(wheels); im = c.done(); T(im, "Edirne – İstanbul", 390, 168, 30, (250, 240, 220), M.BOLD); return im
@lru_cache(None)
def hard_glass(w=180):
    im = glass(w, HRD).copy(); return im
@lru_cache(None)
def grapes(w=200):
    c = C(w + 20, int(w * 1.1) + 20); o = 10
    def g(d):
        for r in range(5):
            for q in range(5 - r):
                x = o + w * (.15 + q * .17 + r * .085); y = o + w * (.18 + r * .17); d.ellipse(S(x - w * .1, y - w * .1, x + w * .1, y + w * .1), fill=255)
    c.fill(g, (80, 30, 90), top=1.3, bot=.75, ink=2.5)
    c.fill(lambda d: d.polygon(SP([(o + w * .45, o), (o + w * .9, o + w * .1), (o + w * .5, o + w * .2)]), fill=255), (90, 140, 60), ink=2.5)
    return c.done()

def s_hook(t):
    k = 'hook'; im = darkbg(t); c1 = ct(k, 1) - .05
    chip(im, SER, 540, 300, 34, 1, fill=PAPER, tc=INK)
    rs = random.Random(1)
    for i in range(40):
        x = (rs.uniform(0, W) + 30 * math.sin(t + i)) % W; y = (rs.uniform(0, H) + t * rs.uniform(60, 140)) % H; circle(im, x, y, rs.uniform(3, 7), (236, 236, 244))
    TS(im, "KIŞ GELDİ", 540, 470, 112, (252, 244, 222), scale=pop(t, .05, .3))
    if t >= c1:
        TS(im, "HANGİSİ?", 540, 600, 104, (255, 206, 84), scale=pop(t, c1, .3) * (1 + .03 * math.sin(t * 7)))
        put(im, glass(230, BOZ, 'leblebi'), 320, 1030 + 6 * math.sin(t * 2.4), s=pop(t, wt(k, 1, "bozası") - .1, .3) or .01, sh=18)
        put(im, glass(230, HRD), 760, 1030 + 6 * math.sin(t * 2.4 + 1), s=pop(t, wt(k, 1, "hardaliyesi") - .1, .3) or .01, sh=18)
        chip(im, "Velimeşe bozası", 320, 1300, 38, pop(t, wt(k, 1, "bozası"), .25), fill=GOLD, tc=INK)
        chip(im, "Kırklareli hardaliyesi", 760, 1300, 38, pop(t, wt(k, 1, "hardaliyesi"), .25), fill=(120, 30, 60))
    else:
        steam(im, 540, 920, t, n=5, spread=120, rise=220, sz=1.1); put(im, glass(260, BOZ), 540, 1060, s=pop(t, .2, .3) or .01, sh=18)
    T(im, "Çizim temsilidir", 540, 1690, 24, (230, 214, 184), LORAI, a=.9); return im
def s_boza(t):
    k = 'boza'; c1, c2, c3 = [ct(k, i) - .05 for i in (1, 2, 3)]
    def il(im, t):
        if t < c2: put(im, glass(200, BOZ, 'leblebi'), 540, 1100, s=(pop(t, .6, .3) or .01), sh=10)
        elif t < c3: put(im, train(), 540 + 260 * (1 - eout((t - c2) / .8)), 1110, s=.88, sh=10)
        else: put(im, glass(180, BOZ, 'tarcin'), 430, 1100, s=pop(t, c3, .3) or .01, sh=10); put(im, stamp("2021", 140), 760, 1060, s=pop(t, wt(k, 3, "tescillendi") - .1, .3), rot=-12, sh=6)
    ch = ([("Karpuz yarışının adayı", .6, GOLD)] if t < c1 else [("Velimeşe'de üretilmeye başlandı", c1 + .1, CLAY)] if t < c2 else [("Edirne–İstanbul trenlerinde tanındı", c2 + .3, DKBLUE)] if t < c3 else [("Darı + mısır · mahreç işareti", c3 + .1, GREEN)])
    return rakip(t, k, "Velimeşe bozası", "Ergene · Tekirdağ", VELC, "Velimeşe", il, ch, "Kaynak: TÜRKPATENT tescil no. 721 (2021)", note="Çizim temsilidir")
def s_hard(t):
    k = 'hard'; c1, c2 = [ct(k, i) - .05 for i in (1, 2)]
    def il(im, t):
        put(im, glass(190, HRD), 420, 1100, s=(pop(t, .6, .3) or .01), sh=10); put(im, grapes(180), 640, 1110, s=pop(t, .8, .25), sh=8)
        if t >= c2: put(im, stamp("2017", 140), 820, 1050, s=pop(t, c2 + .1, .3), rot=-12, sh=6)
    ch = [("Bağbozumunda üzümden", .6, (120, 30, 60))] if t < c1 else ([("Hardal tohumu + vişne yaprağı · tescillisi alkolsüz", c1 + .1, CLAY)] if t < c2 else [("Mahreç işareti · 2017", c2 + .1, RUST)])
    return rakip(t, k, "Kırklareli hardaliyesi", "Kırklareli", KIR, "Kırklareli", il, ch, "Kaynak: TÜRKPATENT tescil no. 278 (2017)", note="İğne il merkezini gösterir · Çizim temsilidir")
def s_tablo(t):
    k = 'tablo'; im = stage(.46, t, h=900, cy=1000); banner(im, "Adaylar", None, y=320, sz=84); c1 = ct(k, 1) - .05
    rows = [("Velimeşe bozası", "Ergene", "Tekirdağ"), ("Kırklareli hardaliyesi", "Kırklareli", "Kırklareli")] + ([("? Edirne'nin içeceği", "yorumlara yaz", "Edirne")] if t >= c1 else [])
    for i, (name, ilce, il) in enumerate(rows):
        t0 = .1 + i * .15 if i < 2 else c1
        g = eout((t - t0) / .35); y = 680 + i * 140
        rrect(im, 130 + (1 - g) * 120, y - 54, 950, y + 54, 20, (238, 212, 140) if i == 2 else (244, 236, 216), .95 * g)
        tw = text_mask(name, 46, LORA).width; T(im, name, 165 + tw / 2 + (1 - g) * 120, y - 14, 46, INK, LORA, a=g)
        sw = text_mask(ilce, 26, LORAI).width; T(im, ilce, 165 + sw / 2 + (1 - g) * 120, y + 28, 26, (104, 80, 54), LORAI, a=g)
        chip(im, il, 840, y, 32, g, fill=ILC[il])
    if t >= c1: chip(im, "Edirneliler, içeceğiniz ne?", 540, 1270, 44, pop(t, c1 + .2, .25) * (1 + .04 * math.sin(t * 6)), fill=(120, 60, 110)); sparkle(im, 540, 1270, t, n=5, R=280, seed=3)
    return im
def s_kavga(t):
    k = 'kavga'; im = darkbg(t); im = Image.blend(im, DARK, .35); c1 = ct(k, 1) - .05
    TS(im, "ASIL KAVGA", 540, 400, 110, (255, 206, 84), scale=pop(t, .05, .3) * (1 + .03 * math.sin(t * 8)))
    if t >= c1:
        gL = pop(t, wt(k, 1, "leblebiyle") - .12, .3); gR = pop(t, wt(k, 1, "tarçınla") - .12, .3)
        if gL > 0: put(im, glass(230, BOZ, 'leblebi'), 280, 880, s=gL, sh=16); chip(im, "Leblebiyle", 280, 1150, 44, gL, fill=GOLD, tc=INK)
        if gR > 0: put(im, glass(230, BOZ, 'tarcin'), 800, 880, s=gR, sh=16); chip(im, "Tarçınla", 800, 1150, 44, gR, fill=RUST)
        if gL > 0 and gR > 0:
            g = pop(t, wt(k, 1, "tarçınla") + .25, .3)
            circle(im, 540, 880, 70 * g * (1 + .06 * math.sin(t * 9)), (255, 206, 84)); ImageDraw.Draw(im).ellipse([540 - 70 * g, 880 - 70 * g, 540 + 70 * g, 880 + 70 * g], outline=INK, width=4)
            T(im, "VS", 540, 877, 60, INK, M.BOLD, scale=g); sparkle(im, 540, 880, t, n=6, R=140, seed=9)
            chip(im, "Sen hangisisin? Yorumda yaz", 540, 1300, 42, pop(t, wt(k, 1, "tarçınla") + .5, .25) * (1 + .03 * math.sin(t * 5)), fill=(60, 44, 30))
    T(im, "Çizim temsilidir", 540, 1690, 24, (230, 214, 184), LORAI, a=.9); return im
def s_cta(t):
    k = 'cta'; im = stage(.44, t, h=820, cy=995); banner(im, "Sen hangisini içersin?", None, y=320, sz=80)
    put(im, glass(210, BOZ, 'leblebi'), 300, 860 - 260 * (1 - eout((t - .1) / .45)), s=1 if t > .1 else .01, sh=10)
    put(im, glass(210, HRD), 780, 860 - 260 * (1 - eout((t - .2) / .45)), s=1 if t > .2 else .01, sh=10)
    g = pop(t, .45, .3); circle(im, 540, 860, 62 * g, (255, 206, 84)); T(im, "?", 540, 856, 70, INK, M.BOLD, scale=g)
    if t > .7: sparkle(im, 540, 860, t, n=6, R=170, seed=7)
    chip(im, "Boza · Tekirdağ", 300, 1110, 40, pop(t, .5, .22), fill=GREEN); chip(im, "Hardaliye · Kırklareli", 780, 1110, 38, pop(t, .6, .22), fill=RUST)
    c1 = ct(k, 1) - .05
    if t >= c1:
        chip(im, "Yorumlara yaz · kış arkadaşını etiketle", 540, 1270, 40, pop(t, c1) * (1 + .03 * math.sin(t * 5)), fill=(60, 44, 30))
        if t > c1 + .9: chip(im, "Takip et · @ciceklipatikalar", 540, 1612, 36, pop(t, c1 + .9, .25), fill=PAPER, tc=INK)
    T(im, "Müzik özgündür · Çizim temsilidir", 540, 1690, 24, (92, 70, 44), LORAI, a=.9); return im
F = {'hook': s_hook, 'boza': s_boza, 'hard': s_hard, 'tablo': s_tablo, 'kavga': s_kavga, 'cta': s_cta}
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
                d.ellipse([540 - r - 26, 960 - r - 26, 540 + r + 26, 960 + r + 26], outline=(150, 120, 60), width=26); d.ellipse([540 - r, 960 - r, 540 + r, 960 + r], outline=(250, 236, 190), width=12)
            M.caption(im, now); return im
exec("if __name__" + _c.split("if __name__")[1])
