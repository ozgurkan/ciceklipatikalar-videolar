#!/usr/bin/env python3
import os; os.chdir('/home/claude/lezzet/tt')
_s = open('/home/claude/lezzet/kf/r.py').read().replace("os.chdir('/home/claude/lezzet/kf')", "os.chdir('/home/claude/lezzet/tt')")
_s = _s.replace("_s = _s.replace(\"os.chdir('/home/claude/lezzet/s1')\", \"os.chdir('/home/claude/lezzet/kf')\")", "_s = _s.replace(\"os.chdir('/home/claude/lezzet/s1')\", \"os.chdir('/home/claude/lezzet/tt')\")")
exec(_s.split("\nF = {")[0])
SER = "Trakya Lezzet Rotası · Tatlı Yarışı"
SYR = (214, 140, 40); GOLDB = (226, 172, 80)
ILC = {"Kırklareli": RUST, "Edirne": (120, 60, 110), "Tekirdağ": GREEN}
ALLT = [("Hayrabolu tatlısı", "Hayrabolu", "Tekirdağ"), ("Tekirdağ peynir helvası", "Tekirdağ", "Tekirdağ"), ("Edirne badem ezmesi", "Edirne", "Edirne"), ("Deva-i misk helvası", "Edirne", "Edirne"), ("Brakana tatlısı", "Babaeski · Büyükmandıra", "Kırklareli")]

# ---------- tatlı çizimleri ----------
@lru_cache(None)
def hayra(w=360):
    c = C(w + 20, int(w * .62) + 20); o = 10
    c.fill(lambda d: d.rounded_rectangle(S(o, o + w * .1, o + w, o + w * .6), 18 * SS_, fill=255), (200, 196, 190), top=1.1, bot=.85, ink=3)
    im = c.done(); n = 0
    for r in range(2):
        for q in range(3):
            pc = C(int(w * .3), int(w * .2)); pc.fill(lambda d: d.rounded_rectangle(S(4, 4, w * .3 - 4, w * .2 - 4), 10 * SS_, fill=255), (214, 146, 66), top=1.35, bot=.75, noise=10, seed=n, ink=2.5)
            p = pc.done(); dd = ImageDraw.Draw(p); rs = random.Random(n)
            for i in range(10): x, y = rs.uniform(10, w * .3 - 10), rs.uniform(8, w * .2 - 8); dd.ellipse([x - 3, y - 2, x + 3, y + 2], fill=(250, 226, 170, 200))
            put(im, p, o + w * (.2 + q * .3), o + w * (.25 + r * .22)); n += 1
    d = ImageDraw.Draw(im)
    for i in range(18): x, y = random.Random(i).uniform(o + 30, o + w - 30), random.Random(i + 50).uniform(o + w * .16, o + w * .5); d.ellipse([x - 4, y - 3, x + 4, y + 3], fill=(120, 80, 40))
    return im
@lru_cache(None)
def helva(w=360, ice=False):
    c = C(w + 20, int(w * .6) + 20); o = 10
    c.fill(lambda d: d.ellipse(S(o, o + w * .1, o + w, o + w * .58), fill=255), (248, 244, 236), top=1.05, bot=.9, ink=2.5)
    im = c.done()
    for i in range(3):
        pc = C(int(w * .3), int(w * .22)); pc.fill(lambda d: d.ellipse(S(4, 4, w * .3 - 4, w * .22 - 4), fill=255), GOLDB, top=1.3, bot=.75, noise=16, seed=i + 7, ink=2.5)
        put(im, pc.done(), o + w * (.28 + i * .22), o + w * (.32 + (i % 2) * .06))
    if ice:
        sc = C(int(w * .26), int(w * .24)); sc.fill(lambda d: d.ellipse(S(4, 4, w * .26 - 4, w * .24 - 4), fill=255), (252, 250, 244), top=1.08, bot=.9, ink=2.5)
        put(im, sc.done(), o + w * .74, o + w * .2)
    return im
@lru_cache(None)
def badem(w=360):
    c = C(w + 20, int(w * .6) + 20); o = 10
    c.fill(lambda d: d.rounded_rectangle(S(o, o + w * .12, o + w, o + w * .56), 20 * SS_, fill=255), (176, 40, 34), top=1.15, bot=.8, ink=3)
    im = c.done()
    for i in range(5):
        pc = C(int(w * .17), int(w * .17)); pc.fill(lambda d: d.ellipse(S(4, 4, w * .17 - 4, w * .17 - 4), fill=255), (244, 228, 196), top=1.15, bot=.85, noise=5, seed=i, ink=2.5)
        put(im, pc.done(), o + w * (.16 + i * .17), o + w * .34)
    for i in range(3):
        al = C(60, 36); al.fill(lambda d: d.ellipse(S(4, 4, 56, 32), fill=255), (176, 110, 60), top=1.2, bot=.8, ink=2, seed=i)
        put(im, al.done(), o + w * (.2 + i * .3), o + w * .5, rot=20 * (i - 1))
    return im
