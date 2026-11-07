#!/usr/bin/env python3
import os; os.chdir('/home/claude/sakli/s2')
exec(open('/home/claude/sakli/shead.py').read())
SER="Trakya'nın Saklı Doğası · 2"
def town(im,t,s=1.):
    card(im,90,640,990,1330); d=ImageDraw.Draw(im)
    water(im,100,650,980,800,t,(120,170,190)); T(im,"Karadeniz",540,700,40,(60,90,110),LORAI)
    d.polygon([(100,800),(980,800),(980,1320),(100,1320)],fill=(220,206,170))
    for x0 in (230,850): d.rectangle([x0-28,800,x0+28,1320],fill=WATER)
    d.rounded_rectangle([330,900,750,1220],30,outline=STONE2,width=14)
    rs=random.Random(6)
    for i in range(10): hx,hy=rs.uniform(380,700),rs.uniform(950,1180); ink_poly(im,[(hx-26,hy),(hx+26,hy),(hx+26,hy-30),(hx-26,hy-30)],(236,226,206),w=2); poly(im,[(hx-32,hy-30),(hx+32,hy-30),(hx,hy-58)],RUST)
def s_hook(t):
    k='hook'; x,y=Q['kiy']; im,m=cam(x,y,.5+.01*t); banner(im,"Surlu sahil kasabası",SER,y=320,sz=80); town(im,t)
    mark(im); return im
def s_yer(t):
    k='yer'; x,y=Q['kiy']; im,m=cam(x,y,.8+.03*t); banner(im,"Kıyıköy","Vize · Kırklareli",y=320,sz=90)
    sx,sy=m(x,y); pin(im,sx,sy,t)
    if t>=ct(k,1)-.05: chip(im,"Karadeniz kıyısı",540,1300,48,back((t-ct(k,1)+.05)/.25),fill=DKBLUE)
    mark(im); return im
def s_dere(t):
    k='dere'; x,y=Q['kiy']; im,m=cam(x,y,.45); banner(im,"İki dere arasında",None,y=320,sz=80); town(im,t)
    if t>=ct(k,0): chip(im,"Kazandere",230,1270,38,back(t/.25),fill=DKBLUE)
    if t>=.5: chip(im,"Pabuçdere",850,1270,38,back((t-.5)/.25),fill=DKBLUE)
    if t>=ct(k,1)-.05:
        for x0 in (230,850):
            for i in range(4):
                ph=(t*.8+i/4)%1; circle(im,x0,1300-ph*500,8,(240,250,250),1-ph)
    return im
def s_sur(t):
    k='sur'; x,y=Q['kiy']; im,m=cam(x,y,.45); banner(im,"Bizans surları",None,y=320,sz=84); card(im,90,620,990,1340)
    wall_gate(im,540,1120,1.25)
    T(im,"Justinianus dönemi",540,740,48,RUST,LORA,a=clamp(t/.3))
    if t>=ct(k,1)-.05: chip(im,"Kapısından hâlâ geçiliyor",540,1240,42,back((t-ct(k,1)+.05)/.25),fill=GREEN)
    return im
def s_manastir(t):
    k='manastir'; x,y=Q['kiy']; im,m=cam(x,y,.45); banner(im,"Kayaya oyulmuş",None,y=320,sz=84); card(im,90,620,990,1340)
    cave_monastery(im,540,1120,1.3)
    if t>=ct(k,1)-.05: chip(im,"Aya Nikola · Bizans dönemi",540,1230,46,back((t-ct(k,1)+.05)/.25),fill=RUST)
    return im
def s_cam(t):
    k='cam'; x,y=Q['kiy']; im,m=cam(x,y,.45); banner(im,"Kasatura Koyu",None,y=320,sz=84); card(im,90,620,990,1340)
    water(im,100,1100,980,1330,t)
    for i in range(9):
        if t>=i*.12: pine(im,170+i*92,1090-(i%2)*40,1.1)
    T(im,"Trakya'nın tek doğal",540,740,44,INK,LORA,a=clamp(t/.3)); T(im,"karaçam korusu",540,800,48,RUST,LORA,a=clamp(t/.3))
    return im
def s_cta(t):
    k='cta'; x,y=Q['kiy']; im,m=cam(x,y,.42); banner(im,"Duymuş muydun?",None,y=320,sz=84); town(im,t)
    if t>=ct(k,1)-.05: chip(im,"Yorumlara yaz",540,1090,50,back((t-ct(k,1)+.05)/.25))
    v=ve-TM[k]['start']
    if t>v+.2: chip(im,"Yarın: Suyun içindeki orman",540,1200,40,back((t-v-.2)/.3),fill=GREEN); T(im,"Takip et · @ciceklipatikalar",540,1290,42,INK,LORA,a=clamp((t-v-.2)/.5))
    mark(im,"Müzik özgündür · Çizim temsilidir"); return im
F={'hook':s_hook,'yer':s_yer,'dere':s_dere,'sur':s_sur,'manastir':s_manastir,'cam':s_cam,'cta':s_cta}
exec(open('/home/claude/masal4/common.py').read())
