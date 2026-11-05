#!/usr/bin/env python3
import sys, os, json, math, subprocess, random
sys.path.insert(0,'/home/claude/reels')
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from video import T, poly, circle, rrect, ease, eout, back, clamp, text_mask, BOLD, MED, warnings
Image.MAX_IMAGE_PIXELS=None
W,H,FPS=1080,1920,30
TM=json.load(open('timing.json')); ORDER=[k for k in TM if k[0]!='_']; XF=.34
LORA='/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf'; LORAI='/usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf'
TH=Image.open('thrace.png').convert('RGB'); TH.load(); EU=Image.open('europe.png').convert('RGB'); EU.load()
INK=(66,44,28); RUST=(150,70,40); PAPER=(242,228,194); CLAY=(186,108,62); GOLD=(190,128,34); DKBLUE=(36,66,76); GREEN=(92,114,58)
K=1500;OY=3000
def PT(lat,lon): return ((lon-25.8)*.755*K, OY-(lat-41)*K)
G0=PT(40.77,27.28)
def cam(cx,cy,z):
    # z: screen px per canvas px. returns view image, mapper
    z=max(z,.325); w,h=W/z,H/z; x0,y0=cx-w/2,cy-h/2
    x0=max(0,min(x0,TH.width-w)); y0=max(0,min(y0,TH.height-h))
    im=TH.crop((int(x0),int(y0),int(x0+w),int(y0+h))).resize((W,H),Image.BILINEAR)
    return im,lambda px,py:((px-x0)*z,(py-y0)*z)
def lerpc(a,b,p): return tuple(a[i]+(b[i]-a[i])*p for i in range(3))
def ink_poly(img,pts,fill,outline=INK,w=3):
    poly(img,pts,fill); ImageDraw.Draw(img).line(list(pts)+[pts[0]],fill=outline,width=w)
def ship(img,x,y,s=1,phase=0,sail=(244,232,204)):
    yb=y+5*s*math.sin(phase); w=max(2,int(3*s))
    ink_poly(img,[(x-105*s,yb),(x+115*s,yb),(x+78*s,yb+36*s),(x-70*s,yb+36*s)],(120,74,44),w=w)
    ImageDraw.Draw(img).line([(x,yb),(x,yb-160*s)],fill=INK,width=max(3,int(5*s)))
    ink_poly(img,[(x+2*s,yb-156*s),(x+105*s,yb-22*s),(x+2*s,yb-22*s)],sail,w=w)
    d=ImageDraw.Draw(img)
    for i,fx in enumerate((.35,.55,.75)):
        d.line([(x+2*s,yb-22*s-fx*134*s),(x+2*s+(1-fx)*103*s,yb-22*s-fx*134*s)],fill=(196,178,142),width=max(1,int(1.5*s)))
    for i in range(3):
        ox=(phase*12+i*70)%180-90
        d.arc([x+ox*s-34*s,yb+32*s,x+ox*s+34*s,yb+50*s],200,340,fill=(70,112,112),width=max(2,int(3*s)))
def amphora(img,x,y,s=1,fill=CLAY):
    pts=[(x-16*s,y-142*s),(x+16*s,y-142*s),(x+18*s,y-114*s),(x+42*s,y-96*s),(x+58*s,y-56*s),(x+50*s,y-14*s),(x+24*s,y+22*s),(x,y+36*s),(x-24*s,y+22*s),(x-50*s,y-14*s),(x-58*s,y-56*s),(x-42*s,y-96*s),(x-18*s,y-114*s)]
    ink_poly(img,pts,fill,w=max(2,int(4*s)))
    d=ImageDraw.Draw(img); d.line([(x-46*s,y-30*s),(x+46*s,y-30*s)],fill=(120,64,38),width=max(1,int(3*s))); d.line([(x-40*s,y-62*s),(x+40*s,y-62*s)],fill=(120,64,38),width=max(1,int(3*s)))
    for sn in(-1,1): d.arc([x+sn*22*s-18*s,y-132*s,x+sn*22*s+18*s,y-84*s],-90 if sn>0 else 90,90 if sn>0 else 270,fill=INK,width=max(2,int(5*s)))
