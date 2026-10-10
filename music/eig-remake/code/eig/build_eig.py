"""EVERYWHERE I GO [REMIND ME] instrumental rebuild. Bar numbers = structure.md (bar 1 = first downbeat). 115 BPM, 104 bars."""
import sys, json, numpy as np, scipy.signal as ss, soundfile as sf
sys.path.insert(0,'../tools')
from seq import *; from synth import *
from pedalboard import Reverb, HighpassFilter, LowpassFilter, Compressor, Gain, Chorus
BPM=115; NB=104; S=Song(BPM,NB,seed=3); N=S.N; BEAT=S.beat; BAR=S.bar
DET=1.00812                      # sample layer +14 cents
NUDGE=0.025                      # sample layer sits ~25 ms behind the drum grid
CH=['Bm','F#m','C','Em']; chord=lambda n: CH[(n-1)%4]
ROOT2={'Bm':47,'F#m':42,'C':48,'Em':40}; ROOT1={'Bm':35,'F#m':30,'C':36,'Em':28}; ROOT0={'Bm':23,'F#m':30,'C':24,'Em':28}
VOICE={'Bm':[59,62,66,71,74,78],'F#m':[57,61,66,69,73,76],'C':[55,60,64,67,72,76],'Em':[55,59,64,67,71,76]}   # triad oct3-4 + triad oct4-5
PAD2V={'Bm':[47,59,62,66,71,74,78,81,85],'F#m':[42,57,61,66,69,73,76],'C':[48,55,60,64,67,72,76,79,86],'Em':[40,55,59,64,67,71,76,78,83]}
ODD=lambda n: n%2==1            # odd bars = Bm/C bars
def b0(n): return n-1           # structure bar -> 0-based bar index
def slot(n,s): return S.B(b0(n),s/4)   # 16th slot -> beats
hz=lambda p:440*2**((p-69)/12)
def sec_mask(ranges,fade=0.02): return S.mask([(b0(a),b0(b)+1) for a,b in ranges],fade)

# ============ SAMPLE LAYERS (+14 c, nudged) ============
def pad_level(n):
    if 25<=n<=40: return 100 if (chord(n)=='C' or n in (29,37)) else 40     # drop 1: pad ducked ~16 dB except C bars / alt Bm
    return 100
for n in range(1,104):
    c=chord(n); L=pad_level(n)
    for bt in range(4):
        for i,p in enumerate(VOICE[c]): S.add('pad',S.B(b0(n),bt)+NUDGE/BEAT,0.985,p,int(L*(1 if i<3 else 0.38)))
    if n<=8:   # intro top voice
        top={'Bm':[(15,69,5)],'F#m':[(7,73,2)],'C':[(5,72,6),(15,76,1)],'Em':[(0,71,9),(5,76,1),(14,76,2)]}[c]
        for s,p,l in top: S.add('pad',slot(n,s)+NUDGE/BEAT,l/4,p,62)
# ---- sample bass (sine + 0.4 octave, continuous), sample sub (9-16) : numpy ----
def tone_track(bars,pitch_of,level_db,oct_mix=0.4,det=DET,gate_bars=None):
    out=np.zeros(N); ph=0.0; ph2=0.0
    for n in bars:
        f=hz(pitch_of(n))*det; i=int((S.t(b0(n))+NUDGE)*SR); j=int((S.t(b0(n)+1)+NUDGE)*SR); t=np.arange(j-i)/SR
        seg=np.sin(ph+2*np.pi*f*t)+oct_mix*np.sin(ph2+2*np.pi*2*f*t); ph=(ph+2*np.pi*f*(j-i)/SR)%(2*np.pi); ph2=(ph2+2*np.pi*2*f*(j-i)/SR)%(2*np.pi)
        if gate_bars: seg*=np.minimum(1,t/0.02)*np.minimum(1,((j-i)-np.arange(j-i))/(0.02*SR))
        out[i:j]+=seg
    x=np.stack([out,out],1)*db(level_db); return x
