# EVERYWHERE I GO [REMIND ME] (BNYX / Kid Cudi) - DRUM PROGRAMMING, measured from the instrumental

Source: `refs/eig_inst.wav` (44.1 kHz stereo, 3:37.3). Everything below is a measurement unless marked otherwise. Nothing was listened to.

## 0. Grid (corrects the brief)

- Tempo: **115.000 BPM** (not 114.84). Phase-concentration fit of band-wise transient onsets on 8th/16th/32nd periods peaks at 115.000 +/- 0.005 in every band (sub, kick, snare, hat). 114.84 drifts 66 ms per 24 bars, which is why 808s looked ~0.2 s late on the old grid.
- Bar 1 beat 1 (downbeat): **0.277 s** (the first transient in the file, a full-band stab at -3 dBFS; silence before it). The brief's 0.813 s is beat 2 of bar 1 (0.277 + 0.5217). With 0.813 the snare read as beats 1 and 3 and the first kick (4.451 s) as bar 2 beat 4; with 0.277 the snare is on 2 and 4 and the first kick is bar 3 beat 1.
- 1 beat = 521.74 ms, 1 bar = 2086.96 ms, 16th = 130.43 ms, 32nd = 65.22 ms. 104 bars; drums run bars 1-96; bars 97-104 are the sample alone.
- Feel: **straight 16ths, fully quantized, no swing** (see section 5). This is a 115 BPM backbeat groove (snare on 2 and 4), not halftime.

Grid legend: 32 slots per bar, `|` every beat (8 slots = 1 beat, 2 slots = 1 16th). Slot n -> beat 1+n/8; slot 4 = '1&' (8th), slot 2 = '1e', slot 6 = '1a'.
K line: `X` kick with sub peak >= -3 dB (rel. max), `x` -3..-9 dB, `o` < -9 dB. B line: `b` = onset of a sustained 808 BASS note (not a drum; cross-reference for the bass task). S line: `S` main snare/clap, `s` secondary/ghost (-12..-17.5 dB in 1.5-5 kHz). H line (>9 kHz band): `O` open-hat/crash-type (>150 ms decay), `X` >= -20 dBFS peak (full-velocity closed hat), `x` -20..-28, `o` -28..-37 (ghost), `-` -37..-48 (very faint), `S` = the snare's own high-frequency content on the backbeat (a hat under the snare cannot be confirmed).

## 1. The sounds (measured)

