import numpy as np, librosa, soundfile as sf, sys
KEYS=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
maj=np.array([6.35,2.23,3.48,2.33,4.38,4.09,2.52,5.19,2.39,3.66,2.29,2.88]); mnr=np.array([6.33,2.68,3.52,5.38,2.60,3.53,2.54,4.75,3.98,2.69,3.34,3.17])
for p in sys.argv[1:]:
    x,sr=sf.read(p); L,R=x[:,0],x[:,1]; m=(L+R)/2; s=(L-R)/2
    y=m.astype(np.float32)
    tempo=float(np.atleast_1d(librosa.beat.beat_track(y=y,sr=sr)[0])[0])
    H,P=librosa.effects.hpss(y)
    chroma=librosa.feature.chroma_cqt(y=H,sr=sr).mean(1)
    sc=[(np.corrcoef(np.roll(maj,k),chroma)[0,1],KEYS[k]+' maj') for k in range(12)]+[(np.corrcoef(np.roll(mnr,k),chroma)[0,1],KEYS[k]+' min') for k in range(12)]
    sc.sort(reverse=True)
    rms=np.sqrt(np.mean(m**2)); pk=np.max(np.abs(x))
    S=np.abs(librosa.stft(y,n_fft=4096,hop_length=1024))**2; f=librosa.fft_frequencies(sr=sr,n_fft=4096); tot=S.sum()
    band=lambda a,b: round(100*S[(f>=a)&(f<b)].sum()/tot,1)
    side_ratio=20*np.log10(np.sqrt(np.mean(s**2))/np.sqrt(np.mean(m**2)))
    corr=np.corrcoef(L,R)[0,1]
    # side-channel spectrum: where the wide stuff lives
    Ss=np.abs(librosa.stft(s.astype(np.float32),n_fft=4096,hop_length=1024))**2
    sband=lambda a,b: round(10*np.log10(Ss[(f>=a)&(f<b)].sum()/max(S[(f>=a)&(f<b)].sum(),1e-12)),1)
    print(f"\n== {p}  {int(len(m)/sr//60)}:{len(m)/sr%60:04.1f}")
    print(f" tempo {tempo:.1f} | key {sc[0][1]} ({sc[0][0]:.2f}) / {sc[1][1]} ({sc[1][0]:.2f})")
    print(f" RMS {20*np.log10(rms):.1f} dB | crest {20*np.log10(pk/rms):.1f} | centroid {librosa.feature.spectral_centroid(y=y,sr=sr).mean():.0f} Hz")
    print(f" bands %: <60 {band(0,60)} | 60-120 {band(60,120)} | 120-400 {band(120,400)} | 400-2k {band(400,2000)} | 2-6k {band(2000,6000)} | >6k {band(6000,22050)}")
    print(f" harmonic/percussive: {20*np.log10(np.sqrt(np.mean(H**2))):.1f} / {20*np.log10(np.sqrt(np.mean(P**2))):.1f} dB")
    print(f" stereo: L/R corr {corr:.3f} | side vs mid {side_ratio:.1f} dB | side-vs-mid by band: <120 {sband(0,120)} | 120-400 {sband(120,400)} | 400-2k {sband(400,2000)} | 2-6k {sband(2000,6000)} | >6k {sband(6000,22050)}")
    # 8-bar section map
    blk=8*4*60/tempo; n=int(len(m)/sr/blk)+1
    rows=[]
    for i in range(n):
        a,b=int(i*blk*sr),min(len(m),int((i+1)*blk*sr))
        if b-a<sr: break
        seg=m[a:b]; sseg=s[a:b]; Hs=H[a:b]; Ps=P[a:b]
        Sg=np.abs(librosa.stft(seg.astype(np.float32),n_fft=2048,hop_length=1024))**2; ff=librosa.fft_frequencies(sr=sr,n_fft=2048)
        rows.append((i*blk, 20*np.log10(np.sqrt(np.mean(seg**2))+1e-9), 20*np.log10(np.sqrt(np.mean(sseg**2))/(np.sqrt(np.mean(seg**2))+1e-9)+1e-9),
            20*np.log10(np.sqrt(np.mean(Hs**2))+1e-9),20*np.log10(np.sqrt(np.mean(Ps**2))+1e-9),
            100*Sg[ff<120].sum()/Sg.sum(), librosa.feature.spectral_centroid(y=seg.astype(np.float32),sr=sr).mean()))
    print("  t      rms   side  harm  perc  sub%  centroid")
    for t,r,sd,h,pp,sb,c in rows: print(f"  {int(t//60)}:{t%60:04.1f} {r:6.1f} {sd:5.1f} {h:6.1f} {pp:6.1f} {sb:5.1f} {c:6.0f}")