@lru_cache(None)
def misk(w=340):
    c = C(w + 20, int(w * .6) + 20); o = 10
    c.fill(lambda d: d.rounded_rectangle(S(o, o + w * .1, o + w, o + w * .55), 16 * SS_, fill=255), (130, 74, 40), top=1.25, bot=.75, noise=18, seed=3, ink=3)
    im = c.done(); d = ImageDraw.Draw(im); rs = random.Random(9)
    for i in range(60):
        x, y = rs.uniform(o + 14, o + w - 14), rs.uniform(o + w * .14, o + w * .5); col = rs.choice([(220, 170, 90), (90, 40, 20), (230, 200, 140), (160, 60, 40)]); s = rs.uniform(2, 4); d.ellipse([x - s, y - s, x + s, y + s], fill=col)
    return im
@lru_cache(None)
def cup(w=260):
    c = C(w + 20, int(w * 1.15)); o = 10
    c.fill(lambda d: (d.polygon(SP([(o + w * .15, o), (o + w * .85, o), (o + w * .72, o + w * .5), (o + w * .28, o + w * .5)]), fill=255),
                      d.rectangle(S(o + w * .44, o + w * .48, o + w * .56, o + w * .78), fill=255), d.rounded_rectangle(S(o + w * .25, o + w * .76, o + w * .75, o + w * .92), 8 * SS_, fill=255)), (236, 186, 60), top=1.35, bot=.75, ink=3)
    c.over(lambda d: (d.arc(S(o - w * .02, o + w * .04, o + w * .3, o + w * .34), 90, 270, fill=(200, 150, 40, 255), width=8 * SS_), d.arc(S(o + w * .7, o + w * .04, o + w * 1.02, o + w * .34), 270, 90, fill=(200, 150, 40, 255), width=8 * SS_)))
    im = c.done(); T(im, "32", o + w * .5, o + w * .22, int(w * .2), (120, 70, 10), M.BOLD); return im

# ---------- sahneler ----------
def s_hook(t):
    k = 'hook'; im = darkbg(t); c1 = ct(k, 1) - .05; c2 = ct(k, 2) - .05
    chip(im, SER, 540, 300, 34, 1, fill=PAPER, tc=INK)
    if t < c1:
        TS(im, "EN İYİ TATLI", 540, 470, 108, (252, 244, 222), scale=pop(t, .05, .3)); TS(im, "HANGİSİ?", 540, 595, 112, (255, 206, 84), scale=pop(t, .2, .3) * (1 + .03 * math.sin(t * 7)))
        for i, (sp, x, y) in enumerate(((hayra(300), 300, 960), (helva(300), 780, 960), (badem(300), 300, 1260), (misk(280), 780, 1260))):
            put(im, sp, x, y + 6 * math.sin(t * 2.5 + i), s=pop(t, .3 + i * .12, .3) or .01, sh=14)
    else:
        sparkle(im, 540, 900, t, n=10, R=420, seed=2)
        put(im, cup(260), 540, 760 + 6 * math.sin(t * 2.4), s=pop(t, c1, .35) or .01, sh=18)
        TS(im, "32 TATLI YARIŞTI", 540, 470, 84, (252, 244, 222), scale=pop(t, c1 + .1, .3))
        if t >= c2:
            put(im, hayra(300), 540, 1130, s=pop(t, c2, .3) or .01, sh=14); put(im, badge(1), 540, 1000, s=1.8 * pop(t, c2 + .2, .3), sh=6)
            chip(im, "Birinci: Hayrabolu tatlısı", 540, 1290, 44, pop(t, c2 + .3, .25), fill=GREEN)
    T(im, "Kaynak: Gazete Vatan, Gazete Birlik, Haberkenti (Nisan 2026) · Çizim temsilidir", 540, 1690, 22, (230, 214, 184), LORAI, a=.9); return im
def s_hayra(t):
    k = 'hayra'; c1 = ct(k, 1) - .05
    def il(im, t):
        put(im, hayra(400), 470, 1110, s=(pop(t, .6, .3) or .01), sh=10)
    ch = [("1972 · ilk adı Kadı Göbeği", wt(k, 0, "kadı") - .1, GREEN)] if t < c1 else [("Tuzsuz peynir + irmik + şerbet", c1 + .1, CLAY)]
    return rakip(t, k, "Hayrabolu tatlısı", "Hayrabolu · Tekirdağ", HAYC, "Hayrabolu", il, ch, "Kaynak: TÜRKPATENT tescil no. 839 · NTV")