sbass=tone_track(range(1,104),lambda n:ROOT2[chord(n)],-17)
ssub=tone_track(range(9,17),lambda n:ROOT1[chord(n)],-30,0.0)
subl=tone_track(range(17,24),lambda n:ROOT1[chord(n)],-21,0.28,det=1.0,gate_bars=True)      # SUB layer, A440, whole-bar gated
# ============ LEAD riff (chopped-vocal line) ============
def lead_notes(n):
    c=chord(n); k=n
    busy=73<=n<=88; thin=57<=n<=72; post=89<=n<=96
    if c=='Bm':
        va=(k in (25,33,57,65,73,81))
        if post: va=False
        if thin: return [(6,66,1.6),(14,64,1.5)] if va else [(6,62,2.7),(14,69,1.7)]
        if va: return [(6,66,1.6),(9,67,1.4)]+([(11,66,1.6)] if busy else [])+[(14,64,1.5)]
        return [(6,62,2.7),(9,61,1.3),(11,62,2.5),(14,69,1.7)]
    if c=='F#m':
        prev=chord(n-1); va=((n-1) in (25,33,57,65,73,81))
        return [(0,66 if va else 61,3.0 if va else 2.3)]
    if c=='C':
        if thin: return [(5,64,4),(11,64,2)]
        if post: return [(4,64,8)]
        out=[(6,64,2.4)]
        if n in (75,83,87): out.append((8,64,1.4))
        out.append((9,62,1.3) if n in (27,31,83,87) else (9,64,1.2))
        if n in (39,75,79,83,87): out.append((11,64,2.6))
        out.append((14,66,1.7)); return out
    if c=='Em':
        if thin: return [(0,64,10)]
        if post: return [(0,67,4),(4,66,4),(8,64,4),(12,62,4)]
        out=[(0,67,2.2)]
        if n in (28,32,88): out.append((5,66,1.5))
        out+= [(8,64,3.0),(12,62,2.3)]; return out
for n in list(range(25,41))+list(range(57,73))+list(range(73,89))+list(range(89,97)):
    for s,p,l in lead_notes(n): S.add('lead',slot(n,s)+NUDGE/BEAT,l/4*0.95,p,100)
# ============ HUM (Cudi hook line, C#3-A3) + choir shadow ============
def hum_notes(n):
    c=chord(n)
    if c=='Bm':
        va=n in (25,33,57,65,89,97)
        if va: return [(6,54,2),(8,57,1),(9,55,1.8),(11,54,2.2),(14,52,1.4)]
        return [(3,50,1.5),(5,50,1.2),(9,49,1.1),(11,50,1.5),(14,57,1.6)]
    if c=='F#m': return [(0,54 if (n-1) in (25,33,57,65,89,97) else 49,3.8)]
    if c=='C':
        out=[(0,52,2.5)] if n in (31,39,59,67,71,95,103) else []
        out+=[(6,52,2.2),(9,50,1.1) if n in (27,59,99) else (9,52,1.0),(11,52,2.3),(14,54,1.4)]; return out
    return [(0,55,3.4),(4,54,3),(8,52,3),(12,50,3)]
for n in list(range(25,41))+list(range(57,73))+list(range(89,104)):
    for s,p,l in hum_notes(n):
        S.add('hum',slot(n,s)+0.012/BEAT,l/4*0.95,p,100)
        if n>=97: S.add('choirhi',slot(n,s)+0.02/BEAT,l/4*0.95,p+12,80)
# ============ PAD-2 (A440 unison pad, 57-103) and WIDE choir layer ============
for n in range(57,104):
    for p in PAD2V[chord(n)]: S.add('pad2',S.B(b0(n)),3.98,p,88 if p<76 else 60)
WIDE=set([35,36,39])|{57,59,60,63,64,67,68,71}|set(range(73,88))|set(range(89,104))
for n in sorted(WIDE):
    for p in VOICE[chord(n)][1:5]: S.add('wide',S.B(b0(n)),3.95,p,80)
# ============ GLIDE BASS (41-56) ============
GL=[[(.25,23,.4),(1,37,.5),(1.75,38,.5),(2.75,37,.3),(3.25,23,.15),(3.5,35,.4)],
    [(.25,33,.4),(1,30,.5),(1.75,33,.5),(2.75,33,.3),(3.5,28,.4)],
    [(.25,33,.4),(.75,28,.2),(1,40,.4),(1.75,33,.4),(2.25,28,.6),(3.5,33,.4)],
    [(.25,40,.4),(.75,28,.2),(1.75,40,.4),(2.25,28,.25),(2.5,26,.5),(3,28,.5),(3.5,33,.4)]]
for n in range(41,57):
    for bt,p,l in GL[(n-41)%4]:
        if n==56 and bt>=2: continue
        S.add('glide',S.B(b0(n),bt),l,p,110)