def monastery(img,x,y,s=1):
    ink_poly(img,[(x-80*s,y),(x+80*s,y),(x+80*s,y-60*s),(x-80*s,y-60*s)],(238,226,196),w=max(2,int(3*s)))
    ink_poly(img,[(x-92*s,y-60*s),(x+92*s,y-60*s),(x,y-108*s)],RUST,w=max(2,int(3*s)))
    ink_poly(img,[(x-24*s,y-60*s),(x+24*s,y-60*s),(x+24*s,y-132*s),(x-24*s,y-132*s)],(232,216,184),w=max(2,int(3*s)))
    ink_poly(img,[(x-34*s,y-132*s),(x+34*s,y-132*s),(x,y-176*s)],RUST,w=max(2,int(3*s)))
    d=ImageDraw.Draw(img); d.line([(x,y-176*s),(x,y-206*s)],fill=INK,width=max(2,int(4*s))); d.line([(x-12*s,y-194*s),(x+12*s,y-194*s)],fill=INK,width=max(2,int(4*s)))
    for i in range(4): d.rectangle([x-62*s+i*38*s,y-44*s,x-48*s+i*38*s,y-12*s],fill=(90,66,46))
def banner(img,t1,t2=None,y=300,sz=78,sz2=46,col=INK,alpha=1):
    w=max(text_mask(t1,sz,LORA).width,(text_mask(t2,sz2,LORAI).width if t2 else 0))+110; h=(sz*1.35+(sz2*1.55 if t2 else 0))
    x0,x1=540-w/2,540+w/2; y0,y1=y-sz*.8,y-sz*.8+h
    # scroll ends
    for sx in(-1,1):
        ex=(x0 if sx<0 else x1)
        poly(img,[(ex-sx*6,y0+16),(ex+sx*34,y0+6),(ex+sx*20,(y0+y1)/2),(ex+sx*34,y1-6),(ex-sx*6,y1-16)],(214,194,150))
    rrect(img,x0,y0,x1,y1,12,PAPER); ImageDraw.Draw(img).rounded_rectangle([x0,y0,x1,y1],12,outline=INK,width=4)
    T(img,t1,540,y,sz,col,LORA)
    if t2: T(img,t2,540,y+sz*.62+sz2*.55,sz2,RUST,LORAI)
def chip(img,txt,x,y,sz,s=1,fill=RUST,tc=(250,240,220)):
    tw=text_mask(txt,sz,LORA).width; hw,hh=(tw/2+26)*s,sz*.82*s
    rrect(img,x-hw,y-hh,x+hw,y+hh,16*s,fill); ImageDraw.Draw(img).rounded_rectangle([x-hw,y-hh,x+hw,y+hh],16*s,outline=INK,width=3); T(img,txt,x,y,sz,tc,LORA,scale=s)
def mark(img,txt="Çizim temsilidir"):
    T(img,txt,540,1600,26,(92,70,44),LORAI,a=.9)
def caption(img,now):
    for k in ORDER:
        s=TM[k]['start']
        for a,b,txt in TM[k]['chunks']:
            if s+a<=now<s+b:
                if now<.2: return
                sz=50; tw=text_mask(txt,sz,BOLD).width
                while tw>840 and sz>34: sz-=4; tw=text_mask(txt,sz,BOLD).width
                rrect(img,540-tw/2-26,1490-44,540+tw/2+26,1490+44,16,(250,240,216),.96); ImageDraw.Draw(img).rounded_rectangle([540-tw/2-26,1446,540+tw/2+26,1534],16,outline=INK,width=3)
                T(img,txt,540,1490,sz,INK,BOLD); return
def s_hook(t):
    px=PT(40.68,27.65); im,m=cam(px[0],px[1],.42+.02*t)
    x,y=m(*PT(40.72,27.55)); ship(im,x+t*12,y,.95,phase=t*1.6)
    banner(im,"Trakya Bağ Rotası","Bölüm 1 · Bin yıllık yolculuk",y=320,sz=82); mark(im); return im
def s_homer(t):
    im,m=cam(*PT(40.72,27.1),.36); c=TM['homer']['chunks']
    banner(im,"Trakya'nın bağ ünü",None,y=320,sz=76)
    a=eout((t-.15)/.45); y0=560+50*(1-a)
    rrect(img:=im,150,y0,930,y0+650,20,PAPER,a); ImageDraw.Draw(im).rounded_rectangle([150,y0,930,y0+650],20,outline=INK,width=5)
    T(im,"Homeros · Odysseia",540,y0+74,48,RUST,LORAI,a=a)
    # engraved sea
    d=ImageDraw.Draw(im)
    for i in range(7):
        yy=y0+470+i*26; o=(t*30+i*50)%110
        for xx in range(170,900,110): d.arc([xx+o-55,yy,xx+o+15,yy+18],200,340,fill=(80,120,120),width=3)
    if a>.5: ship(im,420+t*18,y0+470,1.15,phase=t*1.3)
    if t>=c[2][0]-.1:
        s=back((t-c[2][0]+.1)/.25); chip(im,"Kiklop'u uyutan Trakya şarabı",540,y0+170,40,s)
    return im
