import numpy as np, soundfile as sf, scipy.signal as ss, librosa, sys
SR=44100; BAR=4*60/115
SECS=[('intro',1,8),('A',9,16),('B',17,23),('pre24',24,24),('drop1',25,39),('t40',40,40),('verse',41,55),('pre56',56,56),('drop2',57,71),('t72',72,72),('drop3',73,87),('t88',88,88),('post',89,96),('outro',97,103)]
def load(p,t0):
    x,sr=sf.read(p); return x, t0
def feats(x,t0,a,b):
    i=int((t0+(a-1)*BAR)*SR); j=int((t0+b*BAR)*SR); seg=x[i:j]; m=seg.mean(1); s=(seg[:,0]-seg[:,1])/2
    S=np.abs(librosa.stft(m.astype(np.float32),n_fft=4096,hop_length=1024))**2; f=librosa.fft_frequencies(sr=SR,n_fft=4096); tot=S.sum()
    bands=[(0,60),(60,120),(120,400),(400,2000),(2000,6000),(6000,22050)]
    bs=[100*S[(f>=lo)&(f<hi)].sum()/tot for lo,hi in bands]
    sm=ss.sosfilt(ss.butter(4,[500,4000],'band',fs=SR,output='sos'),s); mm=ss.sosfilt(ss.butter(4,[500,4000],'band',fs=SR,output='sos'),m)
    return dict(rms=20*np.log10(np.sqrt(np.mean(m**2))+1e-9), bands=bs, cent=librosa.feature.spectral_centroid(y=m.astype(np.float32),sr=SR).mean(), sm=20*np.log10(np.sqrt(np.mean(sm**2))/(np.sqrt(np.mean(mm**2))+1e-9)+1e-9), corr=np.corrcoef(seg[:,0],seg[:,1])[0,1])
ref,rt=load('../refs/eig_inst.wav',0.290); mine,mt=load(sys.argv[1] if len(sys.argv)>1 else 'out/mix.wav',0.0)
# global
for name,x,t0 in (('REF',ref,rt),('MINE',mine,mt)):
    F=feats(x,t0,1,103); print(f"{name:5s} rms {F['rms']:6.1f}  bands <60 {F['bands'][0]:4.1f} 60-120 {F['bands'][1]:4.1f} 120-400 {F['bands'][2]:4.1f} 400-2k {F['bands'][3]:4.1f} 2-6k {F['bands'][4]:4.1f} >6k {F['bands'][5]:4.1f}  cent {F['cent']:5.0f}  S/M(0.5-4k) {F['sm']:5.1f}  corr {F['corr']:.2f}")
print(f"\n{'sec':6s} {'rmsR':>6s} {'rmsM':>6s} | {'<60R':>5s} {'<60M':>5s} | {'midR':>5s} {'midM':>5s} | {'hiR':>5s} {'hiM':>5s} | {'centR':>5s} {'centM':>5s} | {'S/M R':>5s} {'S/M M':>5s}")
for n,a,b in SECS:
    R=feats(ref,rt,a,b); M=feats(mine,mt,a,b)
    print(f"{n:6s} {R['rms']:6.1f} {M['rms']:6.1f} | {R['bands'][0]:5.1f} {M['bands'][0]:5.1f} | {R['bands'][3]:5.1f} {M['bands'][3]:5.1f} | {R['bands'][4]+R['bands'][5]:5.1f} {M['bands'][4]+M['bands'][5]:5.1f} | {R['cent']:5.0f} {M['cent']:5.0f} | {R['sm']:5.1f} {M['sm']:5.1f}")
