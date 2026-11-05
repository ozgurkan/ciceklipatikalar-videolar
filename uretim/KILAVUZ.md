# Üretim kılavuzu

Hedef: 1080x1920, 30 fps, 40-70 sn Reels. Tarz: canlanan masal haritası (parşömen, mürekkep,
gerçek kıyı verisi, afişler, krem kapsül altyazı). Sözde gerçekçi sinematik tarz beğenilmedi.

- Araçlar: Python, PIL, numpy, ffmpeg. `pip install --break-system-packages piper-tts soundfile sherpa-onnx`
- Ses: Piper tr_TR-fahrettin-medium (sherpa-onnx tts-models GitHub sürümü). length_scale 1.0, noise_scale .7, noise_w .95. Doğal, abartısız, hafif yerel söyleyiş.
- Müzik: numpy ile özgün 9/8 klarnet (`ornek_music.py`). Konuşmada çok kısık, anlatıcı bitince 5-10 sn tek başına. Gerçek şarkı kullanılmaz.
- Montaj: `build.sh` (sahneler, birleştirme, loudnorm I=-14). Örnek bölüm: `ornek_bolum.py`, ses: `ornek_voice.py`.
- Harita: `thrace.png`, `europe.png` hazır; `base.py` world-atlas countries-50m ile yeniden üretir. Yardımcılar `m.py`, `video.py`.
- Metin: en çok 5 etiket. Bilgileri kaynaktan doğrula, emin olmadığını "anlatılır" diye söyle.
- Alkol konularında marka, tadım, fiyat veya satın alma çağrısı olmaz.
- Metricool: marka 7883710, tür REEL, showReelOnFeed true, isAiGenerated true, zaman dilimi Europe/Istanbul.
