import numpy as np, soundfile as sf, json, sys, scipy.signal as ss
SR=44100; db=lambda g:10**(g/20)
st=np.load(sys.argv[1]); g=json.load(open(sys.argv[2])); over=json.loads(sys.argv[3]) if len(sys.argv)>3 else {}
g.update(over)
stems={k:st[k]*db(g.get(k,0.0)) for k in st.files}
mix=sum(stems.values()); mix=ss.sosfilt(ss.butter(2,22,'high',fs=SR,output='sos'),mix,axis=0)
sc=db(-1)/np.abs(mix).max(); mix*=sc
sf.write('out/mix.wav',mix,SR,subtype='PCM_24'); np.savez_compressed('out/stems_mixed.npz',**{k:(v*sc).astype(np.float32) for k,v in stems.items()})
print('remixed; peak-normalised by %.1f dB'%(20*np.log10(sc)))
