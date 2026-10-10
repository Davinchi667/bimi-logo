"""master(mix_wav, ref_wav, out_wav): Matchering to the reference, then gentle glue + soft clip to a target crest."""
import sys, types, numpy as np, scipy.signal as ss, soundfile as sf, subprocess, os
rp=types.ModuleType('resampy')
def _rs(x,sr_orig,sr_new,axis=-1,**kw):
    if sr_orig==sr_new: return x
    g=np.gcd(int(sr_orig),int(sr_new)); return ss.resample_poly(x,int(sr_new)//g,int(sr_orig)//g,axis=axis)
rp.resample=_rs; sys.modules['resampy']=rp
import matchering as mg
def stats(x):
    m=x.mean(1); r=np.sqrt(np.mean(m**2)); return 20*np.log10(r+1e-9), 20*np.log10(np.max(np.abs(x))/(r+1e-9))
def master(mix_wav, ref_wav, out_wav, crest_target=None, thr=-22, drive=1.5, peak_db=-0.8):
    tmp=out_wav.replace('.wav','_mg.wav')
    mg.process(target=mix_wav, reference=ref_wav, results=[mg.pcm24(tmp)])
    x,sr=sf.read(tmp); rms,crest=stats(x)
    if crest_target and crest>crest_target+0.5:
        for th,dr in [(-20,1.4),(-24,1.8),(-28,2.4),(-32,3.0)]:
            subprocess.run(['sox',tmp,tmp.replace('_mg','_c'),'compand','0.01,0.22',f'6:-80,-80,{th},{th},0,{th/4:.1f}'],check=True)
            y,_=sf.read(tmp.replace('_mg','_c')); y=y/np.max(np.abs(y)); y=np.tanh(y*dr)/np.tanh(dr); y=y/np.max(np.abs(y))*10**(peak_db/20)
            if stats(y)[1]<=crest_target+0.4: x=y; break
            x=y
    else:
        x=x/np.max(np.abs(x))*10**(peak_db/20)
    sf.write(out_wav,x,sr,subtype='PCM_16'); return stats(x)
if __name__=='__main__':
    print(master(*sys.argv[1:4], crest_target=float(sys.argv[4]) if len(sys.argv)>4 else None))
