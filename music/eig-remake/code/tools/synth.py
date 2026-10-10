"""Faust/DawDreamer polyphonic renderer + Pedalboard FX helpers. All audio = float32 (N,2) at 44100."""
import numpy as np, dawdreamer as dd, soundfile as sf
SR=44100
HEAD='import("stdfaust.lib");\nfreq=hslider("freq",220,20,8000,0.01); gain=hslider("gain",0.5,0,1,0.001); gate=button("gate");\neffect=_,_;\n'

def render_faust(dsp, notes, seconds, bpm=None, voices=24, params=None):
    """notes: list of (start_sec_or_beats, dur, midi_pitch, vel 0-127). If bpm given, start/dur are in beats."""
    eng=dd.RenderEngine(SR,256); f=eng.make_faust_processor('v'); f.num_voices=voices
    f.set_dsp_string(HEAD+dsp); f.compile()
    if params:
        names=[d['name'] for d in f.get_parameters_description()]
        for k,v in params.items():
            m=[n for n in names if n.endswith('/'+k)]
            if not m: raise KeyError(f'param {k} not in {names}')
            f.set_parameter(m[0],v)
    sc=(60/bpm) if bpm else 1.0
    for st,du,p,v in notes: f.add_midi_note(int(p),int(max(1,min(127,v))),float(st*sc),float(max(0.01,du*sc)))
    eng.load_graph([(f,[])]); eng.render(float(seconds)); a=eng.get_audio().T.astype(np.float32)
    return a

def render_faust_mono_fx(dsp, seconds, params=None):
    """non-polyphonic generator (noise risers, drones): dsp must define process with no gate."""
    eng=dd.RenderEngine(SR,256); f=eng.make_faust_processor('g'); f.set_dsp_string('import("stdfaust.lib");\n'+dsp); f.compile()
    if params:
        names=[d['name'] for d in f.get_parameters_description()]
        for k,v in params.items(): f.set_parameter([n for n in names if n.endswith('/'+k)][0],v)
    eng.load_graph([(f,[])]); eng.render(float(seconds)); return eng.get_audio().T.astype(np.float32)

