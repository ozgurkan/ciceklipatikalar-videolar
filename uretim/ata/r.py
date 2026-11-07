#!/usr/bin/env python3
import os; os.chdir('/home/claude/ata')
exec(open('/home/claude/sakli/shead.py').read())
AN=Image.open('anatolia.png').convert('RGB'); AN.load()
CC=math.cos(math.radians(37.5)); S=3240/(25*CC); LON0=19.5; LAT0=35.5+2880/S
def AP(lat,lon): return ((lon-LON0)*S*CC,(LAT0-lat)*S)
def cam2(cx,cy,z):
    w,h=W/z,H/z; x0,y0=cx-w/2,cy-h/2
    x0=max(0,min(x0,AN.width-w)); y0=max(0,min(y0,AN.height-h))
    im=AN.crop((int(x0),int(y0),int(x0+w),int(y0+h))).resize((W,H),Image.BILINEAR)
    return im,lambda px,py:((px-x0)*z,(py-y0)*z)
STOPS=[('selanik',40.64,22.94,'Selanik','1881','Doğduğu şehir','house'),('manastir',41.03,21.33,'Manastır','1896','Askerî idadi yılları','school'),
 ('harbiye',41.04,28.98,'İstanbul','1899','Harbiye yılları','school'),('sam',33.51,36.29,'Şam','1905','İlk görev yeri','dome'),
 ('trablus',32.08,23.96,'Trablusgarp','1911','Tobruk Savaşı','palm'),('sofya',42.70,23.32,'Sofya','1913','Askerî ataşe','bldg'),
 ('canakkale',40.24,26.33,'Çanakkale','1915','Anafartalar','hills'),('samsun',41.29,36.33,'Samsun','1919','Kurtuluşun ilk adımı','ship'),
 ('erzurum',39.91,41.27,'Erzurum','1919','Erzurum Kongresi','mount'),('sivas',39.75,37.02,'Sivas','1919','Sivas Kongresi','school'),
 ('meclis',39.94,32.85,'Ankara','1920','TBMM açıldı','meclis'),('sakarya',39.58,32.14,'Sakarya','1921','Sakarya Meydan Muharebesi','river'),
 ('dumlupinar',38.85,30.0,'Dumlupınar','1922','Büyük Zafer','victory'),('cumhuriyet',39.93,32.86,'Ankara','1923','Cumhuriyet ilan edildi','meclisflag'),
 ('istanbul',41.04,29.02,'İstanbul','1938','Dolmabahçe','palace')]
RED=(196,18,34); CREAM=(244,236,214); NIGHT=(34,30,40)
_vig=None
def vignette():
    global _vig
    if _vig is None:
        y,x=np.mgrid[0:H,0:W]; r=np.sqrt(((x-W/2)/(W*.62))**2+((y-H/2)/(H*.62))**2); _vig=np.clip(1-.55*np.clip(r-.45,0,1)**1.3,0,1).astype(np.float32)
    return _vig
def grade(im,t,sep=.35,dust=True):
    a=np.asarray(im).astype(np.float32); g=a.mean(2,keepdims=True)
    sepia=np.concatenate([g*1.07+12,g*.98+4,g*.82-6],2); a=a*(1-sep)+sepia*sep
    a*=vignette()[...,None]; im=Image.fromarray(np.clip(a,0,255).astype(np.uint8))
    if dust:
        rs=random.Random(7)
        for i in range(28):
            x0=rs.uniform(0,W); y0=rs.uniform(0,H); sp=rs.uniform(8,22)
            x=(x0+math.sin(t*.4+i)*30)%W; y=(y0-t*sp)%H; circle(im,x,y,rs.uniform(2,4.5),(255,240,210),.25+.2*math.sin(t+i))
    return im
def petals(im,t,n=18,seed=3):
    rs=random.Random(seed)
    for i in range(n):
        x0=rs.uniform(60,W-60); sp=rs.uniform(60,120); ph=rs.uniform(0,10)
        y=((t+ph)*sp)%(H+200)-100; x=x0+40*math.sin((t+ph)*1.3)
        ang=(t+ph)*2; r=14
        pts=[(x+math.cos(ang)*r,y+math.sin(ang)*r*.5),(x+math.cos(ang+2.4)*r*.6,y+math.sin(ang+2.4)*r*.4),(x+math.cos(ang+3.14)*r,y+math.sin(ang+3.14)*r*.5),(x+math.cos(ang+4)*r*.6,y+math.sin(ang+4)*r*.4)]
        poly(im,pts,(178,24,40))
