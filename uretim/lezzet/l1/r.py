#!/usr/bin/env python3
import os; os.chdir('/home/claude/lezzet/l1')
exec(open('/home/claude/lezzet/head.py').read())
SER="Trakya Lezzet Rotası · 1"
def s_hook(t):
    k='hook'; x,y=P['tek']; im,m=cam(x,y,.5+.01*t); banner(im,"Tekirdağ Köftesi",SER,y=320,sz=86)
    card(im,140,640,940,1330); T(im,"18-24 saat",540,760,84,RUST,LORA,scale=back(t/.4))
    d=ImageDraw.Draw(im); cx,cy=540,1010; d.ellipse([cx-150,cy-150,cx+150,cy+150],fill=(250,244,226),outline=INK,width=6)
    a=t*2.4; d.line([(cx,cy),(cx+math.sin(a)*120,cy-math.cos(a)*120)],fill=RUST,width=10); d.line([(cx,cy),(cx+math.sin(a/12)*80,cy-math.cos(a/12)*80)],fill=INK,width=12); circle(im,cx,cy,12,INK)
    for i in range(5): kofte(im,300+i*120,1250,.9,0.)
    if t>=ct(k,1)-.05: T(im,"?",870,780,140,RUST,LORA,scale=back((t-ct(k,1)+.05)/.25))
    mark(im); return im
def s_yer(t):
    k='yer'; x,y=P['tek']; im,m=cam(x,y,.8+.03*t); banner(im,"Tekirdağ","Marmara kıyısı",y=320,sz=88)
    sx,sy=m(x,y); pin(im,sx,sy,t)
    if t>=ct(k,1)-.05: chip(im,"Bütün Türkiye'de bilinir",540,1300,46,back((t-ct(k,1)+.05)/.25),fill=GREEN)
    mark(im); return im
def s_et(t):
    k='et'; x,y=P['tek']; im,m=cam(x,y,.45); banner(im,"Ne giriyor?",None,y=320,sz=84); card(im,110,600,970,1340)
    T(im,"Trakya'da yetişen dana eti",540,700,46,INK,LORA,a=clamp(t/.3))
    items=["Bayat ekmek","Soğan","Sarımsak","Kimyon"]
    for i,n in enumerate(items):
        s0=ct(k,1)+i*.45
        if t>=s0: chip(im,n,320+(i%2)*440,880+(i//2)*170,46,back((t-s0)/.25),fill=[CLAY,RUST,GREEN,GOLD][i])
    # yoğurma kabı
    d=ImageDraw.Draw(im); d.chord([300,1080,780,1330],0,180,fill=(176,120,80),outline=INK,width=5); d.ellipse([300,1150,780,1210],fill=MEAT,outline=INK,width=4)
    return im
def s_dinlen(t):
    k='dinlen'; x,y=P['tek']; im,m=cam(x,y,.45); banner(im,"En az 18 saat",None,y=320,sz=84); card(im,110,600,970,1340)
    d=ImageDraw.Draw(im); d.rectangle([250,700,830,1180],fill=(206,226,232),outline=INK,width=6)
    d.rectangle([290,880,790,960],fill=(150,150,150),outline=INK,width=4); d.rectangle([310,860,770,900],fill=MEAT,outline=INK,width=3)
    for i in range(6):
        ph=(t*.6+i/6)%1; T(im,"*",290+i*90,730+ph*120,40,(120,160,190),LORA,a=1-ph)
    hrs=min(18,int(18*ease(t/2.5))); T(im,f"{hrs}. saat",540,1060,70,RUST,LORA)
    T(im,"0-4 °C",540,1140,40,INK,LORAI)
    if t>=ct(k,1)-.05: T(im,"Lezzetin sırlarından biri",540,1270,44,INK,LORA,a=clamp((t-ct(k,1))/.3))
    return im
def s_sekil(t):
    k='sekil'; x,y=P['tek']; im,m=cam(x,y,.45); banner(im,"Ölçüsü belli",None,y=320,sz=84); card(im,110,600,970,1340)
    s=back(t/.3); kofte(im,540,960,3.2*max(s,.05),0.)
    T(im,"15 g",540,780,90,RUST,LORA,scale=s)
    if t>=ct(k,1)-.05:
        p=clamp((t-ct(k,1))/.4); d=ImageDraw.Draw(im); d.line([(355,1080),(355+370*p,1080)],fill=INK,width=5)
        d.line([(355,1060),(355,1100)],fill=INK,width=5)
        if p>=1: d.line([(725,1060),(725,1100)],fill=INK,width=5)
        T(im,"6,5 cm",540,1150,64,INK,LORA,a=p)
    return im
def s_izgara(t):
    k='izgara'; x,y=P['tek']; im,m=cam(x,y,.45); banner(im,"Mangalda",None,y=320,sz=84); card(im,90,600,990,1340)
    grill(im,170,820,910,1000,t); smoke(im,540,800,t)
    for i in range(10):
        c=clamp(t/3); kofte(im,250+(i%5)*145,860+(i//5)*90,.9,c)
    if t>=ct(k,1)-.05: chip(im,"Porsiyon: 10 köfte",540,1200,50,back((t-ct(k,1)+.05)/.25))
    return im
def s_tescil(t):
    k='tescil'; x,y=P['tek']; im,m=cam(x,y,.5); banner(im,"2020","Coğrafi işaret",y=320,sz=94); card(im,140,640,940,1330)
    s=back((t-.15)/.35); circle(im,540,900,160*max(s,.05),RUST); circle(im,540,900,130*max(s,.05),PAPER)
    if s>.6: T(im,"Tekirdağ",540,870,50,RUST,LORA); T(im,"Köftesi",540,935,50,RUST,LORA)
    if t>=ct(k,1)-.05: T(im,"~100 yıl önce bir usta",540,1160,50,INK,LORA,a=clamp((t-ct(k,1))/.3)); T(im,"anlatılır",540,1235,38,(100,76,50),LORAI,a=clamp((t-ct(k,1))/.3))
    return im
def s_cta(t):
    k='cta'; x,y=P['tek']; im,m=cam(x,y,.42); banner(im,"Sen yedin mi?",None,y=320,sz=88); card(im,200,620,880,1420)
    plate(im,540,880,280,100)
    for i in range(5): kofte(im,400+i*70,860+(i%2)*30,.8,1.)
    if t>=ct(k,1)-.05: chip(im,"Yorumlara yaz",540,1080,50,back((t-ct(k,1)+.05)/.25))
    outro(im,t,nxt="Yarın: Edirne")
    mark(im,"Müzik özgündür · Çizim temsilidir"); return im
F={'hook':s_hook,'yer':s_yer,'et':s_et,'dinlen':s_dinlen,'sekil':s_sekil,'izgara':s_izgara,'tescil':s_tescil,'cta':s_cta}
exec(open('/home/claude/masal4/common.py').read())
