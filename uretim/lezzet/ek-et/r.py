#!/usr/bin/env python3
import os; os.chdir('/home/claude/lezzet/et')
_s = open('/home/claude/lezzet/tt/r.py').read().replace("/home/claude/lezzet/tt", "/home/claude/lezzet/et")
exec(_s.split("\nF = {")[0])
SER = "Trakya Lezzet Rotası · Kuzu ve Ciğer"
CORC = PT(41.16, 27.80)

@lru_cache(None)
def sheep(w=220, face=(70, 56, 50)):
    c = C(w + 20, int(w * .8) + 20); o = 10
    def wool(d):
        rs = random.Random(5)
        for i in range(16):
            x, y = o + w * rs.uniform(.15, .75), o + w * rs.uniform(.15, .45); r = w * rs.uniform(.1, .15); d.ellipse(S(x - r, y - r, x + r, y + r), fill=255)
    c.fill(lambda d: [d.rectangle(S(x, o + w * .45, x + w * .07, o + w * .72), fill=255) for x in (o + w * .22, o + w * .34, o + w * .56, o + w * .66)], face, ink=2)
    c.fill(wool, (246, 242, 230), top=1.08, bot=.86, ink=2.5)
    c.fill(lambda d: d.ellipse(S(o + w * .72, o + w * .16, o + w * .98, o + w * .42), fill=255), face, top=1.1, bot=.85, ink=2.5)
    return c.done()
@lru_cache(None)
def sarma(w=120, seed=1, egg=False):
    c = C(w + 20, int(w * .8) + 20); o = 10
    c.fill(lambda d: d.ellipse(S(o, o, o + w, o + w * .8), fill=255), (176, 106, 60) if not egg else (214, 160, 80), top=1.35, bot=.7, noise=12, seed=seed, ink=2.5)
    im = c.done(); d = ImageDraw.Draw(im)
    for j in range(5): d.arc([o + w * .1, o + w * (.05 + j * .12), o + w * .9, o + w * (.4 + j * .12)], 200, 340, fill=(240, 220, 190, 150), width=2)
    return im
@lru_cache(None)
def tray(n=5, egg=False, w=440):
    c = C(w + 20, int(w * .55) + 20); o = 10
    c.fill(lambda d: d.rounded_rectangle(S(o, o + w * .08, o + w, o + w * .5), 20 * SS_, fill=255), (186, 98, 52), top=1.25, bot=.75, ink=3)
    c.over(lambda d: d.rounded_rectangle(S(o + w * .05, o + w * .12, o + w * .95, o + w * .46), 14 * SS_, fill=(70, 40, 26, 255)))
    im = c.done()
    for i in range(n): put(im, sarma(int(w * .2), i + (9 if egg else 1), egg), o + w * (.16 + i * .17), o + w * (.25 + (i % 2) * .08))
    return im

def s_hook(t):
    k = 'hook'; im = darkbg(t); c1, c2 = ct(k, 1) - .05, ct(k, 2) - .05
    chip(im, SER, 540, 300, 34, 1, fill=PAPER, tc=INK)
    if t < c2:
        TS(im, "İKİ SARMA", 540, 450, 100, (252, 244, 222), scale=pop(t, .05, .3)); TS(im, "İKİ TESCİL", 540, 570, 108, (255, 206, 84), scale=pop(t, .25, .3) * (1 + .03 * math.sin(t * 7)))
        put(im, tray(4, False, 400), 290, 1000 + 6 * math.sin(t * 2.4), s=pop(t, .4, .3) * .9 or .01, sh=16); put(im, stamp("2022", 120), 290, 820, s=pop(t, .6, .25), rot=-10)
        put(im, tray(4, True, 400), 790, 1000 + 6 * math.sin(t * 2.4 + 1), s=pop(t, .55, .3) * .9 or .01, sh=16); put(im, stamp("2024", 120), 790, 820, s=pop(t, .75, .25), rot=10)
        if t >= c1:
            chip(im, "Edirne", 290, 1180, 46, pop(t, c1 + .1, .25), fill=(120, 60, 110)); chip(im, "Çorlu", 790, 1180, 46, pop(t, wt(k, 1, "çorlu") - .1, .25), fill=GREEN)
            g = pop(t, wt(k, 1, "çorlu") + .2, .3); circle(im, 540, 1000, 66 * g, (255, 206, 84)); T(im, "VS", 540, 997, 56, INK, M.BOLD, scale=g)
    else:
        u = t - c2; put(im, sheep(320), 540 - 300 + 300 * eout(u / .6), 1020 + 10 * abs(math.sin(u * 8)), s=1, sh=14)
        TS(im, "ÖNCE KUZU", 540, 520, 100, (252, 244, 222), scale=pop(t, c2, .3))
    T(im, "Kaynak: TRT Haber (2022) · TÜRKPATENT tescil no. 1604 (2024) · Çizim temsilidir", 540, 1690, 22, (230, 214, 184), LORAI, a=.9); return im
