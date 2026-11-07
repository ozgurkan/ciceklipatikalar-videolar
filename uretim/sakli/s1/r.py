#!/usr/bin/env python3
import os; os.chdir('/home/claude/sakli/s1')
exec(open('/home/claude/sakli/shead.py').read())
SER="Trakya'nın Saklı Doğası · 1"
def s_hook(t):
    k='hook'; x,y=Q['uzk']; im,m=cam(x,y,.5+.01*t); banner(im,"580 yıllık köprü",SER,y=320,sz=84)
    card(im,90,640,990,1330); water(im,100,1060,980,1320,t)
    stone_bridge(im,110,970,940,16,ease(t/1.6),t)
    if t>=ct(k,1)-.05: chip(im,"Tamamen taş",540,760,52,back((t-ct(k,1)+.05)/.25),fill=RUST)
    mark(im); return im
def s_yer(t):
    k='yer'; x,y=Q['uzk']; im,m=cam(x,y,.8+.03*t); banner(im,"Uzunköprü","Edirne",y=320,sz=90)
    sx,sy=m(x,y); pin(im,sx,sy,t)
    if t>=ct(k,1)-.05: chip(im,"Ergene Nehri",540,1300,48,back((t-ct(k,1)+.05)/.25),fill=DKBLUE)
    mark(im); return im
def s_yapim(t):
    k='yapim'; x,y=Q['uzk']; im,m=cam(x,y,.45); banner(im,"II. Murad",None,y=320,sz=90); card(im,140,640,940,1330)
    s=back(t/.35); circle(im,540,900,150*max(s,.05),RUST); circle(im,540,900,122*max(s,.05),PAPER)
    if s>.6: T(im,"Bitiş",540,870,40,RUST,LORA); T(im,"1443",540,940,56,RUST,LORA)
    if t>=ct(k,1)-.05: chip(im,"Açılış: 1444",540,1180,56,back((t-ct(k,1)+.05)/.25),fill=GREEN)
    return im
def s_olcu(t):
    k='olcu'; c=TM[k]['chunks']; x,y=Q['uzk']; im,m=cam(x,y,.45); banner(im,"Kemer kemer",None,y=320,sz=84); card(im,60,620,1020,1350)
    water(im,70,960,1010,1340,t); n=min(174,int(174*ease((t-.1)/2.2)))
    stone_bridge(im,80,1000,900,24,1.,t)
    T(im,f"{n} kemer",540,730,84,RUST,LORA)
    if t>=c[1][0]-.05: chip(im,"Boyu 1 km'den uzun",540,1100,48,back((t-c[1][0]+.05)/.25),fill=INK)
    if t>=c[2][0]-.05: chip(im,"Kitabede: 174 göz",540,1230,44,back((t-c[2][0]+.05)/.25),fill=GREEN)
    return im
def s_kabartma(t):
    k='kabartma'; x,y=Q['uzk']; im,m=cam(x,y,.45); banner(im,"Taştaki hayvanlar",None,y=320,sz=80); card(im,90,620,990,1340)
    for i,kd in enumerate(['fil','aslan','kuş']):
        if t>=i*.4: relief(im,250+i*290,900,kd,1.3*max(.05,back((t-i*.4)/.3)))
        if t>=i*.4+.2: T(im,kd.capitalize() if kd!='kuş' else 'Kuş',250+i*290,1050,46,INK,LORA)
    if t>=ct(k,1)-.05: T(im,"Bir kısmı hâlâ görülebiliyor",540,1220,42,INK,LORAI,a=clamp((t-ct(k,1))/.3))
    return im
def s_unesco(t):
    k='unesco'; x,y=Q['uzk']; im,m=cam(x,y,.5); banner(im,"2015","UNESCO Geçici Listesi",y=320,sz=94); card(im,140,640,940,1330)
    s=back((t-.15)/.35); circle(im,540,920,170*max(s,.05),DKBLUE); circle(im,540,920,140*max(s,.05),PAPER)
    if s>.6: T(im,"Dünya Mirası",540,885,34,DKBLUE,LORA); T(im,"Geçici Listesi",540,940,34,DKBLUE,LORA)
    return im
def s_cta(t):
    k='cta'; x,y=Q['uzk']; im,m=cam(x,y,.42); banner(im,"Bu köprüden geçtin mi?",None,y=320,sz=72); card(im,120,620,960,1420)
    water(im,130,860,950,1000,t); stone_bridge(im,140,940,810,10,1.,t)
    if t>=ct(k,1)-.05: chip(im,"Yorumlara yaz",540,1080,50,back((t-ct(k,1)+.05)/.25))
    outro(im,t,nxt="Yarın: Karadeniz'de saklı kasaba")
    mark(im,"Müzik özgündür · Çizim temsilidir"); return im
F={'hook':s_hook,'yer':s_yer,'yapim':s_yapim,'olcu':s_olcu,'kabartma':s_kabartma,'unesco':s_unesco,'cta':s_cta}
exec(open('/home/claude/masal4/common.py').read())
