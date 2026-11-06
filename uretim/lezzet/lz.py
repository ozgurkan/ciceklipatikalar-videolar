# Lezzet Rotası ortak çizim yardımcıları (masal haritası tarzı)
import math, random
from PIL import ImageDraw
from m import *
BROWN=(122,72,40); MEAT=(150,86,52); LIVER=(112,40,34); PEP=(176,40,30); CREAM=(250,246,232); KASAR=(232,196,110); SMOKE=(200,190,170)
P={'tek':PT(40.98,27.51),'mal':PT(40.89,26.90),'edi':PT(41.677,26.556),'kar':PT(41.655,26.53),'kir':PT(41.735,27.225),
   'lul':PT(41.40,27.355),'ahm':PT(41.433,27.567),'ist':PT(41.85,27.65)}
def LC(a,b,p): return tuple(int(v) for v in lerpc(a,b,p))
def card(im,x0,y0,x1,y1): rrect(im,x0,y0,x1,y1,24,PAPER,.97); ImageDraw.Draw(im).rounded_rectangle([x0,y0,x1,y1],24,outline=INK,width=5)
def pin(im,x,y,t,lab=None,col=RUST,sz=44):
    pl=1+.08*math.sin(t*5); d=ImageDraw.Draw(im)
    d.ellipse([x-70*pl,y-70*pl,x+70*pl,y+70*pl],outline=col,width=7); circle(im,x,y,16,col)
    if lab: chip(im,lab,x,y-120,sz,fill=col)
def plate(im,x,y,rx=300,ry=110):
    d=ImageDraw.Draw(im); d.ellipse([x-rx,y-ry,x+rx,y+ry],fill=(236,236,230),outline=INK,width=5); d.ellipse([x-rx*.78,y-ry*.72,x+rx*.78,y+ry*.72],outline=(200,196,186),width=3)
def kofte(im,x,y,s=1,c=1.):
    col=LC((176,112,84),BROWN,c); hw,hh=58*s,17*s
    rrect(im,x-hw,y-hh,x+hw,y+hh,hh,col); d=ImageDraw.Draw(im); d.rounded_rectangle([x-hw,y-hh,x+hw,y+hh],int(hh),outline=INK,width=max(2,int(3*s)))
    if c>.5:
        for i in range(3): d.line([(x-30*s+i*28*s,y-hh+3),(x-38*s+i*28*s,y+hh-3)],fill=(70,40,22),width=max(2,int(4*s)))
def grill(im,x0,y0,x1,y1,t):
    d=ImageDraw.Draw(im); rs=random.Random(3)
    d.rectangle([x0,y1-10,x1,y1+70],fill=(60,52,48),outline=INK,width=4)
    for i in range(26):
        cx=rs.uniform(x0+20,x1-20); cy=rs.uniform(y1+5,y1+60); g=.5+.5*math.sin(t*4+i)
        circle(im,cx,cy,14,LC((120,40,20),(240,130,40),g))
    d.rectangle([x0-10,y0,x1+10,y1],fill=(92,88,84),outline=INK,width=4)
    for x in range(int(x0),int(x1),34): d.line([(x,y0+4),(x,y1-4)],fill=(58,56,54),width=8)
def smoke(im,x,y,t,n=5):
    for i in range(n):
        ph=(t*.5+i/n)%1; circle(im,x+40*math.sin(ph*6+i),y-ph*260,18+ph*40,SMOKE,(1-ph)*.55)
def liver_slice(im,x,y,s=1,c=0.,ang=0):
    col=LC(LIVER,(150,88,44),c); pts=[]
    for i in range(24):
        a=i/24*2*math.pi; r=1+.12*math.sin(3*a+x)
        px,py=math.cos(a)*70*s*r,math.sin(a)*24*s*r; ca,sa=math.cos(ang),math.sin(ang)
        pts.append((x+px*ca-py*sa,y+px*sa+py*ca))
    ink_poly(im,pts,col,w=max(2,int(3*s)))
def pepper(im,x,y,s=1,ang=0.,col=PEP):
    pts=[]
    for i in range(14):
        u=i/13; px=-8*s*(1-u)+16*s*math.sin(u*2.2); py=u*110*s; w=(13*s)*(1-u**1.6)
        pts.append((px+w,py))
    for i in range(13,-1,-1):
        u=i/13; px=-8*s*(1-u)+16*s*math.sin(u*2.2); py=u*110*s; w=(13*s)*(1-u**1.6)
        pts.append((px-w,py))
    ca,sa=math.cos(ang),math.sin(ang); pts=[(x+a*ca-b*sa,y+a*sa+b*ca) for a,b in pts]
    ink_poly(im,pts,col,w=max(2,int(3*s))); ImageDraw.Draw(im).line([(x,y),(x+4*s,y-18*s)],fill=GREEN,width=max(2,int(6*s)))
def string_peppers(im,x0,x1,y,t,n=9,dry=0.):
    d=ImageDraw.Draw(im); d.line([(x0,y),(x1,y)],fill=INK,width=4)
    for i in range(n):
        x=x0+40+i*(x1-x0-80)/(n-1); sw=.12*math.sin(t*2+i)
        pepper(im,x,y,1.0,sw,LC(PEP,(122,30,24),dry))