# ---------- presets (Faust bodies; HEAD provides freq/gain/gate) ----------
P={}
P['supersaw']='''det=hslider("det",0.12,0,1,0.001); cut=hslider("cut",2200,100,16000,1); res=hslider("res",0.3,0,0.95,0.01);
a=hslider("a",0.02,0.001,4,0.001); d=hslider("d",0.4,0.001,8,0.001); s=hslider("s",0.7,0,1,0.01); r=hslider("r",0.8,0.001,10,0.001);
env=en.adsr(a,d,s,r,gate); fenv=en.adsr(0.005,0.6,0.3,0.5,gate);
sawL=par(i,4,os.sawtooth(freq*(1+det*0.01*(i-1.5)))):>_/4; sawR=par(i,4,os.sawtooth(freq*(1+det*0.011*(i-1.5))*1.0007)):>_/4;
flt(x)=x:ve.moog_vcf_2b(res,min(16000,cut*(0.4+0.6*fenv)+freq*2));
process=(sawL:flt)*env*gain*0.6,(sawR:flt)*env*gain*0.6;'''
P['pad']='''det=hslider("det",0.25,0,1,0.001); cut=hslider("cut",1400,100,16000,1); lfo=0.5+0.5*os.osc(0.11);
a=hslider("a",1.2,0.001,8,0.001); r=hslider("r",2.5,0.001,12,0.001); env=en.asr(a,1,r,gate);
v(k)=os.sawtooth(freq*(1+det*0.01*(k-2)))+0.5*os.triangle(freq*0.5*(1+det*0.005*(k-2)));
L=par(i,5,v(i)):>_/5; R=par(i,5,v(i+0.37)):>_/5;
process=(L:fi.lowpass(2,cut*(0.6+0.5*lfo)))*env*gain*0.5,(R:fi.lowpass(2,cut*(0.6+0.5*(1-lfo))))*env*gain*0.5;'''
P['808']='''punch=hslider("punch",0.5,0,2,0.01); pdec=hslider("pdec",0.012,0.001,0.2,0.001); dec=hslider("dec",2.5,0.1,10,0.01);
drive=hslider("drive",3,1,12,0.1); gl=hslider("glide",0.08,0,1,0.001);
f=freq:si.smooth(ba.tau2pole(gl)); pe=en.ar(0.001,pdec,gate); env=en.asr(0.002,1,dec,gate):min(1);
osc=os.osc(f*(1+punch*pe)); body=osc*env; sat=ma.tanh(body*drive)/ma.tanh(drive);
process=(sat*0.75+body*0.35)*gain<:_,_;'''
P['pluck']='''cut=hslider("cut",3000,100,16000,1); d=hslider("d",0.35,0.01,4,0.001);
env=en.ar(0.002,d,gate); fenv=en.ar(0.001,d*0.6,gate);
x=os.sawtooth(freq)*0.6+os.square(freq*0.5)*0.3; y=x:ve.moog_vcf_2b(0.4,cut*fenv+200);
process=y*env*gain*0.8<:_,_*0.9;'''
P['fm_bell']='''ratio=hslider("ratio",3.5,0.5,12,0.01); idx=hslider("idx",2.5,0,12,0.01); d=hslider("d",1.8,0.05,10,0.01);
env=en.ar(0.002,d,gate); ienv=en.ar(0.001,d*0.4,gate);
mod=os.osc(freq*ratio)*idx*ienv*freq; car=os.osc(freq+mod);
process=car*env*gain*0.7<:_,_;'''
P['choir']='''vow=hslider("vowel",2,0,4,1); a=hslider("a",0.25,0.001,4,0.001); r=hslider("r",1.2,0.001,10,0.001);
env=en.asr(a,1,r,gate); vib=1+0.004*os.osc(5.2+0.3*no.lfnoise(0.5));
src=par(i,3,os.sawtooth(freq*vib*(1+0.003*(i-1)))):>_/3 + 0.08*no.noise:fi.lowpass(1,4000);
f1=ba.selectn(5,vow,730,530,300,400,350); f2=ba.selectn(5,vow,1090,1840,2200,800,600); f3=ba.selectn(5,vow,2440,2480,2900,2600,2700);
form=src<:(fi.resonbp(f1,8,1)+0.5*fi.resonbp(f2,10,1)+0.25*fi.resonbp(f3,12,1)):>_;
process=form*env*gain*0.9<:_,_;'''
P['sine_lead']='''a=hslider("a",0.01,0.001,2,0.001); r=hslider("r",0.3,0.001,5,0.001); env=en.asr(a,1,r,gate);
vib=1+0.006*os.osc(5.5)*en.asr(0.6,1,0.1,gate);
x=os.osc(freq*vib)+0.25*os.osc(freq*2*vib)+0.08*os.osc(freq*3*vib);
process=ma.tanh(x*1.4)*env*gain*0.7<:_,_;'''
P['hum']='''a=hslider("a",0.12,0.001,4,0.001); r=hslider("r",0.35,0.001,10,0.001); breath=hslider("breath",0.05,0,0.5,0.001); nasal=hslider("nasal",0.5,0,1,0.01);
env=en.asr(a,1,r,gate); vibd=en.asr(0.35,1,0.1,gate); vib=1+0.007*vibd*os.osc(5.3+0.4*no.lfnoise(0.7));
f=freq*vib; src=os.osc(f)+0.45*os.osc(2*f)+0.22*os.osc(3*f)+0.1*os.osc(4*f)+0.05*os.osc(5*f);
nas=src:fi.resonbp(250,3,1)*nasal+src*(1-nasal)*0.5; br=no.pink_noise*breath:fi.resonbp(1200,2,1);
out=(nas+br*env):fi.lowpass(1,2600);
process=ma.tanh(out*1.3)*env*gain*0.8<:_,_;'''
# ---- EVERYWHERE I GO voices (from the measured fingerprint) ----
P['rpad']='''det=hslider("det",1.00812,0.9,1.1,0.00001); vibr=hslider("vibr",7.667,0.1,20,0.001); vibc=hslider("vibc",11.5,0,50,0.1);
cut=hslider("cut",1400,100,16000,1); a=hslider("a",0.015,0.001,2,0.001); r=hslider("r",0.015,0.001,5,0.001); top=hslider("top",1,0,1,0.01);
env=en.asr(a,1,r,gate); vib=pow(2,(vibc/1200)*os.osc(vibr));
f=freq*det*vib; v=os.sawtooth(f)*0.5+os.pulsetrain(f,0.5)*0.5;
hi=(freq>1000)*(1-top)+top;   /* top-octave attenuation handled by velocity instead */
y=v:fi.lowpass(2,cut);
process=y*env*gain*0.9<:_,_*0.97;'''
P['rlead']='''det=hslider("det",1.00812,0.9,1.1,0.00001); cut=hslider("cut",1600,100,16000,1);
env=en.asr(0.035,1,0.04,gate); vib=pow(2,(11.5/1200)*os.osc(7.667));
f=freq*det*vib; v=os.sawtooth(f)*0.5+os.pulsetrain(f,0.5)*0.5; y=v:fi.lowpass(4,cut);
process=y*env*gain*0.9<:_,_;'''
P['pad2']='''cut=hslider("cut",3500,100,16000,1); a=hslider("a",0.03,0.001,2,0.001); r=hslider("r",0.05,0.001,5,0.001); spread=hslider("spread",3.5,0,30,0.1);
env=en.asr(a,1,r,gate); d=pow(2,spread/1200);
L=os.sawtooth(freq/d)*0.7+os.sawtooth(freq)*0.3; R=os.sawtooth(freq*d)*0.7+os.sawtooth(freq)*0.3;
process=(L:fi.lowpass(2,cut))*env*gain*0.6,(R:fi.lowpass(2,cut))*env*gain*0.6;'''
P['glide']='''gl=hslider("glide",0.15,0.001,2,0.001); cut=hslider("cut",500,50,8000,1); drive=hslider("drive",1.4,1,6,0.01);
f=freq:si.smooth(ba.tau2pole(gl)); env=en.asr(0.02,1,0.15,gate); d=pow(2,7/1200);
sub=os.osc(f)*0.5; L=(os.sawtooth(f/d)*0.6+os.sawtooth(f)*0.4):ve.moog_vcf_2b(0.2,cut); R=(os.sawtooth(f*d)*0.6+os.sawtooth(f)*0.4):ve.moog_vcf_2b(0.2,cut);
wl=(L:fi.highpass(2,90))*0.8+sub; wr=(R:fi.highpass(2,90))*0.8+sub;
process=ma.tanh(wl*drive)*env*gain*0.8,ma.tanh(wr*drive)*env*gain*0.8;'''
P['noise_riser']='''len=hslider("len",4,0.5,32,0.01); t=ba.time/ma.SR; p=min(1,t/len);
n=no.pink_noise:fi.resonlp(200+p*p*9000,2+p*4,1); process=n*p*p*0.8<:_,_*(1-0.3*os.osc(6));'''

