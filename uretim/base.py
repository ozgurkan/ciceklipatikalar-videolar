import json, math, random, numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
def fbm(h,w,seed,oct=6,base=4,pers=.55,sx=1.,sy=1.):
    r=np.random.default_rng(seed); o=np.zeros((h,w),np.float32);a=1.;t=0
    for i in range(oct):
        gw=max(3,int(base*2**i*sx)+2); gh=max(3,int(base*2**i*sy*h/w)+2)
        o+=a*np.asarray(Image.fromarray((r.random((gh,gw))*255).astype(np.uint8)).resize((w,h),Image.BICUBIC),np.float32)/255; t+=a;a*=pers
    o/=t; return (o-o.min())/(o.max()-o.min())
d=json.load(open('package/countries-50m.json')); tr=d['transform']; ARCS=[]
for a in d['arcs']:
    x=y=0;pts=[]
    for dx,dy in a: x+=dx;y+=dy;pts.append((x*tr['scale'][0]+tr['translate'][0],y*tr['scale'][1]+tr['translate'][1]))
    ARCS.append(pts)
def ring(r):
    o=[]
    for i in r:
        p=ARCS[i] if i>=0 else ARCS[~i][::-1]; o+=p[1:] if o else p
    return o
def rings(pred):
    out=[]
    for g in d['objects']['countries']['geometries']:
        if g.get('arcs') and pred(g.get('properties',{}).get('name','')):
            for p in (g['arcs'] if g['type']=='MultiPolygon' else [g['arcs']]): out.append(ring(p[0]))
    return out