def s_helva(t):
    k = 'helva'; c1 = ct(k, 1) - .05
    def il(im, t):
        put(im, helva(400, ice=t >= c1), 470, 1110, s=(pop(t, .6, .3) or .01), sh=10)
        if t < c1: put(im, stamp("2020", 140), 800, 1060, s=pop(t, wt(k, 0, "işaretli") - .1, .3), rot=-12, sh=6)
    ch = [("Coğrafi işaretli", wt(k, 0, "işaretli") - .1, GREEN)] if t < c1 else [("Yazın dondurmayla", c1 + .1, DKBLUE)]
    return rakip(t, k, "Tekirdağ peynir helvası", "Süleymanpaşa · Tekirdağ", TEKC, "Tekirdağ", il, ch, "Kaynak: TRT Haber (2020)")
def s_badem(t):
    k = 'badem'; c1 = ct(k, 1) - .05
    def il(im, t):
        put(im, badem(400), 470, 1110, s=(pop(t, .6, .3) or .01), sh=10)
    ch = [("Osmanlı'dan kalma", wt(k, 0, "osmanlı") - .1, (120, 60, 110))] if t < c1 else [("Badem + şeker · coğrafi işaretli", c1 + .1, CLAY)]
    return rakip(t, k, "Edirne badem ezmesi", "Edirne Merkez", EDC, "Edirne", il, ch, "Kaynak: Milliyet · Akşam · Trakya Gezi Rehberi", note="İğne il merkezini gösterir · Çizim temsilidir")
def s_misk(t):
    k = 'misk'
    def il(im, t): put(im, misk(400), 540, 1110, s=(pop(t, .6, .3) or .01), sh=10)
    return rakip(t, k, "Deva-i misk helvası", "Edirne Merkez", EDC, "Edirne", il, [("39 baharat ve bitki", wt(k, 0, "baharat") - .1, (120, 60, 110))], "Kaynak: TÜRKPATENT tescil no. 643", note="İğne il merkezini gösterir · Çizim temsilidir")
