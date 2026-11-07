#!/usr/bin/env python3
import os; os.chdir('/home/claude/ata')
exec(open('/home/claude/sakli/shead.py').read())
AN=Image.open('anatolia.png').convert('RGB'); AN.load()
S=218.6; LON0=19.5; LAT0=40.5+2880/S
CC=math.cos(math.radians(40.5))
def AP(lat,lon): return ((lon-LON0)*S*CC,(LAT0-lat)*S)
def cam2(cx,cy,z):
    z=max(z,.334); w,h=W/z,H/z; x0,y0=cx-w/2,cy-h/2
    x0=max(0,min(x0,AN.width-w)); y0=max(0,min(y0,AN.height-h))
    im=AN.crop((int(x0),int(y0),int(x0+w),int(y0+h))).resize((W,H),Image.BILINEAR)
    return im,lambda px,py:((px-x0)*z,(py-y0)*z)
STOPS=[('selanik',40.64,22.94,'Selanik','1881','Doğduğu şehir'),('manastir',41.03,21.33,'Manastır','1896','Askerî idadi yılları'),
       ('canakkale',40.24,26.33,'Çanakkale','1915','Anafartalar'),('samsun',41.29,36.33,'Samsun','1919','Kurtuluşun ilk adımı'),
       ('ankara',39.93,32.86,'Ankara','1923','Cumhuriyet'),('istanbul',41.04,29.0,'İstanbul','1938','Dolmabahçe')]
RED=(200,16,32); DARK=(28,24,22)
def dim(im,a):
    ov=Image.new('RGB',im.size,DARK); return Image.blend(im,ov,a)
def flag(w,t):
    h=int(w*2/3); f=Image.new('RGB',(w,h),RED); d=ImageDraw.Draw(f); G=h
    cx=.5*G; d.ellipse([cx-.25*G,G/2-.25*G,cx+.25*G,G/2+.25*G],fill=(255,255,255))
    cx2=cx+.0625*G; d.ellipse([cx2-.2*G,G/2-.2*G,cx2+.2*G,G/2+.2*G],fill=RED)
    sx=cx2+.2*G+.0333*G+.125*G; r=.125*G; pts=[]
    for i in range(10):
        a=math.pi+i*math.pi/5; rr=r if i%2==0 else r*.382; pts.append((sx+rr*math.cos(a),G/2+rr*math.sin(a)))
    d.polygon(pts,fill=(255,255,255))
    a=np.asarray(f); out=np.zeros((h+40,w,3),np.uint8)+0
    for x in range(w):
        off=int(14*math.sin(x/w*5-t*3)*(x/w)); out[20+off:20+off+h,x]=a[:,x]
    sh=np.ones((h+40,w))*1.0
    for x in range(w): sh[:,x]=.85+.15*math.sin(x/w*5-t*3+1)
    out=(out*sh[...,None]).astype(np.uint8)
    m=np.zeros((h+40,w),np.uint8)
    for x in range(w):
        off=int(14*math.sin(x/w*5-t*3)*(x/w)); m[20+off:20+off+h,x]=255
    return Image.fromarray(out),Image.fromarray(m)
def put_flag(im,x,y,w,t):
    f,m=flag(w,t); ImageDraw.Draw(im).line([(x-6,y-10),(x-6,y+f.height+90)],fill=(200,200,200),width=10); im.paste(f,(int(x),int(y)),m)
def carnation(im,x,y,s=1):
    d=ImageDraw.Draw(im); d.line([(x,y),(x+6*s,y+170*s)],fill=(70,110,60),width=max(2,int(6*s)))
    rs=random.Random(int(x))
    for i in range(14):
        a=rs.uniform(0,2*math.pi); r=rs.uniform(4,26)*s; circle(im,x+math.cos(a)*r,y-8*s+math.sin(a)*r*.7,14*s,(186+rs.randint(-20,20),20,36))
def clock(im,cx,cy,R,t):
    d=ImageDraw.Draw(im); d.ellipse([cx-R-14,cy-R-14,cx+R+14,cy+R+14],fill=(176,140,70)); d.ellipse([cx-R,cy-R,cx+R,cy+R],fill=(246,238,214),outline=INK,width=6)
    for i in range(12):
        a=i*math.pi/6; d.line([(cx+math.sin(a)*R*.82,cy-math.cos(a)*R*.82),(cx+math.sin(a)*R*.94,cy-math.cos(a)*R*.94)],fill=INK,width=8)
    hm=(9+5/60)/12*2*math.pi; mm=5/60*2*math.pi
    d.line([(cx,cy),(cx+math.sin(hm)*R*.5,cy-math.cos(hm)*R*.5)],fill=INK,width=16)
    d.line([(cx,cy),(cx+math.sin(mm)*R*.78,cy-math.cos(mm)*R*.78)],fill=INK,width=10)
    sec=min(t,1.4); sa=(50+sec*6)/60*2*math.pi if t<1.4 else (50+1.4*6)/60*2*math.pi
    d.line([(cx,cy),(cx+math.sin(sa)*R*.86,cy-math.cos(sa)*R*.86)],fill=RED,width=4); circle(im,cx,cy,14,INK)
