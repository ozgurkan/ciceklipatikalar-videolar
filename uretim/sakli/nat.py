# Saklı Doğa çizimleri (masal haritası tarzı)
import math, random
from PIL import ImageDraw
from m import *
from lz import *
STONE=(196,176,140); STONE2=(160,138,104); WATER=(150,190,196); DPINE=(52,92,62); PINK=(236,140,150)
Q={'uzk':PT(41.268,26.689),'kiy':PT(41.632,28.092),'ign':PT(41.877,27.983),'gal':PT(40.77,26.20),'gan':PT(40.75,27.27),'enz':PT(40.72,26.08),'ips':PT(40.92,26.38),'vize':PT(41.573,27.765)}
def water(im,x0,y0,x1,y1,t,col=WATER):
    d=ImageDraw.Draw(im); d.rectangle([x0,y0,x1,y1],fill=col)
    for r in range(int((y1-y0)/34)):
        yy=y0+18+r*34; off=(t*40+r*23)%60
        for x in range(int(x0-60+off),int(x1),120): d.arc([x,yy-8,x+44,yy+8],200,340,fill=(110,150,160),width=3)
def stone_bridge(im,x0,x1,y,n,p=1.,t=0):
    d=ImageDraw.Draw(im); w=(x1-x0)/n; m=int(n*p+.999)
    d.rectangle([x0,y-34,x0+(x1-x0)*min(1,p),y],fill=STONE,outline=INK,width=3)
    for i in range(m):
        ax=x0+i*w; d.rectangle([ax,y,ax+w,y+w*.9],fill=STONE,outline=INK,width=2)
        d.chord([ax+w*.12,y+w*.12,ax+w*.88,y+w*1.5],180,360,fill=WATER,outline=INK,width=2)
    for x in range(int(x0),int(x0+(x1-x0)*min(1,p)),26): d.line([(x,y-34),(x,y-30)],fill=STONE2,width=2)
def wall_gate(im,x,y,s=1):
    d=ImageDraw.Draw(im); w,h=320*s,220*s
    d.rectangle([x-w,y-h,x+w,y],fill=STONE,outline=INK,width=5)
    for i in range(9):
        cx=x-w+i*(2*w/8.5); d.rectangle([cx,y-h-34*s,cx+40*s,y-h],fill=STONE,outline=INK,width=4)
    d.chord([x-70*s,y-170*s,x+70*s,y+40*s],180,360,fill=(70,56,44)); d.rectangle([x-70*s,y-70*s,x+70*s,y],fill=(70,56,44))
    rs=random.Random(2)
    for i in range(30):
        bx=rs.uniform(x-w+10,x+w-50); by=rs.uniform(y-h+10,y-20)
        if abs(bx-x)>90*s: d.rectangle([bx,by,bx+40*s,by+18*s],outline=STONE2,width=2)
def cave_monastery(im,x,y,s=1):
    pts=[(x-300*s,y),(x-260*s,y-180*s),(x-120*s,y-260*s),(x+60*s,y-280*s),(x+240*s,y-200*s),(x+300*s,y)]
    ink_poly(im,pts,(176,160,130),w=5); d=ImageDraw.Draw(im)
    for (ox,oy,ww,hh) in [(-150,-80,70,110),(-40,-120,60,90),(60,-70,80,120),(170,-110,50,70)]:
        X,Y=x+ox*s,y+oy*s; d.chord([X-ww/2*s,Y-hh*s,X+ww/2*s,Y],180,360,fill=(60,48,40)); d.rectangle([X-ww/2*s,Y-hh/2*s,X+ww/2*s,Y],fill=(60,48,40))
    d.line([(x+60*s,y-200*s),(x+60*s,y-160*s)],fill=INK,width=5); d.line([(x+44*s,y-186*s),(x+76*s,y-186*s)],fill=INK,width=5)
def pine(im,x,y,s=1,col=DPINE):
    for k in range(3):
        ink_poly(im,[(x-50*s+k*10*s,y-k*44*s),(x+50*s-k*10*s,y-k*44*s),(x,y-90*s-k*44*s)],col,w=3)
    ImageDraw.Draw(im).rectangle([x-7*s,y,x+7*s,y+24*s],fill=BROWN)
