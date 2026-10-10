import struct
def vlq(n):
    b=[n&0x7F]; n>>=7
    while n: b.append((n&0x7F)|0x80); n>>=7
    return bytes(reversed(b))
class MIDI:
    def __init__(self,tpq=480): self.tpq=tpq; self.tracks=[]
    def track(self,name,events,ch,prog=None,tempo=None):
        """events: list of (start_beats, dur_beats, pitch, vel)"""
        ev=[]
        if tempo:
            mpqn=int(60_000_000/tempo)
            ev.append((0,0,b'\xFF\x51\x03'+struct.pack('>I',mpqn)[1:]))
        nb=name.encode()[:120]
        ev.append((0,0,b'\xFF\x03'+vlq(len(nb))+nb))
        if prog is not None: ev.append((0,1,bytes([0xC0|ch,prog])))
        for st,du,pi,ve in events:
            a=int(round(st*self.tpq)); b=int(round((st+du)*self.tpq))
            if b<=a: b=a+1
            ev.append((a,2,bytes([0x90|ch,max(0,min(127,int(pi))),max(1,min(127,int(ve)))])))
            ev.append((b,2,bytes([0x80|ch,max(0,min(127,int(pi))),0])))
        ev.sort(key=lambda x:(x[0],x[1]))
        out=b''; last=0
        for tick,_,data in ev:
            out+=vlq(tick-last)+data; last=tick
        out+=vlq(0)+b'\xFF\x2F\x00'
        self.tracks.append(out)
    def save(self,path):
        hdr=b'MThd'+struct.pack('>IHHH',6,1,len(self.tracks),self.tpq)
        body=b''.join(b'MTrk'+struct.pack('>I',len(t))+t for t in self.tracks)
        open(path,'wb').write(hdr+body)
