# Yüksek kaliteli çizim parçaları: 3x örneklemeli, gölgeli, önbellekli sprite'lar
import math, random
from functools import lru_cache
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageFont
SS = 3
INKC = (66, 44, 28)
LORA = '/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf'
def S(*v): return [x * SS for x in v]
def SP(pts): return [(x * SS, y * SS) for x, y in pts]

def _grad(mask, col, top, bot, noise, seed):
    w, h = mask.size; bb = mask.getbbox() or (0, 0, w, h)
    g = np.full(h, bot, np.float32); g[:bb[1]] = top; g[bb[1]:bb[3]] = np.linspace(top, bot, bb[3] - bb[1])
    a = np.array(col, np.float32)[None, None, :] * g[:, None, None] * np.ones((1, w, 1), np.float32)
    if noise:
        rng = np.random.default_rng(seed); n = rng.normal(0, noise, (h // SS + 1, w // SS + 1))
        a += np.kron(n, np.ones((SS, SS)))[:h, :w, None]
    return Image.fromarray(np.dstack([np.clip(a, 0, 255).astype(np.uint8), np.asarray(mask)]), 'RGBA')

class C:
    def __init__(s, w, h):
        s.w, s.h = w, h; s.im = Image.new('RGBA', (w * SS, h * SS), (0, 0, 0, 0))
    @property
    def d(s): return ImageDraw.Draw(s.im)
    def fill(s, fn, col, top=1.12, bot=.82, noise=0, seed=1, ink=2.5, inkc=INKC):
        m = Image.new('L', s.im.size, 0); fn(ImageDraw.Draw(m))
        if ink:
            k = int(ink * SS) * 2 + 1; ring = m.filter(ImageFilter.MaxFilter(k))
            lay = Image.new('RGBA', s.im.size, inkc + (0,)); lay.putalpha(ring); s.im.alpha_composite(lay)
        s.im.alpha_composite(_grad(m, col, top, bot, noise, seed)); return m
    def over(s, fn, clip=None):
        lay = Image.new('RGBA', s.im.size, (0, 0, 0, 0)); fn(ImageDraw.Draw(lay))
        if clip is not None: lay.putalpha(ImageChops.multiply(lay.getchannel('A'), clip))
        s.im.alpha_composite(lay)
    def done(s): return s.im.resize((s.w, s.h), Image.LANCZOS)

_sh = {}
def shadow(sp, blur=14, op=.34):
    k = (id(sp), blur)
    if k not in _sh:
        p = blur * 3; a = Image.new('L', (sp.width + 2 * p, sp.height + 2 * p), 0); a.paste(sp.getchannel('A'), (p, p))
        a = a.filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v * op))
        o = Image.new('RGBA', a.size, (40, 26, 14, 0)); o.putalpha(a); _sh[k] = o
    return _sh[k]
def _put(im, sp, cx, cy, s, rot, a):
    if s != 1: sp = sp.resize((max(1, int(sp.width * s)), max(1, int(sp.height * s))), Image.BICUBIC)
    if rot: sp = sp.rotate(rot, Image.BICUBIC, expand=True)
    if a < 1:
        sp = sp.copy(); sp.putalpha(sp.getchannel('A').point(lambda v: int(v * a)))
    im.paste(sp, (int(cx - sp.width / 2), int(cy - sp.height / 2)), sp)
def put(im, sp, cx, cy, s=1., rot=0., a=1., sh=0):
    if s <= .02 or a <= 0: return
    if sh: _put(im, shadow(sp), cx + sh * .35, cy + sh, s, rot, a)
    _put(im, sp, cx, cy, s, rot, a)