def flood_tree(im,x,y,s=1,t=0,col=(96,132,70)):
    d=ImageDraw.Draw(im); d.rectangle([x-9*s,y-120*s,x+9*s,y],fill=BROWN,outline=INK,width=2)
    for (ox,oy,r) in [(0,-170,70),(-50,-130,52),(50,-130,52)]: circle(im,x+ox*s,y+oy*s,r*s,col)
    for i in range(3):
        ph=(t*.7+i/3)%1; d.ellipse([x-30*s-ph*60*s,y-6*s-ph*8*s,x+30*s+ph*60*s,y+6*s+ph*8*s],outline=(110,150,160),width=3)
def flamingo(im,x,y,s=1,t=0,ph=0):
    d=ImageDraw.Draw(im); b=math.sin(t*2+ph)*4*s
    d.line([(x-6*s,y),(x-6*s,y+110*s)],fill=(200,90,100),width=max(2,int(4*s))); d.line([(x+8*s,y),(x+18*s,y+60*s),(x+4*s,y+110*s)],fill=(200,90,100),width=max(2,int(4*s)))
    d.ellipse([x-46*s,y-40*s+b,x+46*s,y+10*s+b],fill=PINK,outline=INK,width=3)
    pts=[(x+36*s,y-24*s+b),(x+54*s,y-70*s+b),(x+34*s,y-110*s+b),(x+48*s,y-140*s+b)]
    d.line(pts,fill=PINK,width=max(3,int(10*s)),joint='curve'); circle(im,x+50*s,y-142*s+b,11*s,PINK)
    d.polygon([(x+58*s,y-146*s+b),(x+76*s,y-136*s+b),(x+60*s,y-132*s+b)],fill=INK)
def swan(im,x,y,s=1,t=0):
    d=ImageDraw.Draw(im); b=math.sin(t*1.5)*3*s
    d.chord([x-60*s,y-40*s+b,x+60*s,y+30*s+b],0,180,fill=(250,250,246),outline=INK,width=3)
    d.line([(x+40*s,y-4*s+b),(x+52*s,y-50*s+b),(x+40*s,y-74*s+b)],fill=(250,250,246),width=max(3,int(11*s)),joint='curve')
    d.polygon([(x+36*s,y-80*s+b),(x+18*s,y-72*s+b),(x+36*s,y-68*s+b)],fill=(230,130,40))
def relief(im,x,y,kind,s=1):
    d=ImageDraw.Draw(im); d.rounded_rectangle([x-90*s,y-80*s,x+90*s,y+80*s],14,fill=STONE,outline=INK,width=4); c=STONE2
    if kind=='fil':
        d.ellipse([x-55*s,y-35*s,x+40*s,y+25*s],fill=c); d.ellipse([x+20*s,y-45*s,x+60*s,y],fill=c); d.line([(x+56*s,y-10*s),(x+62*s,y+40*s)],fill=c,width=int(12*s))
        for lx in (-40,-15,10,30): d.rectangle([x+lx*s,y+15*s,x+(lx+12)*s,y+55*s],fill=c)
    elif kind=='aslan':
        circle(im,x+30*s,y-20*s,32*s,c); d.ellipse([x-55*s,y-20*s,x+30*s,y+25*s],fill=c); d.line([(x-55*s,y),(x-75*s,y-30*s)],fill=c,width=int(8*s))
        for lx in (-45,-20,5,20): d.rectangle([x+lx*s,y+15*s,x+(lx+10)*s,y+55*s],fill=c)
    else:
        d.ellipse([x-40*s,y-20*s,x+30*s,y+25*s],fill=c); circle(im,x+35*s,y-25*s,18*s,c); d.polygon([(x-30*s,y-10*s),(x-70*s,y-50*s),(x,y-5*s)],fill=c); d.polygon([(x+50*s,y-28*s),(x+68*s,y-22*s),(x+50*s,y-18*s)],fill=c)
def paraglider(im,x,y,s=1):
    d=ImageDraw.Draw(im); d.chord([x-90*s,y-40*s,x+90*s,y+40*s],180,360,fill=RUST,outline=INK,width=3)
    for dx in (-80,-30,30,80): d.line([(x+dx*s,y),(x,y+110*s)],fill=INK,width=2)
    circle(im,x,y+118*s,10*s,INK)