def s_hook(t):
    k='hook'; im=Image.new('RGB',(W,H),(232,220,192)); im=dim(im,.55)
    clock(im,540,860,300,t)
    T(im,"Saatler 09.05'te durdu",540,350,76,(240,230,206),LORA)
    if t>=ct(k,1)-.05: T(im,"10 Kasım 1938",540,1290,64,(240,230,206),LORA,a=clamp((t-ct(k,1))/.4)); T(im,"Dolmabahçe",540,1370,44,(214,200,170),LORAI,a=clamp((t-ct(k,1))/.4))
    return im
def base(t,upto,prog,focus=None,z=.334):
    if focus is None: cx,cy=AP(40.6,29.4)
    else: cx,cy=AP(*focus)
    im,m=cam2(cx,cy,z); pts=[m(*AP(s[1],s[2])) for s in STOPS]
    seg=pts[:upto+1]
    if upto>=1:
        full=pts[:upto]; route(im,full,1,RED,9)
        if prog<1: route(im,[pts[upto-1],pts[upto]],prog,RED,9)
        else: route(im,[pts[upto-1],pts[upto]],1,RED,9)
    for i in range(min(upto+1,len(pts))):
        if i<upto or prog>.95 or upto==0:
            x,y=pts[i]; circle(im,x,y,16,RED); circle(im,x,y,7,(250,240,220))
    return im,pts
def s_iz(t):
    im,pts=base(t,0,0); im=dim(im,.18); T(im,"Atatürk'ün izinde",540,330,80,INK,LORA,a=clamp(t/.5))
    for s in STOPS:
        pass
    return im
def mkstop(i):
    key,lat,lon,name,year,sub=STOPS[i]
    def f(t):
        p=ease(clamp(t/1.6)); fz=(.334+.2*ease(clamp((t-.2)/2.5)))
        cx=AP(lat,lon); prevc=AP(STOPS[i-1][1],STOPS[i-1][2]) if i>0 else cx
        im,pts=base(t,i,p,None,.334)
        x,y=pts[i]
        if p>.9: pin(im,x,y,t,None,RED)
        card(im,170,1250,910,1540); T(im,year,540,1320,72,RED,LORA,scale=back((t-.2)/.35)); T(im,name,540,1410,52,INK,LORA,a=clamp((t-.3)/.3)); T(im,sub,540,1480,40,(100,76,50),LORAI,a=clamp((t-.5)/.3))
        T(im,"Atatürk'ün izinde",540,330,64,INK,LORA)
        return im
    return f
def s_soz(t):
    im=Image.new('RGB',(W,H),(232,220,192)); im=dim(im,.6); c=TM['soz']['chunks']
    put_flag(im,330,300,420,t)
    T(im,"“Beni görmek demek,",540,820,58,(244,236,214),LORA,a=clamp(t/.5))
    T(im,"mutlaka yüzümü görmek değildir.",540,900,52,(244,236,214),LORA,a=clamp(t/.5))
    a=clamp((t-c[1][0])/.5) if t>=c[1][0]-.05 else 0
    for j,l in enumerate(["Benim fikirlerimi, benim duygularımı","anlıyorsanız ve hissediyorsanız","bu kâfidir.”"]):
        T(im,l,540,1030+j*70,44,(228,216,190),LORAI,a=a)
    T(im,"Mustafa Kemal Atatürk",540,1300,40,(214,190,140),LORA,a=a)
    return im
def s_cta(t):
    im=Image.new('RGB',(W,H),(232,220,192)); im=dim(im,.6)
    put_flag(im,330,300,420,t)
    T(im,"Saygıyla, özlemle",540,860,72,(244,236,214),LORA,a=clamp(t/.6)); T(im,"anıyoruz.",540,950,72,(244,236,214),LORA,a=clamp(t/.6))
    for i in range(7): carnation(im,240+i*100,1180+(i%2)*30,1.1)
    v=ve-TM['cta']['start']
    if t>v+.3: chip(im,"Yorumlara bir çiçek bırak",540,1460,44,back((t-v-.3)/.3),fill=RED)
    mark(im,"Müzik özgündür · Çizimler temsilidir"); return im
F={'hook':s_hook,'iz':s_iz,'soz':s_soz,'cta':s_cta}
for i,s in enumerate(STOPS): F[s[0]]=mkstop(i)
_oc=M.caption
def _cap2(img,now):
    if TM['selanik']['start']<=now<TM['cta']['end']+1 or now<TM['iz']['start']: return
    _oc(img,now)
M.caption=_cap2
exec(open('/home/claude/masal4/common.py').read())
