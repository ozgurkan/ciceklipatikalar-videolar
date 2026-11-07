import json, math
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
topo=json.load(open('/home/claude/trakya/package/countries-50m.json'))
sc=topo['transform']['scale']; tr=topo['transform']['translate']
arcs=[]
for a in topo['arcs']:
    x=y=0; pts=[]
    for dx,dy in a: x+=dx; y+=dy; pts.append((x*sc[0]+tr[0], y*sc[1]+tr[1]))
    arcs.append(pts)
def ring(idx):
    out=[]
    for i in idx:
        p=arcs[i] if i>=0 else arcs[~i][::-1]
        out+=p if not out else p[1:]
    return out
W,H=3240,5760; LON0=19.5; LAT0=40.5+ (H/2)/218.6; S=218.6; C=math.cos(math.radians(40.5))
def P(lat,lon): return ((lon-LON0)*S*C/.76*.76, (LAT0-lat)*S)
SEA=(170,196,190); LAND=(232,214,170); INK=(90,66,44)
im=Image.new('RGB',(W,H),SEA); d=ImageDraw.Draw(im)
for g in topo['objects']['countries']['geometries']:
    polys=g['arcs'] if g['type']=='MultiPolygon' else [g['arcs']] if g['type']=='Polygon' else []
    for pg in polys:
        for k,r in enumerate(pg):
            pts=[P(la,lo) for lo,la in ring(r)]
            if len(pts)>2: d.polygon(pts,fill=LAND if k==0 else SEA)
for g in topo['objects']['countries']['geometries']:
    polys=g['arcs'] if g['type']=='MultiPolygon' else [g['arcs']] if g['type']=='Polygon' else []
    for pg in polys:
        for r in pg:
            pts=[P(la,lo) for lo,la in ring(r)]
            if len(pts)>2: d.line(pts+[pts[0]],fill=INK,width=3)
rng=np.random.default_rng(1); n=(rng.normal(0,1,(H//8,W//8))*6).astype(np.float32)
n=np.array(Image.fromarray(n).resize((W,H),Image.BILINEAR))
a=np.asarray(im).astype(np.float32)+n[...,None]
Image.fromarray(np.clip(a,0,255).astype(np.uint8)).save('anatolia.png')
print(P(40.64,22.94),P(39.93,32.86))