# ============ 808 (numpy, two-stage envelope, H2 -5 dB) ============
E808=[]   # (bar, slot, pitch, level_db, floor_db)
def add808(n,s,p,lv,floor=None): E808.append((n,s,p,lv,floor))
for n in range(25,97):
    c=chord(n); r=ROOT0[c]
    if 41<=n<=55: continue
    if n==56:
        add808(n,1,r,-24); add808(n,4,r,-24); add808(n,7,r,-24,-34); add808(n,13,30,-22); continue
    if n in (40,72,88):
        add808(n,1,r,-13); add808(n,4,r,-4); add808(n,7,r,-4); add808(n,10,r,-4); add808(n,13,30,-5); continue
    if 89<=n<=96:
        if c=='Bm': add808(n,4,r,-8,-13)
        elif c=='F#m': add808(n,0,r,-8); add808(n,4,r,-7,-12)
        elif c=='C': add808(n,0,r,-8,-13)
        else: add808(n,10,r,-5); add808(n,13,30,-5)
        continue
    hook2=57<=n<=71
    if ODD(n) or hook2:
        add808(n,0,r,-11); add808(n,4,r,-4); add808(n,7,r,-4); add808(n,10,r,-4); add808(n,13,r,-4)
        if hook2 and c=='Em': E808[-1]=(n,13,30,-7,None)
    else:
        add808(n,1,r,-11); add808(n,4,r,-4); add808(n,7,r,-4,-16)
        if c=='Em': add808(n,13,30,-10)
add808(24,15,30,-27)
def render_808():
    out=np.zeros(N); ev=sorted(E808,key=lambda e:(e[0],e[1]))
    for k,(n,s,p,lv,floor) in enumerate(ev):
        t0=S.t(b0(n),s/4)
        if k+1<len(ev): t1=S.t(b0(ev[k+1][0]),ev[k+1][1]/4)
        else: t1=t0+2.5
        tend=S.t(b0(n)+1) if floor is not None else t1
        dur=max(0.05,min(tend,t1)-t0); i=int(t0*SR); j=min(N,i+int(dur*SR)); t=np.arange(j-i)/SR; f=hz(p)
        fast=10**(-29*np.minimum(t,0.3)/20); slow=10**(-29*0.3/20)*10**(-15*np.maximum(0,t-0.3)/20); env=np.where(t<0.3,fast,slow)
        if floor is not None: env=np.maximum(env,db(floor-lv))
        env*=np.minimum(1,t/0.02); env[-int(0.01*SR):]*=np.linspace(1,0,int(0.01*SR))
        x=(np.sin(2*np.pi*f*t)+db(-5)*np.sin(2*np.pi*2*f*t+0.3)+db(-17)*np.sin(2*np.pi*3*f*t)+db(-22)*np.sin(2*np.pi*4*f*t)+db(-24)*np.sin(2*np.pi*6*f*t))*env*db(lv)
        out[i:j]+=x
    out=ss.sosfilt(ss.butter(1,2000,'low',fs=SR,output='sos'),out); out=ss.sosfilt(ss.butter(2,25,'high',fs=SR,output='sos'),out)
    return np.stack([out,out],1).astype(np.float32)
# ============ DRUMS ============
def kick_e1(sec=0.32):
    n=int(sec*SR); t=np.arange(n)/SR; f=40.6+90*np.exp(-t/0.015); ph=2*np.pi*np.cumsum(f)/SR
    env=np.where(t<0.08,1.0,np.exp(-(t-0.08)/0.05)); env*=np.minimum(1,t/0.003)
    body=np.tanh(np.sin(ph)*1.4)/np.tanh(1.4)*env
    rng=np.random.default_rng(9); click=ss.sosfilt(ss.butter(2,[1000,8000],'band',fs=SR,output='sos'),rng.normal(0,1,n))*np.exp(-t/0.006)*db(-13)
    thump=ss.sosfilt(ss.butter(2,[120,400],'band',fs=SR,output='sos'),rng.normal(0,1,n))*np.exp(-t/0.008)*db(-5)
    x=body+click+thump; x/=np.abs(x).max(); return np.stack([x,x],1).astype(np.float32)
def hat_eig(tau=0.016,sec=0.12,peak1=3700,peak2=12400,seed=5):
    rng=np.random.default_rng(seed); n=int(sec*SR); t=np.arange(n)/SR; x=rng.normal(0,1,n)
    x=ss.sosfilt(ss.butter(2,3000,'high',fs=SR,output='sos'),x)
    for fc,g,q in ((peak1,6,2),(peak2,4,3)):
        b,a=ss.iirpeak(fc,q,fs=SR); x=x+ (db(g)-1)*ss.lfilter(b,a,x)
    x=ss.sosfilt(ss.butter(4,16000,'low',fs=SR,output='sos'),x)*np.exp(-t/tau)*np.minimum(1,t/0.001); x/=np.abs(x).max()
    return np.stack([x,np.roll(x,3)*0.97],1).astype(np.float32)
