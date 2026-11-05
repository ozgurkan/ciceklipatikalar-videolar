import numpy as np, json, wave
TM=json.load(open('timing.json')); DUR=TM['_dur']; VE=TM['_voice_end']
SR=44100; N=int(DUR*SR)+SR; mel=np.zeros(N); perc=np.zeros(N); pad=np.zeros(N); rs=np.random.default_rng(12)
def add(b,t,x,g=1.):
    i=int(t*SR); e=min(N,i+len(x))
    if 0<=i<N: b[i:e]+=x[:e-i]*g
def klarnet(f,dur,g=1.):
    n=int(dur*SR); t=np.arange(n)/SR
    v=1+.006*np.sin(2*np.pi*5.4*t)*np.minimum(t/.25,1)
    ph=2*np.pi*f*np.cumsum(v)/SR
    x=np.sin(ph)+.38*np.sin(3*ph)+.2*np.sin(5*ph)+.09*np.sin(7*ph)+.06*np.sin(2*ph)
    e=np.minimum(t/.018,1)*np.minimum((dur-t)/.04,1).clip(0,1)*(.86+.14*np.exp(-t/.12))
    return x*e*g
def dum(g=1.):
    n=int(.28*SR); t=np.arange(n)/SR; return np.sin(2*np.pi*(72*t+1.2*(1-np.exp(-t*30))))*np.exp(-t/.11)*g
def tek(g=1.):
    n=int(.09*SR); t=np.arange(n)/SR; x=rs.normal(size=n); return (.45*x+np.sin(2*np.pi*640*t))*np.exp(-t/.018)*g
def drone(f,dur):
    n=int(dur*SR); t=np.arange(n)/SR; return (np.sin(2*np.pi*f*t)+.3*np.sin(4*np.pi*f*t))*np.sin(np.pi*t/dur)**.8
# Original tune: 9/8 (2+2+2+3), written for this series, not an existing song. Clarinet leads.
def klarnet2(f,dur,g=1.,orn=None,bend=0.):
    n=int(dur*SR); t=np.arange(n)/SR
    fr=np.full(n,f,np.float64)
    if bend: fr*=2**(bend*np.clip(1-t/.07,0,1)/12)
    if orn:  # upper trill
        tr=np.where(np.sin(2*np.pi*11*t)>0,1.,2**(orn/12)); fr=fr*np.where(t<dur*.55,tr,1)
    v=1+.008*np.sin(2*np.pi*5.2*t)*np.minimum(t/.22,1)
    ph=2*np.pi*np.cumsum(fr*v)/SR
    x=np.sin(ph)+.46*np.sin(3*ph)+.27*np.sin(5*ph)+.13*np.sin(7*ph)+.06*np.sin(9*ph)+.05*np.sin(2*ph)
    br=rs.normal(size=n); br=np.convolve(br,np.ones(14)/14,'same')*.035
    e=np.minimum(t/.018,1)*np.minimum((dur-t)/.035,1).clip(0,1)*(.84+.16*np.exp(-t/.12))
    return (x+br)*e*g
A=220.;sc={'G3':196,'A':A,'Bb':233.1,'C#':277.2,'D':293.7,'E':329.6,'F':349.2,'G':392,'A2':440,'Bb2':466.2,'C#2':554.4,'D2':587.3}
bpm=430; e=60/bpm
phr=[('A',2,0,1),('C#',2,0,0),('D',2,0,0),('E',3,1,0), ('F',2,0,1),('E',2,0,0),('D',2,0,0),('C#',3,2,0), ('D',2,0,0),('E',2,0,0),('F',2,0,1),('G',3,1,0), ('F',2,0,0),('E',2,0,0),('D',2,0,1),('C#',1,0,0),('D',1,0,0),('E',1,0,0),
     ('A2',2,0,1),('G',2,0,0),('F',2,0,0),('E',3,2,0), ('D',2,0,0),('E',2,0,0),('F',1,0,0),('E',1,0,0),('D',1,0,0),('C#',1,0,0),('D',1,0,0), ('C#',2,0,0),('Bb',2,0,1),('C#',2,0,0),('D',3,1,0), ('C#',2,0,0),('Bb',1,0,0),('C#',1,0,0),('A',2,0,1),('A',3,1,0)]
t=0.;i=0
while t<DUR+1:
    n_,l,o,b=phr[i%len(phr)]
    add(mel,t,klarnet2(sc[n_],l*e*1.02,orn=o,bend=-1.5 if b else 0),.42); t+=l*e; i+=1
bar=9*e;k=0
while k*bar<DUR+1:
    b=k*bar
    for o,g,kind in [(0,1,'d'),(2,.5,'t'),(4,.75,'d'),(6,.55,'t'),(7,.42,'t'),(8,.5,'t')]:
        tt=b+o*e; add(perc,tt,dum(g) if kind=='d' else tek(g),.3 if kind=='d' else .15)
    if k%2==0: add(pad,b,drone(110,bar*2.1),.1)
    k+=1
m=mel+perc+pad; m=m/np.abs(m).max()*.82
# automation: very low under speech, clarinet lifts in the short pauses, full after narrator ends
env=np.full(N,.20,np.float32); x=np.arange(N)/SR
for k_ in [q for q in TM if q[0]!='_']:
    st=TM[k_]['start']
    for a_,b_,_ in TM[k_]['chunks']:
        env[(x>=st+a_-.12)&(x<=st+b_-.05)]=.04
ker=np.hanning(int(.18*SR)); ker/=ker.sum(); env=np.convolve(env,ker,'same')
up=np.clip((x-(VE+.05))/1.0,0,1)**1.3; env=np.where(x>VE+.05,.04+(.5-.04)*up,env)
fd=np.clip((DUR-x)/2.0,0,1); env=env*fd
o=(m*env)[:int(DUR*SR)]
with wave.open('music.wav','wb') as w:
    w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.clip(o,-1,1)*32767).astype(np.int16).tobytes())
print('bars',k,'dur',DUR)
