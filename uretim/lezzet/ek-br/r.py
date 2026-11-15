#!/usr/bin/env python3
import os; os.chdir('/home/claude/lezzet/br')
_s = open('/home/claude/lezzet/tt/r.py').read().replace("/home/claude/lezzet/tt", "/home/claude/lezzet/br")
exec(_s.split("\nF = {")[0])
SER = "Trakya Lezzet Rotası · Göçmen Börekleri"
MALC = PT(40.89, 26.90); HAVC = PT(41.45, 27.0)

@lru_cache(None)
def dizmana(w=440):
    c = C(w + 20, int(w * .62) + 20); o = 10
    c.fill(lambda d: d.ellipse(S(o, o + w * .06, o + w, o + w * .6), fill=255), (60, 56, 56), top=1.15, bot=.8, ink=3)
    im = c.done()
    for r in range(3):
        for q in range(4 - (r % 2)):
            x = o + w * (.2 + q * .2 + (.1 if r % 2 else 0)); y = o + w * (.2 + r * .13)
            pc = C(int(w * .2), int(w * .15)); pc.fill(lambda d: d.ellipse(S(4, 4, w * .2 - 4, w * .15 - 4), fill=255), (226, 168, 92), top=1.4, bot=.75, noise=10, seed=r * 5 + q, ink=2)
            p = pc.done(); dd = ImageDraw.Draw(p); rs = random.Random(r * 5 + q)
            for i in range(6): xx, yy = rs.uniform(8, p.width - 8), rs.uniform(6, p.height - 6); dd.ellipse([xx - 2, yy - 1.5, xx + 2, yy + 1.5], fill=(40, 30, 20))
            put(im, p, x, y)
    return im
@lru_cache(None)
def tikvenik(w=440):
    c = C(w + 20, int(w * .62) + 20); o = 10
    c.fill(lambda d: d.ellipse(S(o, o + w * .06, o + w, o + w * .6), fill=255), (186, 98, 52), top=1.2, bot=.8, ink=3)
    im = c.done(); cx, cy = o + w / 2, o + w * .33; d = ImageDraw.Draw(im)
    for r in range(8, 0, -1):
        rr = w * .045 * r; col = (232, 166, 70) if r % 2 else (214, 120, 40); d.ellipse([cx - rr, cy - rr * .55, cx + rr, cy + rr * .55], fill=col, outline=(150, 80, 30))
    return im
@lru_cache(None)
def pumpkin(w=150):
    c = C(w + 20, int(w * .9) + 20); o = 10
    def body(d):
        for i, dx in enumerate((-.22, 0, .22)): d.ellipse(S(o + w * (.2 + dx), o + w * .15, o + w * (.8 + dx), o + w * .85), fill=255)
    c.fill(body, (230, 130, 40), top=1.3, bot=.75, ink=2.5)
    c.fill(lambda d: d.rectangle(S(o + w * .46, o, o + w * .56, o + w * .2), fill=255), (90, 120, 50), ink=2)
    return c.done()

def s_hook(t):
    k = 'hook'; im = darkbg(t); c1 = ct(k, 1) - .05
    chip(im, SER, 540, 300, 34, 1, fill=PAPER, tc=INK)
    TS(im, "GÖÇLE GELEN", 540, 450, 100, (252, 244, 222), scale=pop(t, .05, .3)); TS(im, "BÖREKLER", 540, 570, 112, (255, 206, 84), scale=pop(t, .25, .3) * (1 + .03 * math.sin(t * 7)))
    put(im, dizmana(400), 300, 1000 + 6 * math.sin(t * 2.4), s=pop(t, .4, .3) * .9 or .01, sh=16); put(im, tikvenik(400), 780, 1000 + 6 * math.sin(t * 2.4 + 1), s=pop(t, .55, .3) * .9 or .01, sh=16)
    steam(im, 540, 880, t, n=5, spread=260, rise=200)
    if t >= c1: chip(im, "Senin ailen nereden geldi?", 540, 1250, 50, pop(t, c1, .25) * (1 + .04 * math.sin(t * 6)), fill=RUST)
    T(im, "Çizim temsilidir", 540, 1690, 24, (230, 214, 184), LORAI, a=.9); return im
def s_diz(t):
    k = 'diz'; c1, c2 = ct(k, 1) - .05, ct(k, 2) - .05
    def il(im, t): put(im, dizmana(440), 540, 1110, s=(pop(t, .6, .3) or .01), sh=10)
    ch = [("Balkan muhacirlerinden", .6, GREEN)] if t < c1 else ([("Mayalı hamur + lor + yoğurtlu sos", c1 + .1, CLAY)] if t < c2 else [("Düğünlerde ve ramazanda", c2 + .1, GOLD)])
    return rakip(t, k, "Dızmana", "Karaiğdemir · Malkara · Tekirdağ", MALC, "Malkara", il, ch, "Kaynak: AA via Habertürk (Şubat 2026) · Gazete Birlik", note="İğne ilçe merkezini gösterir · Çizim temsilidir")
