import numpy as np, json, soundfile as sf
TM=json.load(open('timing.json')); SR=44100; N=int(TM['_dur']*SR)+SR; out=np.zeros(N,np.float32); rng=np.random.default_rng(1)
def add(x,t,g=1.):
    i=int(t*SR); x=x[:max(0,N-i)]; out[i:i+len(x)]+=x*g
def env(n,a=.01,d=.2): t=np.arange(n)/SR; return np.minimum(t/a,1)*np.exp(-t/d)
def whoosh(dur=.42):
    n=int(dur*SR); x=rng.normal(0,1,n); t=np.arange(n)/SR; k=np.exp(-((t-dur*.55)/(dur*.22))**2)
    y=np.zeros(n); c=0.
    for i in range(n):
        al=.02+.25*(i/n); c+=al*(x[i]-c); y[i]=c
    return (y*k).astype(np.float32)
def pop(f=760,dur=.07):
    n=int(dur*SR); t=np.arange(n)/SR; return (np.sin(2*np.pi*(f+f*.6*t/dur)*t)*env(n,.004,.025)).astype(np.float32)
def ding(f=1320,dur=.9):
    n=int(dur*SR); t=np.arange(n)/SR; return ((np.sin(2*np.pi*f*t)+.5*np.sin(2*np.pi*f*1.5*t)+.25*np.sin(2*np.pi*f*2.01*t))*env(n,.003,.28)).astype(np.float32)
def crack():
    n=int(.5*SR); t=np.arange(n)/SR; nz=rng.normal(0,1,n)*np.exp(-t/.05); th=np.sin(2*np.pi*(120-70*t/.5)*t)*np.exp(-t/.12)
    sq=rng.normal(0,1,n)*np.exp(-((t-.12)/.09)**2)*.5; c=0.; y=np.zeros(n)
    for i in range(n): c+=.18*(sq[i]-c); y[i]=c
    return (nz*.6+th*1.1+y*1.4).astype(np.float32)
def rumble(dur):
    n=int(dur*SR); t=np.arange(n)/SR; f=62+4*np.sin(2*np.pi*.7*t); ph=2*np.pi*np.cumsum(f)/SR
    x=np.sin(ph)+.5*np.sin(2*ph)+.25*np.sin(3*ph); x*=(.75+.25*np.sin(2*np.pi*13*t)); e=np.minimum(t/.5,1)*np.minimum((dur-t)/.6,1)
    return (x*e).astype(np.float32)
def tick(): 
    n=int(.04*SR); t=np.arange(n)/SR; return (np.sin(2*np.pi*1900*t)*env(n,.002,.01)).astype(np.float32)
S=lambda k: TM[k]['start']; C=lambda k,i: TM[k]['start']+TM[k]['chunks'][i][0]
W=whoosh()
for k in list(TM)[1:]:
    if k[0]!='_': add(W,S(k)-.1,.5)
add(crack(),C('hook',1)+.05,.6); add(ding(1320),C('hook',1)+.42,.3); add(ding(1760),C('hook',1)+.5,.16)
add(pop(),S('yer')+.9,.35); add(pop(900),S('yer')+1.0,.3)
ks=S('kamyon'); add(rumble(TM['kamyon']['end']-ks-.2),ks+.2,.14)
for i in range(7): add(tick(),S('azal')+.9+i*.16,.3)
add(pop(520),C('azal',1)+.15,.3); add(pop(420),C('azal',1)+1.2,.3)
for i in range(5): add(pop(700+i*90),(S('diger')+.12) if i==0 else C('diger',i)-.05,.32)
add(ding(1320),S('cta')+.6,.26); add(pop(880),C('cta',1),.35)
out=np.tanh(out*1.2)*.8
sf.write('sfx.wav',out[:int(TM['_dur']*SR)],SR,subtype='PCM_16'); print('sfx ok',abs(out).max())