def zoomed(im,s):
    if s<=1.001: return im
    w,h=W/s,H/s; return im.crop((int((W-w)/2),int((H-h)/2),int((W+w)/2),int((H+h)/2))).resize((W,H),Image.BILINEAR)
def sky(top=(52,46,62),bot=(196,150,110)):
    g=np.linspace(0,1,H)[:,None,None]; a=np.array(top)[None,None,:]*(1-g)+np.array(bot)[None,None,:]*g
    return Image.fromarray(np.repeat(a,W,1).astype(np.uint8))
def tower(im,cx,base,t,s=1.):
    d=ImageDraw.Draw(im); C=(222,210,186); D=(170,156,132)
    d.rectangle([cx-120*s,base-300*s,cx+120*s,base],fill=C,outline=INK,width=4)
    d.rectangle([cx-95*s,base-760*s,cx+95*s,base-300*s],fill=C,outline=INK,width=4)
    for i in range(3): d.rectangle([cx-130*s,base-300*s-i*6*s-12*s,cx+130*s,base-300*s-i*6*s],fill=D)
    d.rectangle([cx-75*s,base-1000*s,cx+75*s,base-760*s],fill=C,outline=INK,width=4)
    d.polygon([(cx-90*s,base-1000*s),(cx+90*s,base-1000*s),(cx,base-1160*s)],fill=(120,128,120),outline=INK)
    for k in (-1,1): d.chord([cx+k*55*s-30*s,base-260*s,cx+k*55*s+30*s,base-120*s],180,360,fill=(90,80,70)); d.rectangle([cx+k*55*s-30*s,base-190*s,cx+k*55*s+30*s,base-30*s],fill=(90,80,70))
    clock(im,cx,base-560*s,105*s,t)
def clock(im,cx,cy,R,t):
    d=ImageDraw.Draw(im); d.ellipse([cx-R-12,cy-R-12,cx+R+12,cy+R+12],fill=(176,140,70),outline=INK,width=3); d.ellipse([cx-R,cy-R,cx+R,cy+R],fill=(248,240,218),outline=INK,width=4)
    for i in range(12):
        a=i*math.pi/6; d.line([(cx+math.sin(a)*R*.8,cy-math.cos(a)*R*.8),(cx+math.sin(a)*R*.93,cy-math.cos(a)*R*.93)],fill=INK,width=max(3,int(R/30)))
    hm=(9+5/60)/12*2*math.pi; mm=5/60*2*math.pi
    d.line([(cx,cy),(cx+math.sin(hm)*R*.5,cy-math.cos(hm)*R*.5)],fill=INK,width=max(6,int(R/14)))
    d.line([(cx,cy),(cx+math.sin(mm)*R*.78,cy-math.cos(mm)*R*.78)],fill=INK,width=max(4,int(R/22)))
    sec=min(t,1.4); sa=(52+sec*5)/60*2*math.pi
    d.line([(cx,cy),(cx+math.sin(sa)*R*.86,cy-math.cos(sa)*R*.86)],fill=RED,width=3); circle(im,cx,cy,max(6,R/12),INK)
def s_hook(t):
    k='hook'; c=TM[k]['chunks']; im=sky()
    d=ImageDraw.Draw(im); water(im,0,1500,W,H,t,(88,104,120))
    tower(im,540,1500,t,1.0)
    for x in (120,960): d.rectangle([x-110,1260,x+110,1500],fill=(200,188,164),outline=INK,width=3)
    im=zoomed(im,1+.04*t)
    T(im,"10 Kasım 1938 · 09.05",540,230,62,CREAM,LORA,a=clamp((t+.4)/.4))
    if t>=c[1][0]-.05: T(im,"Dolmabahçe Sarayı",540,310,44,(230,214,180),LORAI,a=clamp((t-c[1][0])/.4))
    return grade(im,t,.25)
def s_iz(t):
    cx,cy=AP(34.9,32.0); im,m=cam2(cx,cy,.334)
    T(im,"Atatürk'ün izinde",540,300,84,INK,LORA,a=clamp(t/.5))
    pts=[m(*AP(s[1],s[2])) for s in STOPS]
    for i,(x,y) in enumerate(pts):
        if t>=.3+i*.25: circle(im,x,y,12,RED,.7)
    return grade(im,t)
