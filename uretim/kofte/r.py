#!/usr/bin/env python3
import os; os.chdir('/home/claude/lezzet/kf')
_s = open('/home/claude/lezzet/s1/r.py').read()
_s = _s.replace("os.chdir('/home/claude/lezzet/s1')", "os.chdir('/home/claude/lezzet/kf')")
exec(_s.split("\nF = {")[0])
SER = "Trakya Lezzet Rotası · Köfte Savaşı"
KOF = (128, 70, 42); KOFD = (80, 40, 22)
EDC = PT(41.68, 26.56); KESC = PT(40.856, 26.63); UZC = PT(41.27, 26.69); HAYC = PT(41.21, 27.10)
ILC = {"Kırklareli": RUST, "Edirne": (120, 60, 110), "Tekirdağ": GREEN}
ALLK = [("Kırklareli köftesi", "Kırklareli Merkez", "Kırklareli"), ("Ahmetbey", "Lüleburgaz", "Kırklareli"), ("Yenibedir düğün köftesi", "Lüleburgaz", "Kırklareli"),
        ("Edirne köftesi", "Edirne Merkez", "Edirne"), ("Uzunköprü", "Uzunköprü", "Edirne"), ("Keşan satır et", "Keşan", "Edirne"),
        ("Tekirdağ köftesi", "Süleymanpaşa", "Tekirdağ"), ("Çerkezmüsellim pabuç", "Hayrabolu", "Tekirdağ")]

# ---------- köfte çizimleri ----------
def _grillmarks(im, w, h, o, n=3, ang=-.5):
    d = ImageDraw.Draw(im)
    for j in range(n):
        x0 = o + w * (.22 + j * .24); d.line([(x0, o + h * .2), (x0 + h * .5 * ang * -1, o + h * .8)], fill=(50, 24, 12, 210), width=max(3, int(h * .09)))
@lru_cache(None)
def kofte(w=200, seed=1, shape='oval'):
    h = int(w * .5); c = C(w + 20, h + 20); o = 10
    if shape == 'oval':
        body = lambda d: d.rounded_rectangle(S(o, o, o + w, o + h), h * .48 * SS_, fill=255)
    elif shape == 'kare':
        h = int(w * .82); c = C(w + 20, h + 20); body = lambda d: d.rounded_rectangle(S(o, o, o + w, o + h), w * .14 * SS_, fill=255)
    else:  # pabuç
        h = int(w * .42); c = C(w + 20, h + 20)
        def body(d):
            d.ellipse(S(o, o, o + w * .62, o + h), fill=255); d.ellipse(S(o + w * .5, o + h * .12, o + w, o + h * .88), fill=255); d.rectangle(S(o + w * .3, o + h * .1, o + w * .75, o + h * .9), fill=255)
    c.fill(body, KOF, top=1.3, bot=.7, noise=14, seed=seed, ink=2.5, inkc=(50, 24, 12))
    im = c.done(); rs = random.Random(seed); d = ImageDraw.Draw(im)
    for i in range(int(w * .25)):
        x, y = o + rs.uniform(.1, .9) * w, o + rs.uniform(.15, .85) * h; s = rs.uniform(1, 2.6); d.ellipse([x - s, y - s, x + s, y + s], fill=(170, 106, 70, 160))
    _grillmarks(im, w, h, o)
    return im
