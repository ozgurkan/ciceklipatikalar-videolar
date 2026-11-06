#!/usr/bin/env python3
import os; os.chdir('/home/claude/lezzet/l3')
exec(open('/home/claude/lezzet/head.py').read())
SER="Trakya Lezzet Rotası · 3"
def s_hook(t):
    k='hook'; x,y=PT(41.35,26.95); im,m=cam(x,y,.36+.01*t); banner(im,"Trakya'nın 3 peyniri",SER,y=320,sz=80)
    for i,(kk,lab) in enumerate([('edi','Edirne'),('mal','Malkara'),('kir','Kırklareli')]):
        if t>=i*.35:
            sx,sy=m(*P[kk]); pin(im,sx,sy,t,lab,col=[RUST,GOLD,GREEN][i],sz=40)
    if t>=ct(k,1)-.05: chip(im,"3 tescil · 3 mera",540,1385,50,back((t-ct(k,1)+.05)/.25),fill=INK)
    mark(im); return im
def s_edirne(t):
    k='edirne'; c=TM[k]['chunks']; x,y=P['edi']; im,m=cam(x,y,.45); banner(im,"Edirne Beyaz Peyniri","Tescil: 2007",y=320,sz=74)
    card(im,110,600,970,1340); cheese_block(im,520,820,1.25)
    if t>=c[1][0]-.05:
        for i,n in enumerate(["Tunca","Meriç","Arda","Ergene"]):
            s0=c[1][0]+i*.3
            if t>=s0: chip(im,n,320+(i%2)*440,1010+(i//2)*120,44,back((t-s0)/.25),fill=DKBLUE)
    if t>=c[2][0]-.05: chip(im,"En az 90 gün olgunlaşır",540,1260,44,back((t-c[2][0]+.05)/.25),fill=RUST)
    return im
def s_malkara(t):
    k='malkara'; c=TM[k]['chunks']; x,y=P['mal']; im,m=cam(x,y,.45); banner(im,"Malkara Eski Kaşarı","Tescil: 2017",y=320,sz=74)
    card(im,110,600,970,1340); kasar_wheel(im,540,830,1.3)
    if t>=c[1][0]-.05:
        for i,n in enumerate(["Keçi","Koyun","İnek"]):
            s0=c[1][0]+i*.3
            if t>=s0: chip(im,n,290+i*250,1040,46,back((t-s0)/.25),fill=[GREEN,CLAY,DKBLUE][i])
    if t>=c[2][0]-.05: T(im,"Kelle: en az 11 kg",540,1150,52,RUST,LORA,a=clamp((t-c[2][0])/.3))
    if t>=c[3][0]-.05: T(im,"Seyahatname'de anılır",540,1250,42,INK,LORAI,a=clamp((t-c[3][0])/.3))
    return im
def s_kirk(t):
    k='kirk'; c=TM[k]['chunks']
    x,y=PT(41.8,27.4); im,m=cam(x,y,.6+.02*t); banner(im,"Kırklareli Peyniri","Istranca'nın otları",y=320,sz=76)
    sx,sy=m(*P['ist']); d=ImageDraw.Draw(im)
    for i in range(4):
        bx=sx-160+i*100; ink_poly(im,[(bx-70,sy+40),(bx+70,sy+40),(bx,sy-90-20*(i%2))],(120,132,90),w=3)
    sx,sy=m(*P['kir']); pin(im,sx,sy,t)
    if t>=c[1][0]-.05: chip(im,"Tescil: 2021",540,1300,52,back((t-c[1][0]+.05)/.25),fill=GREEN)
    mark(im); return im
def s_cta(t):
    k='cta'; x,y=PT(41.35,26.95); im,m=cam(x,y,.42); banner(im,"Sen hangisini denedin?",None,y=320,sz=72); card(im,160,620,920,1420)
    cheese_block(im,380,830,.75); kasar_wheel(im,700,820,.75)
    if t>=ct(k,1)-.05: chip(im,"Yorumlara yaz",540,1080,50,back((t-ct(k,1)+.05)/.25))
    outro(im,t,nxt="Yarın: Az bilinen 2 lezzet")
    mark(im,"Müzik özgündür · Çizim temsilidir"); return im
F={'hook':s_hook,'edirne':s_edirne,'malkara':s_malkara,'kirk':s_kirk,'cta':s_cta}
exec(open('/home/claude/masal4/common.py').read())
