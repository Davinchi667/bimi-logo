"""v1 final stage: section automation on the fitted stems, matchering vs the reference, soft clip. Run from eig/ after fit_gains.py."""
import numpy as np, soundfile as sf, json, scipy.signal as ss, sys
sys.path.insert(0,'../tools'); from master import master, stats
SR=44100; BAR=4*60/115; db=lambda g:10**(g/20)
st=np.load('out/stems.npz'); g=json.load(open('out/gains.json')); g.update({"19 Wash":8})
stems={k:st[k]*db(g.get(k,0.0)) for k in st.files}; N=len(next(iter(stems.values())))
def mask(ranges,fade=0.04):
    m=np.zeros(N)
    for a,b in ranges: m[int((a-1)*BAR*SR):int(b*BAR*SR)]=1
    k=np.hanning(int(fade*SR)); k/=k.sum(); return np.convolve(m,k,'same')[:,None]
auto=np.zeros((N,1))
for rng_,gdb in [((1,8),-2.5),((9,16),-1.5),((17,23),-0.5),((24,24),-4.0),((40,40),-1.0),((56,56),-2.5),((72,72),-1.0),((88,88),-1.0),((89,96),-0.5),((97,103),-6.0)]:
    auto+=mask([rng_])*gdb
gl=10**(auto/20)
mix=sum(stems.values())*gl; mix=ss.sosfilt(ss.butter(2,22,'high',fs=SR,output='sos'),mix,axis=0); sc=db(-1)/np.abs(mix).max(); mix*=sc
sf.write('out/mix.wav',mix,SR,subtype='PCM_24'); np.savez_compressed('out/stems_mixed.npz',**{k:(v*gl*sc).astype(np.float32) for k,v in stems.items()})
print('matchering only:',master('out/mix.wav','../refs/eig_inst.wav','out/master.wav',crest_target=None))
x,sr=sf.read('out/master.wav')
for drive in (1.3,1.6,2.0):
    y=np.tanh(x*drive)/np.tanh(drive); y=y/np.max(np.abs(y))*db(-0.8); r,c=stats(y); print(f'clip drive {drive}: rms {r:.1f} crest {c:.1f}')
    if c<=10.2: sf.write('out/master.wav',y,sr,subtype='PCM_16'); break
