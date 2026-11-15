#!/usr/bin/env python3
import os; os.chdir('/home/claude/lezzet/pr')
_s = open('/home/claude/lezzet/tt/r.py').read().replace("/home/claude/lezzet/tt", "/home/claude/lezzet/pr")
exec(_s.split("\nF = {")[0])
SER = "Trakya Lezzet Rotası · Pirinç"
IPC = PT(40.92, 26.38)
EUB = (30, 60, 140)

@lru_cache(None)
def pilav(w=420):
    c = C(w + 20, int(w * .7) + 20); o = 10
    c.fill(lambda d: d.ellipse(S(o, o + w * .18, o + w, o + w * .66), fill=255), (70, 110, 150), top=1.2, bot=.8, ink=3)
    c.fill(lambda d: d.ellipse(S(o + w * .12, o, o + w * .88, o + w * .5), fill=255), (248, 242, 226), top=1.15, bot=.85, noise=6, ink=2.5)
    im = c.done(); d = ImageDraw.Draw(im); rs = random.Random(4)
    for i in range(90):
        x, y = o + w * rs.uniform(.22, .78), o + w * rs.uniform(.08, .42)
        if ((x - o - w / 2) / (w * .36)) ** 2 + ((y - o - w * .25) / (w * .22)) ** 2 > 1: continue
        a = rs.uniform(0, math.pi); dx, dy = 9 * math.cos(a), 4 * math.sin(a)
        d.line([(x - dx, y - dy), (x + dx, y + dy)], fill=(214, 200, 168), width=3)
    return im
@lru_cache(None)
def sack(w=260):
    h = int(w * 1.15); c = C(w + 20, h + 20); o = 10
    c.fill(lambda d: d.polygon(SP([(o + w * .12, o + h * .12), (o + w * .88, o + h * .12), (o + w, o + h * .9), (o + w * .5, o + h), (o, o + h * .9)]), fill=255), (214, 190, 140), top=1.15, bot=.8, noise=8, ink=3)
    c.fill(lambda d: d.rectangle(S(o + w * .3, o, o + w * .7, o + h * .14), fill=255), (196, 170, 120), ink=2.5)
    im = c.done(); T(im, "İPSALA", o + w / 2, o + h * .5, int(w * .15), (120, 70, 40), M.BOLD); T(im, "pirinç", o + w / 2, o + h * .66, int(w * .1), (120, 70, 40), LORAI)
    return im
@lru_cache(None)
def grain(w=360):
    h = int(w * .42); c = C(w + 20, h + 20); o = 10
    c.fill(lambda d: d.ellipse(S(o, o, o + w, o + h), fill=255), (244, 240, 228), top=1.25, bot=.8, ink=3)
    im = c.done(); d = ImageDraw.Draw(im)
    d.ellipse([o + w * .15, o + h * .2, o + w * .55, o + h * .45], fill=(255, 255, 255, 150))
    return im
@lru_cache(None)
def eubadge(w=220):
    im = Image.new('RGBA', (w, w), (0, 0, 0, 0)); circle(im, w / 2, w / 2, w * .48, EUB)
    for i in range(12):
        a = i * math.pi / 6; sx, sy = w / 2 + w * .34 * math.cos(a), w / 2 + w * .34 * math.sin(a); R = w * .055
        ImageDraw.Draw(im).polygon([(sx + (R if j % 2 == 0 else R * .45) * math.cos(-math.pi / 2 + j * math.pi / 5), sy + (R if j % 2 == 0 else R * .45) * math.sin(-math.pi / 2 + j * math.pi / 5)) for j in range(10)], fill=(255, 210, 40))
    T(im, "AB", w / 2, w / 2 - 2, int(w * .2), (255, 255, 255), M.BOLD); return im
@lru_cache(None)
def butter(w=240):
    h = int(w * .55); c = C(w + 20, h + 20); o = 10
    c.fill(lambda d: d.rectangle(S(o, o + h * .3, o + w, o + h), fill=255), (220, 220, 226), top=1.1, bot=.85, ink=3)
    c.fill(lambda d: d.rounded_rectangle(S(o + w * .12, o, o + w * .88, o + h * .55), 14 * SS_, fill=255), (250, 222, 120), top=1.2, bot=.85, ink=3)
    return c.done()
@lru_cache(None)
def bottle(w=150):
    h = int(w * 2.2); c = C(w + 20, h + 20); o = 10
    c.fill(lambda d: (d.rounded_rectangle(S(o, o + h * .3, o + w, o + h), 22 * SS_, fill=255), d.rectangle(S(o + w * .34, o, o + w * .66, o + h * .32), fill=255)), (236, 196, 60), top=1.25, bot=.8, ink=3)
    c.fill(lambda d: d.rectangle(S(o + w * .3, o, o + w * .7, o + h * .07), fill=255), (60, 120, 60), ink=2)
    im = c.done(); circle(im, o + w / 2, o + h * .64, w * .26, (250, 236, 180)); circle(im, o + w / 2, o + h * .64, w * .1, (120, 80, 30)); return im

