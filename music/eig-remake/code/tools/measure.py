import sys, numpy as np, librosa
def measure(path, bpm=None, bars=8):
    y,sr=librosa.load(path,sr=44100,mono=True)
    rms=np.sqrt(np.mean(y**2)); pk=np.max(np.abs(y))
    S=np.abs(librosa.stft(y,n_fft=4096,hop_length=1024))**2; f=librosa.fft_frequencies(sr=sr,n_fft=4096)
    tot=S.sum()
    if bpm is None: bpm=float(np.atleast_1d(librosa.beat.beat_track(y=y,sr=sr)[0])[0])
    out=dict(len=f"{int(len(y)/sr//60)}:{int(len(y)/sr%60):02d}",bpm=round(bpm,1),
        rms=round(20*np.log10(rms),1),crest=round(20*np.log10(pk/rms),1),
        centroid=int(librosa.feature.spectral_centroid(y=y,sr=sr).mean()),
        sub120=round(100*S[f<120].sum()/tot,1),hi6k=round(100*S[f>6000].sum()/tot,1))
    # per-block features: 5 band energies (dB) + onset density
    blk=int(bars*4*60/bpm*sr/1024); bands=[0,120,400,2000,6000,22050]
    on=librosa.onset.onset_strength(S=librosa.power_to_db(S),sr=sr)
    feats=[]
    for i in range(0,S.shape[1]-blk//2,blk):
        B=S[:,i:i+blk]
        feats.append([10*np.log10(B[(f>=a)&(f<b)].sum()/B.shape[1]+1e-9) for a,b in zip(bands,bands[1:])]+[on[i:i+blk].mean()*3])
    F=np.array(feats); d=np.linalg.norm(np.diff(F,axis=0),axis=1)
    out['boundary_change']=[round(x,1) for x in d]
    out['flat_boundaries']=int((d<2.0).sum())
    out['energy_curve_db']=[round(x,1) for x in F[:,:5].max(axis=1)-F[:,:5].max()]
    return out
if __name__=='__main__':
    for p in sys.argv[1:]: print(p, measure(p))
