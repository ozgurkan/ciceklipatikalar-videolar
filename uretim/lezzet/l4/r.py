#!/usr/bin/env python3
import os; os.chdir('/home/claude/lezzet/l4')
exec(open('/home/claude/lezzet/head.py').read())
SER="Trakya Lezzet Rotası · 4"
def s_hook(t):
    k='hook'; x,y=P['edi']; im,m=cam(x,y,.45+.01*t); banner(im,"Az bilinen 2 lezzet",SER,y=320,sz=80)
    card(im,140,640,940,1330); n=39
    T(im,f"{n}",540,800,150,RUST,LORA,scale=back(t/.4)); T(im,"baharat",540,920,56,INK,LORA)
    helva_bowl(im,540,1150,1.1,t,1.)
    mark(im); return im
def s_helva(t):
    k='helva'; c=TM[k]['chunks']
    if t<c[2][0]-.05:
        x,y=P['edi']; im,m=cam(x,y,.8+.03*t); banner(im,"Deva-i misk","Edirne",y=320,sz=90)
        sx,sy=m(x,y); pin(im,sx,sy,t); return im
    x,y=P['edi']; im,m=cam(x,y,.45); banner(im,"Deva-i misk helvası",None,y=320,sz=78); card(im,110,600,970,1340)
    helva_bowl(im,540,800,1.0,t,1.)
    for i,n in enumerate(["Yumurta akı","Şeker","39 baharat"]):
        s0=c[2][0]+i*.4
        if t>=s0: chip(im,n,270+i*270,1010,42,back((t-s0)/.25),fill=[CLAY,GOLD,RUST][i])
    if t>=c[3][0]-.05: T(im,"Osmanlı'da halka dağıtıldığı anlatılır",540,1130,38,INK,LORAI,a=clamp((t-c[3][0])/.3))
    if t>=c[4][0]-.05: chip(im,"Coğrafi işaret: 2021",540,1250,46,back((t-c[4][0]+.05)/.25),fill=GREEN)
    return im
def s_ahmet(t):
    k='ahmet'; c=TM[k]['chunks']
    if t<c[1][0]-.05:
        x,y=PT(41.42,27.46); im,m=cam(x,y,.8+.03*t); banner(im,"Ahmetbey","Lüleburgaz · Kırklareli",y=320,sz=90)
        sx,sy=m(*P['ahm']); pin(im,sx,sy,t); sx,sy=m(*P['lul']); circle(im,sx,sy,12,INK); T(im,"Lüleburgaz",sx,sy+44,34,INK,LORA)
        return im
    x,y=P['ahm']; im,m=cam(x,y,.45); banner(im,"Ahmetbey köftesi",None,y=320,sz=80); card(im,110,600,970,1340)
    if t<c[2][0]-.05:
        mill(im,440,1050,1.5,t); T(im,"Değirmen sırası",540,1230,46,INK,LORA); T(im,"anlatılır",540,1290,34,(100,76,50),LORAI)
    else:
        grill(im,200,860,880,1020,t); smoke(im,540,840,t)
        for i in range(8): kofte(im,270+(i%4)*165,900+(i//4)*80,.9,clamp((t-c[2][0])/2))
        T(im,"Kömür ateşinde",540,1180,48,INK,LORA)
        if t>=c[3][0]-.05: chip(im,"Coğrafi işaret: 2026",540,1270,46,back((t-c[3][0]+.05)/.25),fill=GREEN)
    return im
def s_cta(t):
    k='cta'; x,y=P['edi']; im,m=cam(x,y,.42); banner(im,"Hangisini merak ettin?",None,y=320,sz=72); card(im,160,620,920,1420)
    helva_bowl(im,360,860,.6,t); plate(im,700,860,170,62)
    for i in range(3): kofte(im,640+i*60,850+(i%2)*14,.6,1.)
    if t>=ct(k,1)-.05: chip(im,"Yorumlara yaz",540,1080,50,back((t-ct(k,1)+.05)/.25))
    outro(im,t,nxt="Yarın: 3 günlük lezzet rotası")
    mark(im,"Müzik özgündür · Çizim temsilidir"); return im
F={'hook':s_hook,'helva':s_helva,'ahmet':s_ahmet,'cta':s_cta}
exec(open('/home/claude/masal4/common.py').read())