def icon(im,key,cx,cy,t):
    d=ImageDraw.Draw(im)
    if key in ('dome','palm','bldg','mount','river','victory','meclisflag'): return icon2(im,key,cx,cy,t)
    key={'house':'selanik','school':'manastir','hills':'canakkale','ship':'samsun','meclis':'ankara','palace':'istanbul'}.get(key,key)
    if key=='selanik':
        ink_poly(im,[(cx-110,cy+80),(cx+110,cy+80),(cx+110,cy-30),(cx-110,cy-30)],(226,170,170)); ink_poly(im,[(cx-130,cy-30),(cx+130,cy-30),(cx,cy-110)],(150,70,50))
        ink_poly(im,[(cx-50,cy-30),(cx+50,cy-30),(cx+60,cy+20),(cx-60,cy+20)],(240,200,200))
        for x in (-80,-20,40,80): d.rectangle([cx+x-12,cy+30,cx+x+12,cy+66],fill=(90,80,90))
    elif key=='manastir':
        ink_poly(im,[(cx-140,cy+80),(cx+140,cy+80),(cx+140,cy-40),(cx-140,cy-40)],(222,208,176))
        for i in range(6): d.rectangle([cx-120+i*46,cy-20,cx-100+i*46,cy+20],fill=(90,90,100))
        d.rectangle([cx-24,cy+30,cx+24,cy+80],fill=(110,74,44)); d.line([(cx,cy-40),(cx,cy-130)],fill=INK,width=4); d.rectangle([cx,cy-130,cx+60,cy-92],fill=RED)
    elif key=='canakkale':
        water(im,cx-160,cy+20,cx+160,cy+90,t,(110,150,170))
        ink_poly(im,[(cx-160,cy+30),(cx-80,cy-60),(cx,cy-20),(cx+80,cy-90),(cx+160,cy+30)],(150,140,96))
        for i in range(9): x=cx-140+i*35; circle(im,x,cy+5-(i%3)*12,9,(200,30,36))
    elif key=='samsun':
        water(im,cx-160,cy+40,cx+160,cy+90,t,(110,150,170))
        ink_poly(im,[(cx-140,cy+40),(cx+140,cy+40),(cx+110,cy+80),(cx-110,cy+80)],(60,56,56))
        ink_poly(im,[(cx-90,cy+40),(cx+80,cy+40),(cx+80,cy),(cx-90,cy)],(236,228,210)); d.rectangle([cx-10,cy-80,cx+20,cy],fill=(60,56,56))
        for i in range(3): ph=(t*.5+i/3)%1; circle(im,cx+5+ph*40,cy-90-ph*90,12+ph*16,(200,196,190),1-ph)
    elif key=='ankara':
        ink_poly(im,[(cx-150,cy+80),(cx+150,cy+80),(cx+150,cy-20),(cx-150,cy-20)],(214,176,140))
        ink_poly(im,[(cx-165,cy-20),(cx+165,cy-20),(cx,cy-80)],(150,90,60))
        for i in range(5): d.rectangle([cx-120+i*60,cy,cx-100+i*60,cy+60],fill=(240,232,214),outline=INK)
    else:
        ink_poly(im,[(cx-160,cy+80),(cx+160,cy+80),(cx+160,cy-10),(cx-160,cy-10)],(232,224,206))
        for i in range(8): d.chord([cx-150+i*38,cy+10,cx-122+i*38,cy+70],180,360,fill=(120,120,130))
        d.rectangle([cx-26,cy-120,cx+26,cy-10],fill=(232,224,206),outline=INK,width=2); clock(im,cx,cy-80,20,9)
