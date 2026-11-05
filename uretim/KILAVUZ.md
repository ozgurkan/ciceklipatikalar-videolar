# Üretim kılavuzu

Hedef: 1080x1920, 30 fps, 40-70 sn Reels. Tarz: canlanan masal haritası (parşömen, mürekkep,
gerçek kıyı verisi, afişler, krem kapsül altyazı). Sözde gerçekçi sinematik tarz beğenilmedi.

- Araçlar: Python, PIL, numpy, ffmpeg. `pip install --break-system-packages piper-tts soundfile sherpa-onnx`
- Ses (Özgür 5 Kasım'da onayladı): Piper tr_TR-fahrettin-medium (https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-tr_TR-fahrettin-medium.tar.bz2). Yöntem `ornek_son_voice.py`: her cümle kendi içinde tek parça sentezlenir, kelime birleştirme yok; length_scale 1.24-1.32, noise_scale .6-.75, noise_w .75-.85; her cümle için birkaç okuma üretilir, whisper-tiny dökümünde en doğru olan seçilir. Dosyadaki yolları kendi ortamına uyarla. Cümle araları .14-.5 sn, soru ve vurgudan sonra daha uzun. Tonlama yapay artırılmaz, yankı yok. Ses zinciri dosyadaki FX. Kolay okunan kısa cümleler yaz; yıl ve zor kelimeleri gerektiği kadar kullan, sayıları yazıyla yaz; -yo şive yazımı yok. Hız yaklaşık 5,4 hece/sn. Sesi dinleyemediğini söyle, dökümde takılan kelimeleri Özgür'e yaz.
- Müzik: numpy ile özgün 9/8 klarnet (`ornek_music.py`). Konuşma boyunca sabit kısık kalır (env .05), kelime aralarında yükselmez; anlatıcı bitince 5-10 sn tek başına. Gerçek şarkı kullanılmaz.
- Montaj: `build.sh` (sahneler, birleştirme, loudnorm I=-14). Örnek bölüm: `ornek_bolum.py`, ses: `ornek_voice.py`.
- Harita: `thrace.png`, `europe.png` hazır; `base.py` world-atlas countries-50m ile yeniden üretir. Yardımcılar `m.py`, `video.py`.
- Metin: en çok 5 etiket. Bilgileri kaynaktan doğrula, emin olmadığını "anlatılır" diye söyle.
- Alkol konularında marka, tadım, fiyat veya satın alma çağrısı olmaz.
- Metricool: marka 7883710, tür REEL, showReelOnFeed true, isAiGenerated true, zaman dilimi Europe/Istanbul.
