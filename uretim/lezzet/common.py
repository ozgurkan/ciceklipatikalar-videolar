def frame(now):
    for i,k in enumerate(ORDER):
        a,b=TM[k]['start'],TM[k]['end']
        if now<b or i==len(ORDER)-1:
            im=F[k](now-a)
            if i and now-a<.34:
                p=ORDER[i-1]; im=Image.blend(F[p](now-TM[p]['start']),im,ease((now-a)/.34))
            M.caption(im,now); return im
def render(k):
    a,b=TM[k]['start'],TM[k]['end']; n0,n1=round(a*FPS),round(b*FPS); os.makedirs('parts',exist_ok=True); tmp,out=f'parts/{k}.tmp.mp4',f'parts/{k}.mp4'
    p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-','-c:v','libx264','-crf','20','-preset','veryfast','-pix_fmt','yuv420p',tmp],stdin=subprocess.PIPE)
    for i in range(n0,n1): p.stdin.write(frame(i/FPS).tobytes())
    p.stdin.close()
    if p.wait()==0: os.replace(tmp,out); print('done',k,flush=True)
    else: sys.exit(1)
if __name__=='__main__':
    if sys.argv[1]=='still':
        os.makedirs('stills',exist_ok=True)
        for f in os.listdir('stills'): os.remove('stills/'+f)
        for k in ORDER:
            a,b=TM[k]['start'],TM[k]['end']; frame(a+(b-a)*.88).save(f'stills/{a+(b-a)*.88:06.2f}_{k}.jpg',quality=86)
        frame(0).save('stills/000.00_c.jpg',quality=88); print('warn',M.warnings)
    else: render(sys.argv[2])