def s_kuzu(t):
    k = 'kuzu'; c1 = ct(k, 1) - .05
    def il(im, t):
        if t < c1: put(im, sheep(260), 470, 1110, s=(pop(t, .6, .3) or .01), sh=10); put(im, stamp("2021", 140), 790, 1050, s=pop(t, wt(k, 0, "tescilli") - .1, .3), rot=-12, sh=6)
        else:
            im.paste(Image.composite(hills(700, 300), Image.new('RGB', (700, 300)), Image.new('L', (700, 300), 255)), (190, 950)) if False else None
            for j in range(3): put(im, sheep(170), 330 + j * 210, 1110 + 8 * math.sin(t * 3 + j), s=pop(t, c1 + j * .12, .25) or .01, sh=6)
    ch = [("Menşe adı · 2021", wt(k, 0, "menşe") - .1, RUST)] if t < c1 else [("3–6 aylık · orman içi ve çevre meralar", c1 + .2, GREEN)]
    return rakip(t, k, "Kıvırcık kuzusu", "Kırklareli", KIR, "Kırklareli", il, ch, "Kaynak: TÜRKPATENT tescil no. 680 (2021)", note="İğne il merkezini gösterir · Çizim temsilidir")
def s_satir(t):
    k = 'satir'; c1 = ct(k, 1) - .05
    def il(im, t):
        put(im, block(), 460, 1120, s=(pop(t, .6, .3) or .01) * .95, sh=10); put(im, cleaver(190), 630, 1030 - 30 * abs(math.sin(t * 5)), s=pop(t, .8, .25), rot=-28 + 14 * math.sin(t * 5), sh=6)
        put(im, sheep(130), 820, 1150, s=pop(t, 1.0, .25), sh=4)
    ch = [("Ağırlıklı olarak kıvırcık süt kuzusu", .6, (120, 60, 110))] if t < c1 else [("Meşe kütüğünde satırla · makine yok", c1 + .1, CLAY)]
    return rakip(t, k, "Keşan satır et", "Keşan · Edirne", KESC, "Keşan", il, ch, "Kaynak: TÜRKPATENT tescil no. 153 · Trakya Gezi Rehberi")
def s_edirne(t):
    k = 'edirne'; c1 = ct(k, 1) - .05
    def il(im, t):
        put(im, tray(5, False, 440), 470, 1110, s=(pop(t, .6, .3) or .01), sh=10); put(im, stamp("2022", 140), 800, 1050, s=pop(t, wt(k, 0, "tescillendi") - .1, .3), rot=-12, sh=6)
    ch = [("Coğrafi işaret · 2022", wt(k, 0, "tescillendi") - .1, (120, 60, 110))] if t < c1 else [("Ciğer + iç pilav · kuzu gömleği", c1 + .1, CLAY)]
    return rakip(t, k, "Edirne ciğer sarması", "Edirne Merkez", EDC, "Edirne", il, ch, "Kaynak: TRT Haber, 20 Temmuz 2022", note="İğne il merkezini gösterir · Çizim temsilidir")
