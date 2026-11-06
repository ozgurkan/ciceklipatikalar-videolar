#!/usr/bin/env python3
import os; os.chdir('/home/claude/sakli/s5')
exec(open('/home/claude/sakli/shead.py').read())
SER="Trakya'nın Saklı Doğası · Final"
CX,CY=PT(41.25,27.15); Z=.34
ST=[('gal','Gala Gölü'),('uzk','Uzunköprü'),('gan','Ganos Dağı'),('kiy','Kıyıköy'),('ign','İğneada')]
COL=[RUST,GOLD,CLAY,DKBLUE,GREEN]
def base(t,shown,hl=None,title="5 saklı durak",sub=None):
    im,m=cam(CX,CY,Z); banner(im,title,sub,y=320,sz=84)
    pts=[m(*Q[s[0]]) for s in ST]; route(im,pts[:max(1,shown)],1,INK,7)
    for i in range(shown):
        x,y=pts[i]; circle(im,x,y,24,COL[i]); T(im,str(i+1),x,y,28,(250,240,220),LORA)
        if ST[i][0] in ('uzk','gan','kiy','gal'): T(im,ST[i][1],x,y+48,32,INK,LORA)
    if hl is not None: pin(im,*pts[hl],t,col=COL[hl])
    return im
def s_hook(t):
    k='hook'; im=base(t,5,None,"5 saklı durak",SER)
    if t>=ct(k,1)-.05: chip(im,"Rotayı kaydet",540,1385,52,back((t-ct(k,1)+.05)/.25),fill=GOLD)
    mark(im); return im
def mk(i,lines,title):
    def f(t):
        k=f'd{i+1}'; im=base(t,i+1,i,title)
        c=TM[k]['chunks']
        for j,l in enumerate(lines):
            s0=c[j][0] if j<len(c) else c[-1][0]
            if t>=s0-.05: chip(im,l,540,1220+j*95,40,back((t-s0+.05)/.25),fill=COL[i])
        mark(im); return im
    return f
def s_cta(t):
    k='cta'; im=base(t,5,None,"Hangisinden başlardın?")
    if t>=ct(k,1)-.05: chip(im,"Yorumda yaz · etiketle",540,1220,46,back((t-ct(k,1)+.05)/.25))
    if t>=ct(k,2)-.05: chip(im,"Sıradaki seri: Balkan Rotası",540,1320,42,back((t-ct(k,2)+.05)/.25),fill=GREEN)
    v=ve-TM[k]['start']
    if t>v+.2: T(im,"Takip et · @ciceklipatikalar",540,1400,42,INK,LORA,a=clamp((t-v-.2)/.5))
    mark(im,"Müzik özgündür · Çizim temsilidir"); return im
F={'hook':s_hook,'d1':mk(0,["Flamingolar · kuğular"],"1 · Gala Gölü"),'d2':mk(1,["580 yıllık taş köprü"],"2 · Uzunköprü"),
   'd3':mk(2,["Marmara'ya bakan yamaçlar","Bizans keşişlerinin dağı"],"3 · Ganos Dağı"),'d4':mk(3,["İki nehir · Bizans surları"],"4 · Kıyıköy"),
   'd5':mk(4,["Su basar longoz ormanı"],"5 · İğneada"),'cta':s_cta}
exec(open('/home/claude/masal4/common.py').read())