def s_ganos(t):
    c=TM['ganos']['chunks']; p=ease(t/2.2); z=.42+.5*p
    a,b=PT(40.72,27.1),G0; cx=a[0]+(b[0]-a[0])*p; cy=a[1]+(b[1]-a[1])*p-60
    im,m=cam(cx,cy,z)
    banner(im,"Gaziköy","O zamanki adıyla Ganos" if t>=c[1][0]-.05 else None,y=320,sz=86)
    x,y=m(*G0); pulse=1+.12*math.sin(t*5); ImageDraw.Draw(im).ellipse([x-90*pulse,y-90*pulse,x+90*pulse,y+90*pulse],outline=RUST,width=6)
    if t>=c[2][0]-.05: chip(im,"Ganos Dağı · Marmara",540,1320,44,back((t-c[2][0]+.05)/.25))
    mark(im); return im
def s_monks(t):
    c=TM['monks']['chunks']; im,m=cam(G0[0]+40,G0[1]-200,.92+.015*t)
    banner(im,"10. yüzyıl",None,y=320,sz=86)
    x,y=m(*PT(40.875,27.26))
    s=back((t-.35)/.4); monastery(im,x,y,1.0*max(s,.01))
    if t>=c[1][0]: chip(im,"Dağda manastır topluluğu",540,560,44,back((t-c[1][0])/.25))
    if t>=c[2][0]-.05: chip(im,"Bağların bir kısmı onların olabilir",540,1320,40,back((t-c[2][0]+.05)/.25),fill=GREEN)
    mark(im); return im
def s_amph(t):
    c=TM['amph']['chunks']; im,m=cam(G0[0]+150,G0[1]+40,.8+.015*t)
    banner(im,"11. yüzyıl",None,y=320,sz=86)
    # kiln vignette
    a=eout(t/.5); bx,by=540,1040
    rrect(im,60,690,1020,1345,26,PAPER,.97); ImageDraw.Draw(im).rounded_rectangle([60,690,1020,1345],26,outline=INK,width=5)
    ink_poly(im,[(bx-140,by),(bx+140,by),(bx+110,by-170),(bx+40,by-240),(bx-40,by-240),(bx-110,by-170)],(168,120,86),w=5)
    fl=.55+.45*math.sin(t*9)*math.sin(t*5.3+1); ImageDraw.Draw(im).pieslice([bx-82,by-170,bx+82,by-12],180,360,fill=(44,24,18))
    for r,col in [(66,(204,92,36)),(44+6*fl,(236,150,50)),(24+5*fl,(252,212,110))]: circle(im,bx,by-40,r,col)
    d=ImageDraw.Draw(im)
    for i in range(5):
        ph=(t*.4+i*.2)%1; circle(im,bx+12*math.sin(ph*9+i),by-260-ph*230,18+ph*30,(120,108,96),.55*(1-ph))
    if t>=c[1][0]-.05:
        n=min(5,int(max(0,t-c[1][0])*1.7)+1)
        for i in range(n):
            s=back((t-c[1][0]-i*.42)/.28); amphora(im,170+i*185,1240,1.1*max(s,.02))
    if t>=c[2][0]-.05:
        s=eout((t-c[2][0]+.05)/.8); x,y=m(*PT(40.70,27.52)); ship(im,1320-300*s,1160,.7,phase=t*1.4)
    return im
DEST=[("İstanbul",41.01,28.98,1),("Atina",37.98,23.73,-1),("Mısır",31.2,29.92,1),("G. İtalya",40.64,17.0,-1),("Kiev",50.45,30.52,1),("İsveç",59.6,17.72,1)]
def Pm(lat,lon): return (540+(lon-23)*.707*31,860-(lat-44.5)*31)
def s_map(t):
    c=TM['map']['chunks']; im=EU.copy(); banner(im,"Küplerin izi",None,y=300,sz=72)
    ts={"İstanbul":c[0][0]+.5,"Atina":c[1][0],"Mısır":c[2][0],"G. İtalya":c[3][0]-.45,"Kiev":c[3][0]+.2,"İsveç":c[3][0]+.95}
    g=Pm(40.77,27.28); d=ImageDraw.Draw(im)
    for name,la,lo,side in DEST:
        p=eout((t-ts[name])/.65)
        if p<=0: continue
        q=Pm(la,lo); mid=((g[0]+q[0])/2+(q[1]-g[1])*.08,(g[1]+q[1])/2-30)
        pts=[((1-u)**2*g[0]+2*(1-u)*u*mid[0]+u*u*q[0],(1-u)**2*g[1]+2*(1-u)*u*mid[1]+u*u*q[1]) for u in np.linspace(0,p,40)]
        for j in range(0,len(pts)-1,2): d.line([pts[j],pts[j+1]],fill=RUST,width=6)
        if p>.9:
            amphora(im,q[0],q[1]+6,.24); w=text_mask(name,40,LORA).width
            T(im,name,min(max(q[0]+side*(w/2+26),w/2+70),W-w/2-130),q[1],40,INK,LORA)
    amphora(im,g[0],g[1]+8,.3,fill=RUST); T(im,"Ganos",g[0]-80,g[1]+40,34,RUST,LORAI)
    chip(im,"Bu tip küpler Ganos ile ilişkilendirilir",540,1385,28,1,fill=PAPER,tc=INK); return im