@lru_cache(None)
def kofte(L=200, q=0):
    hg = int(L * .3); c = C(L + 14, hg + 14); raw = (198, 116, 96); ck = (132, 74, 38)
    col = tuple(int(raw[i] + (ck[i] - raw[i]) * q / 6) for i in range(3)); box = S(7, 7, 7 + L, 7 + hg); r = hg * SS // 2
    m = c.fill(lambda d: d.rounded_rectangle(box, r, fill=255), col, top=1.24, bot=.7, noise=7, seed=L + q)
    c.over(lambda d: d.rounded_rectangle(S(7 + L * .1, 7 + hg * .14, 7 + L * .9, 7 + hg * .34), hg * SS // 7, fill=(255, 236, 214, 62)), m)
    if q >= 3:
        a = int(215 * (q - 2) / 4); n = max(3, L // 44)
        def marks(d):
            for i in range(n):
                x = 7 + L * (.14 + .72 * i / (n - 1)); d.line(S(x + hg * .2, 4, x - hg * .2, 10 + hg), fill=(50, 26, 12, a), width=int(hg * .13 * SS))
        c.over(marks, m)
    return c.done()

@lru_cache(None)
def plate(w=660):
    h = int(w * .38); c = C(w + 20, h + 20)
    c.fill(lambda d: d.ellipse(S(10, 10, 10 + w, 10 + h), fill=255), (246, 244, 236), top=1.03, bot=.9)
    c.over(lambda d: d.ellipse(S(10 + w * .11, 10 + h * .13, 10 + w * .89, 10 + h * .85), outline=(196, 190, 176, 255), width=3 * SS))
    c.over(lambda d: d.ellipse(S(10 + w * .13, 10 + h * .16, 10 + w * .87, 10 + h * .83), fill=(236, 233, 222, 255)))
    return c.done()

@lru_cache(None)
def bread():
    c = C(210, 200)
    body = lambda d: (d.ellipse(S(18, 14, 192, 136), fill=255), d.rounded_rectangle(S(34, 74, 176, 184), 20 * SS, fill=255))
    c.fill(body, (178, 118, 58), top=1.12, bot=.86)
    inner = lambda d: (d.ellipse(S(31, 27, 179, 128), fill=255), d.rounded_rectangle(S(47, 78, 163, 171), 13 * SS, fill=255))
    m = c.fill(inner, (240, 220, 178), top=1.04, bot=.93, noise=5, ink=0)
    rs = random.Random(4)
    def holes(d):
        for i in range(26):
            x, y, r = rs.uniform(50, 160), rs.uniform(45, 160), rs.uniform(2, 5); d.ellipse(S(x - r, y - r * .7, x + r, y + r * .7), fill=(214, 186, 136, 255))
    c.over(holes, m); return c.done()

@lru_cache(None)
def onion():
    c = C(200, 210)
    sh = lambda d: (d.ellipse(S(22, 58, 178, 196), fill=255), d.polygon(SP([(78, 78), (100, 14), (122, 78)]), fill=255))
    m = c.fill(sh, (214, 150, 72), top=1.2, bot=.76)
    def lines(d):
        for k in (-52, -26, 0, 26, 52):
            d.arc(S(100 - abs(k) * 1.5 - 4, 40, 100 + abs(k) * 1.5 + 4, 200), 90 if k < 0 else 270, 270 if k < 0 else 90, fill=(160, 98, 40, 170), width=2 * SS) if k else d.line(S(100, 30, 100, 194), fill=(160, 98, 40, 150), width=2 * SS)
        d.ellipse(S(52, 82, 84, 128), fill=(255, 236, 190, 90))
    c.over(lines, m)
    c.over(lambda d: [d.line(S(100 + k, 194, 100 + k * 2, 206), fill=INKC + (255,), width=2 * SS) for k in (-8, 0, 8)])
    return c.done()

@lru_cache(None)
def garlic():
    c = C(200, 210)
    sh = lambda d: (d.ellipse(S(24, 70, 176, 196), fill=255), d.polygon(SP([(70, 96), (92, 20), (108, 20), (130, 96)]), fill=255))
    m = c.fill(sh, (244, 236, 218), top=1.05, bot=.84)
    def lines(d):
        for k in (-40, 0, 40):
            d.arc(S(60 + k - 30, 60, 60 + k + 110, 230), 200, 300, fill=(176, 160, 134, 230), width=2 * SS)
        d.arc(S(40, 60, 160, 240), 240, 300, fill=(190, 150, 170, 120), width=5 * SS)
    c.over(lines, m)
    c.over(lambda d: d.ellipse(S(84, 186, 116, 200), fill=(170, 140, 100, 255)))
    return c.done()

@lru_cache(None)
def cumin():
    c = C(210, 190)
    c.fill(lambda d: d.chord(S(20, 10, 190, 180), 0, 180, fill=255), (160, 104, 60), top=1.1, bot=.74)
    c.fill(lambda d: d.ellipse(S(20, 72, 190, 118), fill=255), (132, 84, 46), top=1.0, bot=.9)
    m = c.fill(lambda d: d.ellipse(S(34, 62, 176, 110), fill=255), (168, 124, 62), top=1.12, bot=.9, noise=14, ink=0)
    rs = random.Random(2)
    def seeds(d):
        for i in range(60):
            x, y, a = rs.uniform(42, 168), rs.uniform(68, 104), rs.uniform(0, 3.14); d.line(S(x - 5 * math.cos(a), y - 3 * math.sin(a), x + 5 * math.cos(a), y + 3 * math.sin(a)), fill=(112, 76, 30, 255), width=int(1.6 * SS))
    c.over(seeds, m); return c.done()

@lru_cache(None)
def bowl(w=520):
    h = int(w * .56); c = C(w + 20, h + 30); x0 = 10
    c.fill(lambda d: d.chord(S(x0, 20 - h * .55, x0 + w, 20 + h * .98), 0, 180, fill=255), (226, 214, 196), top=1.08, bot=.78)
    c.over(lambda d: d.arc(S(x0 + w * .06, 20 - h * .3, x0 + w * .94, 20 + h * .8), 20, 160, fill=(70, 104, 128, 200), width=5 * SS))
    c.fill(lambda d: d.ellipse(S(x0, 20 + h * .08, x0 + w, 20 + h * .38), fill=255), (206, 194, 176), top=1.0, bot=.92)
    m = c.fill(lambda d: (d.ellipse(S(x0 + w * .05, 20 + h * .1, x0 + w * .95, 20 + h * .35), fill=255), d.ellipse(S(x0 + w * .16, 20 - h * .06, x0 + w * .84, 20 + h * .3), fill=255)), (200, 104, 90), top=1.2, bot=.84, noise=13, ink=0)
    rs = random.Random(7)
    def strands(d):
        for i in range(90):
            x, y = rs.uniform(x0 + w * .12, x0 + w * .88), rs.uniform(20 - h * .02, 20 + h * .32); a = rs.uniform(0, 3.14); l = rs.uniform(6, 13)
            d.line(S(x - l * math.cos(a), y - l * .5 * math.sin(a), x + l * math.cos(a), y + l * .5 * math.sin(a)), fill=rs.choice([(232, 150, 130, 220), (170, 70, 62, 200), (246, 214, 196, 200)]), width=int(2.2 * SS))
    c.over(strands, m); return c.done()

@lru_cache(None)
def pinsp():
    c = C(120, 170)
    m = c.fill(lambda d: (d.ellipse(S(10, 10, 110, 110), fill=255), d.polygon(SP([(22, 86), (60, 162), (98, 86)]), fill=255)), (176, 66, 40), top=1.2, bot=.8)
    c.over(lambda d: d.ellipse(S(40, 40, 80, 80), fill=(250, 240, 220, 255))); return c.done()

@lru_cache(None)
def scale_sp():
    c = C(720, 330)
    c.fill(lambda d: d.rounded_rectangle(S(60, 120, 660, 310), 34 * SS, fill=255), (96, 100, 108), top=1.18, bot=.74)
    c.fill(lambda d: d.rectangle(S(300, 60, 420, 124), fill=255), (132, 136, 142), top=1.0, bot=.8, ink=2)
    c.fill(lambda d: d.rounded_rectangle(S(20, 20, 700, 66), 20 * SS, fill=255), (214, 218, 220), top=1.1, bot=.82)
    c.fill(lambda d: d.rounded_rectangle(S(235, 170, 485, 270), 14 * SS, fill=255), (196, 220, 186), top=1.04, bot=.92, ink=2)
    c.over(lambda d: (d.ellipse(S(110, 196, 158, 244), fill=(60, 64, 70, 255)), d.ellipse(S(562, 196, 610, 244), fill=(176, 66, 40, 255))))
    return c.done()

@lru_cache(None)
def ruler(cm=7, px=80):
    L = cm * px; c = C(L + 60, 110)
    m = c.fill(lambda d: d.rounded_rectangle(S(8, 8, L + 52, 100), 8 * SS, fill=255), (232, 196, 112), top=1.1, bot=.88)
    f = ImageFont.truetype(LORA, 26 * SS)
    def ticks(d):
        for i in range(cm * 10 + 1):
            x = 30 + i * px / 10; ln = 34 if i % 10 == 0 else 24 if i % 5 == 0 else 14
            d.line(S(x, 9, x, 9 + ln), fill=INKC + (255,), width=int((2.4 if i % 10 == 0 else 1.5) * SS))
        for i in range(cm + 1):
            t = str(i); w_ = d.textlength(t, font=f); d.text((30 * SS + i * px * SS - w_ / 2, 50 * SS), t, font=f, fill=INKC + (255,))
    c.over(ticks, m); return c.done()

@lru_cache(None)
def sac(w=760, h=300):
    c = C(w + 40, h + 40)
    m = c.fill(lambda d: d.rounded_rectangle(S(20, 20, 20 + w, 20 + h), 22 * SS, fill=255), (76, 72, 72), top=1.15, bot=.8, ink=3)
    def ridges(d):
        for x in range(46, w, 30):
            d.line(S(20 + x, 34, 20 + x, 6 + h), fill=(118, 112, 110, 255), width=5 * SS); d.line(S(26 + x, 34, 26 + x, 6 + h), fill=(40, 38, 40, 255), width=4 * SS)
    c.over(ridges, m)
    c.over(lambda d: d.rounded_rectangle(S(20, 20, 20 + w, 20 + h), 22 * SS, outline=(110, 104, 102, 255), width=6 * SS))
    return c.done()

@lru_cache(None)
def brazier(w=700, h=210):
    c = C(w + 40, h + 130)
    for lx in (90, w - 50):
        c.fill(lambda d, lx=lx: d.polygon(SP([(lx, h), (lx + 30, h), (lx + 14, h + 120), (lx - 4, h + 120)]), fill=255), (60, 56, 56), top=1., bot=.8)
    c.fill(lambda d: d.polygon(SP([(20, 20), (20 + w, 20), (w - 20, 20 + h), (60, 20 + h)]), fill=255), (70, 64, 62), top=1.2, bot=.72, ink=3)
    c.over(lambda d: d.rectangle(S(20, 20, 20 + w, 44), fill=(104, 96, 92, 255)))
    return c.done()

@lru_cache(None)
def puff(r=90, col=(246, 240, 228), peak=150):
    n = 2 * r; y, x = np.mgrid[0:n, 0:n]; d2 = ((x - r) ** 2 + (y - r) ** 2) / (r * .45) ** 2
    a = (np.exp(-d2) * peak).astype(np.uint8); rgb = np.ones((n, n, 3), np.uint8) * np.array(col, np.uint8)
    return Image.fromarray(np.dstack([rgb, a]), 'RGBA')

@lru_cache(None)
def seal(year="2020"):
    c = C(460, 560); cx, cy, R = 230, 220, 178
    for sx in (-1, 1):
        c.fill(lambda d, sx=sx: d.polygon(SP([(cx + sx * 20, cy + 120), (cx + sx * 120, cy + 110), (cx + sx * 150, cy + 320), (cx + sx * 96, cy + 282), (cx + sx * 50, cy + 330)]), fill=255), (128, 54, 30), top=1.05, bot=.8)
    def ros(d):
        d.ellipse(S(cx - R, cy - R, cx + R, cy + R), fill=255)
        for i in range(28):
            a = i / 28 * 2 * math.pi; x, y = cx + math.cos(a) * R, cy + math.sin(a) * R; d.ellipse(S(x - 24, y - 24, x + 24, y + 24), fill=255)
    c.fill(ros, (168, 72, 40), top=1.18, bot=.8)
    c.over(lambda d: d.ellipse(S(cx - 150, cy - 150, cx + 150, cy + 150), fill=(250, 240, 214, 255)))
    c.over(lambda d: d.ellipse(S(cx - 136, cy - 136, cx + 136, cy + 136), outline=(168, 72, 40, 255), width=3 * SS))
    def txt(d):
        for s_, y, sz, col in (("TEKİRDAĞ", cy - 84, 34, (150, 70, 40)), ("KÖFTESİ", cy - 44, 34, (150, 70, 40)), (year, cy + 26, 84, (66, 44, 28)), ("COĞRAFİ İŞARET", cy + 92, 22, (150, 70, 40))):
            f = ImageFont.truetype(LORA, sz * SS)
            try: f.set_variation_by_name('Bold')
            except Exception: pass
            w_ = d.textlength(s_, font=f); b = f.getbbox(s_); d.text((cx * SS - w_ / 2, y * SS - (b[1] + b[3]) / 2), s_, font=f, fill=col + (255,))
    c.over(txt); return c.done()

@lru_cache(None)
def panel(w, h, r=34):
    c = C(w + 8, h + 8)
    c.fill(lambda d: d.rounded_rectangle(S(4, 4, 4 + w, 4 + h), r * SS, fill=255), (250, 241, 216), top=1.0, bot=.965, noise=2.2, ink=1.6, inkc=(120, 86, 52))
    c.over(lambda d: d.rounded_rectangle(S(20, 20, w - 12, h - 12), (r - 12) * SS, outline=(196, 160, 110, 255), width=int(1.6 * SS)))
    return c.done()
