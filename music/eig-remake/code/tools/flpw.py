import struct
def vlq(n):
    b=b''
    while True:
        x=n&0x7F; n>>=7
        b+=bytes([x|(0x80 if n else 0)])
        if not n: return b
def U8(i,v):  return bytes([i,v&0xFF])
def U16(i,v): return bytes([i])+struct.pack('<H',v&0xFFFF)
def U32(i,v): return bytes([i])+struct.pack('<I',v&0xFFFFFFFF)
def TXT(i,s):
    d=s.encode('utf-16-le')+b'\x00\x00'
    return bytes([i])+vlq(len(d))+d
def ASC(i,s):
    d=s.encode('ascii')+b'\x00'
    return bytes([i])+vlq(len(d))+d
def DAT(i,d): return bytes([i])+vlq(len(d))+d

# --- event ids ---
ID_CHAN_TYPE=21; ID_NEW_CHAN=64; ID_NEW_PAT=65; ID_FINETEMPO=156
ID_TXT_CHANNAME=203; ID_TXT_PATNAME=193; ID_TXT_TITLE=194; ID_VERSION=199
ID_TXT_PLUGNAME=201; ID_PATNOTES=224; ID_PLAYLIST=233
ID_CHAN_VOL=2; ID_CHAN_PAN=3; ID_CHAN_ROUTEDTO=22; ID_CHAN_COLOR=128
ID_ARR_NEW=99; ID_ARR_CUR=100; ID_ARR_NAME=241; ID_PAT_LEN=164
ID_TSNUM=17; ID_TSBEAT=18; ID_TRACK_DATA=238; ID_TRACK_NAME=239
ID_SLOT_INDEX=98; ID_INSERT_NAME=204; ID_INSERT_FLAGS=236; ID_MIXER_PARAMS=225; ID_PAT_COLOR=150
ID_NEWPLUGIN=212; ID_PLUGPARAMS=213

def note(pos,ch,key,dur,vel=100,pan=128,rel=0x40,mod=0x80):
    """24-byte FL note struct"""
    return (struct.pack('<I',pos)+struct.pack('<H',0)+struct.pack('<H',ch)
            +struct.pack('<I',dur)+bytes([key&0x7F,0,0,0])
            +bytes([rel,0,pan,max(0,min(127,vel))*2 if vel<128 else 255,mod,mod])+b'\x00\x00')

class FLP:
    PPQ=96
    def __init__(self,title='Claude',tempo=120.0):
        self.title=title; self.tempo=tempo
        self.channels=[]      # (name, colour)
        self.patterns=[]      # (name, [notes], colour)
        self.blocks=[]        # (pattern, track, start_tick, len_tick)
        self.inserts=[]       # mixer insert names
    def add_channel(self,name,colour=0x5C8CB4):
        self.channels.append((name,colour)); return len(self.channels)-1
    def add_pattern(self,name,notes,colour=0x5C8CB4):
        self.patterns.append((name,notes,colour)); return len(self.patterns)
    def place(self,pattern_idx,track,start_beat,length_beats):
        self.blocks.append((pattern_idx,track,int(start_beat*self.PPQ),int(length_beats*self.PPQ)))
    def add_insert(self,name):
        self.inserts.append(name); return len(self.inserts)
    def build(self):
        e=b''
        e+=ASC(ID_VERSION,'20.8.3.2304')   # must be ASCII: it is what tells FL the rest is UTF-16
        e+=U32(ID_FINETEMPO,int(round(self.tempo*1000)))
        e+=TXT(ID_TXT_TITLE,self.title)
        e+=U16(67,1)                                  # current pattern
        e+=TXT(231,'Unsorted')                        # display group 0 must exist
        # ---- channels ----
        for i,(nm,col) in enumerate(self.channels):
            e+=U16(ID_NEW_CHAN,i)
            e+=U8(ID_CHAN_TYPE,0)                     # 0 = sampler
            e+=TXT(ID_TXT_PLUGNAME,'Sampler')
            e+=DAT(ID_NEWPLUGIN,b'\x00'*52)
            e+=TXT(ID_TXT_CHANNAME,nm)
            e+=U32(ID_CHAN_COLOR,col)
            e+=U8(ID_CHAN_VOL,100)
            e+=U8(ID_CHAN_PAN,0)
            e+=U8(ID_CHAN_ROUTEDTO,(i+1)&0xFF)
            e+=U32(145,0)                             # GroupNum: required by the format
        # ---- patterns ----
        for pi,(nm,notes,col) in enumerate(self.patterns,start=1):
            e+=U16(ID_NEW_PAT,pi)
            e+=TXT(ID_TXT_PATNAME,nm)
            e+=U32(ID_PAT_COLOR,col)
            if notes:
                e+=DAT(ID_PATNOTES,b''.join(notes))
        # ---- arrangement ----
        e+=U16(ID_ARR_NEW,0)
        e+=TXT(ID_ARR_NAME,'Arrangement')
        items=b''
        blocks=self.blocks
        if not blocks:
            for pi,(nm,notes,col) in enumerate(self.patterns,start=1):
                if not notes: continue
                end=max(struct.unpack('<I',n[0:4])[0]+struct.unpack('<I',n[8:12])[0] for n in notes)
                blocks.append((pi,pi,0,end))
        for (pi,trk,pos,ln) in blocks:
            items+=(struct.pack('<I',pos)               # position
                   +struct.pack('<H',20480)             # pattern_base, always 20480
                   +struct.pack('<H',20480+pi)          # item_index = base + pattern iid
                   +struct.pack('<I',ln)                # length
                   +struct.pack('<H',500-trk)           # track index, stored REVERSED
                   +struct.pack('<H',0)                 # group
                   +bytes([120,0])                      # _u1
                   +struct.pack('<H',64)                # item_flags
                   +bytes([64,100,128,128])             # _u2
                   +struct.pack('<f',0.0)               # start_offset
                   +struct.pack('<f',-1.0))             # end_offset
        if items: e+=DAT(ID_PLAYLIST,items)
        ntr=max(len(self.patterns),1)
        for ti in range(ntr):
            e+=DAT(ID_TRACK_DATA,struct.pack('<I',ti+1)+b'\x00'*62)
            e+=TXT(ID_TRACK_NAME,self.patterns[ti][0] if ti<len(self.patterns) else f'Track {ti+1}')
        e+=U16(ID_ARR_CUR,0)
        # ---- named mixer inserts ----
        for ii,nm in enumerate(self.inserts):
            e+=U16(ID_SLOT_INDEX,ii)
            e+=TXT(ID_INSERT_NAME,nm)
        hdr=b'FLhd'+struct.pack('<I',6)+struct.pack('<HHH',0,max(len(self.channels),1),self.PPQ)
        return hdr+b'FLdt'+struct.pack('<I',len(e))+e
    def save(self,path):
        open(path,'wb').write(self.build())