def icon2(im,key,cx,cy,t):
    d=ImageDraw.Draw(im)
    if key=='dome':
        d.rectangle([cx-140,cy+70,cx+140,cy+80],fill=(200,170,120))
        for dx,r in ((-70,40),(30,60)): d.chord([cx+dx-r,cy+70-r*1.4,cx+dx+r,cy+70+r*.6],180,360,fill=(230,214,180),outline=INK,width=3); d.rectangle([cx+dx-r,cy+30,cx+dx+r,cy+75],fill=(230,214,180),outline=INK)
        d.rectangle([cx+110,cy-90,cx+126,cy+75],fill=(230,214,180),outline=INK); d.polygon([(cx+106,cy-90),(cx+130,cy-90),(cx+118,cy-120)],fill=(150,110,70))
    elif key=='palm':
        water(im,cx-160,cy+40,cx+160,cy+90,t,(110,150,170)); d.rectangle([cx-160,cy+20,cx+160,cy+42],fill=(220,190,130))
        for x in (cx-60,cx+50):
            d.line([(x,cy+25),(x+10,cy-70)],fill=BROWN,width=9)
            for a in (-2.6,-2.0,-1.2,-0.5): d.line([(x+10,cy-70),(x+10+math.cos(a)*60,cy-70+math.sin(a)*40+25)],fill=GREEN,width=8)
    elif key=='bldg':
        ink_poly(im,[(cx-130,cy+80),(cx+130,cy+80),(cx+130,cy-10),(cx-130,cy-10)],(226,214,190)); d.chord([cx-50,cy-80,cx+50,cy+20],180,360,fill=(140,150,140),outline=INK)
        for i in range(5): d.rectangle([cx-110+i*48,cy+10,cx-92+i*48,cy+60],fill=(90,90,100))
    elif key=='mount':
        ink_poly(im,[(cx-160,cy+80),(cx-60,cy-70),(cx+20,cy+10),(cx+90,cy-90),(cx+160,cy+80)],(150,150,160))
        poly(im,[(cx-80,cy-40),(cx-60,cy-70),(cx-40,cy-40)],(250,250,250)); poly(im,[(cx+68,cy-58),(cx+90,cy-90),(cx+112,cy-58)],(250,250,250))
        ink_poly(im,[(cx-60,cy+80),(cx+60,cy+80),(cx+60,cy+30),(cx-60,cy+30)],(226,210,180))
    elif key=='river':
        ink_poly(im,[(cx-160,cy+80),(cx-160,cy-20),(cx-40,cy-70),(cx+80,cy-30),(cx+160,cy-60),(cx+160,cy+80)],(170,160,110))
        d.line([(cx-160,cy+60),(cx-40,cy+30),(cx+60,cy+55),(cx+160,cy+25)],fill=WATER,width=16)
    elif key=='victory':
        ink_poly(im,[(cx-160,cy+80),(cx-70,cy-30),(cx+20,cy+20),(cx+100,cy-50),(cx+160,cy+80)],(160,150,100))
        d.line([(cx+100,cy-50),(cx+100,cy-150)],fill=INK,width=5); d.rectangle([cx+100,cy-150,cx+170,cy-105],fill=RED)
        circle(im,cx+125,cy-128,13,(255,255,255)); circle(im,cx+130,cy-128,10,RED)
    elif key=='meclisflag':
        icon(im,'meclis',cx,cy,t); d.line([(cx,cy-80),(cx,cy-160)],fill=INK,width=5); d.rectangle([cx,cy-160,cx+70,cy-115],fill=RED)
        circle(im,cx+25,cy-138,13,(255,255,255)); circle(im,cx+30,cy-138,10,RED)
def mkstop(i):
    key,lat,lon,name,year,sub,ic=STOPS[i]
    def f(t):
        p=ease(clamp(t/1.0)); cxx,cyy=AP(34.9,32.0)
        im,m=cam2(cxx,cyy,.334+.012*clamp(t/3))
        pts=[m(*AP(s[1],s[2])) for s in STOPS]
        if i: route(im,pts[:i],1,RED,9); route(im,[pts[i-1],pts[i]],p,RED,9)
        for j in range(i+1):
            if j<i or p>.95: x,y=pts[j]; circle(im,x,y,15,RED); circle(im,x,y,6,CREAM)
        if p>.9: pin(im,*pts[i],t,None,RED)
        T(im,"Atatürk'ün izinde",540,250,60,INK,LORA); T(im,f"{i+1} / {len(STOPS)}",540,325,34,(110,80,56),LORA)
        a=back((t-.15)/.35)
        card(im,160,1250,920,1700)
        icon(im,ic,540,1370,t)
        T(im,year,540,1525,72,RED,LORA,scale=a); T(im,name,540,1600,52,INK,LORA,a=clamp((t-.2)/.3)); T(im,sub,540,1660,38,(100,76,50),LORAI,a=clamp((t-.35)/.3))
        return grade(im,t)
    return f
