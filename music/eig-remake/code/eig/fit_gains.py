import numpy as np, soundfile as sf, librosa, json
SR=44100; BAR=4*60/115
SECS=[('intro',1,8),('A',9,16),('B',17,23),('pre24',24,24),('drop1',25,39),('t40',40,40),('verse',41,55),('pre56',56,56),('drop2',57,71),('t72',72,72),('drop3',73,87),('t88',88,88),('post',89,96),('outro',97,103)]
W={'intro':1,'A':1,'B':1,'pre24':0.7,'drop1':2,'t40':0.7,'verse':1.5,'pre56':0.7,'drop2':2,'t72':0.7,'drop3':2,'t88':0.7,'post':1.5,'outro':1}
bands=[(0,60),(60,120),(120,400),(400,2000),(2000,6000),(6000,22050)]
def bandE(x,t0,a,b):
    i=int((t0+(a-1)*BAR)*SR); j=int((t0+b*BAR)*SR); m=x[i:j].mean(1).astype(np.float32)
    S=np.abs(librosa.stft(m,n_fft=4096,hop_length=2048))**2; f=librosa.fft_frequencies(sr=SR,n_fft=4096)
    return np.array([S[(f>=lo)&(f<hi)].sum() for lo,hi in bands])
ref,_=sf.read('../refs/eig_inst.wav'); T={n:bandE(ref,0.290,a,b) for n,a,b in SECS}; T={n:v/v.sum() for n,v in T.items()}
st=np.load('out/stems.npz'); names=list(st.files)
E={n:{k:bandE(st[k],0.0,a,b) for k in names} for n,a,b in SECS}
import sys
FIX=json.loads(sys.argv[1]) if len(sys.argv)>1 else {}
g={k:0.0 for k in names}; g.update(FIX); fixed={'01 Kick'}|set(FIX)
def err(g):
    e=0
    for n,_,_ in SECS:
        tot=sum(E[n][k]*10**(g[k]/10) for k in names); sh=tot/max(tot.sum(),1e-12)
        e+=W[n]*np.sum((np.log(sh+0.002)-np.log(T[n]+0.002))**2)
    return e
print('start err %.2f'%err(g))
for it in range(8):
    for k in names:
        if k in fixed: continue
        best=None
        for d in np.arange(-24,24.5,0.5):
            gg=dict(g); gg[k]=d; e=err(gg)
            if best is None or e<best[0]: best=(e,d)
        g[k]=best[1]
    print('iter',it,'err %.2f'%err(g))
for k in names: print(f'  {k:16s} {g[k]:+5.1f} dB')
json.dump(g,open('out/gains.json','w'))
print('\nresulting shares vs target (sub/60-120/120-400/400-2k/2-6k/>6k):')
for n,_,_ in SECS:
    tot=sum(E[n][k]*10**(g[k]/10) for k in names); sh=100*tot/tot.sum(); print(f'  {n:6s} mine',np.round(sh,1),' ref',np.round(100*T[n],1))