# ---------- Pedalboard FX ----------
from pedalboard import Pedalboard, Reverb, Chorus, Delay, LadderFilter, Distortion, Compressor, HighpassFilter, LowpassFilter, Phaser, Gain, Limiter, PitchShift
def fx(x, *plugins): return Pedalboard(list(plugins))(x.T.astype(np.float32), SR).T
def db(g): return 10**(g/20)
def write(path,x): sf.write(path, x/max(1e-9,np.max(np.abs(x)))*0.9 if np.max(np.abs(x))>1 else x, SR)

# ---------- designed drums (numpy) ----------
def _env(n,a,d,curve=1.0):
    t=np.arange(n)/SR; e=np.exp(-t/d)**curve; e[:int(a*SR)]*=np.linspace(0,1,int(a*SR)) if a>0 else 1; return e
def kick(f0=52,f1=180,pdec=0.035,dec=0.45,click=0.3,drive=2.0,sec=0.9):
    n=int(sec*SR); t=np.arange(n)/SR; f=f0+(f1-f0)*np.exp(-t/pdec); ph=2*np.pi*np.cumsum(f)/SR
    x=np.sin(ph)*np.exp(-t/dec); c=np.random.default_rng(1).normal(0,1,n)*np.exp(-t/0.004)*click
    x=np.tanh((x+c)*drive)/np.tanh(drive); return np.stack([x,x],1).astype(np.float32)
