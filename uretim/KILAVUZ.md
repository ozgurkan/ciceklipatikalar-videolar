# Üretim kılavuzu

Hedef: 1080x1920, 30 fps, 40-70 sn Reels. Tarz: canlanan masal haritası (parşömen, mürekkep,
gerçek kıyı verisi, afişler, krem kapsül altyazı). Sözde gerçekçi sinematik tarz beğenilmedi.

- Araçlar: Python, PIL, numpy, ffmpeg. `pip install --break-system-packages piper-tts soundfile sherpa-onnx`
- Ses: Piper tr_TR-fahrettin-medium, metnin TAMAMI tek seferde sentezlenir (`ornek_akici_voice.py`). Parça parça sentez, kırpma, ekstra sessizlik ve yankı yok; Özgür eski yöntemde sesin takıldığını söyledi. length_scale 1.0, noise_scale .667, noise_w .8. Sayıları yazıyla yaz, -yo gibi şive yazımı kullanma. Ses zinciri: highpass=f=70, equalizer=f=3000:t=q:w=1:g=1.5, acompressor=threshold=-22dB:ratio=2:attack=15:release=200, volume=1.2.
- Müzik: numpy ile özgün 9/8 klarnet (`ornek_music.py`). Konuşma boyunca sabit kısık kalır (env .05), kelime aralarında yükselmez; anlatıcı bitince 5-10 sn tek başına. Gerçek şarkı kullanılmaz.
- Montaj: `build.sh` (sahneler, birleştirme, loudnorm I=-14). Örnek bölüm: `ornek_bolum.py`, ses: `ornek_voice.py`.
- Harita: `thrace.png`, `europe.png` hazır; `base.py` world-atlas countries-50m ile yeniden üretir. Yardımcılar `m.py`, `video.py`.
- Metin: en çok 5 etiket. Bilgileri kaynaktan doğrula, emin olmadığını "anlatılır" diye söyle.
- Alkol konularında marka, tadım, fiyat veya satın alma çağrısı olmaz.
- Metricool: marka 7883710, tür REEL, showReelOnFeed true, isAiGenerated true, zaman dilimi Europe/Istanbul.