- **Kick**: one sample, an 808-style kick ~200 ms long. Isolated hits (4.451 s, 12.800 s) in the intro: peak 0 dBFS in the 25-250 Hz band, -6 dB at 75-93 ms, -10 dB at 115-122 ms, -20 dB at 163-178 ms, -30 dB at ~205 ms, gone by ~220 ms. Pitch (zero-crossing, 25-150 Hz): ~90 Hz in the first 20 ms, 44 Hz at 20-40 ms, 43 Hz at 40-60 ms, settling ~41 Hz (E1 = 41.2 Hz) until it dies. Broadband click on the attack (100-3000 Hz rise >= 25 dB). It is tuned to E (track key E minor).
- **808 bass (separate instrument)**: a quieter (-11 dB rel. kick peak), long (>800 ms) sustained sub note with no click: ~31 Hz (B0) / ~32.7 Hz (C1) on odd bars of the main loop, ~46-47 Hz (F#1) on even bars; it starts in bar 9 (odd bars) and is present through bar 96. Its note onsets are shown on the B line only so the kick line is not confused with it. Pitch/notes belong to the bass task.
- **Snare**: a clap-type snare. In the 1.5-5 kHz band it has 4-5 sub-transients spread over 0-45 ms (strongest at +13-15 ms and +38-44 ms after the first), peak -6 to -8 dBFS, strong mid body (600-1500 Hz peak -5.5 dBFS, 200-600 Hz -12 dBFS), spectral centroid ~3.7 kHz; HF (>9 kHz) content -23 dBFS with ~100-150 ms tail. Its first transient sits exactly on the grid (0 ms).
- **Closed hat**: peak -17 dBFS in >9 kHz, decays to -60 dB in ~100-120 ms (a medium-length closed hat, not a tight tick).
- **Open-hat / crash-type hit**: on beat 1 of every ODD bar from bar 1 through bar 95: >9 kHz peak -22..-25 dBFS followed by a ~-30 dB plateau lasting ~300 ms (d20 ~275 ms). This is what makes odd bars 2 dB louder than even bars above 8 kHz. It reads as an open hat or short crash/noise burst that marks the start of each 2-bar loop.
- **Mid-band (600-1500 Hz) onsets**: dense 16th-note activity at every slot in every section = the sampled arpeggio/pluck line (Royksopp 'Remind Me' sample), NOT percussion. Excluded from the drum grids. No rim/shaker/perc one-shot layer could be isolated outside the kick/snare/hat bands.

## 2. Section map (4-bar/8-bar energy blocks on the corrected grid) and per-section summary

Per-bar band RMS (dBFS, mono) that the boundaries were read from: sub<80 / low-mid 150-400 / mid 400-1.5k / 1.5-5k / >8k. Phrase ends (bars 24, 48, 56, 72, 88, 96) are where fills/drop-outs sit.

### Bars 1-8  INTRO   (  0.3 s -  17.0 s)
- band RMS: sub -28.3 | lowmid -21.6 | mid -23.0 | 1.5-5k -28.6 | >8k -35.6 dB
- counts: kicks 4 (0.50/bar), main snares 18, full/medium hats 44, open-type 3, ghost hats 9
- microtiming vs 32nd grid (ms, + = late): kick mean -1.3 sd 6.2 (n=4) | snare mean -0.6 sd 10.6 (n=18) | hats mean -1.3 sd 8.4 (n=44)
- kick slot usage (count per 32nd slot, 0..31): 0:4
- hat velocity profile (mean >9k peak dBFS per slot, hits in >=1/2 of bars shown as slot:dB): 0:-19 3:-25 4:-17 6:-16 20:-17 22:-17

```
bar   1  K:x.......|........|........|........  S:........|S.......|........|S.......  H:O..xX.X-|S.......|....XoX.|S.......  B:........|........|........|........
bar   2  K:........|........|........|........  S:........|SS......|........|S.......  H:X...X.X.|S.......|....X.X.|S.......  B:........|........|........|........
bar   3  K:X.......|........|........|........  S:........|S.......|........|S.......  H:xx.xX-X.|S.......|....X.X.|S.......  B:........|........|........|........
bar   4  K:........|........|........|........  S:........|S.......|........|S.......  H:X...X.X.|S.......|....X-X.|S.......  B:........|........|........|........
bar   5  K:o.......|........|........|........  S:........|S.......|........|S.......  H:xO.xX.X.|S.......|....X.X.|S.......  B:........|........|........|........
bar   6  K:........|........|........|........  S:........|S.......|........|S.......  H:X...X.X.|S.......|....X.X.|So......  B:........|........|........|........
bar   7  K:X.......|........|........|........  S:........|S.......|........|S.......  H:Ox.xX.X.|S.......|....XoX.|S.......  B:........|........|........|........
bar   8  K:........|........|........|........  S:........|S.......|........|S.......  H:X...XoX-|S.......|....X.X.|S.-.....  B:........|........|........|........
```

### Bars 9-16  A1 verse-build   ( 17.0 s -  33.7 s)
- band RMS: sub -15.6 | lowmid -21.1 | mid -23.4 | 1.5-5k -28.5 | >8k -35.7 dB
- counts: kicks 16 (2.00/bar), main snares 28, full/medium hats 45, open-type 3, ghost hats 9
- microtiming vs 32nd grid (ms, + = late): kick mean +4.1 sd 12.5 (n=16) | snare mean -2.7 sd 18.3 (n=28) | hats mean -1.8 sd 6.5 (n=45)
- kick slot usage (count per 32nd slot, 0..31): 0:8 12:8
- hat velocity profile (mean >9k peak dBFS per slot, hits in >=1/2 of bars shown as slot:dB): 0:-19 3:-26 4:-16 6:-17 12:-38 20:-16 22:-17

```
bar   9  K:o.......|....X...|........|........  S:........|SS......|........|SS......  H:xOxxX-X.|S...-...|....X.X.|S.......  B:........|........|........|........
bar  10  K:X.......|....X...|........|........  S:........|S.......|........|SS......  H:X...X.X.|S...-...|....X.X-|S.......  B:........|........|........|........
bar  11  K:X.......|....X...|........|........  S:........|SS..S...|........|S.......  H:xx.xX.Xo|S...S...|....X.X.|S.......  B:........|........|........|........
bar  12  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:X...X.X.|S.......|....X.X.|S.......  B:........|........|........|........
bar  13  K:X.......|....X...|........|........  S:........|SS..s...|........|S.......  H:OO.xX.X.|S...-...|....X.X.|S.......  B:........|........|........|........
bar  14  K:X.......|....X...|........|........  S:S.......|S.......|........|S.......  H:S...X.X.|S.......|....X.X.|S.......  B:........|........|........|........
bar  15  K:X.......|....X...|........|........  S:........|SS......|........|S.......  H:x.xxX.X.|S-..-...|....X.X.|S.......  B:........|........|........|........
bar  16  K:X.......|....o...|........|........  S:........|S.......|........|S.......  H:X...X.X.|S...-...|....X.X.|S.......  B:........|........|........|........
```

### Bars 17-24  A2 build / drop-out   ( 33.7 s -  50.4 s)
- band RMS: sub -17.3 | lowmid -21.2 | mid -23.4 | 1.5-5k -28.8 | >8k -37.4 dB
- counts: kicks 5 (0.62/bar), main snares 27, full/medium hats 37, open-type 2, ghost hats 75
- microtiming vs 32nd grid (ms, + = late): kick mean -9.6 sd 12.3 (n=5) | snare mean +3.2 sd 19.7 (n=27) | hats mean -0.8 sd 4.8 (n=37)
- kick slot usage (count per 32nd slot, 0..31): 0:2 1:1 20:1 26:1
- hat velocity profile (mean >9k peak dBFS per slot, hits in >=1/2 of bars shown as slot:dB): 0:-21 2:-31 3:-36 4:-19 6:-19 12:-38 16:-37 18:-35 19:-38 20:-17 22:-19 26:-37 27:-37 28:-38 29:-40

```
bar  17  K:X.......|........|........|........  S:s.......|S...s...|........|S.......  H:x...X.X.|S...-...|--o.X.X.|S.-.--..  B:........|........|........|........
bar  18  K:.X......|........|........|........  S:S.......|S...s...|........|S.s.....  H:X.--X.X.|S...-...|-.o-X.X.|S.-o.-..  B:........|........|........|........
bar  19  K:........|........|........|........  S:s.......|SS..s...|........|S.......  H:x.O.X.X.|S...-...|o.ooX-Xo|..o-o...  B:........|........|........|........
bar  20  K:........|........|....X...|..X.....  S:........|SS..s...|........|S.......  H:X--oX.X.|S...-...|-.o.xoXo|S.oo-...  B:........|........|........|........
bar  21  K:X.......|........|........|........  S:........|S...s...|........|SS......  H:x.x.X.Xo|....-...|oo.-X.X.|S.-.o-..  B:........|........|........|........
bar  22  K:........|........|........|........  S:........|S...s...|........|S.s.....  H:X.o.X.X.|S...-...|o.o-X.X.|S.oo....  B:........|........|........|........
bar  23  K:........|........|........|........  S:s.......|SS..S...|........|S.......  H:x.OxX.X-|S.......|o.o-X.X.|S.--o-..  B:........|........|........|........
bar  24  K:........|........|........|........  S:........|........|........|......s.  H:o-.-oooo|.-......|o..-..o-|o.oo-...  B:........|........|........|........
```

### Bars 25-32  B1 main loop   ( 50.4 s -  67.1 s)
- band RMS: sub -11.0 | lowmid -21.1 | mid -23.0 | 1.5-5k -28.6 | >8k -35.7 dB
- counts: kicks 45 (5.62/bar), main snares 32, full/medium hats 42, open-type 4, ghost hats 65
- microtiming vs 32nd grid (ms, + = late): kick mean -0.9 sd 18.0 (n=45) | snare mean +3.3 sd 15.2 (n=32) | hats mean +0.1 sd 5.0 (n=42)
- kick slot usage (count per 32nd slot, 0..31): 0:7 1:1 3:2 5:2 6:2 7:1 8:5 9:1 12:6 15:1 20:4 21:3 25:1 26:4 27:2 31:3
- hat velocity profile (mean >9k peak dBFS per slot, hits in >=1/2 of bars shown as slot:dB): 0:-19 1:-28 2:-33 3:-37 4:-17 6:-16 12:-39 16:-37 17:-40 18:-36 19:-39 20:-18 22:-16 26:-36 27:-41 28:-35

```
bar  25  K:X.......|x...X...|.....x..|........  S:........|S.......|........|S.......  H:xO.xX.X.|S...-...|--.-x-X-|xo-.oo..  B:.......b|........|........|........
bar  26  K:X.......|....X...|.....X..|...X....  S:........|S.......|....S...|S.S.....  H:X-.-X.Xo|S...-...|o.ooX.X.|S.S-o...  B:........|........|........|........
bar  27  K:X..o....|.x......|....x...|.ox.....  S:s.......|S...s...|........|S.......  H:OO..X.X-|S...-...|-o-.X.X.|S.oo....  B:........|........|........|........
bar  28  K:.X......|x...X...|.....X..|..X.....  S:........|S.......|....S...|S.......  H:X.o.X.X.|S...-...|o.o-X.X.|S.o---..  B:........|........|........|........
bar  29  K:X....oo.|x...X..x|....x...|..x....o  S:........|S...S...|........|SS......  H:xx.xX.X.|S.......|-.o-X.Xo|S.--o...  B:........|........|........|........
bar  30  K:X.......|....X...|....X...|...X....  S:........|SS..S...|....S...|S.s.....  H:X.o-X.X.|o.......|o-o.X.X.|S.o-o...  B:........|........|........|........
bar  31  K:X..o.ooo|x.......|........|.......o  S:........|S.......|........|S.......  H:x.O.X.X.|So......|-.o.X-X.|S.-o.-..  B:........|........|........|........
bar  32  K:X.......|....X...|....X...|..X.....  S:........|S.......|....S...|S.S.....  H:X.o-X.X.|S...-...|--.-S.X.|S.S-....  B:........|........|........|........
```

### Bars 33-40  B2 main loop, busier hats   ( 67.1 s -  83.8 s)
- band RMS: sub -11.0 | lowmid -21.3 | mid -21.1 | 1.5-5k -28.6 | >8k -34.2 dB
- counts: kicks 44 (5.50/bar), main snares 24, full/medium hats 71, open-type 4, ghost hats 46
- microtiming vs 32nd grid (ms, + = late): kick mean +3.8 sd 16.5 (n=44) | snare mean +0.7 sd 10.4 (n=24) | hats mean +0.1 sd 5.4 (n=71)
- kick slot usage (count per 32nd slot, 0..31): 0:7 1:1 3:2 8:7 12:6 18:1 19:3 20:4 21:2 22:1 24:1 25:2 26:5 30:1 31:1
- hat velocity profile (mean >9k peak dBFS per slot, hits in >=1/2 of bars shown as slot:dB): 0:-19 1:-32 2:-35 3:-36 4:-17 6:-16 12:-17 14:-17 16:-33 18:-18 20:-17 22:-17 26:-37 27:-39 28:-34 29:-38

```
bar  33  K:X.......|x...X...|...o.xx.|xox...oo  S:........|SS......|........|S.......  H:xxxxX.X.|S...X.X.|-.X.X.X.|S.-oo...  B:........|........|........|........
bar  34  K:X.......|x...X...|....X...|..X.....  S:S.......|S.......|s...S...|S.S.....  H:X.o-X.X.|S...X.X.|o-X.X.X.|S.So.o..  B:........|........|........|........
bar  35  K:.X.o....|x.......|....x...|........  S:s.......|S...s...|........|S.......  H:OO.xX.X.|S...X.X.|-.X.X.X.|x.o.o-..  B:........|........|........|........
bar  36  K:X.......|x.......|.....X..|..X.....  S:........|S...s...|s.......|S.S.....  H:X-o-X.X.|x...X.X.|o.X.X.X.|S.S.-o..  B:........|........|........|........
bar  37  K:X.......|x...X...|..oox...|..x.....  S:........|S...S...|........|S.......  H:O...X.X.|S...X.x.|--X.X.X-|S.o.--..  B:......bb|........|........|........
bar  38  K:X.......|....X...|....X...|..X.....  S:........|S.......|s...S...|S.S.....  H:X.--X.X.|S...X.X.|o-X.XoX.|S.S-.-..  B:........|........|........|........
bar  39  K:X..o....|x...X...|........|.x......  S:S.......|S.......|........|S.......  H:SO..X.X.|S...X.X.|o.X.X.X.|S.---...  B:........|........|........|........
bar  40  K:X.......|X.......|........|........  S:........|........|........|........  H:X---X-X.|X...X.X.|X.o-x.Xo|X.-.XoX.  B:........|........|........|........
```

### Bars 41-48  C1 verse (16th-run hats)   ( 83.8 s - 100.5 s)
- band RMS: sub -12.8 | lowmid -19.8 | mid -23.7 | 1.5-5k -28.8 | >8k -34.6 dB
- counts: kicks 20 (2.50/bar), main snares 24, full/medium hats 70, open-type 3, ghost hats 11
- microtiming vs 32nd grid (ms, + = late): kick mean -3.8 sd 10.6 (n=20) | snare mean +7.3 sd 13.6 (n=24) | hats mean -1.5 sd 7.9 (n=70)
- kick slot usage (count per 32nd slot, 0..31): 0:4 1:1 3:2 8:2 12:5 20:2 26:2 28:2
- hat velocity profile (mean >9k peak dBFS per slot, hits in >=1/2 of bars shown as slot:dB): 0:-29 3:-26 4:-18 6:-16 10:-18 12:-16 20:-17 22:-17 26:-16 28:-17

```
bar  41  K:.X.o....|........|........|....o...  S:s.......|S.....s.|........|S.......  H:O..xX.X.|S.X.X-..|....X.X.|SoX.X...  B:........|........|........|........
bar  42  K:X.......|o...X...|....X...|..X.....  S:........|S.....s.|........|S.....s.  H:o...X.X.|S.x.X...|....x.x.|S.X.X...  B:........|........|.......b|......b.
bar  43  K:........|....X...|........|........  S:s.s.....|S.....s.|........|S.......  H:x.xxX.X.|S.X.X-..|....X.X.|S.X.X-..  B:........|........|........|........
bar  44  K:X.......|........|........|........  S:..s.....|S.....s.|........|S.......  H:-...X.X.|S.X.X...|....X.X.|S.X.X...  B:........|........|........|........
bar  45  K:X..o....|........|........|....o...  S:..s.....|S.....s.|........|S.......  H:Ox.xX.X.|S.X.X...|....X.X.|S.Xox...  B:........|........|........|........
bar  46  K:X.......|o...X...|....X...|..X.....  S:..s.....|S.....s.|........|S.......  H:o...X.X.|S.X-X...|....X.X.|S.X.X...  B:........|........|.......b|......b.
bar  47  K:........|....X...|........|........  S:..s.....|S.....s.|........|S.......  H:O.xxo.X.|S.X.X...|....X-X.|S.X.X...  B:........|........|........|........
bar  48  K:........|....X...|........|........  S:..s.....|S.....s.|........|S.S.S...  H:....X.X.|S.X.X...|....X.X.|S.S.S...  B:........|........|........|........
```

### Bars 49-56  C2 verse + fill   (100.5 s - 117.1 s)
- band RMS: sub -14.1 | lowmid -19.7 | mid -22.8 | 1.5-5k -28.2 | >8k -34.6 dB
- counts: kicks 19 (2.38/bar), main snares 28, full/medium hats 73, open-type 5, ghost hats 16
- microtiming vs 32nd grid (ms, + = late): kick mean +0.0 sd 12.6 (n=19) | snare mean +3.5 sd 16.2 (n=28) | hats mean -0.8 sd 7.6 (n=73)
- kick slot usage (count per 32nd slot, 0..31): 0:3 1:1 3:2 8:2 11:1 12:3 14:1 20:2 26:2 28:2
- hat velocity profile (mean >9k peak dBFS per slot, hits in >=1/2 of bars shown as slot:dB): 0:-30 2:-26 3:-26 4:-17 6:-19 10:-17 12:-18 20:-17 22:-17 26:-17 28:-17

```
bar  49  K:X..o....|........|........|....o...  S:........|S.....s.|........|S.......  H:x.xxx.X.|S.X.X...|....X.X.|S.X.X...  B:........|........|........|........
bar  50  K:.X......|o...X...|....X...|..X.....  S:........|S.....s.|........|S.......  H:-...X.X.|S.x.X-..|....X.X.|S.X.X...  B:........|........|.......b|.......b
bar  51  K:........|......o.|........|........  S:s.......|SS......|........|S.......  H:O.OxX.X-|S.X.X...|....X.X.|S.X.X...  B:........|........|........|........
bar  52  K:........|...o....|........|........  S:..s.....|S.....s.|........|S.......  H:-...X.X.|S.X.X...|....X.X.|S.X-X...  B:........|........|........|........
bar  53  K:X..o....|........|........|....o...  S:..s.....|SS..S.s.|........|S.......  H:O.OxX-X.|S.X.X...|....X.X.|S.X.X...  B:........|........|........|........
bar  54  K:X.......|o...X...|....X...|..X.....  S:........|S.....s.|........|S.......  H:-...X.x.|S.X.X-..|....X.X.|S.XoX-..  B:........|........|.......b|......b.
bar  55  K:........|....X...|........|........  S:s.......|S.....s.|........|S.......  H:Ox.xX.X-|S.X.X...|....X.X.|S.X.X...  B:........|........|........|........
bar  56  K:........|........|........|........  S:..s.....|s.....s.|..s.S...|S.S.S.S.  H:-.o...o.|x...x.x.|..x.S...|X.X-X.xo  B:........|........|........|........
```

### Bars 57-64  D1 (hats fill in 2&/2a)   (117.1 s - 133.8 s)
- band RMS: sub -11.6 | lowmid -18.6 | mid -20.7 | 1.5-5k -27.3 | >8k -35.4 dB
- counts: kicks 32 (4.00/bar), main snares 23, full/medium hats 75, open-type 3, ghost hats 50
- microtiming vs 32nd grid (ms, + = late): kick mean -0.5 sd 17.0 (n=32) | snare mean +9.3 sd 11.9 (n=23) | hats mean +0.8 sd 6.5 (n=75)
- kick slot usage (count per 32nd slot, 0..31): 0:6 1:2 3:1 4:1 6:1 8:4 9:2 12:4 13:1 15:1 19:2 20:3 24:2 26:1 27:1
- hat velocity profile (mean >9k peak dBFS per slot, hits in >=1/2 of bars shown as slot:dB): 0:-19 1:-26 2:-31 3:-32 4:-17 6:-16 8:-24 12:-25 14:-25 16:-37 17:-40 18:-23 20:-17 22:-17 26:-38 27:-41 28:-40 29:-41

```
bar  57  K:X.......|x...X...|...ox...|o..x....  S:........|S.......|........|S.......  H:xxxxX.X.|S.-.x.o.|--x.X.X.|x.--.-..  B:........|........|........|........
bar  58  K:.X......|....X...|........|........  S:S.......|S.....s.|s.......|S.......  H:X.--X.X.|S...x.x.|-.x.X.X.|S.o-.-..  B:........|........|........|........
bar  59  K:X.......|x......x|...ox...|........  S:S.......|S...s...|........|S.......  H:S.OxX.X.|S...x.x.|-.x.X.X.|x--.-...  B:........|........|........|........
bar  60  K:X.......|x.......|........|........  S:........|S...s...|........|S.s.....  H:X--.X.X.|x-..x.x.|o-x.X-X.|xo-.--..  B:........|........|........|........
bar  61  K:X...o.o.|x...X...|....x...|........  S:........|S.......|........|S.......  H:Oxx.X.X.|x...x.x.|-.x.X.X.|S.--....  B:.......b|........|........|........
bar  62  K:X.......|....X...|........|........  S:........|S...S...|........|S.......  H:X.o.X.X.|xx..S.o.|oox.X.X.|S.--....  B:........|........|........|........
bar  63  K:.X.o....|.x......|........|o.x.....  S:........|S...s...|.....s..|S..s....  H:xxOxX.X.|x...x.x.|.-x.X-X.|S.----..  B:........|........|........|........
bar  64  K:X.......|.x...X..|........|........  S:........|S...s...|........|S.......  H:X.o-X.X.|S...x.x.|o-x.X.X.|S.--....  B:........|........|........|........
```

### Bars 65-72  D2 + drop-out bar   (133.8 s - 150.5 s)
- band RMS: sub -11.8 | lowmid -18.4 | mid -20.6 | 1.5-5k -27.4 | >8k -36.8 dB
- counts: kicks 40 (5.00/bar), main snares 23, full/medium hats 59, open-type 4, ghost hats 54
- microtiming vs 32nd grid (ms, + = late): kick mean +0.3 sd 15.4 (n=40) | snare mean +5.3 sd 14.6 (n=23) | hats mean +1.0 sd 7.7 (n=59)
- kick slot usage (count per 32nd slot, 0..31): 0:7 1:1 3:1 4:1 5:2 6:1 7:1 8:5 9:1 12:3 13:2 15:1 18:1 19:1 20:2 21:1 23:1 24:1 25:1 26:2 30:2 31:2
- hat velocity profile (mean >9k peak dBFS per slot, hits in >=1/2 of bars shown as slot:dB): 0:-21 1:-24 2:-32 4:-21 6:-20 12:-24 14:-24 16:-36 18:-28 20:-18 22:-16 26:-40 27:-41 28:-33 29:-42

```
bar  65  K:X....o..|x....X..|.....x..|..x...oo  S:........|S...S...|........|S.......  H:Ox..X.X.|x...S.x.|x.x.X.X.|S.--o.-.  B:......bb|........|........|........
bar  66  K:X.......|.....X..|........|........  S:........|S.s.S.s.|........|S.......  H:X..-X-X.|So..S.x.|--x.X-X.|S.-o.-..  B:........|........|........|........
bar  67  K:X...oooo|x.......|........|.......o  S:........|S...s...|........|S.......  H:OOxxX.Xo|S...x.x.|-.-.X.X.|S-.-o...  B:........|........|........|........
bar  68  K:X.......|....X...|........|........  S:........|S.......|s.......|S.......  H:X.-.X.X.|S...x.x.|o.x.X.X.|x..--...  B:........|........|........|........
bar  69  K:X.......|x...X...|..oox..x|oox...x.  S:........|S.......|........|S.......  H:Ox..X.X.|S...x.x.|-.x.X.X.|So--x-..  B:........|........|........|........
bar  70  K:oX......|x...X...|........|........  S:........|SS..S...|........|SS......  H:x.--X.X.|S...S.x.|-o..X.X.|S.-o.-..  B:........|........|........|........
bar  71  K:X..o....|.x.....x|....x...|........  S:S.......|S.......|s....s..|S.s.....  H:Sxx.x.X-|xx..x.x.|o.x-X.X.|S.--o...  B:........|........|........|........
bar  72  K:........|x.......|........|........  S:........|s.......|s.......|......s.  H:o.o.-.--|o.......|o.-....-|o..---..  B:........|........|........|........
```

### Bars 73-80  E1 densest hats   (150.5 s - 167.2 s)
- band RMS: sub -11.3 | lowmid -16.5 | mid -19.0 | 1.5-5k -25.7 | >8k -35.0 dB
- counts: kicks 40 (5.00/bar), main snares 37, full/medium hats 77, open-type 5, ghost hats 54
- microtiming vs 32nd grid (ms, + = late): kick mean -0.8 sd 18.8 (n=40) | snare mean +3.4 sd 8.0 (n=37) | hats mean +1.4 sd 6.2 (n=77)
- kick slot usage (count per 32nd slot, 0..31): 0:7 1:1 3:2 4:1 5:1 6:2 8:6 11:1 12:4 13:1 18:1 20:3 21:3 26:7
- hat velocity profile (mean >9k peak dBFS per slot, hits in >=1/2 of bars shown as slot:dB): 0:-19 1:-33 2:-34 3:-32 4:-17 6:-17 10:-30 12:-25 14:-24 16:-30 18:-23 20:-17 21:-29 22:-17 24:-23 26:-41 28:-37

```
bar  73  K:X.......|x..x.X..|..o.ox..|..x.....  S:........|S.s.S...|s.......|S.s.s.S.  H:xO.xX.X.|So.oS-x.|xox.XoX.|S...o.S.  B:......bb|........|........|........
bar  74  K:X.......|....X...|....X...|..X.....  S:........|S..sS.s.|....s...|S.S.s.s.  H:X-.-X.X.|S.o.S.x.|-.x.XxX.|x.S.-.o.  B:........|........|........|........
bar  75  K:X..o....|x.......|........|..x.....  S:S.......|S.s.s...|ss......|SS....S.  H:SOxxX.X.|S.o.x.x.|x-x.XoX.|x.--o.S.  B:........|........|........|........
bar  76  K:X.......|x.......|.....X..|..X.....  S:........|S...s...|s...S...|S.....S.  H:X.-.X.X.|x.o.x..o|o.x.XoX.|S.o--.S.  B:........|........|........|........
bar  77  K:.X...oo.|x...X...|........|..x.....  S:.....s..|S.......|S....s..|S...s.S.  H:O.OxX.X-|S.o.x-x.|S.x.XoX.|S...x-S.  B:.......b|........|........|........
bar  78  K:X.......|....X...|....X...|..X.....  S:S.......|S.s.S...|ss..S.S.|S.s.s.S.  H:X-.-X-X.|x.o.S.x-|..x.XxX.|x.-.--S.  B:........|........|........|........
bar  79  K:X..oo.o.|x.......|........|........  S:........|S.....s.|s...ss..|S.s.s.S.  H:Ox.xX.X-|S.o.x.x.|x.x-XoX.|x.-.o.S.  B:......bb|........|........|........
bar  80  K:X.......|x...X...|.....X..|..X.....  S:........|S...S...|s.......|SS.ss.S.  H:X--.X-X.|Sxo-S.xo|.-x.XxX.|x.-.-.S.  B:........|........|........|........
```

### Bars 81-88  E2 + drop-out bar   (167.2 s - 183.9 s)
- band RMS: sub -11.7 | lowmid -17.0 | mid -18.1 | 1.5-5k -25.8 | >8k -35.8 dB
- counts: kicks 38 (4.75/bar), main snares 31, full/medium hats 70, open-type 7, ghost hats 63
- microtiming vs 32nd grid (ms, + = late): kick mean -2.3 sd 17.6 (n=38) | snare mean +2.7 sd 8.0 (n=31) | hats mean +0.7 sd 7.0 (n=70)
- kick slot usage (count per 32nd slot, 0..31): 0:5 1:2 3:1 8:4 9:2 12:4 13:1 15:1 19:2 20:4 21:2 24:2 25:1 26:6 31:1
- hat velocity profile (mean >9k peak dBFS per slot, hits in >=1/2 of bars shown as slot:dB): 0:-21 2:-35 3:-33 4:-22 6:-18 10:-32 12:-27 13:-42 14:-24 16:-33 17:-38 18:-23 20:-17 21:-29 22:-17 24:-23 26:-38 28:-36 29:-40

```
bar  81  K:X.......|x...X...|....x...|o.x....o  S:s.......|SSs.....|S.s.....|S...s.S.  H:O.O.xoX.|S.o.x.x-|Sox.XoX.|x..-o-S.  B:........|........|........|........
bar  82  K:X.......|....X...|.....X..|..X.....  S:S.......|S...S...|..s.SsS.|S.s...S.  H:X.--X.X.|S.o.S-x-|-.x.XxX.|x.o.-.S.  B:........|........|........|........
bar  83  K:X..o....|.x.....x|...ox...|........  S:s.......|S.s.....|s.......|S...s.S.  H:O.OxX.X.|x.o.x.x.|oox.XoX.|x...o.S-  B:.......b|........|........|........
bar  84  K:.X......|x...X...|....X...|..X.....  S:........|S.s.....|s...s...|S...s.S.  H:X.--X.Xo|S.o.x-x.|o-x-XoX.|x.o..-S.  B:........|........|........|........
bar  85  K:X.......|x....X..|...o.x..|..x.....  S:........|S.s.s...|S.......|S...s.S.  H:OO.xX.X.|S.o.x.x.|S.x.XoX.|S.-.xoS-  B:........|........|........|........
bar  86  K:X.......|....X...|....X...|..X.....  S:........|S.s.....|s.s...S.|S...s.S.  H:X.--X.X.|x.o.x.x.|.-x-XxX.|x.o.-.S.  B:........|........|........|........
bar  87  K:.X......|x.......|........|.ox.....  S:s.......|S.s.s...|s...ss..|S...s.S.  H:O..xX.X.|S.o.x-x.|x-x.XoX.|xo..o.S-  B:...b....|........|........|........
bar  88  K:........|.x......|........|........  S:.s......|s.......|s.....S.|s.s.s.S.  H:x-..-.x.|o.o.--.o|.....xS-|x...--S.  B:........|........|........|........
```

### Bars 89-96  F outro-groove (K 1+2)   (183.9 s - 200.6 s)
- band RMS: sub -13.8 | lowmid -20.6 | mid -18.8 | 1.5-5k -26.0 | >8k -34.9 dB
- counts: kicks 19 (2.38/bar), main snares 29, full/medium hats 76, open-type 2, ghost hats 60
- microtiming vs 32nd grid (ms, + = late): kick mean +1.2 sd 15.1 (n=19) | snare mean +8.3 sd 11.6 (n=29) | hats mean +0.6 sd 6.5 (n=76)
- kick slot usage (count per 32nd slot, 0..31): 0:7 1:1 8:6 11:2 14:1 20:2
- hat velocity profile (mean >9k peak dBFS per slot, hits in >=1/2 of bars shown as slot:dB): 0:-19 3:-31 4:-16 6:-16 10:-33 12:-27 13:-41 14:-23 16:-28 18:-23 20:-16 21:-28 22:-16 26:-38 27:-42 28:-35 29:-38 30:-38

```
bar  89  K:X.......|X.......|........|........  S:........|S.s.....|ss......|S.s...S.  H:O..xX.X.|S.o.x-x.|xox-XoX.|S..--.S.  B:........|........|bbb.....|........
bar  90  K:.X......|X.......|........|........  S:........|S.s.....|s...s.S.|SS..s.S.  H:X.-.X.Xo|S.o.x.x.|..x.XxX.|S...-..-  B:........|........|........|........
bar  91  K:X.......|X..o..o.|........|........  S:........|S.s.s...|........|S...s.S.  H:x...X.X.|S.o-x.x.|x.x.X.X.|xo--ooo.  B:........|.......b|b.......|........
bar  92  K:X.......|X.......|....x...|........  S:........|S.......|s.....S.|S.s...S.  H:X---X.X.|S.o.o.x.|o.x-XxX.|x.-...S.  B:........|........|........|........
bar  93  K:X.......|X.......|........|........  S:s.......|S.......|s.......|S..sss..  H:Ox.xX-X.|S..ox.x.|x.x.X.X.|Sx.-xoo.  B:........|........|........|........
bar  94  K:X.......|X.......|........|........  S:........|S.s.....|s....s.s|S.....s.  H:X.--X.X.|S.o.--x.|..x.XxX.|S.o-.--.  B:........|........|........|........
bar  95  K:X.......|...o....|........|........  S:........|S.......|ss......|S..ss...  H:x..xX.X.|S.o-x-x.|x..-XoX.|x...ooo.  B:........|.......b|bbbb....|........
bar  96  K:X.......|........|....x...|........  S:........|S.s.....|s......s|S.....S.  H:X-..X.X-|S.o.x-x-|o.x.XxX-|S.o...S.  B:........|........|........|........
```

### Bars 97-104  OUTRO (no drums)   (200.6 s - 217.3 s)
- band RMS: sub -49.2 | lowmid -25.9 | mid -28.5 | 1.5-5k -44.1 | >8k -82.6 dB
- counts: kicks 0 (0.00/bar), main snares 0, full/medium hats 0, open-type 0, ghost hats 1
- microtiming vs 32nd grid (ms, + = late): kick mean +0.0 sd 0.0 (n=0) | snare mean +0.0 sd 0.0 (n=0) | hats mean +0.0 sd 0.0 (n=0)
- kick slot usage (count per 32nd slot, 0..31): 
- hat velocity profile (mean >9k peak dBFS per slot, hits in >=1/2 of bars shown as slot:dB): 

```
bar  97  K:........|........|........|........  S:........|........|........|........  H:-.......|........|........|........  B:........|........|........|........
bar  98  K:........|........|........|........  S:........|........|........|........  H:........|........|........|........  B:........|........|........|........
bar  99  K:........|........|........|........  S:........|........|........|........  H:........|........|........|........  B:........|........|........|........
bar 100  K:........|........|........|........  S:........|........|........|........  H:........|........|........|........  B:........|........|........|........
bar 101  K:........|........|........|........  S:........|........|........|........  H:........|........|........|........  B:........|........|........|........
bar 102  K:........|........|........|........  S:........|........|........|........  H:........|........|........|........  B:........|........|........|........
bar 103  K:........|........|........|........  S:........|........|........|........  H:........|........|........|........  B:........|........|........|........
bar 104  K:........|........|........|........  S:........|........|........|........  H:........|........|........|........  B:........|........|........|........
```

## 5. Swing / microtiming (global, bars 1-96)

- hats (X/x): all mean -0.0 ms, sd 6.9 ms (n=739); on 8ths (slots 0,4,..) -0.5 ms (n=356); on 'e'/'a' 16ths (slots 2,6,..) +1.5 ms (n=316); on 32nd off-slots -4.7 ms (n=67)
- snares (S): all mean +3.6 ms, sd 14.0 ms (n=324); on 8ths (slots 0,4,..) +6.3 ms (n=266); on 'e'/'a' 16ths (slots 2,6,..) +2.6 ms (n=36); on 32nd off-slots -26.9 ms (n=22)
- kicks: all mean -0.1 ms, sd 16.4 ms (n=322); on 8ths (slots 0,4,..) +3.1 ms (n=191); on 'e'/'a' 16ths (slots 2,6,..) +3.7 ms (n=45); on 32nd off-slots -9.3 ms (n=86)

Interpretation: offbeat 16ths are not delayed relative to on-beat 8ths, so there is no swing/shuffle; hats and snares sit within a few ms of the straight 16th grid (quantized). Kick times are click-refined (100-3000 Hz attack); their small positive mean is the kick sample's own attack ramp, not a programmed delay. Note the snare's clap sub-transients at +13-15 and +38-44 ms are part of the sample, not separate hits.

## 6. Rolls, fills and drop-outs relative to section boundaries

- bar 2 (): snare roll/fill at slots [8, 9, 24]; no kick
- bar 4 (): hat 32nd-run slots 20-22 (X-X); snare roll/fill at slots [8, 24, 24]; no kick
- bar 7 (): hat 32nd-run slots 20-22 (XoX)
- bar 8 (phrase end): hat 32nd-run slots 4-7 (XoX-); no kick
- bar 9 (): hat 32nd-run slots 2-6 (xxX-X); snare roll/fill at slots [8, 9, 24, 25]
- bar 10 (): snare roll/fill at slots [8, 8, 24, 25]
- bar 11 (): snare roll/fill at slots [8, 9, 12, 24]
- bar 12 (): snare roll/fill at slots [8, 24, 24]
- bar 13 (): snare roll/fill at slots [8, 9, 12, 24, 24]
- bar 14 (): snare roll/fill at slots [0, 8, 24]
- bar 15 (): hat 32nd-run slots 2-4 (xxX); snare roll/fill at slots [8, 9, 24, 24]
- bar 17 (): hat 32nd-run slots 16-18 (--o); snare roll/fill at slots [0, 8, 12, 24]
- bar 18 (): hat 32nd-run slots 2-4 (--X); hat 32nd-run slots 18-20 (o-X); snare roll/fill at slots [0, 8, 8, 12, 24, 24, 26]
- bar 19 (): hat 32nd-run slots 18-23 (ooX-Xo); hat 32nd-run slots 26-28 (o-o); snare roll/fill at slots [0, 8, 9, 12, 24, 24]; no kick
- bar 20 (): hat 32nd-run slots 0-4 (X--oX); hat 32nd-run slots 20-23 (xoXo); hat 32nd-run slots 26-28 (oo-); snare roll/fill at slots [8, 9, 12, 24]
- bar 21 (): snare roll/fill at slots [8, 8, 12, 24, 25]
- bar 22 (): hat 32nd-run slots 18-20 (o-X); snare roll/fill at slots [8, 8, 12, 24, 24, 26]; no kick
- bar 23 (): hat 32nd-run slots 18-20 (o-X); hat 32nd-run slots 26-29 (--o-); snare roll/fill at slots [0, 8, 9, 12, 24, 24]; no kick
- bar 24 (phrase end): hat 32nd-run slots 3-7 (-oooo); hat 32nd-run slots 22-24 (o-o); hat 32nd-run slots 26-28 (oo-); NO backbeat snare (drop-out bar); no kick
- bar 25 (): hat 32nd-run slots 19-26 (-x-X-xo-); snare roll/fill at slots [8, 24, 24]
- bar 26 (): hat 32nd-run slots 18-20 (ooX); snare roll/fill at slots [8, 20, 24, 24, 26]
- bar 27 (): hat 32nd-run slots 16-18 (-o-); snare roll/fill at slots [0, 8, 12, 24, 24]
- bar 28 (): hat 32nd-run slots 18-20 (o-X); hat 32nd-run slots 26-29 (o---); snare roll/fill at slots [8, 20, 24]
- bar 29 (): hat 32nd-run slots 18-20 (o-X); hat 32nd-run slots 26-28 (--o); snare roll/fill at slots [8, 12, 24, 25]
- bar 30 (): hat 32nd-run slots 2-4 (o-X); hat 32nd-run slots 16-18 (o-o); hat 32nd-run slots 26-28 (o-o); snare roll/fill at slots [8, 9, 12, 20, 24, 26]
- bar 31 (): hat 32nd-run slots 20-22 (X-X); snare roll/fill at slots [8, 24, 24]
- bar 32 (phrase end): hat 32nd-run slots 2-4 (o-X); snare roll/fill at slots [8, 8, 20, 24, 24, 26]
- bar 33 (): hat 32nd-run slots 0-4 (xxxxX); hat 32nd-run slots 26-28 (-oo); snare roll/fill at slots [8, 9, 24]
- bar 34 (): hat 32nd-run slots 2-4 (o-X); hat 32nd-run slots 16-18 (o-X); snare roll/fill at slots [0, 8, 16, 20, 24, 24, 26]
- bar 35 (): snare roll/fill at slots [0, 8, 12, 24]
- bar 36 (): hat 32nd-run slots 0-4 (X-o-X); snare roll/fill at slots [8, 12, 16, 24, 26]
- bar 37 (): hat 32nd-run slots 16-18 (--X); snare roll/fill at slots [8, 12, 24]
- bar 38 (): hat 32nd-run slots 2-4 (--X); hat 32nd-run slots 16-18 (o-X); hat 32nd-run slots 20-22 (XoX); snare roll/fill at slots [8, 16, 20, 24, 26]
- bar 39 (): hat 32nd-run slots 26-28 (---); snare roll/fill at slots [0, 8, 24]
- bar 40 (phrase end): hat 32nd-run slots 0-6 (X---X-X); hat 32nd-run slots 18-20 (o-x); hat 32nd-run slots 22-24 (XoX); hat 32nd-run slots 28-30 (XoX); NO backbeat snare (drop-out bar)
- bar 41 (): snare roll/fill at slots [0, 8, 8, 14, 24]
- bar 42 (): snare roll/fill at slots [8, 8, 14, 24, 30]
- bar 43 (): hat 32nd-run slots 2-4 (xxX); snare roll/fill at slots [0, 2, 8, 14, 24]
- bar 44 (): snare roll/fill at slots [2, 8, 8, 14, 24]
- bar 45 (): hat 32nd-run slots 26-28 (Xox); snare roll/fill at slots [2, 8, 14, 24]
- bar 46 (): hat 32nd-run slots 10-12 (X-X); snare roll/fill at slots [2, 8, 14, 24, 24]
- bar 47 (): hat 32nd-run slots 2-4 (xxo); hat 32nd-run slots 20-22 (X-X); snare roll/fill at slots [2, 8, 14, 24, 24]
- bar 48 (phrase end): snare roll/fill at slots [2, 8, 8, 14, 24, 26, 28]
- bar 49 (): hat 32nd-run slots 2-4 (xxx); snare roll/fill at slots [8, 8, 14, 24, 24]
- bar 51 (): snare roll/fill at slots [0, 8, 9, 24]
- bar 52 (): hat 32nd-run slots 26-28 (X-X); snare roll/fill at slots [2, 8, 14, 24, 24]
- bar 53 (): hat 32nd-run slots 3-6 (xX-X); snare roll/fill at slots [2, 8, 9, 12, 14, 24]
- bar 55 (): snare roll/fill at slots [0, 8, 8, 14, 24, 24]
- bar 56 (phrase end): hat 32nd-run slots 26-28 (X-X); snare roll/fill at slots [2, 8, 14, 18, 20, 24, 26, 28, 30, 30]; no kick
- bar 58 (): hat 32nd-run slots 2-4 (--X); snare roll/fill at slots [0, 8, 14, 16, 24, 24]
- bar 59 (): hat 32nd-run slots 24-26 (x--); snare roll/fill at slots [0, 8, 12, 24]
- bar 60 (): hat 32nd-run slots 0-2 (X--); hat 32nd-run slots 16-18 (o-x); hat 32nd-run slots 20-22 (X-X); hat 32nd-run slots 24-26 (xo-); snare roll/fill at slots [8, 12, 24, 24, 26]
- bar 61 (): snare roll/fill at slots [8, 24, 24]
- bar 62 (): hat 32nd-run slots 16-18 (oox); snare roll/fill at slots [8, 12, 24, 24]
- bar 63 (): hat 32nd-run slots 20-22 (X-X); hat 32nd-run slots 26-29 (----); snare roll/fill at slots [8, 12, 21, 24, 27]
- bar 64 (phrase end): hat 32nd-run slots 2-4 (o-X); hat 32nd-run slots 16-18 (o-x)
- bar 65 (): hat 32nd-run slots 26-28 (--o); snare roll/fill at slots [8, 12, 24]
- bar 66 (): hat 32nd-run slots 3-6 (-X-X); hat 32nd-run slots 16-18 (--x); hat 32nd-run slots 20-22 (X-X); snare roll/fill at slots [8, 10, 12, 14, 24, 24]
- bar 67 (): hat 32nd-run slots 2-4 (xxX); snare roll/fill at slots [8, 8, 12, 24]
- bar 69 (): hat 32nd-run slots 25-29 (o--x-); snare roll/fill at slots [8, 8, 24]
- bar 70 (): hat 32nd-run slots 2-4 (--X); snare roll/fill at slots [8, 9, 12, 24, 25]
- bar 71 (): hat 32nd-run slots 6-9 (X-xx); hat 32nd-run slots 18-20 (x-X); hat 32nd-run slots 26-28 (--o); snare roll/fill at slots [0, 8, 16, 21, 21, 24, 26]
- bar 72 (phrase end): hat 32nd-run slots 6-8 (--o); hat 32nd-run slots 27-29 (---); NO backbeat snare (drop-out bar)
- bar 73 (): hat 32nd-run slots 16-18 (xox); hat 32nd-run slots 20-22 (XoX); snare roll/fill at slots [8, 10, 12, 16, 24, 26, 28, 30]
- bar 74 (): hat 32nd-run slots 20-22 (XxX); snare roll/fill at slots [8, 11, 12, 14, 20, 24, 26, 28, 30]
- bar 75 (): hat 32nd-run slots 2-4 (xxX); hat 32nd-run slots 16-18 (x-x); hat 32nd-run slots 20-22 (XoX); hat 32nd-run slots 26-28 (--o); snare roll/fill at slots [0, 8, 10, 12, 16, 17, 24, 25, 30]
- bar 76 (): hat 32nd-run slots 20-22 (XoX); hat 32nd-run slots 26-28 (o--); snare roll/fill at slots [8, 12, 16, 20, 24, 24, 30]
- bar 77 (): hat 32nd-run slots 12-14 (x-x); hat 32nd-run slots 20-22 (XoX); snare roll/fill at slots [5, 8, 16, 21, 24, 28, 30]
- bar 78 (): hat 32nd-run slots 3-6 (-X-X); hat 32nd-run slots 20-22 (XxX); snare roll/fill at slots [0, 8, 10, 12, 16, 17, 20, 22, 24, 26, 28, 30]
- bar 79 (): hat 32nd-run slots 18-22 (x-XoX); snare roll/fill at slots [8, 14, 16, 20, 21, 21, 24, 26, 28, 30]
- bar 80 (phrase end): hat 32nd-run slots 0-2 (X--); hat 32nd-run slots 4-6 (X-X); hat 32nd-run slots 9-11 (xo-); hat 32nd-run slots 20-22 (XxX); snare roll/fill at slots [8, 12, 16, 24, 25, 27, 28, 30]
- bar 81 (): hat 32nd-run slots 4-6 (xoX); hat 32nd-run slots 20-22 (XoX); hat 32nd-run slots 27-29 (-o-); snare roll/fill at slots [0, 8, 9, 10, 16, 18, 24, 28, 28, 30]
- bar 82 (): hat 32nd-run slots 2-4 (--X); hat 32nd-run slots 13-16 (-x--); hat 32nd-run slots 20-22 (XxX); snare roll/fill at slots [0, 8, 12, 18, 20, 21, 22, 24, 26, 30]
- bar 83 (): hat 32nd-run slots 16-18 (oox); hat 32nd-run slots 20-22 (XoX); snare roll/fill at slots [0, 8, 10, 16, 24, 28, 30]
- bar 84 (): hat 32nd-run slots 2-4 (--X); hat 32nd-run slots 12-14 (x-x); hat 32nd-run slots 16-22 (o-x-XoX); snare roll/fill at slots [8, 10, 16, 20, 24, 28, 30]
- bar 85 (): hat 32nd-run slots 20-22 (XoX); snare roll/fill at slots [8, 10, 12, 16, 24, 28, 30]
- bar 86 (): hat 32nd-run slots 2-4 (--X); hat 32nd-run slots 17-22 (-x-XxX); snare roll/fill at slots [8, 10, 16, 18, 22, 24, 28, 30]
- bar 87 (): hat 32nd-run slots 12-14 (x-x); hat 32nd-run slots 16-18 (x-x); hat 32nd-run slots 20-22 (XoX); snare roll/fill at slots [0, 8, 10, 12, 16, 20, 21, 24, 28, 30]
- bar 88 (phrase end): snare roll/fill at slots [1, 8, 16, 22, 24, 26, 28, 30]
- bar 89 (): hat 32nd-run slots 12-14 (x-x); hat 32nd-run slots 16-22 (xox-XoX); snare roll/fill at slots [8, 10, 16, 17, 24, 26, 30]
- bar 90 (): hat 32nd-run slots 20-22 (XxX); snare roll/fill at slots [8, 8, 10, 16, 20, 22, 24, 25, 28, 30]
- bar 91 (): hat 32nd-run slots 10-12 (o-x); hat 32nd-run slots 24-30 (xo--ooo); snare roll/fill at slots [8, 10, 12, 24, 28, 30]
- bar 92 (): hat 32nd-run slots 0-4 (X---X); hat 32nd-run slots 18-22 (x-XxX); snare roll/fill at slots [8, 16, 22, 24, 26, 30]
- bar 93 (): hat 32nd-run slots 3-6 (xX-X); hat 32nd-run slots 27-30 (-xoo); snare roll/fill at slots [0, 8, 8, 16, 24, 24, 27, 28, 29]
- bar 94 (): hat 32nd-run slots 2-4 (--X); hat 32nd-run slots 12-14 (--x); hat 32nd-run slots 20-22 (XxX); snare roll/fill at slots [8, 10, 16, 21, 23, 24, 30]
- bar 95 (): hat 32nd-run slots 10-14 (o-x-x); hat 32nd-run slots 19-22 (-XoX); hat 32nd-run slots 28-30 (ooo); snare roll/fill at slots [8, 8, 16, 17, 24, 27, 28]
- bar 96 (phrase end): hat 32nd-run slots 12-16 (x-x-o); hat 32nd-run slots 20-23 (XxX-); snare roll/fill at slots [8, 10, 16, 23, 23, 24, 24, 30]

## 7. Does the kick pattern change between sections?  Yes - summary of the modal 2-bar loop per section

- bars 1-8 INTRO: odd-bar K `X.......|........|........|........` (2/4), even-bar K `........|........|........|........` (4/4); odd H `O..xX.X-|S.......|....XoX.|S.......` (1), even H `X...X.X.|S.......|....X.X.|S.......` (1); S odd `........|S.......|........|S.......` even `........|S.......|........|S.......`
- bars 9-16 A1 verse-build: odd-bar K `X.......|....X...|........|........` (3/4), even-bar K `X.......|....X...|........|........` (3/4); odd H `xOxxX-X.|S...-...|....X.X.|S.......` (1), even H `X...X.X.|S...-...|....X.X-|S.......` (1); S odd `........|SS......|........|SS......` even `........|S.......|........|S.......`
- bars 17-24 A2 build / drop-out: odd-bar K `X.......|........|........|........` (2/4), even-bar K `........|........|........|........` (2/4); odd H `x...X.X.|S...-...|--o.X.X.|S.-.--..` (1), even H `X.--X.X.|S...-...|-.o-X.X.|S.-o.-..` (1); S odd `s.......|S...s...|........|S.......` even `S.......|S...s...|........|S.s.....`
- bars 25-32 B1 main loop: odd-bar K `X.......|x...X...|.....x..|........` (1/4), even-bar K `X.......|....X...|.....X..|...X....` (1/4); odd H `xO.xX.X.|S...-...|--.-x-X-|xo-.oo..` (1), even H `X-.-X.Xo|S...-...|o.ooX.X.|S.S-o...` (1); S odd `........|S.......|........|S.......` even `........|S.......|....S...|S.S.....`
- bars 33-40 B2 main loop, busier hats: odd-bar K `X.......|x...X...|...o.xx.|xox...oo` (1/4), even-bar K `X.......|x...X...|....X...|..X.....` (1/4); odd H `xxxxX.X.|S...X.X.|-.X.X.X.|S.-oo...` (1), even H `X.o-X.X.|S...X.X.|o-X.X.X.|S.So.o..` (1); S odd `........|SS......|........|S.......` even `S.......|S.......|s...S...|S.S.....`
- bars 41-48 C1 verse (16th-run hats): odd-bar K `........|....X...|........|........` (2/4), even-bar K `X.......|o...X...|....X...|..X.....` (2/4); odd H `O..xX.X.|S.X.X-..|....X.X.|SoX.X...` (1), even H `o...X.X.|S.x.X...|....x.x.|S.X.X...` (1); S odd `..s.....|S.....s.|........|S.......` even `..s.....|S.....s.|........|S.......`
- bars 49-56 C2 verse + fill: odd-bar K `X..o....|........|........|....o...` (2/4), even-bar K `.X......|o...X...|....X...|..X.....` (1/4); odd H `x.xxx.X.|S.X.X...|....X.X.|S.X.X...` (1), even H `-...X.X.|S.x.X-..|....X.X.|S.X.X...` (1); S odd `........|S.....s.|........|S.......` even `........|S.....s.|........|S.......`
- bars 57-64 D1 (hats fill in 2&/2a): odd-bar K `X.......|x...X...|...ox...|o..x....` (1/4), even-bar K `.X......|....X...|........|........` (1/4); odd H `xxxxX.X.|S.-.x.o.|--x.X.X.|x.--.-..` (1), even H `X.--X.X.|S...x.x.|-.x.X.X.|S.o-.-..` (1); S odd `........|S.......|........|S.......` even `S.......|S.....s.|s.......|S.......`
- bars 65-72 D2 + drop-out bar: odd-bar K `X....o..|x....X..|.....x..|..x...oo` (1/4), even-bar K `X.......|.....X..|........|........` (1/4); odd H `Ox..X.X.|x...S.x.|x.x.X.X.|S.--o.-.` (1), even H `X..-X-X.|So..S.x.|--x.X-X.|S.-o.-..` (1); S odd `........|S...S...|........|S.......` even `........|S.s.S.s.|........|S.......`
- bars 73-80 E1 densest hats: odd-bar K `X.......|x..x.X..|..o.ox..|..x.....` (1/4), even-bar K `X.......|....X...|....X...|..X.....` (2/4); odd H `xO.xX.X.|So.oS-x.|xox.XoX.|S...o.S.` (1), even H `X-.-X.X.|S.o.S.x.|-.x.XxX.|x.S.-.o.` (1); S odd `........|S.s.S...|s.......|S.s.s.S.` even `........|S..sS.s.|....s...|S.S.s.s.`
- bars 81-88 E2 + drop-out bar: odd-bar K `X.......|x...X...|....x...|o.x....o` (1/4), even-bar K `X.......|....X...|.....X..|..X.....` (1/4); odd H `O.O.xoX.|S.o.x.x-|Sox.XoX.|x..-o-S.` (1), even H `X.--X.X.|S.o.S-x-|-.x.XxX.|x.o.-.S.` (1); S odd `s.......|SSs.....|S.s.....|S...s.S.` even `S.......|S...S...|..s.SsS.|S.s...S.`
- bars 89-96 F outro-groove (K 1+2): odd-bar K `X.......|X.......|........|........` (2/4), even-bar K `.X......|X.......|........|........` (1/4); odd H `O..xX.X.|S.o.x-x.|xox-XoX.|S..--.S.` (1), even H `X.-.X.Xo|S.o.x.x.|..x.XxX.|S...-..-` (1); S odd `........|S.s.....|ss......|S.s...S.` even `........|S.s.....|s...s.S.|SS..s.S.`
