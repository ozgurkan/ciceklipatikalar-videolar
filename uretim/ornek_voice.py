import json, numpy as np, soundfile as sf
from piper import PiperVoice, SynthesisConfig
d='tts/vits-piper-tr_TR-fahrettin-medium'
pv=PiperVoice.load(f'{d}/tr_TR-fahrettin-medium.onnx',f'{d}/tr_TR-fahrettin-medium.onnx.json'); SR=pv.config.sample_rate
cfg=SynthesisConfig(length_scale=1.0,noise_scale=.7,noise_w_scale=.95,normalize_audio=True)
SEGS={
"hook":[("Üzümden yapılıyo, ama şarap değil.","Üzümden yapılıyor, ama şarap değil",.2),("Adı hardaliye.","Adı: hardaliye",.12),("Evi ise Kırklareli.","Evi ise Kırklareli",.45)],
"yer":[("Kırklareli, Yıldız Dağları'nın eteklerinde.","Kırklareli, Yıldız Dağları'nın eteklerinde",.15),("Eski adı Kırkkilise.","Eski adı: Kırkkilise",.12),("Bugünkü adını, bin dokuz yüz yirmi dörtte aldı.","Bugünkü adını 1924'te aldı",.45)],
"pinar":[("Hemen yakınındaki Aşağı Pınar Höyüğü ise,","Yakınındaki Aşağı Pınar Höyüğü ise",.08),("milattan önce altı bin iki yüzlere uzanıyo.","MÖ 6200'lere uzanıyor",.12),("Trakya'da köy yaşamının ilk izlerinden.","Trakya'da köy yaşamının ilk izlerinden",.45)],
"uzum":[("Gelelim hardaliyeye.","Gelelim hardaliyeye",.15),("Tescilinde kırmızı üzümler sayılıyo:","Tescilinde kırmızı üzümler sayılıyor:",.08),("Papazkarası, Öküzgözü ve daha fazlası.","Papazkarası, Öküzgözü ve daha fazlası",.45)],
"yapim":[("Üzümler ezilir.","1. Üzümler ezilir",.12),("Üstüne vişne yaprağı ve ezilmiş hardal serpilir.","2. Vişne yaprağı ve ezilmiş hardal serpilir",.14),("İlk iki hafta her gün karıştırılır.","3. İlk 1-2 hafta her gün karıştırılır",.12),("Dört, beş hafta fermente edilir.","4. 4-5 hafta fermente edilir",.12),("Sonra serin yerde dinlendirilip şişelenir.","5. Serin yerde dinlendirilip şişelenir",.45)],
"hardal":[("Peki neden hardal?","Peki neden hardal?",.15),("Geleneksel bilgiye göre, şaraplaşmayı engellemeye yardım ediyo.","Geleneksel bilgiye göre şaraplaşmayı engellemeye yardım ediyor",.45)],
"alkol":[("Tescilinde alkolsüz içecek olarak tanımlanıyo.","Tescilinde alkolsüz içecek olarak tanımlanıyor",.15),("Ama fermente bi içecek;","Ama fermente bir içecek:",.08),("eskidikçe az miktarda alkol oluşabilir.","eskidikçe az miktarda alkol oluşabilir",.45)],
"tescil":[("İki bin on yedide,","2017'de",.08),("Kırklareli Hardaliyesi adıyla tescillendi.","Kırklareli Hardaliyesi adıyla tescillendi",.12),("Bu adla satılması için,","Bu adla satılması için",.08),("Kırklareli'nde üretilmesi gerekiyo.","Kırklareli'nde üretilmesi gerekiyor",.45)],
"cta":[("Sen hardaliye içtin mi?","Sen hardaliye içtin mi?",.15),("Yorumlara yaz.","Yorumlara yaz",9.5)],
}

out=[];t=0;tm={}
for k,chs in SEGS.items():
    st=t;cs=[]
    for sp,di,pau in chs:
        x=np.concatenate([c.audio_float_array for c in pv.synthesize(sp,syn_config=cfg)]).astype(np.float32)
        idx=np.where(np.abs(x)>.012)[0]; x=x[max(0,idx[0]-int(.015*SR)):min(len(x),idx[-1]+int(.06*SR))]
        f=int(.022*SR); x[:f]*=np.linspace(0,1,f); x[-f:]*=np.linspace(1,0,f)
        d=len(x)/SR; cs.append((round(t-st,3),round(t-st+d+min(pau,.2),3),di)); out+=[x,np.zeros(int(pau*SR),dtype=np.float32)]; t+=d+pau
    tm[k]={"start":round(st,3),"end":round(t,3),"chunks":cs}
sf.write('voice.wav',np.concatenate(out),SR,subtype='PCM_16')
tm['_voice_end']=round(t-9.5,3); tm['_dur']=round(t,3)
json.dump(tm,open('timing.json','w'),ensure_ascii=False,indent=1); print(round(t,2),{k:v['end'] for k,v in tm.items() if k[0]!='_'}, tm['_voice_end'])