def clap(sec=0.6,tone=1800,bw=1.2,dec=0.11,spread=(0,0.011,0.022,0.031),rev=0.25):
    rng=np.random.default_rng(2); n=int(sec*SR); t=np.arange(n)/SR; out=np.zeros(n)
    import scipy.signal as ss; sos=ss.butter(2,[tone/bw,tone*bw],'band',fs=SR,output='sos')
    for i,s in enumerate(spread):
        nz=ss.sosfilt(sos,rng.normal(0,1,n)); e=np.exp(-(t-s).clip(0)/(dec if i==len(spread)-1 else 0.012))*(t>=s); out+=nz*e
    tail=ss.sosfilt(sos,rng.normal(0,1,n))*np.exp(-t/0.35)*rev; out+=tail
    out/=np.abs(out).max(); L=out; R=np.roll(out,int(0.0004*SR)); return np.stack([L,R],1).astype(np.float32)
def snare(sec=0.5,f0=190,dec=0.12,ndec=0.18,mix=0.5):
    rng=np.random.default_rng(3); n=int(sec*SR); t=np.arange(n)/SR
    body=np.sin(2*np.pi*(f0+60*np.exp(-t/0.02))*t)*np.exp(-t/dec)
    import scipy.signal as ss; nz=ss.sosfilt(ss.butter(2,[1500,9000],'band',fs=SR,output='sos'),rng.normal(0,1,n))*np.exp(-t/ndec)
    x=body*(1-mix)+nz*mix; x=np.tanh(x*2.2)/np.tanh(2.2); return np.stack([x,x],1).astype(np.float32)
def hat(sec=0.25,dec=0.045,open_=False,bright=9000):
    rng=np.random.default_rng(4); n=int(sec*SR); t=np.arange(n)/SR
    # 6 square oscillators at inharmonic ratios (808-style metallic) + noise
    ratios=[1,1.4471,1.6170,1.9265,2.5028,2.6637]; x=sum(np.sign(np.sin(2*np.pi*bright*0.06*r*t+r)) for r in ratios)/6
    import scipy.signal as ss; x=ss.sosfilt(ss.butter(4,bright*0.8,'high',fs=SR,output='sos'),x+0.6*rng.normal(0,1,n))
    x=x*np.exp(-t/(0.28 if open_ else dec)); x/=np.abs(x).max(); return np.stack([x,x*0.95],1).astype(np.float32)
def perc_rim(sec=0.2,f=900,dec=0.03):
    n=int(sec*SR); t=np.arange(n)/SR; x=(np.sin(2*np.pi*f*t)+0.5*np.sin(2*np.pi*f*2.7*t))*np.exp(-t/dec); x/=np.abs(x).max(); return np.stack([x,x],1).astype(np.float32)
