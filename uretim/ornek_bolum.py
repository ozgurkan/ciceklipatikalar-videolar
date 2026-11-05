#!/usr/bin/env python3
import sys, os, json, math, subprocess, random
sys.path.insert(0,'/home/claude/masal'); sys.path.insert(0,'/home/claude/reels')
os.chdir('/home/claude/masal6')
import numpy as np
from PIL import Image, ImageDraw
import m as M
from m import *
TM=M.TM; ORDER=M.ORDER; W,H,FPS=1080,1920,30; ve=TM['_voice_end']
def ct(k,i): return TM[k]['chunks'][i][0]
def card(im,x0,y0,x1,y1): rrect(im,x0,y0,x1,y1,24,PAPER,.97); ImageDraw.Draw(im).rounded_rectangle([x0,y0,x1,y1],24,outline=INK,width=5)
WINE=(120,42,62); GRP=(88,52,110); LEAF=(112,132,70); MUST=(226,186,70)
def bottle(im,cx,base,s=1,lv=1.):
    ink_poly(im,[(cx-70*s,base),(cx+70*s,base),(cx+70*s,base-240*s),(cx+28*s,base-320*s),(cx+28*s,base-430*s),(cx-28*s,base-430*s),(cx-28*s,base-320*s),(cx-70*s,base-240*s)],(214,222,214),w=5)
    yt=base-240*s*lv
    if lv>0: poly(im,[(cx-62*s,base-8*s),(cx+62*s,base-8*s),(cx+62*s,yt),(cx-62*s,yt)],WINE)
    rrect(im,cx-54*s,base-180*s,cx+54*s,base-70*s,8,PAPER); T(im,"H",cx,base-125*s,int(60*s),RUST,LORA)
def grape(im,x,y,s):
    d=ImageDraw.Draw(im); d.line([(x,y-44*s),(x+10*s,y-72*s)],fill=INK,width=max(2,int(4*s)))
    for r,n in [(0,3),(1,3),(2,2),(3,1)]:
        for i in range(n):
            xx=x+(i-(n-1)/2)*22*s; yy=y-30*s+r*20*s; d.ellipse([xx-12*s,yy-12*s,xx+12*s,yy+12*s],fill=GRP,outline=INK,width=max(1,int(2*s)))
    d.polygon([(x-4*s,y-58*s),(x+30*s,y-74*s),(x+44*s,y-46*s),(x+10*s,y-44*s)],fill=LEAF,outline=INK)
def s_hook(t):
    a=PT(41.73,27.22); im,m=cam(a[0],a[1],.46+.012*t); banner(im,"Hardaliye","Trakya Bağ Rotası · Özel Bölüm",y=320,sz=90)
    card(im,190,660,890,1330); p=eout(t/.5); bottle(im,540,1290,1.15,1)
    for x,y in [(300,1000),(780,1020),(320,1220),(770,1240)]: grape(im,x,y,1.3)
    mark(im); return im
def s_yer(t):
    k='yer'; a=PT(41.73,27.22); im,m=cam(a[0],a[1],.72+.02*t); banner(im,"Kırklareli","Yıldız Dağları'nın eteği",y=320,sz=88)
    x,y=m(*a); pl=1+.1*math.sin(t*5); ImageDraw.Draw(im).ellipse([x-80*pl,y-80*pl,x+80*pl,y+80*pl],outline=RUST,width=7)
    if t>=ct(k,1)-.05: chip(im,"Eski adı: Kırkkilise",540,1230,48,back((t-ct(k,1)+.05)/.25),fill=(120,88,56))
    if t>=ct(k,2)-.05: chip(im,"1924: Kırklareli",540,1340,48,back((t-ct(k,2)+.05)/.25))
    mark(im); return im
def hut(im,x,y,s):
    ink_poly(im,[(x-60*s,y),(x+60*s,y),(x+60*s,y-50*s),(x-60*s,y-50*s)],(176,136,96),w=3); ink_poly(im,[(x-72*s,y-50*s),(x+72*s,y-50*s),(x,y-110*s)],(120,92,54),w=3)
def s_pinar(t):
    k='pinar'; a=PT(41.68,27.20); im,m=cam(a[0],a[1],.6); banner(im,"Aşağı Pınar Höyüğü",None,y=320,sz=66)
    card(im,120,600,960,1320)
    n=int(6200*ease(t/1.5)); T(im,f"MÖ {n:,}".replace(',','.'),540,735,96,RUST,LORA)
    d=ImageDraw.Draw(im); d.polygon([(190,1240),(890,1240),(760,920),(330,920)],fill=(170,132,84),outline=INK)
    for y in (980,1040,1100,1160): d.line([(190+(1240-y)*.2,y),(890-(1240-y)*.2,y)],fill=(120,88,52),width=4)
    for i,x in enumerate((370,500,640,740)):
        if t>=ct(k,1)+i*.25: hut(im,x,1020+i%2*80,1.0)
    if t>=ct(k,2)-.05: T(im,"Trakya'da köy yaşamının ilk izleri",540,1275,36,INK,LORAI,a=clamp((t-ct(k,2))/.3))
    return im
