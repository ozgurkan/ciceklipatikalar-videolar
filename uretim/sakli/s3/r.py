#!/usr/bin/env python3
import os; os.chdir('/home/claude/sakli/s3')
exec(open('/home/claude/sakli/shead.py').read())
SER="Trakya'nın Saklı Doğası · 3"
def forest(im,t,n=7):
    card(im,90,640,990,1330); water(im,100,1080,980,1320,t,(120,150,120))
    for i in range(n): flood_tree(im,160+i*125,1130+(i%2)*50,1.0+.1*(i%3),t+i,[(96,132,70),(140,140,60),(176,120,50)][i%3])
def s_hook(t):
    k='hook'; x,y=Q['ign']; im,m=cam(x,y,.5+.01*t); banner(im,"Suyun içindeki orman",SER,y=320,sz=78); forest(im,t)
    if t>=ct(k,1)-.05: chip(im,"Longoz",540,760,64,back((t-ct(k,1)+.05)/.25),fill=GREEN)
    mark(im); return im
def s_yer(t):
    k='yer'; x,y=Q['ign']; im,m=cam(x,y,.8+.03*t); banner(im,"İğneada","Demirköy · Kırklareli",y=320,sz=90)
    sx,sy=m(x,y); pin(im,sx,sy,t); chip(im,"Bulgaristan sınırında",540,1300,46,back((t-.4)/.3),fill=DKBLUE)
    mark(im); return im
def s_nasil(t):
    k='nasil'; c=TM[k]['chunks']; x,y=PT(41.82,27.8); im,m=cam(x,y,.5); banner(im,"Nasıl oluştu?",None,y=320,sz=84)
    card(im,90,640,990,1330); d=ImageDraw.Draw(im)
    for i in range(3): ink_poly(im,[(150+i*140,1000),(330+i*140,1000),(240+i*140,760-i*20)],(120,132,90),w=3)
    T(im,"Istranca",330,1050,40,INK,LORAI); water(im,700,700,980,1320,t,(120,170,190)); T(im,"Karadeniz",840,760,36,(60,90,110),LORAI)
    p=clamp(t/2); d.line([(330,1000),(470,1120),(600,1180),(700,1200)],fill=WATER,width=14)
    for i in range(8):
        ph=(t*.6+i/8)%1; circle(im,330+ph*370,1000+ph*200,9,(170,132,84))
    if t>=c[1][0]-.05:
        for i in range(5): flood_tree(im,450+i*55,1270,.5,t+i)
        chip(im,"Su basar orman",540,700,48,back((t-c[1][0]+.05)/.25),fill=GREEN)
    return im
def s_gol(t):
    k='gol'; c=TM[k]['chunks']; x,y=Q['ign']; im,m=cam(x,y,.45); banner(im,"5 göl",None,y=320,sz=90); card(im,90,620,990,1340)
    d=ImageDraw.Draw(im); L=[("Mert",540,850,230,90),("Erikli",270,1060,110,50),("Hamam",800,1060,90,40),("Pedina",420,1190,70,30),("Saka",680,1200,50,24)]
    for i,(n,gx,gy,rx,ry) in enumerate(L):
        if t>=i*.3:
            s=back((t-i*.3)/.3); d.ellipse([gx-rx*s,gy-ry*s,gx+rx*s,gy+ry*s],fill=WATER,outline=INK,width=3)
            if s>.8: T(im,n,gx,gy,34 if rx>60 else 28,INK,LORA)
    if t>=c[1][0]-.05: chip(im,"En büyüğü: Mert Gölü",540,720,44,back((t-c[1][0]+.05)/.25),fill=RUST)
    if t>=c[2][0]-.05: T(im,"Kumul · sazlık · orman",540,1285,40,INK,LORAI,a=clamp((t-c[2][0])/.3))
    return im
def s_park(t):
    k='park'; x,y=Q['ign']; im,m=cam(x,y,.5); banner(im,"2007","Milli park",y=320,sz=94); forest(im,t,5)
    if t>=ct(k,1)-.05: chip(im,"3.155 hektar",540,780,60,back((t-ct(k,1)+.05)/.25),fill=GREEN)
    return im
def s_cta(t):
    k='cta'; x,y=Q['ign']; im,m=cam(x,y,.42); banner(im,"Sonbahar mı, bahar mı?",None,y=320,sz=72); forest(im,t)
    if t>=ct(k,1)-.05: chip(im,"Yorumlara yaz",540,760,50,back((t-ct(k,1)+.05)/.25))
    v=ve-TM[k]['start']
    if t>v+.2: chip(im,"Yarın: Flamingoların gölü",540,870,42,back((t-v-.2)/.3),fill=GREEN); T(im,"Takip et · @ciceklipatikalar",540,1265,42,(250,246,232),LORA,a=clamp((t-v-.2)/.5))
    mark(im,"Müzik özgündür · Çizim temsilidir"); return im
F={'hook':s_hook,'yer':s_yer,'nasil':s_nasil,'gol':s_gol,'park':s_park,'cta':s_cta}
exec(open('/home/claude/masal4/common.py').read())
