set -e
d=$1; script=$2; out=$3; cover=$4; shift 4
cd /home/claude/$d
printf '%s\n' "$@" | xargs -P2 -I{} python3 $script render {} | grep -c done
for k in "$@"; do echo "file 'parts/$k.mp4'"; done > list.txt
ffmpeg -y -loglevel error -f concat -i list.txt -c copy s.tmp.mp4 && mv s.tmp.mp4 silent.mp4
ffmpeg -y -loglevel error -i silent.mp4 -i vproc.wav -i music.wav -filter_complex "[1:a][2:a]amix=inputs=2:normalize=0:duration=longest,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=44100[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart k.tmp.mp4 && mv k.tmp.mp4 $out
ffprobe -v error -show_entries format=duration,size:stream=codec_name,width,height -of compact $out
ffmpeg -hide_banner -i $out -af volumedetect -vn -f null - 2>&1 | grep -E "mean_volume|max_volume"
ffmpeg -y -loglevel error -ss 0 -i $out -frames:v 1 -q:v 2 $cover
ffmpeg -y -loglevel error -i $out -vf "select='not(mod(n\,135))',scale=216:-1,tile=5x2" -frames:v 1 -vsync 0 final.jpg
ffmpeg -y -loglevel error -i $out -vn -ac 1 -ar 16000 chk.wav
python3 - <<'P' 2>/dev/null
import sherpa_onnx, soundfile as sf, json
d='tts/sherpa-onnx-whisper-tiny'
rec=sherpa_onnx.OfflineRecognizer.from_whisper(encoder=f'{d}/tiny-encoder.int8.onnx',decoder=f'{d}/tiny-decoder.int8.onnx',tokens=f'{d}/tiny-tokens.txt',language='tr',task='transcribe',num_threads=2)
TM=json.load(open('timing.json')); x,sr=sf.read('chk.wav',dtype='float32')
for k,v in TM.items():
    if k[0]=='_': continue
    e=min(v['end'],TM['_voice_end'])
    s=rec.create_stream(); s.accept_waveform(sr,x[int(v['start']*sr):int(e*sr)]); rec.decode_stream(s); print(k,':',s.result.text[:95])
P