def flag(w,t):
    h=int(w*2/3); f=Image.new('RGB',(w,h),RED); d=ImageDraw.Draw(f); G=h
    cx=.5*G; d.ellipse([cx-.25*G,G/2-.25*G,cx+.25*G,G/2+.25*G],fill=(255,255,255))
    cx2=cx+.0625*G; d.ellipse([cx2-.2*G,G/2-.2*G,cx2+.2*G,G/2+.2*G],fill=RED)
    sx=cx2+.2*G+.0333*G+.125*G; r=.125*G; pts=[]
    for i in range(10):
        a=math.pi+i*math.pi/5; rr=r if i%2==0 else r*.382; pts.append((sx+rr*math.cos(a),G/2+rr*math.sin(a)))
    d.polygon(pts,fill=(255,255,255))
    a=np.asarray(f).astype(np.float32); out=np.zeros((h+60,w,3),np.float32); m=np.zeros((h+60,w),np.uint8)
    for x in range(w):
        ph=x/w*6-t*3; off=int(18*math.sin(ph)*(x/w)); sh=.82+.18*math.sin(ph+1.2)
        out[30+off:30+off+h,x]=a[:,x]*sh; m[30+off:30+off+h,x]=255
    return Image.fromarray(out.astype(np.uint8)),Image.fromarray(m)
def put_flag(im,x,y,w,t):
    f,m=flag(w,t); ImageDraw.Draw(im).line([(x-8,y-20),(x-8,y+f.height+90)],fill=(214,206,190),width=12); circle(im,x-8,y-26,12,(214,180,90)); im.paste(f,(int(x),int(y)),m)
def carnation(im,x,y,s=1,seed=0):
    d=ImageDraw.Draw(im); d.line([(x,y),(x+8*s,y+260*s)],fill=(66,104,58),width=max(3,int(7*s)))
    d.polygon([(x+4*s,y+120*s),(x+50*s,y+90*s),(x+10*s,y+140*s)],fill=(80,120,66))
    rs=random.Random(seed)
    for i in range(22):
        a=rs.uniform(0,2*math.pi); r=rs.uniform(2,30)*s; circle(im,x+math.cos(a)*r,y-10*s+math.sin(a)*r*.7,16*s,(170+rs.randint(-25,25),16,30+rs.randint(0,16)))
def dark(t):
    return sky((26,22,28),(70,58,52))
def s_soz(t):
    k='soz'; c=TM[k]['chunks']; im=dark(t); put_flag(im,300,240,480,t); petals(im,t,14)
    L1=["“Beni görmek demek,","mutlaka yüzümü görmek değildir."]; L2=["Benim fikirlerimi, benim duygularımı","anlıyorsanız ve hissediyorsanız","bu kâfidir.”"]
    for j,l in enumerate(L1): T(im,l,540,880+j*80,56,CREAM,LORA,a=clamp((t-j*.6)/.6))
    if t>=c[1][0]-.05:
        for j,l in enumerate(L2): T(im,l,540,1090+j*72,46,(232,220,196),LORAI,a=clamp((t-c[1][0]-j*.7)/.6))
        T(im,"— Mustafa Kemal Atatürk",540,1360,42,(220,190,130),LORA,a=clamp((t-c[1][0]-2.4)/.6))
    return grade(im,t,.15)
def s_cta(t):
    k='cta'; im=dark(t); put_flag(im,300,240,480,t); petals(im,t+5,20,9)
    T(im,"Saygıyla, özlemle",540,880,74,CREAM,LORA,a=clamp(t/.6)); T(im,"anıyoruz.",540,970,74,CREAM,LORA,a=clamp(t/.6))
    for i in range(9): carnation(im,180+i*90,1170+abs(4-i)*18,1.05,i)
    v=ve-TM[k]['start']
    if t>v+.4: chip(im,"Yorumlara bir çiçek bırak",540,1520,46,back((t-v-.4)/.3),fill=RED)
    mark(im,"Müzik özgündür · Çizimler temsilidir"); return grade(im,t,.15)
F={'hook':s_hook,'iz':s_iz,'soz':s_soz,'cta':s_cta}
for i,s in enumerate(STOPS): F[s[0]]=mkstop(i)
_oc=M.caption
def _cap2(img,now):
    if TM['selanik']['start']<=now: return
    _oc(img,now)
M.caption=_cap2
exec(open('/home/claude/masal4/common.py').read())