def knock(sec=0.12):
    rng=np.random.default_rng(11); n=int(sec*SR); t=np.arange(n)/SR
    nz=ss.sosfilt(ss.butter(2,[300,600],'band',fs=SR,output='sos'),rng.normal(0,1,n)); ping=np.sin(2*np.pi*350*t)
    x=(nz*0.7+ping*0.6)*np.exp(-t/0.015)*np.minimum(1,t/0.01)+ss.sosfilt(ss.butter(2,3000,'high',fs=SR,output='sos'),rng.normal(0,1,n))*np.exp(-t/0.004)*db(-12)
    x/=np.abs(x).max(); return np.stack([x,np.roll(x,int(0.0006*SR))],1).astype(np.float32)
def perc2(sec=0.12):
    rng=np.random.default_rng(13); n=int(sec*SR); t=np.arange(n)/SR; sos=ss.butter(2,[2000,8000],'band',fs=SR,output='sos')
    L=ss.sosfilt(sos,rng.normal(0,1,n))*np.exp(-t/0.025); R=ss.sosfilt(sos,rng.normal(0,1,n))*np.exp(-t/0.025)
    m=max(np.abs(L).max(),np.abs(R).max()); return np.stack([L/m,R/m],1).astype(np.float32)
KICK=kick_e1(); HAT=hat_eig(); HATDB=hat_eig(0.025,0.16,7500,9000,seed=6); CLAP=clap(spread=(0,0.010,0.020,0.032),tone=1900,bw=1.4,dec=0.04,rev=0.0); KNOCK=knock(); PERC2=perc2(); TOM=kit('808_long')
for n in range(1,97):
    c=chord(n); odd=ODD(n); b=b0(n)
    # kick
    if n<=8: ks=[0] if odd else []
    elif n<=16: ks=[0,6]
    elif n<=23: ks=[0,6] if odd else [0,6,10,13]
    elif n==24: ks=[]
    elif n<=39: ks=[0,6] if odd else [0,6,10,13]
    elif n==40: ks=[0,1,2,3,4,5,6,7,8,10,12,13,14,15]
    elif n<=55: ks=[0,6] if odd else [0,6,10,13]
    elif n==56: ks=[7,12]
    elif n<=71: ks=[0,6]
    elif n==72: ks=list(range(12))+[12,13]
    elif n<=87: ks=[0,6] if odd else [0,6,10,13]
    elif n==88: ks=[0,1,2,3,4,5,6,7,8,9,10,13,14,15]
    else: ks=[0,4]
    for s in ks:
        v=118 if s in (0,6,4) or n<25 else (100 if s%2==0 else 88)
        if n in (40,72,88) and s not in (0,4,8,12): v=92
        if n==56: v=84
        S.hit('kick',b,s/4,v)
    # clap
    if n not in (24,40,56,72,88):
        for s in (4,12): S.hit('clap',b,s/4,112,ms_late=12)
    # knock
    if n!=24: S.hit('knock',b,2/4,100,ms_late=6)
    # hats
    if n==24: hs=[]
    elif n<=40 and n!=40: hs=[0,2,3,10,11]+([8] if (n>=33 and not odd) else [])
    elif n==40: hs=[]
    elif n<=55: hs=[2,3,4,5,6,10,11,12,13,14]
    elif n==56: hs=[12,13,14,15]
    elif n<=71: hs=[0,2,3,6,7,9,10,11]
    elif n==72 or n==88: hs=[]
    elif n<=87: hs=[0,2,3,10,11]+([15] if odd else [])
    else: hs=[0,2,3,10,11]+([15] if odd else [])
    for s in hs:
        acc=(n==48 and s in (12,13,14)) or (n==56)
        S.hit('hatdb' if (s==0 and odd) else 'hat',b,s/4,100 if not acc else 118,ms_late=16)
    if 73<=n<=96 and n!=88:
        for s in (5,6,7,8,9,13,14,15): S.hit('perc2',b,s/4,96,ms_late=10)