def s_uzum(t):
    k='uzum'; a=PT(41.45,27.2); im,m=cam(a[0],a[1],.5); banner(im,"Üzüm","Kırmızı üzümler",y=320,sz=88); card(im,110,620,970,1330)
    names=["Papazkarası","Öküzgözü","Merlot","Şiraz","Pamit","Cardinal"]
    for i,n in enumerate(names):
        if t>=ct(k,1)+i*.22:
            s=back((t-ct(k,1)-i*.22)/.25); x=300+(i%2)*480; y=760+(i//2)*200; grape(im,x-150,y+40,1.2*max(s,.05)); w=text_mask(n,44,LORA).width; T(im,n,x-70+w/2,y+20,44,INK,LORA,scale=s)
    return im
def s_yapim(t):
    k='yapim'; c=TM[k]['chunks']; a=PT(41.45,27.2); im,m=cam(a[0],a[1],.42)
    banner(im,"Nasıl yapılır?",None,y=320,sz=82); card(im,90,520,990,1370); d=ImageDraw.Draw(im)
    labs=["Ez","Vişne yaprağı + hardal","Her gün karıştır","4-5 hafta","Dinlendir, şişele"]
    # step lamp
    st=max([i for i in range(5) if t>=c[i][0]-.05] or [0])
    # vat
    vx0,vx1,vy0,vy1=300,780,720,1210
    ink_poly(im,[(vx0,vy0),(vx1,vy0),(vx1-30,vy1),(vx0+30,vy1)],(166,120,80),w=6)
    lv=.75
    d.rectangle([vx0+24,vy0+(1-lv)*(vy1-vy0),vx1-24,vy1-12],fill=WINE)
    rs=random.Random(5)
    if st==0:
        for i in range(16): circle(im,rs.randint(vx0+50,vx1-50),rs.randint(vy0+180,vy1-40),24,GRP)
        px=540+60*math.sin(t*9); rrect(im,px-40,vy0-80,px+40,vy0+130,18,(120,88,56))
    if st>=1:
        for i in range(10):
            yy=vy0+180+((t*90+i*70)%200)*(1 if st==1 else 0); x=rs.randint(vx0+60,vx1-60)
            if st>=1: circle(im,x,yy,8,MUST); poly(im,[(x+60,yy-20),(x+100,yy-26),(x+96,yy+6),(x+66,yy+4)],LEAF)
    if st==2:
        ang=t*6; cx,cy=540,vy0+180; d.line([(cx,vy0-90),(cx+math.sin(ang)*90,cy+80)],fill=(90,60,36),width=16)
    if st==3:
        for i in range(8):
            ph=(t*.8+i*.13)%1; circle(im,rs.randint(vx0+60,vx1-60),vy1-30-ph*350,7+ph*6,(226,176,180),1-ph)
        wk=min(5,1+int((t-c[3][0])*3)); T(im,f"{wk}. hafta",540,620,58,RUST,LORA)
    if st==4:
        bottle(im,870,1205,.66,1); bottle(im,755,1205,.66,1)
    T(im,labs[st],540,1275,48,INK,LORA)
    for i in range(5):
        circle(im,370+i*85,1345,12,RUST if i==st else (200,180,140))
    return im
def s_hardal(t):
    k='hardal'; a=PT(41.45,27.2); im,m=cam(a[0],a[1],.46); banner(im,"Neden hardal?",None,y=320,sz=82); card(im,120,620,960,1320)
    rs=random.Random(8)
    for i in range(70):
        x=rs.randint(190,890); y=rs.randint(700,1010)
        if t>i*.012: circle(im,x,y,9,MUST)
    if t>=ct(k,1)-.05:
        chip(im,"Şaraplaşmayı engellemeye yardımcı",540,1115,38,back((t-ct(k,1)+.05)/.25),fill=RUST)
        T(im,"Geleneksel bilgi",540,1235,40,INK,LORAI)
    return im
def s_alkol(t):
    k='alkol'; a=PT(41.45,27.2); im,m=cam(a[0],a[1],.46); banner(im,"Alkolsüz mü?",None,y=320,sz=82); card(im,120,620,960,1340)
    bottle(im,540,1120,.9,1)
    if t>=ct(k,0): chip(im,"Tescilinde: alkolsüz",540,1215,42,back((t-ct(k,0))/.25),fill=GREEN)
    if t>=ct(k,2)-.05: chip(im,"Eskidikçe az alkol oluşabilir",540,1300,38,back((t-ct(k,2)+.05)/.25),fill=RUST)
    return im
def s_tescil(t):
    k='tescil'; a=PT(41.73,27.22); im,m=cam(a[0],a[1],.46); banner(im,"2017","Coğrafi işaret tescili",y=320,sz=94); card(im,120,650,960,1320)
    s=back((t-.2)/.35); circle(im,540,900,160*max(s,.05),RUST); circle(im,540,900,130*max(s,.05),PAPER)
    if s>.6: T(im,"Kırklareli",540,870,48,RUST,LORA); T(im,"Hardaliyesi",540,935,48,RUST,LORA)
    if t>=ct(k,2)-.05: T(im,"Bu adla: Kırklareli'nde üretim",540,1160,44,INK,LORA,a=clamp((t-ct(k,2))/.3)); T(im,"Tescil no: 278",540,1245,36,(100,76,50),LORAI,a=clamp((t-ct(k,2))/.3))
    return im
def s_cta(t):
    a=PT(41.73,27.22); im,m=cam(a[0],a[1],.42); banner(im,"Sen içtin mi?",None,y=320,sz=88); card(im,240,620,840,1240); bottle(im,540,1200,1.05,1)
    c=TM['cta']['chunks']
    if t>=c[1][0]-.05: chip(im,"Yorumlara yaz",540,1335,50,back((t-c[1][0]+.05)/.25))
    v=ve-TM['cta']['start']
    if t>v+.3: T(im,"Takipte kal · @ciceklipatikalar",540,1420,38,INK,LORA,a=clamp((t-v-.3)/.6))
    mark(im,"Müzik özgündür · Çizim temsilidir"); return im
F={'hook':s_hook,'yer':s_yer,'pinar':s_pinar,'uzum':s_uzum,'yapim':s_yapim,'hardal':s_hardal,'alkol':s_alkol,'tescil':s_tescil,'cta':s_cta}
exec(open('/home/claude/masal4/common.py').read())