def pan(im,x,y,r=260,t=0):
    d=ImageDraw.Draw(im); d.line([(x+r-20,y),(x+r+230,y-30)],fill=(50,46,44),width=26)
    d.ellipse([x-r,y-r*.42,x+r,y+r*.42],fill=(64,60,58),outline=INK,width=5); d.ellipse([x-r*.86,y-r*.34,x+r*.86,y+r*.34],fill=(196,150,60))
    rs=random.Random(9)
    for i in range(14):
        ph=(t*1.6+i/14)%1; circle(im,x+rs.uniform(-.7,.7)*r,y+rs.uniform(-.25,.25)*r,4+6*ph,(252,236,170),1-ph)
def cheese_block(im,x,y,s=1):
    d=ImageDraw.Draw(im); w,h,dp=170*s,90*s,60*s
    ink_poly(im,[(x-w,y-h),(x+w,y-h),(x+w,y+h),(x-w,y+h)],CREAM,w=4)
    ink_poly(im,[(x-w,y-h),(x-w+dp,y-h-dp*.6),(x+w+dp,y-h-dp*.6),(x+w,y-h)],(238,234,214),w=4)
    ink_poly(im,[(x+w,y-h),(x+w+dp,y-h-dp*.6),(x+w+dp,y+h-dp*.6),(x+w,y+h)],(222,218,198),w=4)
    rs=random.Random(4)
    for i in range(9): circle(im,x+rs.uniform(-.8,.8)*w,y+rs.uniform(-.7,.7)*h,4*s,(214,210,190))
def kasar_wheel(im,x,y,s=1):
    d=ImageDraw.Draw(im); rx,ry,hh=190*s,60*s,110*s
    d.rectangle([x-rx,y-hh/2,x+rx,y+hh/2],fill=(214,170,80)); d.ellipse([x-rx,y+hh/2-ry,x+rx,y+hh/2+ry],fill=(214,170,80),outline=INK,width=4)
    d.line([(x-rx,y-hh/2),(x-rx,y+hh/2)],fill=INK,width=4); d.line([(x+rx,y-hh/2),(x+rx,y+hh/2)],fill=INK,width=4)
    d.ellipse([x-rx,y-hh/2-ry,x+rx,y-hh/2+ry],fill=KASAR,outline=INK,width=4)
def helva_bowl(im,x,y,s=1,t=0,spice=1.):
    d=ImageDraw.Draw(im)
    d.chord([x-200*s,y-120*s,x+200*s,y+150*s],0,180,fill=(176,108,62),outline=INK,width=5)
    d.ellipse([x-200*s,y-40*s,x+200*s,y+40*s],fill=(150,96,52),outline=INK,width=5)
    d.ellipse([x-170*s,y-30*s,x+170*s,y+30*s],fill=(214,170,110))
    rs=random.Random(11); cols=[(120,60,30),(170,60,40),(90,110,50),(200,150,40),(80,50,40)]
    for i in range(int(41*spice)):
        a=rs.uniform(0,2*math.pi); r=rs.uniform(0,1)**.5; circle(im,x+math.cos(a)*150*s*r,y+math.sin(a)*24*s*r,5*s,cols[i%5])
def mill(im,x,y,s=1,t=0):
    ink_poly(im,[(x-90*s,y),(x+90*s,y),(x+90*s,y-120*s),(x-90*s,y-120*s)],(214,190,150),w=4)
    ink_poly(im,[(x-110*s,y-120*s),(x+110*s,y-120*s),(x,y-200*s)],RUST,w=4)
    d=ImageDraw.Draw(im); wx,wy,r=x+150*s,y-60*s,70*s
    d.ellipse([wx-r,wy-r,wx+r,wy+r],outline=INK,width=6)
    for i in range(8):
        a=t*1.5+i*math.pi/4; d.line([(wx,wy),(wx+math.cos(a)*r,wy+math.sin(a)*r)],fill=BROWN,width=6)
    d.rectangle([x-24*s,y-70*s,x+24*s,y],fill=(110,74,44),outline=INK,width=3)
    for i in range(6):
        ph=(t*.9+i/6)%1; d.arc([wx-r-30*s+ph*40,wy+r-10,wx-r+30*s+ph*40,wy+r+18],200,340,fill=(70,112,112),width=4)
def route(im,pts,p,col=RUST,w=10):
    # pts: ekran noktaları; p: 0-1 ilerleme, kesikli çizgi
    if len(pts)<2 or p<=0: return
    L=[math.dist(pts[i],pts[i+1]) for i in range(len(pts)-1)]; tot=sum(L); goal=tot*min(p,1); d=ImageDraw.Draw(im); acc=0
    for i in range(len(L)):
        a,b=pts[i],pts[i+1]; seg=L[i]; n=int(seg/26)
        for j in range(n):
            if acc+seg*j/n>goal: return
            if j%2==0:
                u0,u1=j/n,min(1,(j+1)/n); d.line([(a[0]+(b[0]-a[0])*u0,a[1]+(b[1]-a[1])*u0),(a[0]+(b[0]-a[0])*u1,a[1]+(b[1]-a[1])*u1)],fill=col,width=w)
        acc+=seg
