#!/usr/bin/env python3
import os; os.chdir('/home/claude/ucmak')
exec(open('/home/claude/sakli/shead.py').read())
SER="Uçmakdere · Trakya Bağ Rotası"
U=PT(40.797,27.36); RT=[PT(40.98,27.51),PT(40.87,27.46),U,PT(40.75,27.31),PT(40.70,27.20),PT(40.61,27.11)]
def slope(im,t,houses=True):
    card(im,90,620,990,1340); d=ImageDraw.Draw(im)
    d.rectangle([100,630,980,1330],fill=(200,220,226))
    water(im,100,1150,980,1330,t,(120,170,190))
    ink_poly(im,[(100,1150),(100,760),(320,700),(560,780),(800,720),(980,800),(980,1150)],(150,168,100),w=4)
    for i in range(9): x=150+i*95; pine(im,x,880+(i%3)*30,.7)
    if houses:
        rs=random.Random(3)
        for i in range(7):
            hx=330+i*60; hy=1060-(i%3)*40; ink_poly(im,[(hx-24,hy),(hx+24,hy),(hx+24,hy-28),(hx-24,hy-28)],(236,226,206),w=2); poly(im,[(hx-30,hy-28),(hx+30,hy-28),(hx,hy-54)],RUST)
def s_hook(t):
    k='hook'; im,m=cam(U[0],U[1],.62+.02*t); banner(im,"Cennet Deresi",SER,y=320,sz=88)
    sx,sy=m(*U); pin(im,sx,sy,t)
    s=back((t+.35)/.35); card(im,200,1040,880,1330)
    T(im,"Uçmak",540,1110,64,RUST,LORA,scale=s); T(im,"eski Türkçede: cennet",540,1200,44,INK,LORA,a=clamp((t+.5)/.3))
    if t>=ct(k,1)-.05: T(im,"+ dere",540,1275,40,DKBLUE,LORAI,a=clamp((t-ct(k,1))/.3))
    mark(im); return im
def s_yer(t):
    k='yer'; im,m=cam(U[0],U[1],.9+.03*t); banner(im,"Uçmakdere","Şarköy · Tekirdağ",y=320,sz=90)
    sx,sy=m(*U); pin(im,sx,sy,t)
    if t>=ct(k,1)-.05: chip(im,"Ganos Dağı'nın eteği",540,1300,46,back((t-ct(k,1)+.05)/.25),fill=GREEN)
    mark(im); return im
def s_yol(t):
    k='yol'; im,m=cam(*PT(40.80,27.31),.9); banner(im,"Kıyı yolu",None,y=320,sz=88)
    pts=[m(*p) for p in RT]; route(im,pts,ease(t/2.5),RUST,14)
    for p,lab in ((RT[0],None),(RT[-1],None)): x,y=m(*p); circle(im,x,y,14,INK)
    x,y=m(*U); circle(im,x,y,18,RUST)
    if t>=ct(k,1)-.05: chip(im,"Motosiklet ve doğa tutkunlarının gözdesi",540,1300,36,back((t-ct(k,1)+.05)/.25),fill=GREEN)
    mark(im); return im
def s_ucus(t):
    k='ucus'; c=TM[k]['chunks']; im,m=cam(U[0],U[1],.45); banner(im,"Yamaç paraşütü",None,y=320,sz=84); slope(im,t,False)
    p=clamp(t/6.); px=260+p*500; py=760+p*260+20*math.sin(t*1.5); paraglider(im,px,py,1.5)
    if t>=c[1][0]-.05: chip(im,"~20 dakika uçuş",540,700,48,back((t-c[1][0]+.05)/.25),fill=RUST)
    return im
def s_koy(t):
    k='koy'; c=TM[k]['chunks']; im,m=cam(U[0],U[1],.45); banner(im,"Eski Rum köyü",None,y=320,sz=84); slope(im,t,True)
    if t>=c[1][0]-.05:
        chip(im,"Köy kahvaltısı",340,700,42,back((t-c[1][0]+.05)/.25),fill=CLAY); chip(im,"Kamp alanları",740,700,42,back((t-c[1][0]-.2)/.25),fill=GREEN)
    return im
def s_cta(t):
    k='cta'; im,m=cam(U[0],U[1],.42); banner(im,"Sen uçar mıydın?",None,y=320,sz=84); slope(im,t,True)
    paraglider(im,700+40*math.sin(t*.8),800,0.9)
    if t>=ct(k,1)-.05: chip(im,"Yorumlara yaz",540,1220,50,back((t-ct(k,1)+.05)/.25))
    v=ve-TM[k]['start']
    if t>=ct(k,2)-.05: chip(im,"Yarın: Üzümden ama şarap değil",540,1395,40,back((t-ct(k,2)+.05)/.25),fill=GREEN)
    if t>v+.2: T(im,"Takip et · @ciceklipatikalar",540,700,40,INK,LORA,a=clamp((t-v-.2)/.5))
    mark(im,"Müzik özgündür · Çizim temsilidir"); return im
F={'hook':s_hook,'yer':s_yer,'yol':s_yol,'ucus':s_ucus,'koy':s_koy,'cta':s_cta}
exec(open('/home/claude/masal4/common.py').read())
