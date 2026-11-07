import numpy as np, soundfile as sf, json
SR=44100; tm=json.load(open('timing.json')); D=tm['_dur']; VE=tm['_voice_end']; N=int(D*SR); t=np.arange(N)/SR
def hz(m): return 440*2**((m-69)/12)
# D minor: Dm - Bb - Gm - A, her biri 7 sn, yavaş
ch=[[50,57,62,65],[46,53,58,62],[43,50,55,58],[45,52,57,61]]
out=np.zeros(N)
L=7.0
for k in range(int(D/L)+2):
    c=ch[k%4]; s=int(k*L*SR); e=min(N,int((k+1)*L*SR+2.5*SR))
    if s>=N: break
    tt=np.arange(e-s)/SR; env=np.minimum(1,tt/2.2)*np.minimum(1,np.maximum(0,(L+2.5-tt)/2.5))
    for m in c:
        f=hz(m); v=np.zeros_like(tt)
        for det in (-0.12,0,0.12):
            ff=f*2**(det/12)
            v+=np.sin(2*np.pi*ff*tt)+.35*np.sin(2*np.pi*2*ff*tt)+.12*np.sin(2*np.pi*3*ff*tt)
        out[s:e]+=v*env*(1+.15*np.sin(2*np.pi*.2*tt))
# sade, seyrek piyano benzeri notalar (melodi) - konuşma bitince
mel=[(VE+0.4,74,1.6),(VE+2.0,72,1.6),(VE+3.6,69,2.8)]
for st,m,du in mel:
    s=int(st*SR)
    if s>=N: continue
    tt=np.arange(min(N-s,int((du+2)*SR)))/SR; f=hz(m)
    out[s:s+len(tt)]+=(np.sin(2*np.pi*f*tt)+.4*np.sin(2*np.pi*2*f*tt)+.15*np.sin(2*np.pi*3*f*tt))*np.exp(-tt*1.4)*3
# yumuşatma (basit low-pass)
from scipy.signal import butter, sosfilt
out=sosfilt(butter(4,2200,fs=SR,output='sos'),out)
out/=np.max(np.abs(out))
env=np.full(N,.07); up=np.clip((t-(VE+.1))/1.5,0,1); env=env+(.32-.07)*up
fade=np.clip((D-t)/2.5,0,1); env*=np.minimum(1,t/1.5)*fade
y=(out*env).astype(np.float32); sf.write('music.wav',np.stack([y,y],1),SR)
print('ok',D,VE)
