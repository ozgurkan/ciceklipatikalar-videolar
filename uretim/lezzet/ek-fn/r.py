#!/usr/bin/env python3
import os; os.chdir('/home/claude/lezzet/fn')
_s = open('/home/claude/lezzet/tt/r.py').read().replace("/home/claude/lezzet/tt", "/home/claude/lezzet/fn")
exec(_s.split("\nF = {")[0])
SER = "Trakya Lezzet Rotası · Final"
ILS = [("Edirne", (120, 60, 110)), ("Tekirdağ", GREEN), ("Kırklareli", RUST)]

def s_hook(t):
    k = 'hook'; im = darkbg(t); c1 = ct(k, 1) - .05
    chip(im, SER, 540, 300, 34, 1, fill=PAPER, tc=INK)
    TS(im, "LEZZET", 540, 470, 120, (252, 244, 222), scale=pop(t, .05, .3)); TS(im, "BAŞKENTİ?", 540, 600, 112, (255, 206, 84), scale=pop(t, .25, .3) * (1 + .03 * math.sin(t * 7)))
    crown_y = 820 + 8 * math.sin(t * 3); g = pop(t, .5, .3)
    if g > 0:
        pts = [(400, crown_y + 80), (400, crown_y - 20), (470, crown_y + 30), (540, crown_y - 50), (610, crown_y + 30), (680, crown_y - 20), (680, crown_y + 80)]
        d = ImageDraw.Draw(im); cx = 540; P = [(cx + (x - cx) * g, crown_y + (y - crown_y) * g) for x, y in pts]
        d.polygon(P, fill=(255, 206, 84), outline=INK); sparkle(im, 540, crown_y, t, n=6, R=200, seed=3)
    if t >= c1:
        for i, (n, col) in enumerate(ILS):
            chip(im, n, 220 + i * 320, 1150, 52, pop(t, wt(k, 1, n.lower()) - .1, .25) * (1 + .03 * math.sin(t * 5 + i)), fill=col)
    T(im, "Çizim temsilidir", 540, 1690, 24, (230, 214, 184), LORAI, a=.9); return im
def s_sayi(t):
    k = 'sayi'; im = stage(.46, t, h=1000, cy=1000); banner(im, "Coğrafi işaret sayısı", None, y=320, sz=80)
    c = [ct(k, i) - .05 for i in range(5)]
    vals = [(15, "15", ""), (15, "15", ""), (10, "10", "")]
    for i, ((n, col), (v, lab, src)) in enumerate(zip(ILS, vals)):
        t0 = c[1] + .3 if i == 0 else c[i + 1] + .1
        g = eout((t - t0) / .7) if t >= t0 else 0; y = 640 + i * 190
        T(im, n, 250, y, 44, INK, M.BOLD, a=min(1, g * 3) if t >= t0 else 0)
        if g > 0:
            bw = 520 * v / 15 * g; rrect(im, 360, y - 36, 360 + bw, y + 36, 18, col)
            T(im, str(int(round(v * g))), 360 + bw + 50, y - 2, 48, INK, M.BOLD)
    if t >= c[4]: chip(im, "Edirne – Tekirdağ: BERABERE", 540, 1250, 48, pop(t, c[4], .25) * (1 + .03 * math.sin(t * 6)), fill=(60, 44, 30)); sparkle(im, 540, 1250, t, n=6, R=320, seed=6)
    T(im, "Kaynak: TÜRKPATENT Coğrafi İşaretler Portalı · 15 Kasım 2026", 540, 1580, 24, (92, 70, 44), LORAI)
    T(im, "El sanatı ürünleri dahil · yeni tescillerle değişebilir", 540, 1620, 24, (92, 70, 44), LORAI); return im
def s_seri(t):
    k = 'seri'; im = stage(.44, t, h=1000, cy=1000); banner(im, "Bu seride yarışanlar", None, y=320, sz=80)
    items = [("Peynir", 0, "peynirden"), ("Karpuz", 0, "karpuza"), ("Köfte", 0, "köfteden"), ("Sucuk", 0, "sucuğa"), ("Boza", 1, "bozadan"), ("Börek", 1, "böreğe"), ("Pirinç", 1, "pirince")]
    cols = [GOLD, (60, 130, 70), RUST, (150, 40, 40), CLAY, (186, 98, 52), DKBLUE]
    for i, (n, ch, kw) in enumerate(items):
        x = 300 + (i % 2) * 480; y = 620 + (i // 2) * 150
        if i == 6: x = 540
        g = pop(t, wt(k, ch, kw) - .1, .25)
        chip(im, n, x, y, 50, g, fill=cols[i], tc=INK if cols[i] == GOLD else (255, 255, 255))
    if t > ct(k, 1) + 1: sparkle(im, 540, 900, t, n=8, R=360, seed=5)
    T(im, "Çizim temsilidir", 540, 1690, 24, (92, 70, 44), LORAI, a=.9); return im
def s_oy(t):
    k = 'oy'; im = darkbg(t); im = Image.blend(im, DARK, .35); c1 = ct(k, 1) - .05
    TS(im, "SON SÖZ SİZDE", 540, 420, 100, (255, 206, 84), scale=pop(t, .05, .3) * (1 + .03 * math.sin(t * 8)))
    if t >= c1:
        for i, (n, col) in enumerate(ILS):
            g = pop(t, c1 + i * .25, .3); y = 760 + i * 170
            chip(im, n, 540, y, 64, g * (1 + .03 * math.sin(t * 5 + i)), fill=col)
        sparkle(im, 540, 930, t, n=6, R=330, seed=9)
    T(im, "Çizim temsilidir", 540, 1690, 24, (230, 214, 184), LORAI, a=.9); return im
def s_cta(t):
    k = 'cta'; im = stage(.44, t, h=820, cy=995); banner(im, "Senin ilin hangisi?", None, y=320, sz=84)
    for i, (n, col) in enumerate(ILS): chip(im, n, 220 + i * 320, 800, 46, pop(t, .1 + i * .12, .25), fill=col)
    chip(im, "İlini yaz · hemşehrini etiketle", 540, 960, 44, pop(t, .5, .25), fill=RUST)
    c1 = ct(k, 1) - .05
    if t >= c1:
        chip(im, "Yarın yeni seri: Saklı Doğa", 540, 1100, 46, pop(t, c1) * (1 + .03 * math.sin(t * 5)), fill=(40, 90, 60)); sparkle(im, 540, 1100, t, n=5, R=300, seed=4)
        if t > c1 + .9: chip(im, "Takip et · @ciceklipatikalar", 540, 1612, 36, pop(t, c1 + .9, .25), fill=PAPER, tc=INK)
    T(im, "Müzik özgündür · Çizim temsilidir", 540, 1690, 24, (92, 70, 44), LORAI, a=.9); return im
F = {'hook': s_hook, 'sayi': s_sayi, 'seri': s_seri, 'oy': s_oy, 'cta': s_cta}
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
