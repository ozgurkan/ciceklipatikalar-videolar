#!/usr/bin/env python3
import os; os.chdir('/home/claude/sakli/s4')
exec(open('/home/claude/sakli/shead.py').read())
SER="Trakya'nın Saklı Doğası · 4"
def lake(im,t,nf=5,sw=False):
    card(im,90,640,990,1330); d=ImageDraw.Draw(im)
    d.rectangle([100,650,980,1320],fill=(206,222,200)); d.ellipse([130,820,950,1300],fill=WATER,outline=INK,width=4)
    for i in range(14): x=120+i*62; d.line([(x,840-(i%3)*20),(x+6,760-(i%3)*20)],fill=(150,140,80),width=6)
    for i in range(nf): flamingo(im,280+i*120,1090+(i%2)*60,1.0,t,i)
    if sw: swan(im,820,1230,1.1,t); swan(im,700,1260,.9,t+1)
def s_hook(t):
    k='hook'; x,y=Q['gal']; im,m=cam(x,y,.5+.01*t); banner(im,"Flamingoların gölü",SER,y=320,sz=78); lake(im,t)
    mark(im); return im
def s_yer(t):
    k='yer'; x,y=Q['gal']; im,m=cam(x,y,.8+.03*t); banner(im,"Gala Gölü","Edirne",y=320,sz=90)
    sx,sy=m(x,y); pin(im,sx,sy,t)
    for kk,lab in (('enz','Enez'),('ips','İpsala')):
        if t>=ct(k,1)-.05: px,py=m(*Q[kk]); circle(im,px,py,12,INK); T(im,lab,px,py+40,36,INK,LORA)
    mark(im); return im
def s_delta(t):
    k='delta'; x,y=PT(40.8,26.15); im,m=cam(x,y,.6+.02*t); banner(im,"Meriç Deltası",None,y=320,sz=84)
    sx,sy=m(*Q['gal']); pin(im,sx,sy,t,col=GREEN)
    if t>=ct(k,1)-.05: chip(im,"Göl · sazlık · orman",540,1300,46,back((t-ct(k,1)+.05)/.25),fill=GREEN)
    mark(im); return im
def s_kus(t):
    k='kus'; c=TM[k]['chunks']; x,y=Q['gal']; im,m=cam(x,y,.45); banner(im,"150+ kuş türü",None,y=320,sz=84); lake(im,t,4,t>=c[2][0]-.05)
    if t>=c[1][0]-.05:
        p=clamp((t-c[1][0])/2.5); d=ImageDraw.Draw(im)
        for i in range(6):
            bx=150+p*780+i*40-120; by=720+(i%3)*30
            d.line([(bx-18,by-8),(bx,by),(bx+18,by-8)],fill=INK,width=4)
        chip(im,"Avrupa ⇄ Afrika göç yolu",540,700,40,back((t-c[1][0]+.05)/.25),fill=DKBLUE)
    return im
def s_park(t):
    k='park'; x,y=Q['gal']; im,m=cam(x,y,.5); banner(im,"2005","Milli park",y=320,sz=94); lake(im,t,3,True)
    return im
def s_cta(t):
    k='cta'; x,y=Q['gal']; im,m=cam(x,y,.42); banner(im,"Flamingo gördün mü?",None,y=320,sz=76); lake(im,t)
    if t>=ct(k,1)-.05: chip(im,"Yorumlara yaz",540,740,50,back((t-ct(k,1)+.05)/.25))
    v=ve-TM[k]['start']
    if t>v+.2: T(im,"Takip et · @ciceklipatikalar",540,1395,42,INK,LORA,a=clamp((t-v-.2)/.5)); chip(im,"Yarın: Serinin finali",540,850,42,back((t-v-.2)/.3),fill=GREEN)
    mark(im,"Müzik özgündür · Çizim temsilidir"); return im
F={'hook':s_hook,'yer':s_yer,'delta':s_delta,'kus':s_kus,'park':s_park,'cta':s_cta}
exec(open('/home/claude/masal4/common.py').read())