def s_hook(t):
    k = 'hook'; im = darkbg(t); c1 = ct(k, 1) - .05
    chip(im, SER, 540, 300, 34, 1, fill=PAPER, tc=INK)
    TS(im, "AB TESCİLLİ", 540, 450, 104, (252, 244, 222), scale=pop(t, .05, .3)); TS(im, "İLK TRAKYA ÜRÜNÜ", 540, 570, 76, (255, 206, 84), scale=pop(t, .25, .3))
    if t < c1:
        put(im, eubadge(300), 540, 1000 + 6 * math.sin(t * 2.4), s=pop(t, .4, .3) or .01, sh=16); sparkle(im, 540, 1000, t, n=6, R=200, seed=2)
    else:
        for i, (n, kw) in enumerate((("Köfte", "köfte"), ("Peynir", "peynir"))):
            g = pop(t, wt(k, 1, kw) - .05, .25); x = 300 + i * 480
            chip(im, n, x, 800, 48, g, fill=(90, 80, 70))
            if g > .9: d = ImageDraw.Draw(im); d.line([(x - 110, 800), (x + 110, 800)], fill=(220, 60, 50), width=10)
        g = pop(t, wt(k, 1, "pirinç") - .1, .3)
        put(im, pilav(440), 540, 1080 + 6 * math.sin(t * 2.4), s=g or .01, sh=16); put(im, eubadge(150), 800, 960, s=g * .9 or .01, sh=8)
        chip(im, "İpsala pirinci", 540, 1300, 52, pop(t, wt(k, 1, "pirinç"), .25) * (1 + .03 * math.sin(t * 6)), fill=RUST)
    T(im, "Çizim temsilidir", 540, 1690, 24, (230, 214, 184), LORAI, a=.9); return im
def s_tescil(t):
    k = 'tescil'; c1, c2 = ct(k, 1) - .05, ct(k, 2) - .05
    def il(im, t):
        put(im, sack(220), 400, 1100, s=(pop(t, .6, .3) or .01), sh=10)
        if t < c1: put(im, stamp("2016", 140), 700, 1060, s=pop(t, wt(k, 0, "tescillendi") - .1, .3), rot=-12, sh=6)
        else: put(im, eubadge(190), 700, 1090, s=pop(t, c1 + .2, .3), sh=8)
    ch = [("Menşe adı · TÜRKPATENT 2016", .6, GREEN)] if t < c1 else ([("AB korumalı menşe adı · Kasım 2025", c1 + .1, DKBLUE)] if t < c2 else [("KTSO: Trakya'nın ilk AB tescili", c2 + .1, RUST)])
    return rakip(t, k, "İpsala pirinci", "İpsala · Edirne", IPC, "İpsala", il, ch, "Kaynak: TÜRKPATENT tescil no. 196 · AB Uyg. Tüzüğü 2025/2317 · DHA", note="İğne ilçe merkezini gösterir · Çizim temsilidir")
def s_ova(t):
    k = 'ova'; c1, c2, c3 = [ct(k, i) - .05 for i in (1, 2, 3)]
    def il(im, t):
        if t < c2:
            for j in range(7):
                x = 330 + j * 70; sw = 8 * math.sin(t * 2 + j)
                d = ImageDraw.Draw(im); d.line([(x, 1170), (x + sw, 1050)], fill=(110, 140, 50), width=6)
                for q in range(4): d.ellipse([x + sw - 8 + q * 3, 1050 + q * 14, x + sw + 8 + q * 3, 1066 + q * 14], fill=(214, 180, 90))
            d.rectangle([300, 1168, 800, 1180], fill=(90, 130, 170))
        else:
            put(im, sack(190), 420, 1100, s=pop(t, c2, .3) or .01, sh=8)
            g = pop(t, c2 + .3, .3)
            if g > 0: circle(im, 700, 1100, 90 * g, (250, 236, 200)); T(im, "~%40", 700, 1096, int(52 * g) or 1, INK, M.BOLD)
    ch = ([("Meriç kıyısı · İpsala Ovası", .6, DKBLUE)] if t < c1 else [("Ekim mayısta · hasat eylülde", c1 + .1, GREEN)] if t < c2 else [("Edirne: Türkiye çeltiğinin ~%40'ı", c2 + .1, CLAY)] if t < c3 else [("İlde en çok üretim İpsala'da", c3 + .1, RUST)])
    return rakip(t, k, "İpsala Ovası", "Meriç kıyısı · Edirne", IPC, "İpsala", il, ch, "Kaynak: TÜRKPATENT tescil no. 196 · DHA (Eylül 2025) · Ekonomist (Kasım 2025)", note="Çizim temsilidir")
