#!/usr/bin/env python3
# Onaylı Fahrettin yöntemi: cümle tek parça, birkaç okuma, whisper-tiny ile en doğrusu seçilir.
# Kullanım: cd lX && python3 ../vgen.py   (spec.py içinde SEGS ve OUTRO tanımlı)
import sys, os, json, re, difflib, subprocess
sys.path.insert(0, os.getcwd())
import numpy as np, soundfile as sf, librosa, sherpa_onnx
from piper import PiperVoice, SynthesisConfig
from spec import SEGS, OUTRO
d = 'tts/vits-piper-tr_TR-fahrettin-medium'; w = 'tts/sherpa-onnx-whisper-tiny'
pv = PiperVoice.load(f'{d}/tr_TR-fahrettin-medium.onnx', f'{d}/tr_TR-fahrettin-medium.onnx.json'); SR = pv.config.sample_rate
rec = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=f'{w}/tiny-encoder.int8.onnx', decoder=f'{w}/tiny-decoder.int8.onnx', tokens=f'{w}/tiny-tokens.txt', language='tr', task='transcribe', num_threads=2)
def norm(s): return ' '.join(re.sub(r'[^a-zçğıöşü ]', '', s.replace('İ', 'i').replace('I', 'ı').replace('â', 'a').lower()).split())
def asr(x):
    s = rec.create_stream(); s.accept_waveform(16000, librosa.resample(x, orig_sr=SR, target_sr=16000)); rec.decode_stream(s); return s.result.text
NZ = [(.6, .75), (.667, .8), (.7, .8), (.75, .85), (.667, .75)]
out = []; t = 0.; tm = {}; log = []
for k, chs in SEGS.items():
    st = t; cs = []
    for disp, vars_, kw, ls, pa in chs:
        ref = norm(vars_[0]); best = None
        for tx in vars_:
            for ns, nw in NZ:
                x = np.concatenate([c.audio_float_array for c in pv.synthesize(tx, syn_config=SynthesisConfig(length_scale=ls, noise_scale=ns, noise_w_scale=nw, normalize_audio=True))]).astype(np.float32)
                tr = norm(asr(x)); r = difflib.SequenceMatcher(None, ref, tr).ratio() + .08 * sum(q in tr for q in kw)
                if best is None or r > best[0]: best = (r, x, tr, tx)
        x = best[1]; i = np.where(np.abs(x) > .01)[0]; x = x[max(0, i[0] - int(.03 * SR)):min(len(x), i[-1] + int(.09 * SR))].copy()
        f = int(.012 * SR); x[:f] *= np.linspace(0, 1, f); x[-f:] *= np.linspace(1, 0, f)
        dur = len(x) / SR; cs.append((round(t - st, 3), round(t - st + dur + min(pa, .2), 3), disp))
        out += [x, np.zeros(int(pa * SR), np.float32)]; t += dur + pa
        log.append(f'{best[0]:.2f} | {vars_[0]} => {best[2]}'); print(log[-1], flush=True)
    tm[k] = {"start": round(st, 3), "end": round(t, 3), "chunks": cs}
ve = t; last = list(tm)[-1]; t += OUTRO; tm[last]['end'] = round(t, 3)
out.append(np.zeros(int(OUTRO * SR), np.float32))
sf.write('voice.wav', np.concatenate(out), SR, subtype='PCM_16')
tm['_voice_end'] = round(ve, 3); tm['_dur'] = round(t, 3)
json.dump(tm, open('timing.json', 'w'), ensure_ascii=False, indent=1)
open('asr_log.txt', 'w').write('\n'.join(log))
FX = 'aresample=44100:resampler=soxr,highpass=f=75,equalizer=f=160:t=q:w=1:g=1.5,equalizer=f=350:t=q:w=1.2:g=-1.5,equalizer=f=2800:t=q:w=1.2:g=2,equalizer=f=7000:t=q:w=1.5:g=-1.5,acompressor=threshold=-22dB:ratio=2.2:attack=12:release=180'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', 'voice.wav', '-af', FX, '-ac', '1', 'vproc.wav'], check=True)
print('voice_end', round(ve, 2), 'dur', round(t, 2))