S.hit('tom',b0(56),1.0,110)
# ============ RENDER ============
print('rendering synth layers...')
pad=S.render_layer('pad',P['rpad'],{'det':DET,'vibc':9.0,'cut':2600},voices=48)
lead=S.render_layer('lead',P['rlead'],{'det':DET,'cut':1600},voices=6)
hum=S.render_layer('hum',P['hum'],{'a':0.09,'r':0.3,'breath':0.06,'nasal':0.55},voices=6)
choirhi=S.render_layer('choirhi',P['choir'],{'vowel':2,'a':0.2,'r':0.8},voices=8)
pad2=S.render_layer('pad2',P['pad2'],{'cut':3500,'spread':3.5},voices=48)
wide=S.render_layer('wide',P['choir'],{'vowel':2,'a':0.35,'r':1.2},voices=24)
glide=S.render_layer('glide',P['glide'],{'glide':0.15,'cut':520,'drive':1.6},voices=1)
b808=render_808()
print('drums...')
K=S.render_drum('kick',KICK); H=S.render_drum('hat',HAT)+S.render_drum('hatdb',HATDB); C=S.render_drum('clap',CLAP); KN=S.render_drum('knock',KNOCK); P2=S.render_drum('perc2',PERC2); T=S.render_drum('tom',TOM)
# ---- processing ----
def norm_peak(x,peak_db): return x/max(1e-9,np.abs(x).max())*db(peak_db)
# pad: narrow, outro low-pass steps, legato
outro=sec_mask([(97,103)],0.05); last=sec_mask([(103,103)],0.05)
pad=norm_peak(pad,-14); pad_lp=filt(filt(pad,2000,'low',4),2000,'low',2); pad_lp2=filt(pad,800,'low',4)
pad=pad*(1-outro)+pad_lp*(outro-last)+pad_lp2*last
pad=width(fx(pad,Chorus(rate_hz=0.3,depth=0.12,mix=0.05)),0.2)*(1+0.58*sec_mask([(40,40),(72,72),(88,88),(56,56)],0.01))
lead=norm_peak(lead,-15)*(1+0.58*sec_mask([(25,39)],0.02)); lead=width(fx(lead,Chorus(rate_hz=0.4,depth=0.1,mix=0.15)),0.7)
sb=sbass; sb=width(sb,0.3)
# pad2: wide unison, level relative to pad; +3 dB in 73-87, -5 dB outro
p2g=db(-9)*(1+0.41*sec_mask([(73,87)])+0.6*outro)
pad2=norm_peak(pad2,-12)*p2g*(1+1.0*sec_mask([(40,40),(72,72),(88,88)],0.01)); pad2=pad2*(1-outro)+filt(pad2,1500,'low',2)*outro; pad2=width(pad2,1.2)
# wide choir layer: hard L/R split + long reverb, HPF 500, LPF 4k
wide=norm_peak(wide,-14); wide=filt(filt(wide,500,'high',2),4500,'low',2)
wide=np.stack([wide[:,0],np.roll(wide[:,1],int(0.013*SR))],1); wide=fx(wide,Reverb(room_size=0.85,damping=0.5,wet_level=0.5,dry_level=0.6,width=1.0)); wide=width(wide,1.7)
# hum: chest vowel, wide-ish, hall
hum=norm_peak(hum,-12); hum=fx(hum,HighpassFilter(200),LowpassFilter(5000),Chorus(rate_hz=0.25,depth=0.15,mix=0.25),Reverb(room_size=0.8,damping=0.6,wet_level=0.28,dry_level=0.8,width=1.0)); hum=width(hum,1.1)
choirhi=norm_peak(choirhi,-18); choirhi=fx(choirhi,HighpassFilter(300),Reverb(room_size=0.9,damping=0.5,wet_level=0.5,dry_level=0.5,width=1.0)); choirhi=width(choirhi,1.6)
glide=norm_peak(glide,-8)
# drums
K=norm_peak(K,0.0); b808=norm_peak(b808,-2.5)
H=norm_peak(H,-19.5); KN=norm_peak(KN,-16); P2=norm_peak(P2,-27); T=norm_peak(filt(T,500,'low',2),-12)
Cbody=norm_peak(C,-9); Cver=fx(np.stack([Cbody[:,0],np.roll(Cbody[:,1],int(0.027*SR))],1),HighpassFilter(400),LowpassFilter(8000),Reverb(room_size=0.88,damping=0.4,wet_level=1.0,dry_level=0.0,width=1.0))
Cver=width(norm_peak(Cver,-36),1.8); C=Cbody+Cver
# ---- FX: reverse swells into 25, 57, 97 ; bright riser in 56 ; washes in 40,72,88 ----
def swell_into(bar,length=2.0,gain_db=-14):
    src=wide if np.abs(wide).max()>0 else pad
    seg=fx(pad[int(S.t(b0(bar))*SR):int(S.t(b0(bar))*SR)+int(2.5*SR)],HighpassFilter(300),Reverb(room_size=0.95,damping=0.3,wet_level=1.0,dry_level=0.0,width=1.0))
    seg=seg[::-1][:int(length*SR)]; L=len(seg); env=(np.linspace(0,1,L)**2.2)[:,None]; seg=seg*env
    rng=np.random.default_rng(bar); seg=np.stack([seg[:,0],ss.sosfilt(ss.butter(2,[300,4000],'band',fs=SR,output='sos'),np.roll(seg[:,1],int(0.021*SR)))],1)   # decorrelate
    for fc in (735,974,1074,1181,1315):
        b,a=ss.iirpeak(fc,8,fs=SR); seg+=0.15*ss.lfilter(b,a,seg)
    out=np.zeros((N,2)); e=int(S.t(b0(bar))*SR)-int(0.012*SR); out[e-L:e]+=seg/max(1e-9,np.abs(seg).max())*db(gain_db); return out