def s_tane(t):
    k = 'tane'
    def il(im, t):
        put(im, grain(340), 540, 1060, s=(pop(t, .5, .3) or .01), rot=-8, sh=10)
        for i, (n, x) in enumerate((("uzun", 330), ("kalın", 540), ("camsı", 750))):
            chip(im, n, x, 1175, 36, pop(t, wt(k, 0, ["tanesi", "kalın", "camsı"][i]) if i else wt(k, 0, "tanesi") + .3, .25), fill=[GREEN, CLAY, DKBLUE][i])
    ch = []
    return rakip(t, k, "Tanesi", "Tescil belgesine göre", IPC, "İpsala", il, ch, "Kaynak: TÜRKPATENT tescil no. 196 (2016)", note="Çizim temsilidir")
def s_kavga(t):
    k = 'kavga'; im = darkbg(t); im = Image.blend(im, DARK, .35); c1 = ct(k, 1) - .05
    TS(im, "ASIL KAVGA", 540, 400, 110, (255, 206, 84), scale=pop(t, .05, .3) * (1 + .03 * math.sin(t * 8)))
    if t >= c1:
        gL = pop(t, wt(k, 1, "tereyağıyla") - .12, .3); gR = pop(t, wt(k, 1, "ayçiçek") - .12, .3)
        if gL > 0: put(im, butter(260), 280, 900, s=gL, sh=16); chip(im, "Tereyağı", 280, 1130, 46, gL, fill=GOLD, tc=INK)
        if gR > 0: put(im, bottle(140), 800, 860, s=gR, sh=16); chip(im, "Ayçiçek yağı", 800, 1130, 44, gR, fill=GREEN)
        if gL > 0 and gR > 0:
            g = pop(t, wt(k, 1, "ayçiçek") + .25, .3)
            circle(im, 540, 880, 70 * g * (1 + .06 * math.sin(t * 9)), (255, 206, 84)); ImageDraw.Draw(im).ellipse([540 - 70 * g, 880 - 70 * g, 540 + 70 * g, 880 + 70 * g], outline=INK, width=4)
            T(im, "VS", 540, 877, 60, INK, M.BOLD, scale=g); sparkle(im, 540, 880, t, n=6, R=140, seed=9)
            chip(im, "Sen hangisisin? Yorumda yaz", 540, 1290, 42, pop(t, wt(k, 1, "ayçiçek") + .6, .25) * (1 + .03 * math.sin(t * 5)), fill=(60, 44, 30))
    T(im, "Çizim temsilidir", 540, 1690, 24, (230, 214, 184), LORAI, a=.9); return im
def s_cta(t):
    k = 'cta'; im = stage(.44, t, h=820, cy=995); banner(im, "Pilavını nasıl yaparsın?", None, y=320, sz=80)
    put(im, pilav(420), 540, 860 - 200 * (1 - eout(t / .45)), s=1 if t > 0.02 else .01, sh=10); steam(im, 540, 760, t, n=5, spread=200, rise=180)
    chip(im, "Yorumlara yaz", 540, 1110, 46, pop(t, .4, .25), fill=RUST)
    c1 = ct(k, 1) - .05
    if t >= c1:
        chip(im, "Yarın final: lezzet başkenti hangisi?", 540, 1230, 42, pop(t, c1) * (1 + .03 * math.sin(t * 5)), fill=(60, 44, 30)); sparkle(im, 540, 1230, t, n=5, R=300, seed=4)
        if t > c1 + .9: chip(im, "Takip et · @ciceklipatikalar", 540, 1612, 36, pop(t, c1 + .9, .25), fill=PAPER, tc=INK)
    T(im, "Müzik özgündür · Çizim temsilidir", 540, 1690, 24, (92, 70, 44), LORAI, a=.9); return im
F = {'hook': s_hook, 'tescil': s_tescil, 'ova': s_ova, 'tane': s_tane, 'kavga': s_kavga, 'cta': s_cta}
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
                d.ellipse([540 - r - 26, 960 - r - 26, 540 + r + 26, 960 + r + 26], outline=(150, 90, 40), width=26); d.ellipse([540 - r, 960 - r, 540 + r, 960 + r], outline=(240, 210, 160), width=12)
            M.caption(im, now); return im
exec("if __name__" + _c.split("if __name__")[1])