def place(canvas,sample,t_sec,gain=1.0,pan=0.0):
    i=max(0,int(t_sec*SR)); j=min(len(canvas),i+len(sample))
    if j<=i: return canvas
    seg=sample[:j-i]*gain
    if pan: a=(pan+1)*np.pi/4; seg=np.stack([seg[:,0]*np.cos(a)*1.414,seg[:,1]*np.sin(a)*1.414],1)
    canvas[i:j]+=seg; return canvas

# ---------- sample loading ----------
SAMPLES='/tmp/claude-0/-home-user-bimi-logo/5f15f32e-d96a-5fe0-b454-eb7800ecdd39/scratchpad/samples'
import librosa as _lr, os as _os
_cache={}
def load_sample(rel,trim_db=60,fade_ms=3,norm=True):
    """rel: path relative to SAMPLES. returns float32 (n,2) at 44100, trimmed, peak-normalised."""
    if rel in _cache: return _cache[rel]
    y,sr=sf.read(_os.path.join(SAMPLES,rel),always_2d=True); y=y.astype(np.float32)
    if sr!=SR: y=_lr.resample(y.T,orig_sr=sr,target_sr=SR).T
    if y.shape[1]==1: y=np.repeat(y,2,1)
    m=np.abs(y).max(1); thr=m.max()*10**(-trim_db/20); idx=np.where(m>thr)[0]
    if len(idx): y=y[max(0,idx[0]-8):idx[-1]+int(0.01*SR)]
    f=int(fade_ms*SR/1000); y[-f:]*=np.linspace(1,0,f)[:,None]
    if norm: y=y/max(1e-9,np.abs(y).max())
    _cache[rel]=y; return y
KIT={ # curated one-shots
 '808_long':'Roland_TR808_hifi_set/Roland TR808 hifi set/BD7575.WAV','808_mid':'Roland_TR808_hifi_set/Roland TR808 hifi set/BD5050.WAV','808_short':'Roland_TR808_hifi_set/Roland TR808 hifi set/BD0075.WAV',
 '808_cp':'Roland_TR808_hifi_set/Roland TR808 hifi set/CP.WAV','808_ch':'Roland_TR808_hifi_set/Roland TR808 hifi set/CH.WAV','808_oh':'Roland_TR808_hifi_set/Roland TR808 hifi set/OH25.WAV','808_oh_long':'Roland_TR808_hifi_set/Roland TR808 hifi set/OH75.WAV',
 '808_rs':'Roland_TR808_hifi_set/Roland TR808 hifi set/RS.WAV','808_sd':'Roland_TR808_hifi_set/Roland TR808 hifi set/SD5050.WAV','808_ma':'Roland_TR808_hifi_set/Roland TR808 hifi set/MA.WAV','808_cb':'Roland_TR808_hifi_set/Roland TR808 hifi set/CB.WAV',
 'sp_snare1':'EMU_SP1200/EMU SP1200/Snare1.wav','sp_snare2':'EMU_SP1200/EMU SP1200/Snare2.wav','sp_kick1':'EMU_SP1200/EMU SP1200/Kick1.wav','sp_clhh':'EMU_SP1200/EMU SP1200/Clhh1.wav','sp_rim':'EMU_SP1200/EMU SP1200/Rim.wav','sp_tamb':'EMU_SP1200/EMU SP1200/Tamb.wav',
 'linn_clap':'Linn_Linndrum/Linn Linndrum/Clap.wav','linn_snare':'Linn_Linndrum/Linn Linndrum/SnareDrum.wav','linn_kick':'Linn_Linndrum/Linn Linndrum/Kick.wav','linn_chh':'Linn_Linndrum/Linn Linndrum/Chh.wav',
 'dmx_clap':'Oberheim_DMX/Oberheim DMX/Clap.wav','dmx_kick':'Oberheim_DMX/Oberheim DMX/Kick02.wav','dmx_snare':'Oberheim_DMX/Oberheim DMX/Snare01.wav',
 'tempest_808':'tempest/tempest_808_kick_02.wav'}
def kit(name): return load_sample(KIT[name])