SW=swell_into(25)+swell_into(57,2.0,-16)+swell_into(97,2.0,-16)
def riser(bar):
    L=int(BAR*SR); rng=np.random.default_rng(56); t=np.arange(L)/SR; p=(t/BAR)**2.5
    n=rng.normal(0,1,L); out=np.zeros(L)
    for k in range(0,L,2048):
        fc=1500*(9000/1500)**p[min(L-1,k)]; out[k:k+2048]=ss.sosfilt(ss.butter(2,[fc/1.6,min(16000,fc*1.6)],'band',fs=SR,output='sos'),n[max(0,k-4096):k+2048])[-(min(L,k+2048)-k):]
    out=out*p*db(-17); z=np.zeros((N,2)); i=int(S.t(b0(bar))*SR); z[i:i+L]=np.stack([out,out],1); return z
RS=riser(56)
def wash(bar):
    i=int(S.t(b0(bar))*SR); L=int(BAR*SR); seg=wide[i:i+L] if np.abs(wide[i:i+L]).max()>0 else pad[i:i+L]
    seg=fx(seg,HighpassFilter(800),LowpassFilter(5000),Reverb(room_size=0.9,damping=0.3,wet_level=1.0,dry_level=0.0,width=1.0))
    seg=np.stack([seg[:,0],-np.roll(seg[:,1],int(0.017*SR))],1); z=np.zeros((N,2)); z[i:i+L]=seg/max(1e-9,np.abs(seg).max())*db(-16); return z
WA=wash(40)+wash(72)+wash(88)
# ---- section gains ----
hum_g=db(-15)*(1+0.3*sec_mask([(89,103)]))
STEMS={'01 Kick':K,'02 808':b808,'03 Sub layers':ssub+subl,'04 Glide Bass':glide,'05 Clap':C,'06 Hats':H,'07 Knock':KN,'08 Perc2':P2,'09 Tom':T,
 '10 Sample Bass':sb,'11 Sample Pad':pad,'12 Lead Riff':lead,'13 Pad2':pad2,'14 Wide Choir':wide*db(-16),'15 Hum':hum*hum_g,'16 Choir High':choirhi*db(-14),
 '17 Swells':SW,'18 Riser':RS,'19 Wash':WA}
mix=sum(STEMS.values())
# hard cut 9 ms before bar 104 line
cut=int((S.t(b0(104))-0.009)*SR); mix[cut:]=0
for k in STEMS: STEMS[k][cut:]=0
mix=filt(mix,22,'high',2)
sc=db(-1)/np.abs(mix).max(); mix*=sc
os.makedirs('out',exist_ok=True); sf.write('out/mix.wav',mix,SR,subtype='PCM_24')
np.savez_compressed('out/stems.npz',**{k:(v*sc).astype(np.float32) for k,v in STEMS.items()})
S.midi('out/eig_remake.mid',{'pad':(0,89),'lead':(1,54),'hum':(2,53),'pad2':(3,90),'wide':(4,52),'glide':(5,38)})
json.dump({'E808':E808},open('out/e808.json','w'))
print('done', mix.shape, 'peak %.2f'%np.abs(mix).max())