def s_tik(t):
    k = 'tik'; c1 = ct(k, 1) - .05
    def il(im, t): put(im, tikvenik(400), 470, 1110, s=(pop(t, .6, .3) or .01), sh=10); put(im, pumpkin(150), 810, 1120, s=pop(t, .9, .25), sh=6)
    ch = [("Bal kabaklı, tatlı", .6, GOLD)] if t < c1 else [("Trakya'daki Pomak köylerinde", c1 + .1, (120, 60, 110))]
    return rakip(t, k, "Tikvenik", "Pomak mutfağı · Trakya", HAVC, "Trakya", il, ch, "Kaynak: Hürriyet (Pomak mutfağı) · Cumhuriyet (tarif)", note="İğne bölgeyi gösterir · Çizim temsilidir")
def s_soru(t):
    k = 'soru'; c1, c2 = ct(k, 1) - .05, ct(k, 2) - .05
    p = ease(t / 1.6); im, m = cam(1500, 1900, .32 + .02 * t); im = vig(im)
    banner(im, "Aileniz nereden geldi?", None, y=320, sz=80)
    cs = [("Bulgaristan", 330, 700), ("Yunanistan", 750, 700), ("Bosna", 330, 840), ("Makedonya", 750, 840)]
    if t >= c1:
        rrect(im, 120, 610, 960, 930, 30, (252, 244, 222), .9 * min(1, (t - c1) * 4))
        for i, (n, x, y) in enumerate(cs):
            chip(im, n, x, y, 50, pop(t, c1 + i * .4, .25), fill=[GREEN, DKBLUE, RUST, CLAY][i])
    if t >= c2: chip(im, "Böreğinizin adını yorumlara yazın", 540, 1290, 42, pop(t, c2, .25) * (1 + .04 * math.sin(t * 6)), fill=(60, 44, 30))
    T(im, "Çizim temsilidir", 540, 1610, 24, (60, 44, 30), LORAI); return im
def s_kavga(t):
    k = 'kavga'; im = darkbg(t); im = Image.blend(im, DARK, .35); c1 = ct(k, 1) - .05
    TS(im, "ASIL KAVGA", 540, 400, 110, (255, 206, 84), scale=pop(t, .05, .3) * (1 + .03 * math.sin(t * 8)))
    if t >= c1:
        gL = pop(t, wt(k, 1, "tuzlu") - .12, .3); gR = pop(t, wt(k, 1, "tatlı") - .12, .3)
        if gL > 0: put(im, dizmana(380), 280, 880, s=gL * .9, sh=16); chip(im, "Tuzlu", 280, 1110, 48, gL, fill=GREEN)
        if gR > 0: put(im, tikvenik(380), 800, 880, s=gR * .9, sh=16); chip(im, "Tatlı", 800, 1110, 48, gR, fill=GOLD, tc=INK)
        if gL > 0 and gR > 0:
            g = pop(t, wt(k, 1, "tatlı") + .25, .3)
            circle(im, 540, 880, 70 * g * (1 + .06 * math.sin(t * 9)), (255, 206, 84)); ImageDraw.Draw(im).ellipse([540 - 70 * g, 880 - 70 * g, 540 + 70 * g, 880 + 70 * g], outline=INK, width=4)
            T(im, "VS", 540, 877, 60, INK, M.BOLD, scale=g); sparkle(im, 540, 880, t, n=6, R=140, seed=9)
            chip(im, "Sen hangisisin? Yorumda yaz", 540, 1290, 42, pop(t, wt(k, 1, "tatlı") + .5, .25) * (1 + .03 * math.sin(t * 5)), fill=(60, 44, 30))
    T(im, "Çizim temsilidir", 540, 1690, 24, (230, 214, 184), LORAI, a=.9); return im
def s_cta(t):
    k = 'cta'; im = stage(.44, t, h=820, cy=995); banner(im, "Senin böreğin hangisi?", None, y=320, sz=80)
    put(im, dizmana(300), 330, 860, s=pop(t, .1, .3) or .01, sh=10); put(im, tikvenik(300), 750, 860, s=pop(t, .25, .3) or .01, sh=10)
    put(im, pumpkin(110), 540, 760, s=pop(t, .4, .25), sh=6)
    c1 = ct(k, 1) - .05
    chip(im, "Aileni ve böreğini yaz", 540, 1110, 46, pop(t, .4, .25), fill=RUST)
    if t >= c1:
        chip(im, "Hemşehrini etiketle", 540, 1210, 42, pop(t, c1) * (1 + .03 * math.sin(t * 5)), fill=(60, 44, 30))
        if t > c1 + .8: chip(im, "Takip et · @ciceklipatikalar", 540, 1612, 36, pop(t, c1 + .8, .25), fill=PAPER, tc=INK)
    T(im, "Müzik özgündür · Çizim temsilidir", 540, 1690, 24, (92, 70, 44), LORAI, a=.9); return im
F = {'hook': s_hook, 'diz': s_diz, 'tik': s_tik, 'soru': s_soru, 'kavga': s_kavga, 'cta': s_cta}
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
