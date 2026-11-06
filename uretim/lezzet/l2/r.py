#!/usr/bin/env python3
import os; os.chdir('/home/claude/lezzet/l2')
exec(open('/home/claude/lezzet/head.py').read())
SER="Trakya Lezzet Rotası · 2"
def s_hook(t):
    k='hook'; x,y=P['edi']; im,m=cam(x,y,.5+.01*t); banner(im,"Edirne Tava Ciğeri",SER,y=320,sz=80)
    card(im,140,640,940,1330); T(im,"< 1 mm",540,760,96,RUST,LORA,scale=back(t/.4))
    for i in range(5):
        liver_slice(im,540,900+i*46,2.3,0.,.04*math.sin(t*2+i))
    if t>=ct(k,1)-.05:
        s=back((t-ct(k,1)+.05)/.25); chip(im,"~2 dakika",540,1220,54,s)
    mark(im); return im
def s_yer(t):
    k='yer'; x,y=P['edi']; im,m=cam(x,y,.8+.03*t); banner(im,"Edirne","Meriç ve Tunca'nın şehri",y=320,sz=88)
    sx,sy=m(x,y); pin(im,sx,sy,t)
    if t>=ct(k,1)-.05: chip(im,"Şehrin en bilinen lezzeti",540,1300,46,back((t-ct(k,1)+.05)/.25),fill=GREEN)
    mark(im); return im
def s_kesim(t):
    k='kesim'; x,y=P['edi']; im,m=cam(x,y,.45); banner(im,"İnce ince",None,y=320,sz=84); card(im,110,600,970,1340)
    d=ImageDraw.Draw(im); d.rounded_rectangle([200,760,880,1000],24,fill=(196,150,100),outline=INK,width=5)
    n=min(9,int(t*4)+1)
    for i in range(n): liver_slice(im,330+(i%3)*210,820+(i//3)*60,1.2,0.)
    if t>=ct(k,1)-.05:
        p=clamp((t-ct(k,1))/.6)
        for i in range(30):
            rs=random.Random(i); circle(im,rs.uniform(200,880),1060+rs.uniform(0,160)*p,6,CREAM,.9)
        chip(im,"Una bulanır",540,1270,48,back((t-ct(k,1)+.05)/.25),fill=CLAY)
    return im
def s_tava(t):
    k='tava'; x,y=P['edi']; im,m=cam(x,y,.45); banner(im,"Kızgın yağda",None,y=320,sz=84); card(im,90,600,990,1340)
    pan(im,470,930,280,t); c=clamp(t/2.5)
    for i in range(6): liver_slice(im,340+(i%3)*130,900+(i//3)*60,.95,c,.3*math.sin(i))
    if t>=ct(k,1)-.05:
        chip(im,"Dışı çıtır",360,1210,46,back((t-ct(k,1)+.05)/.25),fill=RUST)
        chip(im,"İçi yumuşak",720,1210,46,back((t-ct(k,1)-.2)/.25),fill=GREEN)
    return im
def s_biber(t):
    k='biber'; c=TM[k]['chunks']
    if t<c[1][0]-.05:
        x,y=P['edi']; im,m=cam(x,y,.45); banner(im,"Karaağaç biberi",None,y=320,sz=80); card(im,140,640,940,1330)
        plate(im,540,980,300,110)
        for i in range(5): liver_slice(im,420+(i%3)*110,960+(i//3)*40,.9,1.)
        for i in range(3): pepper(im,690+i*40,900,.9,1.2+i*.2,(122,30,24))
        return im
    if t<c[2][0]-.05:
        x,y=P['kar']; im,m=cam(x,y,1.0+.03*(t-c[1][0])); banner(im,"Karaağaç","Yunanistan sınırında",y=320,sz=86)
        sx,sy=m(x,y); pin(im,sx,sy,t); return im
    x,y=P['edi']; im,m=cam(x,y,.45); banner(im,"İpe dizilir",None,y=320,sz=84); card(im,110,600,970,1340)
    dry=clamp((t-c[2][0])/2.)
    string_peppers(im,170,910,760,t,8,dry); string_peppers(im,170,910,960,t+.7,8,dry)
    T(im,"Gölgede kurutulur",540,1240,48,INK,LORA,a=clamp((t-c[2][0])/.4))
    return im
def s_tescil(t):
    k='tescil'; x,y=P['edi']; im,m=cam(x,y,.5); banner(im,"2010","Coğrafi işaret",y=320,sz=94); card(im,140,640,940,1330)
    s=back((t-.15)/.35); circle(im,540,920,170*max(s,.05),RUST); circle(im,540,920,140*max(s,.05),PAPER)
    if s>.6: T(im,"Edirne",540,870,48,RUST,LORA); T(im,"Tava Ciğeri",540,935,46,RUST,LORA)
    return im
def s_cta(t):
    k='cta'; x,y=P['edi']; im,m=cam(x,y,.42); banner(im,"Biberli mi, cacıklı mı?",None,y=320,sz=70); card(im,200,620,880,1420)
    plate(im,540,880,280,100)
    for i in range(5): liver_slice(im,420+(i%3)*110,860+(i//3)*40,.9,1.)
    for i in range(3): pepper(im,690+i*40,800,.9,1.2+i*.2,(122,30,24))
    if t>=ct(k,1)-.05: chip(im,"Yorumlara yaz",540,1080,50,back((t-ct(k,1)+.05)/.25))
    outro(im,t,nxt="Yarın: Trakya peynirleri")
    mark(im,"Müzik özgündür · Çizim temsilidir"); return im
F={'hook':s_hook,'yer':s_yer,'kesim':s_kesim,'tava':s_tava,'biber':s_biber,'tescil':s_tescil,'cta':s_cta}
exec(open('/home/claude/masal4/common.py').read())
