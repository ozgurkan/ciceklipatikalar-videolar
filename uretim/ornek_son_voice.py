import numpy as np, soundfile as sf, librosa, re, difflib, sherpa_onnx, subprocess
from piper import PiperVoice, SynthesisConfig
# (görünen hedef, yazım seçenekleri, anahtar kelimeler, length, ara)
S=[("Bu köprü neredeyse havaya uçuruluyordu.",["Bu köprü neredeyse havaya uçuruluyordu.","Bu köprü, neredeyse havaya uçuruluyordu.","Bu köprü nerdeyse havaya uçuruluyordu."],["köprü","uçuruluyordu"],1.24,.32),
("Peki, neden hâlâ ayakta?",["Peki, neden hâlâ ayakta?"],["ayakta"],1.3,.5),
("Burası Üsküp.",["Burası Üsküp.","Burası, Üsküp.","Burası Üskup."],["üsküp"],1.32,.24),
("Vardar Nehri'nin üstündeki Taş Köprü, Osmanlı döneminden kalma.",["Vardar Nehri'nin üstündeki Taş Köprü, Osmanlı döneminden kalma.","Vardar Nehrinin üstündeki Taş Köprü, Osmanlı döneminden kalma."],["vardar","köprü","osmanlı"],1.3,.35),
("Bir yakasında şehrin meydanı var.",["Bir yakasında şehrin meydanı var."],["meydanı"],1.28,.14),
("Öbür yakasında Eski Çarşı.",["Öbür yakasında Eski Çarşı."],["çarşı"],1.28,.42),
("Anlatılana göre 1944 yılında, çekilen Alman askerleri köprüye patlayıcı yerleştirdi.",["Anlatılana göre bin dokuz yüz kırk dört yılında, çekilen Alman askerleri köprüye patlayıcı yerleştirdi.","Anlatılana göre, bin dokuz yüz kırk dört yılında, çekilen Alman askerleri köprüye patlayıcı yerleştirdi."],["anlatılana","alman","köprüye","patlayıcı"],1.26,.38),
("Ama şehrin ileri gelenleri rica edince son anda vazgeçildi.",["Ama şehrin ileri gelenleri rica edince son anda vazgeçildi."],["vazgeçildi","rica"],1.3,.42),
("Bugün hâlâ şehrin simgesi.",["Bugün hâlâ şehrin simgesi."],["simgesi"],1.32,.45),
("Sen Üsküp'e gittin mi?",["Sen Üsküp'e gittin mi?","Sen Üsküpe gittin mi?","Sen hiç Üsküp'e gittin mi?"],["üsküp","gittin"],1.3,.22),
("Yorumlara yaz.",["Yorumlara yaz."],["yaz"],1.25,.1)]
d0='/home/claude/reels2/tts'; w=d0+'/sherpa-onnx-whisper-tiny'; d=f'{d0}/vits-piper-tr_TR-fahrettin-medium'
pv=PiperVoice.load(f'{d}/tr_TR-fahrettin-medium.onnx',f'{d}/tr_TR-fahrettin-medium.onnx.json'); sr=pv.config.sample_rate
rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=f'{w}/tiny-encoder.int8.onnx',decoder=f'{w}/tiny-decoder.int8.onnx',tokens=f'{w}/tiny-tokens.txt',language='tr',task='transcribe',num_threads=4)
def norm(s): return ' '.join(re.sub(r'[^a-zçğıöşü ]','',s.replace('İ','i').replace('I','ı').replace('â','a').lower()).split())
def asr(x):
    s=rec.create_stream(); s.accept_waveform(16000,librosa.resample(x,orig_sr=sr,target_sr=16000)); rec.decode_stream(s); return s.result.text
out=[]
for tgt,vars_,kw,ls,pa in S:
    best=None
    ref=norm(tgt.replace('1944','bin dokuz yüz kırk dört'))
    for tx in vars_:
        for ns,nw in [(.6,.75),(.667,.8),(.667,.8),(.7,.8),(.75,.85),(.75,.85),(.6,.8),(.667,.75)]:
            x=np.concatenate([c.audio_float_array for c in pv.synthesize(tx,syn_config=SynthesisConfig(length_scale=ls,noise_scale=ns,noise_w_scale=nw,normalize_audio=True))]).astype(np.float32)
            raw=asr(x); t=norm(raw); r=difflib.SequenceMatcher(None,ref,t).ratio()+.08*sum(k in t for k in kw)
            if '1944' in tgt: r+=.5*bool(re.search(r'19|944|dokuz|kırk',raw.lower())); t=raw.lower()
            if best is None or r>best[0]: best=(r,x,t,tx,ns)
    i=np.where(np.abs(best[1])>.01)[0]; x=best[1][max(0,i[0]-int(.03*sr)):min(len(best[1]),i[-1]+int(.09*sr))].copy()
    f=int(.012*sr); x[:f]*=np.linspace(0,1,f); x[-f:]*=np.linspace(1,0,f)
    out+=[x,np.zeros(int(pa*sr),np.float32)]; print(round(best[0],2),best[4],'|',best[3][:42],'=>',best[2][:80],flush=True)
b=np.concatenate(out); sf.write('v3.wav',b,sr)
FX='aresample=44100:resampler=soxr,highpass=f=75,equalizer=f=160:t=q:w=1:g=1.5,equalizer=f=350:t=q:w=1.2:g=-1.5,equalizer=f=2800:t=q:w=1.2:g=2,equalizer=f=7000:t=q:w=1.5:g=-1.5,acompressor=threshold=-22dB:ratio=2.2:attack=12:release=180,loudnorm=I=-16:TP=-1.5'
subprocess.run(['ffmpeg','-y','-loglevel','error','-i','v3.wav','-af',FX,'-b:a','160k','fahrettin-son-hal.mp3'])
print('dur',round(len(b)/sr,1),'peak',round(float(np.abs(b).max()),2))
