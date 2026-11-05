import json, re, numpy as np, soundfile as sf, sys
from piper import PiperVoice, SynthesisConfig
V=sys.argv[1] if len(sys.argv)>1 else 'fahrettin'
# (spoken, shown)
S=[("hook","Bu köprü neredeyse havaya uçuruluyordu.","Bu köprü neredeyse havaya uçuruluyordu."),
("hook","Peki neden hâlâ ayakta?","Peki neden hâlâ ayakta?"),
("uskup","Burası Üsküp.","Burası Üsküp."),
("uskup","Vardar Nehri'nin üstündeki Taş Köprü, Osmanlı döneminden kalma.","Vardar Nehri'nin üstündeki Taş Köprü, Osmanlı döneminden kalma."),
("kopru","Bir yakasında şehrin meydanı var, öbür yakasında Eski Çarşı.","Bir yakasında şehrin meydanı var, öbür yakasında Eski Çarşı."),
("y44","Anlatılana göre, bin dokuz yüz kırk dört yılında, çekilen Alman askerleri köprüye patlayıcı yerleştirdi.","Anlatılana göre, 1944 yılında, çekilen Alman askerleri köprüye patlayıcı yerleştirdi."),
("y44","Ama şehrin ileri gelenleri rica edince, son anda vazgeçildi.","Ama şehrin ileri gelenleri rica edince, son anda vazgeçildi."),
("y63","Köprü, bin dokuz yüz altmış üç depreminde hasar gördü, ama bugün hâlâ şehrin simgesi.","Köprü, 1963 depreminde hasar gördü, ama bugün hâlâ şehrin simgesi."),
("cta","Sen Üsküp'e gittin mi?","Sen Üsküp'e gittin mi?"),
("cta","Yorumlara yaz.","Yorumlara yaz."),]
d=f'../reels2/tts/vits-piper-tr_TR-{V}-medium'; pv=PiperVoice.load(f'{d}/tr_TR-{V}-medium.onnx',f'{d}/tr_TR-{V}-medium.onnx.json'); SR=pv.config.sample_rate
cfg=SynthesisConfig(length_scale=1.0,noise_scale=.667,noise_w_scale=.8,normalize_audio=True)
TXT=' '.join(s[1] for s in S)
ch=list(pv.synthesize(TXT,syn_config=cfg)); print(len(ch),'sentences'); assert len(ch)==len(S)
x=np.concatenate([c.audio_float_array for c in ch]).astype(np.float32)
if V!='fahrettin': sf.write(f'v_{V}.wav',x,SR); sys.exit()
tail=6.5; TM={}; t=0
def split(txt):
    w=txt.split(); out=[];cur=[]
    for a in w:
        cur.append(a)
        if len(' '.join(cur))>=24 or a[-1] in ',.?': out.append(' '.join(cur)); cur=[]
    if cur: out.append(' '.join(cur))
    return out
for (k,sp,di),c in zip(S,ch):
    d_=len(c.audio_float_array)/SR
    if k not in TM: TM[k]={'start':round(t,3),'chunks':[]}
    parts=split(di); L=sum(len(p) for p in parts); u=t
    for p in parts:
        e=u+d_*len(p)/L; TM[k]['chunks'].append([round(u-TM[k]['start'],3),round(e-TM[k]['start'],3),p]); u=e
    t+=d_; TM[k]['end']=round(t,3)
TM['_voice_end']=round(t,3); TM['cta']['end']=round(t+tail,3); TM['_dur']=round(t+tail,3)
sil=np.zeros(int(tail*SR),np.float32); sf.write('voice.wav',np.concatenate([x,sil]),SR,subtype='PCM_16')
json.dump(TM,open('timing.json','w'),ensure_ascii=False,indent=1); print(TM['_voice_end'],{k:v['end'] for k,v in TM.items() if k[0]!='_'})