@lru_cache(None)
def plate(w=420, n=4, shape='oval'):
    c = C(w + 20, int(w * .5) + 20); o = 10
    c.fill(lambda d: d.ellipse(S(o, o, o + w, o + w * .5), fill=255), (248, 244, 236), top=1.05, bot=.9, ink=2.5)
    c.over(lambda d: d.ellipse(S(o + w * .08, o + w * .05, o + w * .92, o + w * .45), fill=(236, 230, 218, 255)))
    im = c.done(); kw = int(w * (.26 if shape != 'kare' else .3))
    for i in range(n):
        x = o + w * (.28 + (i % 2) * .4) + (i // 2) * w * .06; y = o + w * (.18 + (i // 2) * .14)
        put(im, kofte(kw, i + 3, shape), x, y, rot=-8 + i * 5)
    return im
@lru_cache(None)
def stamp(year, w=170):
    c = C(w + 10, w + 10); o = 5
    c.fill(lambda d: d.ellipse(S(o, o, o + w, o + w), fill=255), (176, 40, 34), top=1.15, bot=.85, ink=2.5)
    c.over(lambda d: d.ellipse(S(o + w * .1, o + w * .1, o + w * .9, o + w * .9), outline=(250, 236, 220, 255), width=4 * SS_))
    im = c.done(); T(im, "TESCİL", w / 2 + o, w * .36 + o, int(w * .16), (250, 236, 220), M.BOLD); T(im, year, w / 2 + o, w * .6 + o, int(w * .26), (250, 236, 220), M.BOLD)
    return im
@lru_cache(None)
def mill():
    c = C(520, 360)
    c.fill(lambda d: d.rectangle(S(170, 120, 480, 340), fill=255), (214, 196, 166), top=1.1, bot=.85, noise=6, ink=3)
    c.fill(lambda d: d.polygon(SP([(150, 130), (325, 40), (500, 130)]), fill=255), (130, 74, 50), top=1.2, bot=.8, ink=3)
    c.fill(lambda d: d.rectangle(S(290, 240, 360, 340), fill=255), (110, 70, 44), ink=2.5)
    c.fill(lambda d: d.ellipse(S(30, 150, 210, 330), fill=255), (120, 84, 54), top=1.1, bot=.85, ink=3)
    def spokes(d):
        for a in range(0, 360, 30):
            r = math.radians(a); d.line(S(120, 240, 120 + 80 * math.cos(r), 240 + 80 * math.sin(r)), fill=(70, 46, 30, 255), width=5 * SS_)
    c.over(spokes); c.fill(lambda d: d.rectangle(S(0, 320, 520, 350), fill=255), (110, 160, 200), ink=0)
    return c.done()
@lru_cache(None)
def block():
    c = C(360, 260)
    c.fill(lambda d: d.rectangle(S(40, 80, 320, 240), fill=255), (150, 100, 60), top=1.1, bot=.75, noise=8, ink=3)
    c.fill(lambda d: d.ellipse(S(40, 30, 320, 130), fill=255), (214, 176, 126), top=1.1, bot=.9, ink=3)
    def rings(d):
        for r in (20, 45, 70, 100, 125): d.ellipse(S(180 - r, 80 - r * .36, 180 + r, 80 + r * .36), outline=(170, 126, 80, 255), width=2 * SS_)
    c.over(rings); im = c.done()
    rs = random.Random(4); d = ImageDraw.Draw(im)
    for i in range(70):
        x, y = rs.uniform(110, 250), rs.uniform(60, 100); s = rs.uniform(3, 6); d.ellipse([x - s, y - s * .7, x + s, y + s * .7], fill=(170, 60, 60) if i % 3 else (240, 220, 210))
    return im
@lru_cache(None)
def piyaz(w=380):
    im = art.bowl(w).copy(); d = ImageDraw.Draw(im); rs = random.Random(2); W_, H_ = im.size
    for i in range(46):
        x, y = W_ * rs.uniform(.25, .75), H_ * rs.uniform(.22, .42); d.ellipse([x - 13, y - 8, x + 13, y + 8], fill=(246, 238, 220), outline=(180, 160, 130))
    for i in range(6):
        x, y = W_ * rs.uniform(.3, .7), H_ * rs.uniform(.2, .38); d.arc([x - 26, y - 12, x + 26, y + 12], 180, 360, fill=(170, 70, 120), width=4)
    for i in range(14):
        x, y = W_ * rs.uniform(.28, .72), H_ * rs.uniform(.2, .4); d.ellipse([x - 4, y - 4, x + 4, y + 4], fill=(70, 130, 60))
    return im
@lru_cache(None)
def sandwich(w=420):
    c = C(w + 20, int(w * .55) + 20); o = 10
    c.fill(lambda d: d.rounded_rectangle(S(o, o + w * .22, o + w, o + w * .5), w * .1 * SS_, fill=255), (226, 170, 100), top=1.2, bot=.8, ink=3)
    im = c.done()
    for i in range(3): put(im, kofte(int(w * .3), 9 + i), o + w * (.22 + i * .28), o + w * .2)
    for i in range(4): circle(im, o + w * (.15 + i * .24), o + w * .13, w * .05, (200, 40, 40))
    c2 = C(w + 20, int(w * .3)); c2.fill(lambda d: d.rounded_rectangle(S(o, 4, o + w, w * .2), w * .1 * SS_, fill=255), (236, 186, 116), top=1.3, bot=.85, ink=3)
    put(im, c2.done(), (w + 20) / 2, w * .08)
    return im
def bubble(im, x, y, txt, col, s=1., flip=False):
    if s <= .02: return
    tw = text_mask(txt, int(50 * s), M.BOLD).width; w, h = tw + 60 * s, 96 * s
    rrect(im, x - w / 2, y - h / 2, x + w / 2, y + h / 2, 24 * s, (252, 246, 232)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([x - w / 2, y - h / 2, x + w / 2, y + h / 2], 24 * s, outline=INK, width=4)
    tx = x + (w * .25 if flip else -w * .25); d.polygon([(tx - 18 * s, y + h / 2 - 2), (tx + 18 * s, y + h / 2 - 2), (tx + (14 if flip else -14) * s, y + h / 2 + 34 * s)], fill=(252, 246, 232), outline=INK)
    d.line([(tx - 16 * s, y + h / 2 - 2), (tx + 16 * s, y + h / 2 - 2)], fill=(252, 246, 232), width=6)
    T(im, txt, x, y - 2, int(50 * s), col, M.BOLD)

# ---------- sahneler ----------
def s_hook(t):
    k = 'hook'; im = darkbg(t); c1 = ct(k, 1) - .05
    chip(im, SER, 540, 300, 34, 1, fill=PAPER, tc=INK)
    sh = 6 * math.sin(t * 22) * clamp(1 - abs(t - 1.2) / 1.2)
    steam(im, 540, 900, t, n=5, spread=150, rise=240, sz=1.1)
    put(im, plate(520, 4), 540, 1020 + 6 * math.sin(t * 2.4), s=pop(t, .05, .3) or .01, sh=22)
    bubble(im, 300 + sh, 700, "KIRKLARELİ!", RUST, pop(t, wt(k, 0, "başkanı") - .2, .25) * (1 + .04 * math.sin(t * 9)))
    bubble(im, 780 - sh, 790, "EDİRNE!", (120, 60, 110), pop(t, wt(k, 0, "atıştı") - .15, .25) * (1 + .04 * math.sin(t * 9 + 1)), flip=True)
    if t < c1:
        TS(im, "KÖFTE SAVAŞI", 540, 470, 112, (255, 206, 84), scale=pop(t, .1, .3) * (1 + .02 * math.sin(t * 7)))
    else:
        TS(im, "EN İYİ KÖFTE", 540, 440, 100, (252, 244, 222), scale=pop(t, c1, .3)); TS(im, "HANGİ ŞEHRİN?", 540, 555, 104, (255, 206, 84), scale=pop(t, c1 + .15, .3) * (1 + .03 * math.sin(t * 7)))
    T(im, "Çizim temsilidir", 540, 1690, 24, (230, 214, 184), LORAI, a=.9); return im
def s_kavga(t):
    k = 'kavga'; p = ease(t / 1.4); cx, cy = (KIR[0] + EDC[0]) / 2, (KIR[1] + EDC[1]) / 2
    im, m = cam(cx, cy + 60, .5 + .12 * p + .01 * t); im = vig(im); banner(im, "2018'de tatlı bir atışma", None, y=320, sz=72)
    c1 = ct(k, 1) - .05
    sx, sy = m(*KIR); gpin(im, sx, sy, t, .25, "Kırklareli"); bubble(im, sx + 40, sy - 190, "Kırklareli köftesi", RUST, pop(t, .4, .3) * .8, flip=False)
    if t >= c1:
        ex, ey = m(*EDC); gpin(im, ex, ey, t - c1, 0, "Edirne"); bubble(im, ex + 60, ey + 230, "Edirne köftesi", (120, 60, 110), pop(t, c1 + .2, .3) * .8, flip=True)
    chip(im, "Belediye başkanlarının sosyal medya atışması", 540, 1560, 26, 1, fill=PAPER, tc=INK)
    T(im, "Kaynak: Türkiye Gazetesi, 22 Mart 2018 · Çizim temsilidir", 540, 1610, 24, (60, 44, 30), LORAI); return im
def s_tek(t):
    k = 'tek'
    def il(im, t): put(im, plate(380, 4), 470, 1110, s=(pop(t, .6, .3) or .01), sh=10); put(im, stamp("2020", 150), 790, 1060, s=pop(t, wt(k, 0, "coğrafi") - .1, .3), rot=-12, sh=6)
    return rakip(t, k, "Tekirdağ köftesi", "Süleymanpaşa · Tekirdağ", TEKC, "Tekirdağ", il, [("Coğrafi işaret · 2020", wt(k, 0, "coğrafi") - .1, GREEN)], "Kaynak: TÜRKPATENT · Trakya Gezi Rehberi")
def s_ahmet(t):
    k = 'ahmet'; c1 = ct(k, 1) - .05
    def il(im, t):
        if t < c1: put(im, plate(380, 4), 470, 1110, s=(pop(t, .6, .3) or .01), sh=10); put(im, stamp("2026", 150), 790, 1060, s=pop(t, wt(k, 0, "tescillendi") - .1, .3), rot=-12, sh=6)
        else: put(im, mill(), 480, 1100, s=pop(t, c1, .3) * .7 or .01, sh=10); put(im, kofte(150, 5), 800, 1170, s=pop(t, c1 + .3, .25), sh=6)
    return rakip(t, k, "Ahmetbey köftesi", "Lüleburgaz · Kırklareli", LULC, "Lüleburgaz", il,
                 [("Coğrafi işaret · 2026", wt(k, 0, "tescillendi") - .1, RUST)] if t < c1 else [("Değirmen sırası bekleyenler için (anlatı)", c1 + .2, CLAY)], "Kaynak: NTV · Gazete Vatan (Nisan 2026)")
def s_uzun(t):
    k = 'uzun'
    def il(im, t): put(im, plate(380, 4), 470, 1110, s=(pop(t, .6, .3) or .01), sh=10); put(im, stamp("2025", 150), 790, 1060, s=pop(t, wt(k, 0, "tescil") - .1, .3), rot=-12, sh=6)
    return rakip(t, k, "Uzunköprü köftesi", "Uzunköprü · Edirne", UZC, "Uzunköprü", il, [("Yalnızca dana eti", wt(k, 0, "dana") - .1, (120, 60, 110))], "Kaynak: TÜRKPATENT tescili (Eylül 2025)")
def s_pabuc(t):
    k = 'pabuc'
    def il(im, t):
        for j in range(3): put(im, kofte(220, 20 + j, 'pabuc'), 350 + j * 190, 1100 + 8 * math.sin(t * 3 + j), s=pop(t, .6 + j * .12, .25) or .01, rot=-6 + j * 6, sh=8)
    return rakip(t, k, "Çerkezmüsellim", "Hayrabolu · Tekirdağ", HAYC, "Hayrabolu", il, [("Pabuç şeklinde köfte", wt(k, 0, "pabuç") - .1, GREEN)], "Kaynak: İHA, 2021")
def s_satir(t):
    k = 'satir'; c1 = ct(k, 1) - .05
    if t < c1:
        def il(im, t):
            put(im, block(), 470, 1120, s=(pop(t, .6, .3) or .01) * .95, sh=10); put(im, cleaver(190), 640, 1030 - 30 * abs(math.sin(t * 5)), s=pop(t, .8, .25), rot=-28 + 14 * math.sin(t * 5), sh=6)
            put(im, kofte(150, 30, 'kare'), 810, 1150, s=pop(t, 1.0, .25), sh=6)
        return rakip(t, k, "Keşan satır et", "Keşan · Edirne", KESC, "Keşan", il, [("Satırla kıyılır · tescilli tarifte baharat yok", wt(k, 0, "satırla") - .1, (120, 60, 110))], "Kaynak: TÜRKPATENT · Trakya Gezi Rehberi · CNN Türk")
    u = t - c1
    def il(im, t):
        put(im, block(), 400, 1120, s=(pop(u, .3, .3) or .01) * .9, sh=10); put(im, cleaver(180), 560, 1030 - 30 * abs(math.sin(t * 5)), s=pop(u, .5, .25), rot=-28 + 14 * math.sin(t * 5), sh=6)
        d = ImageDraw.Draw(im); px = 780
        d.line([(px, 960), (px, 1250)], fill=(110, 80, 50), width=8)
        fl = [(px, 966), (px + 150 + 10 * math.sin(t * 4), 990), (px + 140, 1040 + 6 * math.sin(t * 4 + 1)), (px, 1060)]
        d.polygon(fl, fill=(200, 36, 40)); d.polygon(fl, outline=INK)
        T(im, "düğün", px + 66, 1018, 30, (252, 244, 222), M.BOLD)
    return rakip(u, k, "Yenibedir", "Lüleburgaz · Kırklareli", LULC, "Lüleburgaz", il, [("Düğün köftesi satırla · köylü anlatısı", .4, RUST)], "Kaynak: köylülerin anlatımı")
def s_tablo(t):
    k = 'tablo'; im = stage(.46, t, h=930, cy=1010); banner(im, "Adaylar", None, y=320, sz=84)
    c1 = ct(k, 1) - .05; c2 = ct(k, 2) - .05
    for i, (name, ilce, il) in enumerate(ALLK):
        t0 = .1 + i * .1
        if t < t0: continue
        g = eout((t - t0) / .35); y = 590 + i * 84; hl = (il != "Tekirdağ" and t < c1) or (il == "Tekirdağ" and c1 <= t < c2)
        rrect(im, 130 + (1 - g) * 120, y - 36, 950, y + 36, 16, (238, 212, 140) if hl else (244, 236, 216), .95 * g)
        tw = text_mask(name, 36, LORA).width; T(im, name, 160 + tw / 2 + (1 - g) * 120, y - 10, 36, INK, LORA, a=g)
        sw = text_mask(ilce, 22, LORAI).width; T(im, ilce, 160 + sw / 2 + (1 - g) * 120, y + 20, 22, (104, 80, 54), LORAI, a=g)
        chip(im, il, 850, y, 28, g, fill=ILC[il])
    if t >= c2:
        chip(im, "Hangi il kazanır?", 540, 1320, 48, pop(t, c2, .25) * (1 + .04 * math.sin(t * 6)), fill=(60, 44, 30)); sparkle(im, 540, 1320, t, n=5, R=260, seed=3)
    return im
def s_piyaz(t):
    k = 'piyaz'; im = darkbg(t); im = Image.blend(im, DARK, .35); c1 = ct(k, 1) - .05
    TS(im, "ASIL KAVGA", 540, 400, 110, (255, 206, 84), scale=pop(t, .05, .3) * (1 + .03 * math.sin(t * 8)))
    if t >= c1:
        gL = pop(t, wt(k, 1, "piyazla") - .12, .3); gR = pop(t, wt(k, 1, "ekmek") - .12, .3)
        if gL > 0:
            put(im, piyaz(380), 280, 880 + 6 * math.sin(t * 2.4), s=gL * .95, sh=16); put(im, kofte(150, 40), 280, 760, s=gL * .9, sh=6)
            chip(im, "Piyazla", 280, 1140, 42, gL, fill=GOLD, tc=INK)
        if gR > 0:
            put(im, sandwich(400), 800, 880 + 6 * math.sin(t * 2.4 + 1), s=gR * .95, sh=16); chip(im, "Ekmek arası", 800, 1140, 42, gR, fill=RUST)
        if gL > 0 and gR > 0:
            g = pop(t, wt(k, 1, "arası") + .25, .3)
            circle(im, 540, 880, 70 * g * (1 + .06 * math.sin(t * 9)), (255, 206, 84)); ImageDraw.Draw(im).ellipse([540 - 70 * g, 880 - 70 * g, 540 + 70 * g, 880 + 70 * g], outline=INK, width=4)
            T(im, "VS", 540, 877, 60, INK, M.BOLD, scale=g); sparkle(im, 540, 880, t, n=6, R=140, seed=9)
            chip(im, "Sen hangisisin? Yorumda yaz", 540, 1300, 42, pop(t, wt(k, 1, "arası") + .5, .25) * (1 + .03 * math.sin(t * 5)), fill=(60, 44, 30))
    T(im, "Çizim temsilidir", 540, 1690, 24, (230, 214, 184), LORAI, a=.9); return im
def s_cta(t):
    k = 'cta'; im = stage(.44, t, h=820, cy=995); banner(im, "Sence en iyisi hangisi?", None, y=320, sz=80)
    g = eout(t / .45); put(im, podium(), 540, 930 + 200 * (1 - g), a=g, sh=10)
    put(im, kofte(200, 50), 540, 726 + 6 * math.sin(t * 2.6) - 260 * (1 - eout((t - .25) / .45)), s=1 if t > .25 else .01, rot=-6 + 4 * math.sin(t * 2), sh=10)
    if t > .7: sparkle(im, 540, 700, t, n=6, R=170, seed=7)
    for i, il in enumerate(("Kırklareli", "Edirne", "Tekirdağ")):
        chip(im, il, 250 + i * 290, 1110, 40, pop(t, .5 + i * .1, .22), fill=ILC[il])
    c1 = ct(k, 1) - .05
    if t >= c1:
        chip(im, "Şehrini yaz · hemşehrine gönder", 540, 1270, 42, pop(t, c1) * (1 + .03 * math.sin(t * 5)), fill=(60, 44, 30))
        if t > c1 + .9: chip(im, "Takip et · @ciceklipatikalar", 540, 1612, 36, pop(t, c1 + .9, .25), fill=PAPER, tc=INK)
    T(im, "Müzik özgündür · Çizim temsilidir", 540, 1690, 24, (92, 70, 44), LORAI, a=.9); return im
F = {'hook': s_hook, 'kavga': s_kavga, 'tek': s_tek, 'ahmet': s_ahmet, 'uzun': s_uzun, 'pabuc': s_pabuc, 'satir': s_satir, 'tablo': s_tablo, 'piyaz': s_piyaz, 'cta': s_cta}
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
                d.ellipse([540 - r - 26, 960 - r - 26, 540 + r + 26, 960 + r + 26], outline=KOFD, width=26); d.ellipse([540 - r, 960 - r, 540 + r, 960 + r], outline=(236, 196, 140), width=12)
            M.caption(im, now); return im
exec("if __name__" + _c.split("if __name__")[1])
