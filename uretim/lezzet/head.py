import sys, os, json, math, subprocess, random
sys.path.insert(0,'/home/claude/lezzet'); sys.path.insert(0,'/home/claude/masal'); sys.path.insert(0,'/home/claude/reels')
import numpy as np
from PIL import Image, ImageDraw
import m as M
from m import *
from lz import *
TM=M.TM; ORDER=M.ORDER; W,H,FPS=1080,1920,30; ve=TM['_voice_end']
def ct(k,i): return TM[k]['chunks'][i][0]
def on(k,i,t,d=.25): return t>=ct(k,i)-.05, back((t-ct(k,i)+.05)/d)
def outro(im,t,k='cta',nxt=None):
    v=ve-TM[k]['start']
    if t>v+.2:
        a=clamp((t-v-.2)/.5)
        if nxt: chip(im,nxt,540,1250,42,back((t-v-.2)/.3),fill=GREEN)
        T(im,"Takip et · @ciceklipatikalar",540,1360,44,INK,LORA,a=a)
def _cap(img,now):
    for k in ORDER:
        s=TM[k]['start']
        for a,b,txt in TM[k]['chunks']:
            if s+a<=now<s+b:
                if now<.2: return
                sz=50; lines=[txt]
                if text_mask(txt,sz,M.BOLD).width>860:
                    wds=txt.split(); best=None
                    for i in range(1,len(wds)):
                        l1,l2=' '.join(wds[:i]),' '.join(wds[i:]); w_=max(text_mask(l1,sz,M.BOLD).width,text_mask(l2,sz,M.BOLD).width)
                        if best is None or w_<best[0]: best=(w_,[l1,l2])
                    lines=best[1]
                    while best[0]>860 and sz>36: sz-=2; best=(max(text_mask(l,sz,M.BOLD).width for l in lines),lines)
                tw=max(text_mask(l,sz,M.BOLD).width for l in lines); lh=sz*1.25; h=lh*len(lines)/2+24
                rrect(img,540-tw/2-26,1490-h,540+tw/2+26,1490+h,16,(250,240,216),.96); ImageDraw.Draw(img).rounded_rectangle([540-tw/2-26,1490-h,540+tw/2+26,1490+h],16,outline=INK,width=3)
                for i,l in enumerate(lines): T(img,l,540,1490+(i-(len(lines)-1)/2)*lh,sz,INK,M.BOLD)
                return
M.caption=_cap