def s_later(t):
    c=TM['later']['chunks']; im,m=cam(*PT(40.72,27.4),.56); banner(im,"Osmanlı dönemi",None,y=320,sz=80)
    x,y=m(*PT(40.48,27.75)); ship(im,x+t*6,y,.6,phase=t*1.2)
    if t>=.5: chip(im,"Ticaret küçüldü",540,540,46,back((t-.5)/.25))
    if t>=c[1][0]-.05: chip(im,"Üretim yerelde sürdü",540,1320,46,back((t-c[1][0]+.05)/.25),fill=GREEN)
    mark(im); return im
def s_today(t):
    p=ease(t/3.4); a=PT(40.85,27.25); b=PT(41.4,27.1); im,m=cam(a[0]+(b[0]-a[0])*p,a[1]+(b[1]-a[1])*p,.46)
    banner(im,"Bugün","Trakya rotasının kalbi",y=320,sz=86)
    for la,lo in [(40.77,27.28),(40.98,27.51),(41.25,27.2),(41.73,27.22),(41.68,26.56)]:
        x,y=m(*PT(la,lo)); circle(im,x,y,18,RUST); circle(im,x,y,7,PAPER)
    return im
def s_cta(t):
    ve=TM['_voice_end']-TM['cta']['start']; z=.34-.03*ease(t/4); px=PT(40.9,27.5); im,m=cam(px[0],px[1],z)
    s=back(t/.3); banner(im,"Bağlar neden","tam burada?",y=320,sz=86,sz2=70)
    x,y=m(*PT(40.7,27.9)); ship(im,x+t*7,y,.8,phase=t*1.4)
    c=TM['cta']['chunks']
    if t>=c[1][0]-.05: chip(im,"Cevabı 2. bölümde",540,1250,52,back((t-c[1][0]+.05)/.25))
    if t>ve+.3: T(im,"Takipte kal · @ciceklipatikalar",540,1370,40,INK,LORA,a=clamp((t-ve-.3)/.6))
    mark(im,"Müzik özgündür · Çizim temsilidir"); return im
F={'hook':s_hook,'homer':s_homer,'ganos':s_ganos,'monks':s_monks,'amph':s_amph,'map':s_map,'later':s_later,'today':s_today,'cta':s_cta}
def frame(now):
    for i,k in enumerate(ORDER):
        a,b=TM[k]['start'],TM[k]['end']
        if now<b or i==len(ORDER)-1:
            im=F[k](now-a)
            if i and now-a<XF:
                p=ORDER[i-1]; im=Image.blend(F[p](now-TM[p]['start']),im,ease((now-a)/XF))
            caption(im,now); return im
def render(k):
    a,b=TM[k]['start'],TM[k]['end']; n0,n1=round(a*FPS),round(b*FPS); os.makedirs('parts',exist_ok=True); tmp,out=f'parts/{k}.tmp.mp4',f'parts/{k}.mp4'
    p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-crf','20','-preset','veryfast','-pix_fmt','yuv420p',tmp],stdin=subprocess.PIPE)
    for i in range(n0,n1): p.stdin.write(frame(i/FPS).tobytes())
    p.stdin.close()
    if p.wait()==0: os.replace(tmp,out); print('done',k,flush=True)
    else: sys.exit(1)
if __name__=='__main__':
    if sys.argv[1]=='still':
        os.makedirs('stills',exist_ok=True)
        for f in os.listdir('stills'): os.remove('stills/'+f)
        for k in ORDER:
            a,b=TM[k]['start'],TM[k]['end']; frame(a+(b-a)*.85).save(f'stills/{a+(b-a)*.85:06.2f}_{k}.jpg',quality=86)
        frame(0).save('stills/000.00_c.jpg',quality=88); print('warn',warnings)
    else: render(sys.argv[2])