@lru_cache(None)
def brakana(w=380):
    c = C(w + 20, int(w * .6) + 20); o = 10
    c.fill(lambda d: d.ellipse(S(o, o + w * .1, o + w, o + w * .58), fill=255), (90, 60, 140), top=1.15, bot=.8, ink=3)
    im = c.done()
    for i in range(7):
        x = o + w * (.2 + (i % 4) * .2 + (.1 if i >= 4 else 0)); y = o + w * (.27 + (i // 4) * .17)
        pc = C(int(w * .2), int(w * .17)); pc.fill(lambda d: d.ellipse(S(4, 4, w * .2 - 4, w * .17 - 4), fill=255), (196, 120, 50), top=1.4, bot=.7, noise=10, seed=i, ink=2.5)
        p = pc.done(); dd = ImageDraw.Draw(p); cx_, cy_ = p.width / 2, p.height * .45; dd.ellipse([cx_ - 9, cy_ - 6, cx_ + 9, cy_ + 6], fill=(150, 80, 30)); put(im, p, x, y)
    return im
def s_brakana(t):
    k = 'brakana'; c1 = ct(k, 1) - .05; c2 = ct(k, 2) - .05
    def il(im, t):
        put(im, brakana(400), 470, 1110, s=(pop(t, .6, .3) or .01), sh=10)
        if c1 <= t: put(im, stamp("2023", 140), 800, 1060, s=pop(t, c1 + .1, .3), rot=-12, sh=6)
    ch = [("Kırklareli'nin cevabı", .6, RUST)] if t < c1 else ([("1877-78'de yerleşen Pomaklardan", c1 + .4, CLAY)] if t < c2 else [("Düğün ve bayram tatlısı", c2, GOLD)])
    return rakip(t, k, "Brakana tatlısı", "Büyükmandıra · Babaeski", PT(41.43, 27.09), "Babaeski", il, ch, "Kaynak: TÜRKPATENT tescil no. 1494 (2023)")
def s_tablo(t):
    k = 'tablo'; im = stage(.46, t, h=900, cy=1000); banner(im, "Adaylar", None, y=320, sz=84)
    c1 = ct(k, 1) - .05
    for i, (name, ilce, il) in enumerate(ALLT):
        t0 = .1 + i * .12
        if t < t0: continue
        g = eout((t - t0) / .35); y = 620 + i * 108
        rrect(im, 130 + (1 - g) * 120, y - 44, 950, y + 44, 18, (244, 236, 216), .95 * g)
        tw = text_mask(name, 42, LORA).width; T(im, name, 165 + tw / 2 + (1 - g) * 120, y - 12, 42, INK, LORA, a=g)
        sw = text_mask(ilce, 24, LORAI).width; T(im, ilce, 165 + sw / 2 + (1 - g) * 120, y + 24, 24, (104, 80, 54), LORAI, a=g)
        chip(im, il, 840, y, 30, g, fill=ILC[il])
    if t >= c1:
        chip(im, "Hangi il kazanır?", 540, 1300, 48, pop(t, c1, .25) * (1 + .04 * math.sin(t * 6)), fill=(60, 44, 30)); sparkle(im, 540, 1300, t, n=5, R=260, seed=3)
    return im
def s_kavga(t):
    k = 'kavga'; im = darkbg(t); im = Image.blend(im, DARK, .35); c1 = ct(k, 1) - .05
    TS(im, "ASIL KAVGA", 540, 400, 110, (255, 206, 84), scale=pop(t, .05, .3) * (1 + .03 * math.sin(t * 8)))
    if t >= c1:
        gL = pop(t, wt(k, 1, "sıcak") - .12, .3); gR = pop(t, wt(k, 1, "soğuk") - .12, .3)
        if gL > 0: put(im, helva(360), 280, 880, s=gL, sh=16); steam(im, 280, 780, t, n=5, spread=100, rise=220); chip(im, "Sıcak", 280, 1110, 46, gL, fill=RUST)
        if gR > 0: put(im, helva(360, ice=True), 800, 880, s=gR, sh=16); chip(im, "Soğuk", 800, 1110, 46, gR, fill=DKBLUE)
        if gL > 0 and gR > 0:
            g = pop(t, wt(k, 1, "soğuk") + .25, .3)
            circle(im, 540, 880, 70 * g * (1 + .06 * math.sin(t * 9)), (255, 206, 84)); ImageDraw.Draw(im).ellipse([540 - 70 * g, 880 - 70 * g, 540 + 70 * g, 880 + 70 * g], outline=INK, width=4)
            T(im, "VS", 540, 877, 60, INK, M.BOLD, scale=g); sparkle(im, 540, 880, t, n=6, R=140, seed=9)
            chip(im, "Sen hangisisin? Yorumda yaz", 540, 1290, 42, pop(t, wt(k, 1, "soğuk") + .5, .25) * (1 + .03 * math.sin(t * 5)), fill=(60, 44, 30))
    T(im, "Çizim temsilidir", 540, 1690, 24, (230, 214, 184), LORAI, a=.9); return im
def s_cta(t):
    k = 'cta'; im = stage(.44, t, h=820, cy=995); banner(im, "Sence en iyisi hangisi?", None, y=320, sz=80)
    g = eout(t / .45); put(im, podium(), 540, 930 + 200 * (1 - g), a=g, sh=10)
    put(im, hayra(220), 540, 716 + 6 * math.sin(t * 2.6) - 260 * (1 - eout((t - .25) / .45)), s=1 if t > .25 else .01, sh=10)
    put(im, helva(180), 300, 790, s=pop(t, .5, .25), sh=6); put(im, badem(180), 780, 830, s=pop(t, .6, .25), sh=6)
    if t > .7: sparkle(im, 540, 700, t, n=6, R=170, seed=7)
    for i, il in enumerate(("Tekirdağ", "Edirne", "Kırklareli")):
        chip(im, il, 250 + i * 290, 1110, 40, pop(t, .5 + i * .1, .22), fill=list(ILC.values())[[2, 1, 0][i]])
    c1 = ct(k, 1) - .05
    if t >= c1:
        chip(im, "Yorumlara yaz · tatlıcı arkadaşını etiketle", 540, 1270, 38, pop(t, c1) * (1 + .03 * math.sin(t * 5)), fill=(60, 44, 30))
        if t > c1 + .9: chip(im, "Takip et · @ciceklipatikalar", 540, 1612, 36, pop(t, c1 + .9, .25), fill=PAPER, tc=INK)
    T(im, "Müzik özgündür · Çizim temsilidir", 540, 1690, 24, (92, 70, 44), LORAI, a=.9); return im
F = {'hook': s_hook, 'hayra': s_hayra, 'helva': s_helva, 'badem': s_badem, 'misk': s_misk, 'brakana': s_brakana, 'tablo': s_tablo, 'kavga': s_kavga, 'cta': s_cta}
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
                d.ellipse([540 - r - 26, 960 - r - 26, 540 + r + 26, 960 + r + 26], outline=(150, 90, 30), width=26); d.ellipse([540 - r, 960 - r, 540 + r, 960 + r], outline=(250, 226, 170), width=12)
            M.caption(im, now); return im
exec("if __name__" + _c.split("if __name__")[1])