def s_corlu(t):
    k = 'corlu'; c1 = ct(k, 1) - .05
    def il(im, t):
        put(im, tray(5, True, 440), 470, 1110, s=(pop(t, .6, .3) or .01), sh=10); put(im, stamp("2024", 140), 800, 1050, s=pop(t, wt(k, 0, "tescil") - .1, .3), rot=-12, sh=6)
    ch = [("Mahreç işareti · 2024", wt(k, 0, "tescil") - .1, GREEN)] if t < c1 else [("Ciğer takımı · \"ciğer bohçası\"", c1 + .1, GOLD)]
    return rakip(t, k, "Çorlu kuzu ciğer sarma", "Çorlu · Tekirdağ", CORC, "Çorlu", il, ch, "Kaynak: TÜRKPATENT tescil no. 1604 (2024)")
def s_kavga(t):
    k = 'kavga'; im = darkbg(t); im = Image.blend(im, DARK, .35); c1 = ct(k, 1) - .05
    TS(im, "KARAR SİZDE", 540, 400, 104, (255, 206, 84), scale=pop(t, .05, .3) * (1 + .03 * math.sin(t * 8)))
    if t >= c1:
        gL = pop(t, wt(k, 1, "edirne") - .12, .3); gR = pop(t, wt(k, 1, "çorlu") - .12, .3)
        if gL > 0: put(im, tray(3, False, 380), 280, 880, s=gL * .9, sh=16); chip(im, "Edirne", 280, 1110, 48, gL, fill=(120, 60, 110))
        if gR > 0: put(im, tray(3, True, 380), 800, 880, s=gR * .9, sh=16); chip(im, "Çorlu", 800, 1110, 48, gR, fill=GREEN)
        if gL > 0 and gR > 0:
            g = pop(t, wt(k, 1, "çorlu") + .25, .3)
            circle(im, 540, 880, 70 * g * (1 + .06 * math.sin(t * 9)), (255, 206, 84)); ImageDraw.Draw(im).ellipse([540 - 70 * g, 880 - 70 * g, 540 + 70 * g, 880 + 70 * g], outline=INK, width=4)
            T(im, "VS", 540, 877, 60, INK, M.BOLD, scale=g); sparkle(im, 540, 880, t, n=6, R=140, seed=9)
            chip(im, "Hangisi daha iyi? Yorumda yaz", 540, 1290, 42, pop(t, wt(k, 1, "çorlu") + .5, .25) * (1 + .03 * math.sin(t * 5)), fill=(60, 44, 30))
    T(im, "Çizim temsilidir", 540, 1690, 24, (230, 214, 184), LORAI, a=.9); return im
def s_cta(t):
    k = 'cta'; im = stage(.44, t, h=820, cy=995); banner(im, "Edirne mi, Çorlu mu?", None, y=320, sz=84)
    put(im, sarma(220, 3), 300, 860 - 260 * (1 - eout((t - .1) / .45)), s=1 if t > .1 else .01, sh=10)
    put(im, sarma(220, 11, True), 780, 860 - 260 * (1 - eout((t - .2) / .45)), s=1 if t > .2 else .01, sh=10)
    g = pop(t, .45, .3); circle(im, 540, 860, 62 * g, (255, 206, 84)); T(im, "?", 540, 856, 70, INK, M.BOLD, scale=g)
    if t > .7: sparkle(im, 540, 860, t, n=6, R=170, seed=7)
    chip(im, "Edirne", 300, 1050, 44, pop(t, .5, .22), fill=(120, 60, 110)); chip(im, "Çorlu", 780, 1050, 44, pop(t, .6, .22), fill=GREEN)
    chip(im, "Hangisi? Yorumda yaz", 540, 1160, 42, pop(t, .8, .22), fill=RUST)
    c1 = ct(k, 1) - .05
    if t >= c1:
        chip(im, "Ciğerci arkadaşını etiketle", 540, 1270, 42, pop(t, c1) * (1 + .03 * math.sin(t * 5)), fill=(60, 44, 30))
        if t > c1 + .9: chip(im, "Takip et · @ciceklipatikalar", 540, 1612, 36, pop(t, c1 + .9, .25), fill=PAPER, tc=INK)
    T(im, "Müzik özgündür · Çizim temsilidir", 540, 1690, 24, (92, 70, 44), LORAI, a=.9); return im
F = {'hook': s_hook, 'kuzu': s_kuzu, 'satir': s_satir, 'edirne': s_edirne, 'corlu': s_corlu, 'kavga': s_kavga, 'cta': s_cta}
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