LORA='/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf'; LORAI='/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf'
INK=(66,44,28); RUST=(150,70,40)
# ---- Thrace canvas
CW,CH=4300,6000; K=1500; OY=3000
def P(lat,lon): return ((lon-25.8)*.755*K, OY-(lat-41)*K)
def paper(w,h,seed):
    n=fbm(h//2,w//2,seed,6,6,.6); n2=fbm(h//2,w//2,seed+1,4,2,.55)
    p=np.stack([232+n*16-n2*16,216+n*16-n2*22,176+n*18-n2*26],-1)
    fib=fbm(h//2,w//2,seed+2,3,90,.7,sy=.2)[...,None]; p=p*(.96+.08*fib)
    return np.asarray(Image.fromarray(np.clip(p,0,255).astype(np.uint8)).resize((w,h),Image.BICUBIC),np.float32)
def land_mask(rs,proj,w,h,s=2):
    m=Image.new('L',(w//s,h//s),0); dr=ImageDraw.Draw(m)
    for r in rs:
        pts=[proj(la,lo) for lo,la in r]
        if max(p[0] for p in pts)<-400 or min(p[0] for p in pts)>w+400 or max(p[1] for p in pts)<-400 or min(p[1] for p in pts)>h+400: continue
        if max(lo for lo,la in r)-min(lo for lo,la in r)>300: continue
        dr.polygon([(x/s,y/s) for x,y in pts],fill=255)
    return m.resize((w,h),Image.BILINEAR)
def compose(paperarr,mask,seed,sea=(150,184,176),land=(226,204,150)):
    h,w=paperarr.shape[:2]; m=np.asarray(mask,np.float32)/255
    s=np.asarray(mask.resize((w//4,h//4)).filter(ImageFilter.GaussianBlur(14)).resize((w,h),Image.BICUBIC),np.float32)/255
    wash=fbm(h//4,w//4,seed,5,6,.6); wash=np.asarray(Image.fromarray((wash*255).astype(np.uint8)).resize((w,h),Image.BICUBIC),np.float32)/255
    seaC=np.array(sea,np.float32)*(.95+.1*wash[...,None]); landC=np.array(land,np.float32)*(.93+.14*wash[...,None])
    a=paperarr*.52+(seaC*(1-m[...,None])+landC*m[...,None])*.48
    # coastal shading
    edge=np.clip(s-m,0,1); a=a*(1-edge[...,None]*.36)+np.array((104,132,126),np.float32)*(edge[...,None]*.36)
    return a
def build_thrace():
    pa=paper(CW,CH,5)
    mask=land_mask(rings(lambda n:n in('Turkey','Greece','Bulgaria','Romania','North Macedonia')),P,CW,CH)
    a=compose(pa,mask,7)
    im=Image.fromarray(np.clip(a,0,255).astype(np.uint8)); dr=ImageDraw.Draw(im)
    for r in rings(lambda n:n in('Turkey','Greece','Bulgaria')):
        pts=[P(la,lo) for lo,la in r]
        if max(p[0] for p in pts)<-100 or min(p[0] for p in pts)>CW+100 or min(p[1] for p in pts)>CH or max(p[1] for p in pts)<0: continue
        dr.line(pts+pts[:1],fill=INK,width=5,joint='curve')
    rs=random.Random(3)
    ma=np.asarray(mask.resize((CW//4,CH//4)),np.uint8)
    # sea wave ticks
    for i in range(2300):
        x,y=rs.randrange(CW),rs.randrange(1400,4700)
        if ma[min(CH//4-1,y//4),min(CW//4-1,x//4)]>10: continue
        w=rs.randrange(22,46); dr.arc([x,y,x+w,y+16],200,340,fill=(96,132,128),width=3); dr.arc([x+w,y,x+2*w,y+16],200,340,fill=(96,132,128),width=3)
    def mountain(x,y,s,col=(158,140,104)):
        dr.polygon([(x-90*s,y),(x+90*s,y),(x,y-130*s)],fill=col,outline=INK)
        dr.polygon([(x,y-130*s),(x+90*s,y),(x+18*s,y)],fill=(128,110,82))
        dr.line([(x-90*s,y),(x,y-130*s),(x+90*s,y)],fill=INK,width=max(3,int(4*s)))
        dr.polygon([(x-22*s,y-98*s),(x,y-130*s),(x+22*s,y-98*s),(x+6*s,y-104*s),(x-8*s,y-92*s)],fill=(244,236,214))
    def tree(x,y,s,col):
        dr.line([(x,y),(x,y-26*s)],fill=INK,width=max(2,int(4*s))); dr.ellipse([x-26*s,y-72*s,x+26*s,y-20*s],fill=col,outline=INK,width=max(2,int(3*s)))
    def vine(cx,cy,w,h,seed):
        r=random.Random(seed)
        n=int(h/22)
        for i in range(n):
            y=cy+i*22; x0=cx+r.randint(-14,14); x1=cx+w+r.randint(-14,14)
            if ma[min(CH//4-1,int(y)//4),min(CW//4-1,int(x0)//4)]>=200 and ma[min(CH//4-1,int(y)//4),min(CW//4-1,int(x1)//4)]>=200: dr.line([(x0,y),(x1,y)],fill=(88,62,34),width=3)
            for x in range(int(x0),int(x1),18):
                if ma[min(CH//4-1,int(y)//4),min(CW//4-1,int(x)//4)]<200: continue
                dr.ellipse([x-8,y-11,x+8,y+3],fill=r.choice([(94,120,62),(118,132,66),(146,142,70),(176,134,58)]),outline=(58,70,36))
    def town(lat,lon,name,side=1,sz=74,dy=0):
        x,y=P(lat,lon)
        for ox,oy,s in [(-34,4,.9),(4,-8,1.1),(36,8,.8)]:
            xx,yy=x+ox,y+oy; dr.polygon([(xx-22*s,yy),(xx+22*s,yy),(xx+22*s,yy-34*s),(xx-22*s,yy-34*s)],fill=(240,228,198),outline=INK)
            dr.polygon([(xx-28*s,yy-34*s),(xx+28*s,yy-34*s),(xx,yy-60*s)],fill=RUST,outline=INK)
        f=ImageFont.truetype(LORA,sz); f.set_variation_by_name('Bold') if False else None
        w=f.getlength(name); tx=x+side*70 if side>0 else x-70-w
        dr.text((tx,y-sz*.8+dy),name,font=f,fill=INK)
    # Ganos range, hills, vines, trees (positions are artistic within the real area)
    G=[(40.90,27.08),(40.92,27.20),(40.93,27.32),(40.90,27.44),(40.85,27.00),(40.86,27.14),(40.87,27.26),(40.86,27.38),(40.82,26.95)]
    for la,lo in G:
        x,y=P(la,lo); mountain(x,y,1.4)
    for (la,lo,w,h) in [(40.75,26.98,300,176),(40.80,27.42,310,154),(40.98,27.04,320,176),(41.10,27.30,320,176),(41.25,27.05,320,176),(41.45,27.45,320,176),(41.58,26.80,320,176),(41.50,27.05,300,154)]:
        x,y=P(la,lo); vine(x,y,w,h,int(x))
    for i in range(170):
        la,lo=rs.uniform(40.72,41.8),rs.uniform(26.2,28.4); x,y=P(la,lo)
        if ma[min(CH//4-1,int(y)//4),min(CW//4-1,int(x)//4)]<200: continue
        if 40.68<la<41.0 and 26.9<lo<27.6: continue
        if any(abs(la-a)<.05 and abs(lo-b)<.12 for a,b in [(40.98,27.51),(41.68,26.56),(41.73,27.22)]): continue
        tree(x,y,rs.uniform(.8,1.3),rs.choice([(180,130,60),(128,136,70),(166,96,54),(104,120,62)]))
    for la,lo,n,s in [(40.98,27.51,'Tekirdağ',1),(40.77,27.28,'Gaziköy',1),(40.67,27.24,'Mürefte',1),(40.61,27.11,'Şarköy',1),(41.68,26.56,'Edirne',1),(41.73,27.22,'Kırklareli',1),(41.01,28.98,'İstanbul',1)]:
        town(la,lo,n,s)
    # sea & titles
    def label(txt,x,y,sz,col,path=LORAI):
        f=ImageFont.truetype(path,sz); w=f.getlength(txt); dr.text((x-w/2,y),txt,font=f,fill=col)
    x,y=P(40.66,28.25); label('Marmara Denizi',x,y,126,(40,74,84))
    x,y=P(40.25,26.1); label('Ege Denizi',x,y,104,(40,74,84))
    x,y=P(41.75,28.95); label('Karadeniz',x,y,104,(40,74,84))
    # compass
    x,y=P(39.75,28.75); r=170
    dr.ellipse([x-r,y-r,x+r,y+r],outline=INK,width=6)
    for a,l,col in [(0,1,RUST),(90,.72,INK),(180,.72,INK),(270,.72,INK)]:
        t=math.radians(a); tip=(x+math.sin(t)*r*l,y-math.cos(t)*r*l); sd=(math.cos(t)*30,math.sin(t)*30)
        dr.polygon([tip,(x+sd[0],y+sd[1]),(x-sd[0],y-sd[1])],fill=col,outline=INK)
    label('K',x,y-r-90,62,RUST,LORA)
    # vignette on paper edges
    a=np.asarray(im,np.float32); yy,xx=np.mgrid[0:CH,0:CW].astype(np.float32)
    v=np.clip(np.minimum.reduce([xx,yy,CW-xx,CH-yy])/120,0,1)[...,None]
    a=a*(.72+.28*v)
    Image.fromarray(np.clip(a,0,255).astype(np.uint8)).save('thrace.png')
# ---- Europe sheet
def build_europe():
    W,H=1080,1920; k=31; C=(23,44.5)
    def Pm(lat,lon): return (540+(lon-C[0])*.707*k,860-(lat-C[1])*k)
    pa=paper(W,H,11); m=land_mask(rings(lambda n:n!='Antarctica'),Pm,W,H,1)
    a=compose(pa,m,13)
    im=Image.fromarray(np.clip(a,0,255).astype(np.uint8)); dr=ImageDraw.Draw(im)
    for r in rings(lambda n:n!='Antarctica'):
        if max(lo for lo,la in r)-min(lo for lo,la in r)>300: continue
        pts=[Pm(la,lo) for lo,la in r]
        if max(p[0] for p in pts)<0 or min(p[0] for p in pts)>W or max(p[1] for p in pts)<0 or min(p[1] for p in pts)>H: continue
        dr.line(pts+pts[:1],fill=(116,88,58),width=1)
    im.save('europe.png')
build_thrace(); build_europe()
th=Image.open('thrace.png'); x0,y0=P(41.05,26.8); th.crop((int(x0),int(y0),int(x0)+1600,int(y0)+1000)).resize((800,500)).save('p2.jpg',quality=85)
