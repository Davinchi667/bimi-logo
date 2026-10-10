"""Sequencer helpers: bars/beats -> note lists, drum grids -> hits, swing, ducking, stem export."""
import numpy as np, soundfile as sf, scipy.signal as ss, json, os, random
from synth import SR, render_faust, P, fx, db, place, kick, clap, snare, hat, perc_rim

class Song:
    def __init__(self, bpm, bars, seed=7):
        self.bpm=bpm; self.beat=60/bpm; self.bar=4*self.beat; self.bars=bars
        self.N=int((bars*self.bar+6)*SR); self.layers={}; self.drums={}; self.rng=random.Random(seed)
    def B(self,bar,beat=0.0): return bar*4+beat                      # beats
    def t(self,bar,beat=0.0): return (bar*4+beat)*self.beat            # seconds
    def hum(self,beats,ms=6): return beats+self.rng.uniform(-ms,ms)/1000/self.beat
    def add(self,layer,start_beats,dur_beats,pitch,vel):
        self.layers.setdefault(layer,[]).append((max(0,start_beats),dur_beats,int(pitch),int(vel)))
    def chord(self,layer,bar,beat,dur,pitches,vel,strum=0.0):
        for i,p in enumerate(pitches): self.add(layer,self.B(bar,beat)+i*strum,dur,p,vel)
    def hit(self,drum,bar,beat,vel=100,ms_late=0.0,pan=0.0):
        self.drums.setdefault(drum,[]).append((self.t(bar,beat)+ms_late/1000,vel,pan))
    def grid(self,drum,bar,pattern,vel=100,accent=None,res=16,swing=0.0,ms_late=0.0):
        """pattern: string of 16 (or res) chars per bar, 'X' accent, 'x' normal, '.' rest, 'g' ghost. swing 0-1 on the off-steps."""
        pat=pattern.replace('|','').replace(' ',''); step=4/res
        for i,c in enumerate(pat):
            if c=='.': continue
            b=i*step
            if swing and (i%2==1): b+=swing*step*0.5
            v={'X':vel+ (accent or 20),'x':vel,'g':max(20,vel-45)}[c]
            self.hit(drum,bar,self.hum(b,4),v,ms_late)
    def ducker(self,drum='kick',depth_db=-6,rel=0.18,hold=0.02):
        g=np.ones(self.N); L=int((rel*3+hold)*SR); t=np.arange(L)/SR
        shape=np.where(t<hold,db(depth_db),1-(1-db(depth_db))*np.exp(-(t-hold)/rel*2.5))
        for tt,_,_ in self.drums.get(drum,[]):
            i=max(0,int(tt*SR)); j=min(self.N,i+L)
            if j>i: g[i:j]=np.minimum(g[i:j],shape[:j-i])
        return g[:,None]
    def render_layer(self,layer,preset,params=None,voices=24):
        notes=self.layers.get(layer,[])
        if not notes: return np.zeros((self.N,2),np.float32)
        secs=self.N/SR; a=render_faust(preset,notes,secs,bpm=self.bpm,voices=voices,params=params)
        out=np.zeros((self.N,2),np.float32); n=min(self.N,len(a)); out[:n]=a[:n]; return out
    def render_drum(self,drum,sample,gain=1.0):
        c=np.zeros((self.N,2),np.float32)
        for tt,vel,pan in self.drums.get(drum,[]): place(c,sample,tt,gain*(vel/127)**1.5,pan)
        return c
    def mask(self,ranges_bars,fade=0.03):
        m=np.zeros(self.N)
        for a,b in ranges_bars: m[int(a*self.bar*SR):int(b*self.bar*SR)]=1
        k=np.hanning(max(3,int(fade*SR))); k/=k.sum(); return np.convolve(m,k,'same')[:,None]
    def midi(self,path,prog_map,tempo=None):
        import sys; sys.path.insert(0,os.path.dirname(__file__)); from midiw import MIDI
        m=MIDI()
        for i,(layer,notes) in enumerate(self.layers.items()):
            m.track(layer,notes,prog_map.get(layer,(i%15 if i%15!=9 else 10,0))[0],prog=prog_map.get(layer,(0,0))[1],tempo=self.bpm if i==0 else None)
        dr=[]
        for drum,hits in self.drums.items():
            key={'kick':36,'808':35,'snare':38,'clap':39,'hat':42,'ohat':46,'rim':37,'perc':75}.get(drum,60)
            dr+=[(tt/self.beat,0.25,key,int(v)) for tt,v,_ in hits]
        if dr: m.track('drums',dr,9,tempo=None)
        m.save(path)

def filt(x,fc,kind='low',o=4): return ss.sosfilt(ss.butter(o,fc,kind,fs=SR,output='sos'),x,axis=0)
def sat(x,d): return np.tanh(x*d)/np.tanh(d)
def width(x,w):
    M=(x[:,0]+x[:,1])/2; S=(x[:,0]-x[:,1])/2
    if np.ndim(w): w=w[:,0]
    return np.stack([M+S*w,M-S*w],1)
def pan(x,p):
    a=(p+1)*np.pi/4; m=x.mean(1); return np.stack([m*np.cos(a),m*np.sin(a)],1)*1.414
def reverse_into(x,at_sec,length_sec,curve=1.6):
    """take x after at_sec for length, reverse it, fade in, place so it ends at at_sec"""
    L=int(length_sec*SR); i=int(at_sec*SR); seg=x[i:i+L][::-1]*(np.linspace(0,1,L)[:,None]**curve)
    out=np.zeros_like(x); a=max(0,i-L); out[a:i]+=seg[-(i-a):]; return out
def tapestop(x,start_s,dur_s,curve=1.6):
    i,j=int(start_s*SR),int((start_s+dur_s)*SR); n=j-i; speed=np.linspace(1,0,n)**curve; pos=i+np.cumsum(speed); y=x.copy()
    for c in range(x.shape[1]): y[i:j,c]=np.interp(pos,np.arange(len(x)),x[:,c])*np.linspace(1,0.2,n)
    return y
def export(stems,outdir,mixname='mix.wav',peak_db=-1):
    os.makedirs(outdir,exist_ok=True); tot=sum(stems.values()); sc=db(peak_db)/max(1e-9,np.abs(tot).max())
    sf.write(os.path.join(outdir,mixname),tot*sc,SR,subtype='PCM_24')
    np.savez_compressed(os.path.join(outdir,'stems.npz'),**{k:(v*sc).astype(np.float32) for k,v in stems.items()})
    return tot*sc
