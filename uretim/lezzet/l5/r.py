#!/usr/bin/env python3
import os; os.chdir('/home/claude/lezzet/l5')
exec(open('/home/claude/lezzet/head.py').read())
SER="Trakya Lezzet Rotası · Final"
CX,CY=PT(41.10,27.05); Z=.36
STOPS=[('tek','Tekirdağ','Köfte',1),('mal','Malkara','Eski kaşar',1),('ahm','Ahmetbey','Köfte molası',2),('kir','Kırklareli','Peynir · hardaliye',2),('edi','Edirne','Ciğer · helva',3)]
DCOL={1:RUST,2:GREEN,3:DKBLUE}
def base(t,prog,shown,title,sub=None):
    im,m=cam(CX,CY,Z); banner(im,title,sub,y=320,sz=84)
    pts=[m(*P[s[0]]) for s in STOPS]; route(im,pts,prog,INK,8)
    for i,(kk,lab,food,dd) in enumerate(STOPS):
        if i<shown:
            x,y=pts[i]; circle(im,x,y,22,DCOL[dd]); T(im,str(dd),x,y,26,(250,240,220),LORA)
            if kk in ('mal','ahm'): T(im,lab,x,y+46,34,INK,LORA)
    return im,pts
def seg_prog(k,t):
    a=TM[k]['start']; return a+t
def s_hook(t):
    k='hook'; im,pts=base(t,1.0,5,"3 günde Trakya",SER)
    if t>=ct(k,1)-.05: chip(im,"Rotayı kaydet",540,1385,52,back((t-ct(k,1)+.05)/.25),fill=GOLD)
    mark(im); return im
def daycard(im,t,k,day,items):
    c=TM[k]['chunks']
    for i,txt in enumerate(items):
        s0=c[i+1][0] if i+1<len(c) else c[-1][0]
        if t>=s0-.05: chip(im,txt,540,1180+i*110,44,back((t-s0+.05)/.25),fill=DCOL[day])
def s_g1(t):
    k='g1'; p=.0+.25*ease(t/3); im,pts=base(t,p,2,"1. gün","Tekirdağ · Malkara")
    for i in (0,1): pin(im,*pts[i],t)
    daycard(im,t,k,1,["Öğlen: Tekirdağ köftesi","Akşamüstü: Malkara eski kaşarı"]); mark(im); return im
def s_g2(t):
    k='g2'; p=.25+.5*ease(t/4); im,pts=base(t,p,4,"2. gün","Kuzeye: Ahmetbey · Kırklareli")
    for i in (2,3): pin(im,*pts[i],t,col=GREEN)
    daycard(im,t,k,2,["Ahmetbey'de köfte molası","Kırklareli: peynir ve hardaliye"]); mark(im); return im
def s_g3(t):
    k='g3'; p=.75+.25*ease(t/3); im,pts=base(t,p,5,"3. gün","Edirne")
    pin(im,*pts[4],t,col=DKBLUE)
    daycard(im,t,k,3,["Tava ciğeri + Karaağaç biberi","Beyaz peynir · deva-i misk"]); mark(im); return im
def s_cta(t):
    k='cta'; im,pts=base(t,1,5,"Kiminle gidersin?",None)
    if t>=ct(k,1)-.05: chip(im,"Yorumda etiketle",540,1180,50,back((t-ct(k,1)+.05)/.25))
    v=ve-TM[k]['start']
    if t>=ct(k,2)-.05: chip(im,"Sıradaki seri: Trakya'nın Saklı Doğası",540,1290,40,back((t-ct(k,2)+.05)/.25),fill=GREEN)
    if t>v+.2: T(im,"Takip et · @ciceklipatikalar",540,1385,44,INK,LORA,a=clamp((t-v-.2)/.5))
    mark(im,"Müzik özgündür · Çizim temsilidir"); return im
F={'hook':s_hook,'g1':s_g1,'g2':s_g2,'g3':s_g3,'cta':s_cta}
exec(open('/home/claude/masal4/common.py').read())
