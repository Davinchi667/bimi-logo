# EVERYWHERE I GO [REMIND ME] (BNYX, Kid Cudi) - drum programming, measured from the instrumental

Source: `refs/eig_inst.wav` (44.1 kHz stereo, 3:37.3). Every statement below is a measurement on that file (confidence noted where it is an interpretation of a measurement). Nothing was listened to. Machine-readable outputs next to this file: `drums_hits.csv` (every hit: instrument, class, time, bar, 32nd slot, deviation from grid, level, decay), `drums_hits.json`, `drums_measured.mid` (kick 36, clap 39, closed hat 42, open-type 46, velocities from measured levels, quantized to the grid at 115 BPM), and `val_b*.png` (band envelopes with detections, two bars each).

## 0. Grid - this corrects the brief (high confidence, measured)

- Tempo: **115.000 BPM**, not 114.84. A phase-concentration fit of transient onsets in each band (sub, kick, snare, hat) against 8th/16th/32nd periods over bars 1-96 peaks at 115.000 +/- 0.005 BPM in every band. 114.84 drifts 2.7 ms per bar (66 ms by bar 25), which is why the 808 looked ~0.2 s late on the old grid.
- Bar 1 beat 1 = **0.277 s** (the first transient in the file, a full-band stab at -3 dBFS, preceded by digital silence). The brief's 0.813 s is beat 2 of bar 1. On the 0.813 grid the snare fell on beats 1 and 3 and the first kick (4.451 s) on bar 2 beat 4; on the 0.277 grid the snare is on 2 and 4 and the first kick is bar 3 beat 1, and every section change lands on an 8-bar boundary.
- 1 beat = 521.74 ms, 1 bar = 2086.96 ms, 16th = 130.43 ms, 32nd = 65.22 ms. 104 bars total; drums play bars 1-96 (0.277 s to 200.6 s); bars 97-104 are the sample alone.
- Feel: a 115 BPM **backbeat groove (snare on 2 and 4), straight 16ths, fully quantized, no swing** (section 4). It is not a halftime trap grid.

Grid notation: 32 slots per bar, `|` every beat (8 slots per beat, 2 slots per 16th). Slot 0 = beat 1, 2 = 1e, 4 = 1&, 6 = 1a, 8 = beat 2, ... 24 = beat 4, 30 = 4a. Odd slots are 32nd positions.
- K (kick): `X` sub peak >= -3 dBFS (full), `x` -3..-9, `o` -9..-12.5. Kicks are placed on the 16th grid (no kick was found off it; the sub band's slow attack makes 32nd-level kick timing unreliable, so kick timing is reported from the attack click instead).
- S (clap): `S` = the clap sample (1.5-5 kHz peak >= -12 dBFS with the clap's spectrum: mid body, >9 kHz 8-19 dB below the 1.5-5 kHz peak). No quieter hit in the track matched the clap's envelope fingerprint, so there are no ghost claps.
- G (not a drum): every other 1.5-5 kHz transient >= -17.5 dBFS that is not a kick click, a hat or the clap (`G` >= -12 dBFS, `g` below). Spectrally these are low-mid heavy with little or no >9 kHz content: the sampled chop/stab layer. Listed so their positions are known; they belong to the sample/chop task.
- H (hats, >9 kHz band): `O` open-hat/crash-type (300 ms plateau), `X` closed hat >= -20 dBFS (full velocity, the accents are -16/-17), `x` -20..-28, `o` -28..-37, `-` -37..-48 (faint; these are the sample's own hi-hat, see 1.6), `S` = the clap's own HF on the backbeat (a hat under the clap cannot be confirmed either way).
- B: onset of a sustained 808 bass note that is clearly separate from a kick (partial list; the bass is the bass task's job).

## 1. The drum sounds (measured)

1.1 **Kick** (one sample throughout; high confidence). Isolated in the intro at 4.451 s and 12.800 s (bar 3 and bar 7 beat 1): a sub-heavy 808-style kick about 200 ms long. 25-250 Hz envelope: peak 0 dBFS, -6 dB at 75-93 ms, -10 dB at 115-122 ms, -20 dB at 163-178 ms, -30 dB at ~205 ms, inaudible by ~220 ms. Pitch (zero-crossing in a 25-150 Hz band): ~90 Hz in the first 20 ms, 44 Hz at 20-40 ms, 43 Hz at 40-60 ms, then ~41 Hz (E1 = 41.2 Hz) until it dies: i.e. a 90 Hz -> 41 Hz sweep over ~40 ms. Attack has a broadband click (100-3000 Hz rises 25-35 dB within 1 ms). It is tuned to E, the track's key. Full-velocity hits peak 0 to +0.8 dBFS in the sub band, 0 dBFS in 70-200 Hz, and read 38-43 Hz at +80 ms. One softer variant exists: beat 2 (under the clap) of bars 28, 32, 36, 44, 46, 52, 54, ... carries an E1-pitched hit at -5..-6 dBFS sub / -5..-9 dBFS 70-200 Hz, i.e. the same kick at roughly half velocity.

1.2 **808 bass, and why the odd-bar 'kicks' on 2 and 3& are not kicks** (medium-high confidence). A second low instrument sustains under the main loop (bars 9-96): ~11 dB below the kick, > 800 ms long, no click, pitched ~31-33 Hz (B0/C1) in odd bars and ~46-47 Hz (F#1) in even bars (sub pitch measured 200 ms after the hits). In odd bars there are additional sub hits on beat 2, 3& and 4e (slots 8, 20, 26) peaking -4 to -6 dBFS: they have no kick body (70-200 Hz at -8 to -14 dBFS, versus 0 dBFS for the kick and -19..-22 for the clap alone), no stable E1 pitch (zero-crossing pitch fails at +40/+80 ms and reads ~31 Hz at +150 ms), so they are retriggers of the B0/C1 bass note, not the kick. On beat 2 of even bars the same kind of hit alternates every 4 bars: F#1-pitched (46 Hz) bass retrigger in bars 26, 30, 34, 38 and an E1-pitched soft kick in bars 28, 32, 36 (see 1.1). The bass retriggers are on the B line (together with the other bass onsets that are clearly separate from a kick); program them in the 808 bass part, not the drum part.

1.3 **Snare = clap** (high confidence). The 1.5-5 kHz band shows 4-5 sub-transients spread over 0-45 ms (strongest at +13-15 ms and +38-44 ms after the first), i.e. a layered clap. Peak -6 to -9 dBFS in 1.5-5 kHz, mid body 600-1500 Hz at -5.5 dBFS (louder than its top), 200-600 Hz at -12, >9 kHz only -23 to -25 dBFS. Smoothed-envelope decay (1.5-5 kHz): -10 dB at 31 ms, -20 dB at 64 ms, -30 dB at 119 ms (median over 182 backbeats). Its first transient is on the grid (mean +0.1 ms).

1.4 **Closed hat** (high confidence). >9 kHz peak -16 to -17 dBFS on the accents; smoothed-envelope decay -10 dB at 29 ms, -20 dB at 50 ms, -30 dB at 73 ms (median over the 1& hats): a medium-length closed hat, not a tight tick. Accents (1&, 1a, 3&, 3a) are at -16/-17 in every section; added 16ths sit 7-9 dB lower (-24/-25) and the 2e in sections E/F sits 15 dB lower (-31). See the per-section velocity tables.

1.5 **Open-hat / crash-type hit on beat 1 of odd bars** (medium confidence on what it is, high on where it is). Present on beat 1 of EVERY odd bar 1-95, in every section: the mean >9 kHz level 60-250 ms after the odd-bar downbeat is -30.5 to -31.1 dBFS in all eight sections with a standard deviation of 0.1-0.2 dB (same sample every time); after even-bar downbeats the same window reads -85 dB (intro/A), -51 dB (B, D, E, F: only the sample's ghost hats) or -95 dB (C). Shape: a -22 to -25 dBFS peak, then a plateau around -30 dBFS for ~300 ms (smoothed: -6 dB at 276 ms, -10 dB at 288 ms, -20 dB at 307 ms). In the grids it appears at slot 0 of odd bars as `O` or, where its peak reads below -20 dBFS, as `x`; the plateau measurement is the reliable indicator. It is what makes odd bars ~2 dB louder than even bars above 8 kHz. Even bars get a normal closed hat (-16..-20) on beat 1 instead (not in C, where the even-bar downbeat hat is absent).

1.6 **Ghost 32nd 'rolls' at -37 to -48 dBFS** (slots 16-19 and 26-29, sometimes 1-3 and 12): these continue unchanged through the drop-out bars (24, 56, 72, 88) where the programmed drums stop, so they are the hi-hat/shaker inside the Royksopp sample, not programmed hats (high confidence). They are shown as `o`/`-` so you can see them, but you do not need to program them: they come with the sample.

1.7 **No separate percussion layer** could be isolated (rim, shaker, perc one-shots). The dense 600-1500 Hz onsets on every 16th in every section are the sample's arpeggio (50% land on even/16th slots and 50% on odd/32nd slots, i.e. not a drum grid). The only non-kick/clap/hat transients that pass a -17.5 dBFS threshold in 1.5-5 kHz are low-mid-heavy (200-600 Hz at -7..-11 dBFS, 600-1500 at -12..-16, >9 kHz 23 dB or more below the 1.5-5 kHz peak) and sit at 1e (slot 2) in section C, at 2& (slot 12) in A, and all over the second half of the bar in sections E/F with the loudest one on 4a (slot 30, -11..-12 dBFS): these are the sampled chops/stabs, listed on the G line. They do not match the clap's envelope fingerprint (correlation ~0 vs 0.6 for the backbeats).

## 2. Section map and grids

Boundaries come from per-bar band RMS (`bar_band_rms.txt`) and pattern changes; every boundary is an 8-bar multiple on the 0.277 s grid. Band RMS below is the mean over the section in dBFS (mono): sub <80 Hz / 150-400 / 400-1.5k / 1.5-5k / >8k.

### Bars 1-8  (0.3 s - 17.0 s)  INTRO: hats + backbeat, one-shot kick on beat 1 of odd bars
- band RMS: sub -28.3 | 150-400 -21.6 | 400-1.5k -23.0 | 1.5-5k -28.6 | >8k -35.6
- counts: kicks 3 (0.38/bar), main claps 16, programmed hats (X/x) 37, open-type 2
- timing vs 32nd grid (ms, + = late; kick from its click where unmasked): kick +3.2 (sd 0.1, n=2) | clap -0.7 (sd 0.6, n=16) | hats -0.2 (sd 1.7, n=37)
- modal odd bar: K `X.......|........|........|........` (3/4 bars)  H `x...X.X.|S.......|....X.X.|S.......` (2/4)  S `........|S.......|........|S.......` (4/4)
- modal even bar: K `........|........|........|........` (4/4 bars)  H `X...X.X.|S.......|....X.X.|S.......` (4/4)  S `........|S.......|........|S.......` (4/4)
- hat level by slot (median >9k peak dBFS, slots hit in at least half the bars): 0:-19 4:-16 6:-16 20:-16 22:-17

```
bar   1  K:X.......|........|........|........  S:........|S.......|........|S.......  H:O...X.X.|S.......|....X.X.|S.......  G:........|........|........|........  B:........|........|........|........
bar   2  K:........|........|........|........  S:........|S.......|........|S.......  H:X...X.X.|S.......|....X.X.|S.......  G:........|........|........|........  B:........|........|........|........
bar   3  K:X.......|........|........|........  S:........|S.......|........|S.......  H:x...X.X.|S.......|....X.X.|S.......  G:g.......|........|........|........  B:........|........|........|........
bar   4  K:........|........|........|........  S:........|S.......|........|S.......  H:X...X.X.|S.......|....X.X.|S.......  G:........|........|........|........  B:........|........|........|........
bar   5  K:........|........|........|........  S:........|S.......|........|S.......  H:x...X.X.|S.......|....X.X.|S.......  G:g.......|........|........|........  B:b.......|........|........|........
bar   6  K:........|........|........|........  S:........|S.......|........|S.......  H:X...X.X.|S.......|....X.X.|S.......  G:........|........|........|........  B:........|........|........|........
bar   7  K:X.......|........|........|........  S:........|S.......|........|S.......  H:O.....X.|S.......|....X.X.|S.......  G:g.......|........|........|........  B:........|........|........|........
bar   8  K:........|........|........|........  S:........|S.......|........|S.......  H:X...X.X.|S.......|....X.X.|S.......  G:........|........|........|........  B:........|........|........|........
```

### Bars 9-16  (17.0 s - 33.7 s)  A: kick on 1 and 2&, 808 bass enters
- band RMS: sub -15.6 | 150-400 -21.1 | 400-1.5k -23.4 | 1.5-5k -28.5 | >8k -35.7
- counts: kicks 13 (1.62/bar), main claps 16, programmed hats (X/x) 39, open-type 1
- timing vs 32nd grid (ms, + = late; kick from its click where unmasked): kick -1.0 (sd 6.8, n=12) | clap -0.6 (sd 0.8, n=16) | hats -0.4 (sd 1.8, n=39)
- modal odd bar: K `........|....X...|........|........` (2/4 bars)  H `x...X.X.|S...-...|....X.X.|S.......` (2/4)  S `........|S.......|........|S.......` (4/4)
- modal even bar: K `X.......|....X...|........|........` (4/4 bars)  H `X...X.X.|S...-...|....X.X.|S.......` (2/4)  S `........|S.......|........|S.......` (4/4)
- hat level by slot (median >9k peak dBFS, slots hit in at least half the bars): 0:-20 4:-16 6:-16 12:-38 20:-16 22:-16

```
bar   9  K:........|....X...|........|........  S:........|S.......|........|S.......  H:x...X.X.|S...-...|....X.X.|S.......  G:g.......|....g...|........|........  B:b.......|........|........|........
bar  10  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:X...X.X.|S...-...|....X.X.|S.......  G:........|....g...|........|........  B:........|........|........|........
bar  11  K:........|....X...|........|........  S:........|S.......|........|S.......  H:x...X.X.|S...o...|....X.X.|S.......  G:g.......|....G...|........|........  B:b.......|........|........|........
bar  12  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:X...X.X.|S.......|....X.X.|S.......  G:g.......|....g...|........|........  B:........|........|........|........
bar  13  K:X.......|........|........|........  S:........|S.......|........|S.......  H:O...X.X.|S...-...|....X.X.|S.......  G:g.......|....g...|........|........  B:........|.....b..|........|........
bar  14  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:x...X.X.|S.......|....X.X.|S.......  G:G.......|....g...|........|........  B:........|........|........|........
bar  15  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:x...X.X.|S...-...|....X.X.|S.......  G:g.......|....g...|........|........  B:........|........|........|........
bar  16  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:X...X.X.|S...-...|....X.X.|S.......  G:........|....g...|........|........  B:........|........|........|........
```

### Bars 17-24  (33.7 s - 50.4 s)  A2: kick thins out (bass carries), bar 24 drop-out + riser
- band RMS: sub -17.3 | 150-400 -21.2 | 400-1.5k -23.4 | 1.5-5k -28.8 | >8k -37.4
- counts: kicks 19 (2.38/bar), main claps 14, programmed hats (X/x) 35, open-type 0
- timing vs 32nd grid (ms, + = late; kick from its click where unmasked): kick -0.9 (sd 6.5, n=16) | clap -0.3 (sd 0.3, n=14) | hats -0.4 (sd 1.4, n=35)
- modal odd bar: K `X.......|....X...|........|........` (3/4 bars)  H `x...X.X.|S...-...|-.o.X.X.|S.-.-...` (1/4)  S `........|S.......|........|S.......` (4/4)
- modal even bar: K `X.......|....X...|....X...|..X.....` (2/4 bars)  H `X.--X.X.|S...-...|-.o.X.X.|S.-o.-..` (1/4)  S `........|S.......|........|S.......` (3/4)
- hat level by slot (median >9k peak dBFS, slots hit in at least half the bars): 0:-21 4:-17 6:-16 12:-38 16:-37 18:-36 20:-16 22:-16 26:-37 27:-36 28:-36

```
bar  17  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:x...X.X.|S...-...|-.o.X.X.|S.-.-...  G:g.......|........|........|........  B:........|........|........|........
bar  18  K:X.......|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:X.--X.X.|S...-...|-.o.X.X.|S.-o.-..  G:........|........|........|........  B:........|........|........|........
bar  19  K:x.......|....X...|........|........  S:........|S.......|........|S.......  H:x...X.X.|S...-...|o.ooX.Xo|S.o.o...  G:g.......|........|........|........  B:........|........|........|........
bar  20  K:X.......|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:X.-oX.X.|S...-...|-.o.x.X.|S.oo....  G:........|........|........|........  B:........|........|........|........
bar  21  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:x...X.Xo|S...-...|oo..X.X.|S.-.o...  G:........|........|........|........  B:........|........|........|........
bar  22  K:........|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:X.o-X.X.|S...-...|o.o.X.X.|S.ooo...  G:........|........|........|........  B:........|........|........|........
bar  23  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:x...X.X.|S.......|o.o-X.X.|S.--o-..  G:........|........|........|........  B:........|........|........|........
bar  24  K:........|........|........|........  S:........|........|........|........  H:o-..oooo|........|o.....o.|o.oo....  G:........|........|........|......g.  B:........|........|........|........
```

### Bars 25-32  (50.4 s - 67.1 s)  B1: full 2-bar kick loop
- band RMS: sub -11.0 | 150-400 -21.1 | 400-1.5k -23.0 | 1.5-5k -28.6 | >8k -35.7
- counts: kicks 25 (3.12/bar), main claps 16, programmed hats (X/x) 40, open-type 1
- timing vs 32nd grid (ms, + = late; kick from its click where unmasked): kick +1.5 (sd 9.7, n=19) | clap -0.5 (sd 0.5, n=16) | hats +0.8 (sd 4.3, n=40)
- modal odd bar: K `X.......|....X...|........|........` (3/4 bars)  H `x...X.X.|S...-...|-.-.x.X-|x.-.oo..` (1/4)  S `........|S.......|........|S.......` (4/4)
- modal even bar: K `X.......|....X...|....X...|..X.....` (3/4 bars)  H `X-..X.X.|S...-...|o.ooX.X.|S.o.o...` (1/4)  S `........|S.......|........|S.......` (4/4)
- hat level by slot (median >9k peak dBFS, slots hit in at least half the bars): 0:-19 4:-16 6:-16 12:-38 16:-37 18:-35 20:-18 22:-16 26:-37 28:-34

```
bar  25  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:x...X.X.|S...-...|-.-.x.X-|x.-.oo..  G:........|........|........|........  B:........|b.......|....b...|........
bar  26  K:X.......|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:X-..X.X.|S...-...|o.ooX.X.|S.o.o...  G:........|........|........|........  B:........|........|........|........
bar  27  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:O...X.X.|S...-...|-o..X.X.|S.ooo...  G:........|....g...|........|........  B:....b...|b.......|.....b..|..b.....
bar  28  K:X.......|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:X.o.X.X.|S...-...|o.o.X.X.|S.o.....  G:........|........|........|........  B:........|b.......|........|........
bar  29  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:x.....X.|S.......|-.o.X.X.|S.-.o...  G:........|........|........|........  B:.....bbb|b......b|.....b..|..b....b
bar  30  K:X.......|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:X.o.X.X.|x.......|o-o.X.X.|S.o.o...  G:........|........|........|........  B:........|........|........|........
bar  31  K:X.......|x.......|........|........  S:........|S.......|........|S.......  H:x...X.X.|S.......|-.o.X.X.|S.-o.-..  G:........|....g...|........|........  B:....b.b.|........|........|........
bar  32  K:X.......|x...X...|....X...|..X.....  S:........|S.......|........|S.......  H:X.o-X.X.|S...-...|--..x.X.|S.o-....  G:........|........|........|........  B:........|........|........|........
```

### Bars 33-40  (67.1 s - 83.8 s)  B2: same loop, hats add 2& 2a, bar 40 open-hat bar
- band RMS: sub -11.0 | 150-400 -21.3 | 400-1.5k -21.1 | 1.5-5k -28.6 | >8k -34.2
- counts: kicks 24 (3.00/bar), main claps 14, programmed hats (X/x) 67, open-type 2
- timing vs 32nd grid (ms, + = late; kick from its click where unmasked): kick -0.8 (sd 6.8, n=23) | clap +1.5 (sd 6.4, n=14) | hats +1.0 (sd 3.4, n=67)
- modal odd bar: K `X.......|....X...|........|........` (4/4 bars)  H `x...X.X.|S...X.X.|-.X.X.X.|S.-oo...` (1/4)  S `........|S.......|........|S.......` (4/4)
- modal even bar: K `X.......|....X...|....X...|..X.....` (2/4 bars)  H `X.o.X.X.|S...X.X.|ooX.X.X.|S.oo.o..` (1/4)  S `........|S.......|........|S.......` (3/4)
- hat level by slot (median >9k peak dBFS, slots hit in at least half the bars): 0:-20 4:-17 6:-16 12:-17 14:-16 16:-35 18:-16 20:-16 22:-17 26:-37 28:-37

```
bar  33  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:x...X.X.|S...X.X.|-.X.X.X.|S.-oo...  G:........|........|........|........  B:........|b.......|...bbb.b|b.bb..b.
bar  34  K:X.......|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:X.o.X.X.|S...X.X.|ooX.X.X.|S.oo.o..  G:........|........|g.......|........  B:........|b.......|........|........
bar  35  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:O.....X.|S...X.X.|-.X.X.X.|x.o.o...  G:........|........|........|........  B:...b....|b.......|.....b..|........
bar  36  K:X.......|x.......|....X...|..X.....  S:........|S.......|........|S.......  H:X.o.X.X.|x...X.X.|o.X.X.X.|S.o.-o..  G:........|........|g.......|........  B:........|........|........|........
bar  37  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:O...X.X.|S...X.x.|-.X.X.X.|S.o.-...  G:........|........|........|........  B:......b.|b.......|..bbb...|...b....
bar  38  K:X.......|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:X.-.X.X.|S...X.X.|o.X.X.X.|S.o.....  G:........|........|g.......|........  B:........|........|........|........
bar  39  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:x...X.X.|S...X.X.|o.X.X.X.|S.-.-...  G:........|........|........|........  B:....b...|b.......|........|..b.....
bar  40  K:X.......|X.......|X.......|X.......  S:........|........|........|........  H:X...X.X.|X...X.X.|X.o.x.X.|X.-.X.X.  G:........|........|........|........  B:........|........|........|........
```

### Bars 41-48  (83.8 s - 100.5 s)  C1: 16th-run hats, kick thins on odd bars, bar 48 snare fill
- band RMS: sub -12.8 | 150-400 -19.8 | 400-1.5k -23.7 | 1.5-5k -28.8 | >8k -34.6
- counts: kicks 22 (2.75/bar), main claps 18, programmed hats (X/x) 62, open-type 3
- timing vs 32nd grid (ms, + = late; kick from its click where unmasked): kick -0.9 (sd 8.5, n=20) | clap -0.6 (sd 0.7, n=18) | hats -0.2 (sd 1.6, n=62)
- modal odd bar: K `X.......|....X...|........|........` (4/4 bars)  H `O...X.X.|S.X.X...|....X.X.|S.X.X...` (1/4)  S `........|S.......|........|S.......` (4/4)
- modal even bar: K `X.......|....X...|....X...|..X.....` (2/4 bars)  H `o...X.X.|S.x.X...|....x.x.|S.X.X...` (1/4)  S `........|S.......|........|S.......` (3/4)
- hat level by slot (median >9k peak dBFS, slots hit in at least half the bars): 0:-23 4:-16 6:-16 10:-17 12:-16 20:-16 22:-17 26:-16 28:-17

```
bar  41  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:O...X.X.|S.X.X...|....X.X.|S.X.X...  G:........|......g.|........|........  B:....b...|........|........|.....b..
bar  42  K:X.......|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:o...X.X.|S.x.X...|....x.x.|S.X.X...  G:........|......g.|........|......g.  B:........|b.......|........|b.....b.
bar  43  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:x...X.X.|S.X.X...|....X.X.|S.X.X...  G:..g.....|......g.|........|........  B:........|........|........|........
bar  44  K:X.......|........|....X...|..X.....  S:........|S.......|........|S.......  H:-...X.X.|S.X.X...|....X.X.|S.X.X...  G:..g.....|......g.|........|........  B:........|........|........|........
bar  45  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:O...X.X.|S.X.X...|....X.X.|S.X.x...  G:..g.....|......g.|........|........  B:...b....|........|........|....b...
bar  46  K:X.......|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:o...X.X.|S.X.X...|....X.X.|S.X.X...  G:..g.....|......g.|........|........  B:........|b.......|.......b|.......b
bar  47  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:O.....X.|S.X.X...|....X.X.|S.X.X...  G:..g.....|......g.|........|........  B:........|........|........|........
bar  48  K:X.......|....X...|....X...|........  S:........|S.......|........|S.S.S...  H:....X.X.|S.X.X...|....X.X.|S.S.S...  G:..g.....|......g.|........|........  B:........|........|........|........
```

### Bars 49-56  (100.5 s - 117.1 s)  C2: same, bar 56 fill bar (no kick, snare build, riser)
- band RMS: sub -14.1 | 150-400 -19.7 | 400-1.5k -22.8 | 1.5-5k -28.2 | >8k -34.6
- counts: kicks 17 (2.12/bar), main claps 19, programmed hats (X/x) 65, open-type 3
- timing vs 32nd grid (ms, + = late; kick from its click where unmasked): kick -4.3 (sd 14.1, n=14) | clap -1.1 (sd 3.3, n=19) | hats +0.1 (sd 1.0, n=65)
- modal odd bar: K `X.......|....X...|........|........` (2/4 bars)  H `O...X.X.|S.X.X...|....X.X.|S.X.X...` (3/4)  S `........|S.......|........|S.......` (4/4)
- modal even bar: K `X.......|....X...|....X...|..X.....` (2/4 bars)  H `-...X.X.|S.x.X...|....X.X.|S.X.X...` (1/4)  S `........|S.......|........|S.......` (3/4)
- hat level by slot (median >9k peak dBFS, slots hit in at least half the bars): 0:-30 4:-16 6:-16 10:-16 12:-16 20:-16 22:-17 26:-16 28:-16

```
bar  49  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:x...x.X.|S.X.X...|....X.X.|S.X.X...  G:........|......g.|........|........  B:....b...|........|........|....b...
bar  50  K:X.......|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:-...X.X.|S.x.X...|....X.X.|S.X.X...  G:........|......g.|........|........  B:........|b.......|.......b|.......b
bar  51  K:X.......|........|........|........  S:........|S.......|........|S.......  H:O...X.X.|S.X.X...|....X.X.|S.X.X...  G:........|......g.|........|........  B:........|.......b|........|........
bar  52  K:X.......|........|....X...|..X.....  S:........|S.......|........|S.......  H:-...X.X.|S.X.X...|....X.X.|S.X.X...  G:..g.....|......g.|........|........  B:........|....b...|........|........
bar  53  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:O...X.X.|S.X.X...|....X.X.|S.X.X...  G:..g.....|......g.|........|........  B:...b....|........|........|....b...
bar  54  K:X.......|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:-...X.x.|S.X.X...|....X.X.|S.X.X...  G:........|......g.|........|........  B:........|b.......|.......b|.......b
bar  55  K:........|....X...|........|........  S:........|S.......|........|S.......  H:O...X.X.|S.X.X...|....X.X.|S.X.X...  G:g.......|......g.|........|........  B:........|........|........|........
bar  56  K:........|........|........|........  S:........|........|....S...|S.S.S.S.  H:-.o...o.|x...x.x.|..x.S...|X.X.X.x.  G:..g.....|g.....g.|..g.....|.......g  B:........|........|........|........
```

### Bars 57-64  (117.1 s - 133.8 s)  D1: full kick loop, hats add 2& 2a 3e at -8 dB
- band RMS: sub -11.6 | 150-400 -18.6 | 400-1.5k -20.7 | 1.5-5k -27.3 | >8k -35.4
- counts: kicks 16 (2.00/bar), main claps 15, programmed hats (X/x) 69, open-type 1
- timing vs 32nd grid (ms, + = late; kick from its click where unmasked): kick -2.2 (sd 6.9, n=15) | clap +6.2 (sd 9.0, n=15) | hats +0.9 (sd 3.6, n=69)
- modal odd bar: K `X.......|....X...|........|........` (3/4 bars)  H `x...X.X.|x...x.o.|-.x.X.X.|x.-.-...` (1/4)  S `........|S.......|........|S.......` (3/4)
- modal even bar: K `X.......|....X...|........|........` (3/4 bars)  H `X.-.X.X.|S...x.x.|-.x.X.X.|S.o..-..` (1/4)  S `........|S.......|........|S.......` (4/4)
- hat level by slot (median >9k peak dBFS, slots hit in at least half the bars): 0:-20 2:-38 4:-17 6:-16 8:-24 12:-24 14:-24 16:-37 17:-37 18:-23 20:-17 22:-16 26:-38 27:-38 28:-40

```
bar  57  K:X.......|....X...|........|........  S:........|........|........|S.......  H:x...X.X.|x...x.o.|-.x.X.X.|x.-.-...  G:........|G.......|........|........  B:........|.b......|....b...|.b.b....
bar  58  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:X.-.X.X.|S...x.x.|-.x.X.X.|S.o..-..  G:........|......g.|g.......|........  B:........|........|........|........
bar  59  K:X.......|........|........|........  S:........|S.......|........|S.......  H:x...X.X.|S...x.x.|-.x.X.X.|x.-.-...  G:........|....g...|........|........  B:........|b......b|...bb...|........
bar  60  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:X--.X.X.|x...x.x.|o-x.X.X.|x.-.....  G:........|........|........|.gg.....  B:........|.b......|........|........
bar  61  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:O...X.X.|x...x.x.|-.x.X.X.|S.--....  G:........|........|........|........  B:......bb|b.......|....b...|........
bar  62  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:X.o.X.X.|x...x.o.|oox.X.X.|S.--o...  G:........|........|........|........  B:........|........|........|........
bar  63  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:x...X.X.|x...x.x.|.-x.X.X.|S..--...  G:........|....g...|.....g..|...g....  B:...b....|b.......|........|..b.....
bar  64  K:X.......|....X...|....x...|........  S:........|S.......|........|S.......  H:X.o.X.X.|S...x.x.|o.x.X.X.|S.--....  G:........|........|........|........  B:........|b.......|........|........
```

### Bars 65-72  (133.8 s - 150.5 s)  D2: same, bar 72 drop-out (no snare)
- band RMS: sub -11.8 | 150-400 -18.4 | 400-1.5k -20.6 | 1.5-5k -27.4 | >8k -36.8
- counts: kicks 17 (2.12/bar), main claps 14, programmed hats (X/x) 57, open-type 3
- timing vs 32nd grid (ms, + = late; kick from its click where unmasked): kick +3.7 (sd 8.5, n=10) | clap +5.3 (sd 8.9, n=14) | hats +1.6 (sd 4.0, n=57)
- modal odd bar: K `X.......|....X...|........|........` (4/4 bars)  H `O...X.X.|x...x.x.|x.x.X.X.|S.--o...` (1/4)  S `........|S.......|........|S.......` (4/4)
- modal even bar: K `X.......|....X...|....x...|........` (2/4 bars)  H `X...X.X.|S...x.x.|-.x.X.X.|S.-o....` (1/4)  S `........|S.......|........|S.......` (3/4)
- hat level by slot (median >9k peak dBFS, slots hit in at least half the bars): 0:-21 4:-16 6:-17 8:-23 12:-24 14:-24 16:-37 18:-24 20:-17 22:-16 26:-40 27:-41 28:-33

```
bar  65  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:O...X.X.|x...x.x.|x.x.X.X.|S.--o...  G:........|........|........|........  B:.....b.b|bb......|....b...|..b...b.
bar  66  K:X.......|....X...|....x...|........  S:........|S.......|........|S.......  H:X...X.X.|S...x.x.|-.x.X.X.|S.-o....  G:........|..g...g.|........|........  B:........|........|........|........
bar  67  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:O...X.X.|S...x.x.|-...X.X.|S..-o...  G:........|....g...|........|........  B:...b.b.b|b.......|........|........
bar  68  K:X.......|....X...|....x...|........  S:........|S.......|........|S.......  H:X.-.X.X.|S...x.x.|o.x.X.X.|x..--...  G:........|........|g.......|........  B:........|........|........|........
bar  69  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:O...X.X.|S...x.x.|-.x.X.X.|S.--x...  G:........|........|........|........  B:........|b.......|...bbb..|bbb...b.
bar  70  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:x.-.X.X.|x...x.x.|-ox.X.X.|S.-o....  G:........|........|........|........  B:........|b.......|........|........
bar  71  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:x.....X.|x...x.x.|o.x.X.X.|S.-.o...  G:........|........|g....g..|..g.....  B:....b...|b......b|....b...|........
bar  72  K:........|x.......|........|........  S:........|........|........|........  H:o.o.-.-.|o.......|o.-....-|o..--...  G:........|........|g.......|......g.  B:........|........|........|........
```

### Bars 73-80  (150.5 s - 167.2 s)  E1: densest hats (2e 2& 2a 3e, pickup at 4a), low-mid chops
- band RMS: sub -11.3 | 150-400 -16.5 | 400-1.5k -19.0 | 1.5-5k -25.7 | >8k -35.0
- counts: kicks 24 (3.00/bar), main claps 17, programmed hats (X/x) 75, open-type 2
- timing vs 32nd grid (ms, + = late; kick from its click where unmasked): kick +3.6 (sd 15.0, n=15) | clap +6.2 (sd 8.6, n=17) | hats +1.2 (sd 4.4, n=75)
- modal odd bar: K `X.......|....X...|........|........` (3/4 bars)  H `x...X.X.|S...x.x.|x.x.XoX.|S...o.o.` (1/4)  S `........|S.......|........|S.......` (3/4)
- modal even bar: K `X.......|....X...|....X...|..X.....` (3/4 bars)  H `X...X.X.|S.o.x.xo|-.x.XxX.|x.o.-.o.` (1/4)  S `........|S.......|........|S.......` (4/4)
- hat level by slot (median >9k peak dBFS, slots hit in at least half the bars): 0:-19 4:-16 6:-17 10:-31 12:-24 14:-24 16:-28 18:-23 20:-16 21:-29 22:-17 24:-22 26:-38 28:-39 30:-35

```
bar  73  K:X.......|........|........|........  S:........|S.......|........|S.......  H:x...X.X.|S...x.x.|x.x.XoX.|S...o.o.  G:........|..g.G...|g.......|..g.g.G.  B:......bb|b..bb...|..b.b...|..b.....
bar  74  K:X.......|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:X...X.X.|S.o.x.xo|-.x.XxX.|x.o.-.o.  G:........|...g..g.|....g...|....g.g.  B:........|........|........|........
bar  75  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:x...X.X.|S.o.x.x.|x.x.XoX.|x...o.o.  G:........|..g.g...|gg......|......G.  B:...b....|b.......|........|..b.....
bar  76  K:X.......|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:X...X.X.|x.o.x...|o.x.XoX.|S.o.-.o.  G:........|........|g.......|......G.  B:........|b.......|........|........
bar  77  K:X.......|....X...|........|........  S:........|S.......|S.......|S.......  H:O...X.X.|S.o.x.x.|S.x.XoX.|S...x.o.  G:.....g..|........|.....g..|..g.g.G.  B:.....b.b|........|........|...b....
bar  78  K:X.......|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:X...X.X.|x.o.x.x.|..x.XxX.|x.-.-.o.  G:........|..g.....|gg....G.|....g.G.  B:........|........|........|........
bar  79  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:O...X.X.|S.o.x.x.|x.x.XoX.|x.-.o.o.  G:........|......g.|g...gg..|..g.g.G.  B:....b.bb|b.......|........|........
bar  80  K:X.......|x...X...|....X...|..X.....  S:........|S.......|........|S.......  H:X...X.X.|S.o.x.x.|..x.XxX.|x.-.-.o.  G:........|........|g.......|...gg.G.  B:........|........|........|........
```

### Bars 81-88  (167.2 s - 183.9 s)  E2: same, bar 88 drop-out (no snare)
- band RMS: sub -11.7 | 150-400 -17.0 | 400-1.5k -18.1 | 1.5-5k -25.8 | >8k -35.8
- counts: kicks 22 (2.75/bar), main claps 15, programmed hats (X/x) 69, open-type 4
- timing vs 32nd grid (ms, + = late; kick from its click where unmasked): kick +3.8 (sd 8.5, n=11) | clap +5.5 (sd 5.7, n=15) | hats +1.6 (sd 6.4, n=69)
- modal odd bar: K `X.......|....X...|........|........` (3/4 bars)  H `O.....X.|S.o.x.x.|S.x.X.X.|x...o.o.` (1/4)  S `........|S.......|........|S.......` (3/4)
- modal even bar: K `X.......|....X...|....X...|..X.....` (2/4 bars)  H `X...X.X.|S.o.x.x.|..x.XxX.|x.o.-.o.` (1/4)  S `........|S.......|........|S.......` (3/4)
- hat level by slot (median >9k peak dBFS, slots hit in at least half the bars): 0:-22 4:-17 6:-16 10:-31 12:-24 14:-24 16:-28 18:-24 20:-16 21:-29 22:-17 24:-22 28:-34 30:-35

```
bar  81  K:X.......|....X...|........|........  S:........|S.......|S.......|S.......  H:O.....X.|S.o.x.x.|S.x.X.X.|x...o.o.  G:........|..g.....|..g.....|....g.G.  B:........|b.......|....b...|b..b....
bar  82  K:X.......|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:X...X.X.|S.o.x.x.|..x.XxX.|x.o.-.o.  G:........|........|..g..g..|......G.  B:........|........|........|........
bar  83  K:X.......|........|........|........  S:........|S.......|........|S.......  H:O...X.X.|x.o.x.x.|o.x.XoX.|x...o.o.  G:........|..g.....|g.......|....g.G.  B:....b..b|b......b|...bb...|........
bar  84  K:X.......|x...X...|....X...|..X.....  S:........|S.......|........|S.......  H:X...X.X.|S.o.x.xo|o.x.XoX.|x.o...o.  G:........|..g.....|g.......|....g.G.  B:........|........|........|........
bar  85  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:O...X.X.|S.o.x.x.|x.x.XoX.|S...x.o.  G:.g......|..g.....|Gg......|....g.G.  B:........|b.......|....b...|..b.....
bar  86  K:X.......|....X...|....X...|..X.....  S:........|S.......|........|S.......  H:X...X.X.|x.o.x.xo|..x.XxX.|x.o.-.o.  G:........|..g.....|g.g...G.|....g.G.  B:........|........|........|........
bar  87  K:X.......|....X...|........|........  S:........|S.......|........|S.......  H:O...X.X.|S.o.x.x.|x.x.XoX.|x...o.o.  G:........|..g.g...|g...gg..|..g.g.G.  B:...b....|b.......|........|..b.....
bar  88  K:x.......|........|....x...|........  S:........|........|........|........  H:x.....x.|o.o....o|.....xo.|x...-.o.  G:.g......|gg......|g.....G.|g.g.g.G.  B:........|.b......|........|........
```

### Bars 89-96  (183.9 s - 200.6 s)  F: kick on 1 and 2 only, hats as E
- band RMS: sub -13.8 | 150-400 -20.6 | 400-1.5k -18.8 | 1.5-5k -26.0 | >8k -34.9
- counts: kicks 16 (2.00/bar), main claps 16, programmed hats (X/x) 70, open-type 2
- timing vs 32nd grid (ms, + = late; kick from its click where unmasked): kick -0.4 (sd 10.2, n=11) | clap +3.6 (sd 5.8, n=16) | hats +2.0 (sd 4.3, n=70)
- modal odd bar: K `X.......|X.......|........|........` (4/4 bars)  H `O...X.X.|S.o.x.x.|x.x.XoX.|S.....o.` (1/4)  S `........|S.......|........|S.......` (4/4)
- modal even bar: K `X.......|X.......|........|........` (2/4 bars)  H `X...X.X.|S.o.x.xo|..x.XxX.|S...-...` (1/4)  S `........|S.......|........|S.......` (4/4)
- hat level by slot (median >9k peak dBFS, slots hit in at least half the bars): 0:-19 4:-16 6:-16 10:-31 12:-24 14:-23 16:-25 18:-23 20:-16 21:-28 22:-16 28:-32 30:-35

```
bar  89  K:X.......|X.......|........|........  S:........|S.......|........|S.......  H:O...X.X.|S.o.x.x.|x.x.XoX.|S.....o.  G:........|..g.....|ggg.....|..g...G.  B:........|........|b.b.....|........
bar  90  K:X.......|X.......|........|........  S:........|S.......|........|S.......  H:X...X.X.|S.o.x.xo|..x.XxX.|S...-...  G:........|..g.....|g...g...|....g.G.  B:........|........|........|........
bar  91  K:X.......|X.......|........|........  S:........|S.......|........|S.......  H:x...X.X.|S.o.x.x.|x.x.X.X.|x...o...  G:g.......|..g.g...|........|....g.G.  B:........|....b.bb|b.......|........
bar  92  K:X.......|X.......|....x...|........  S:........|S.......|........|S.......  H:X...X.X.|S.o.o.xo|o.x.XxX.|x.....o.  G:........|........|g.....G.|..g...G.  B:........|........|........|........
bar  93  K:X.......|X.......|........|........  S:........|S.......|........|S.......  H:O.....X.|S..ox.x.|x.x.X.X.|S..-x.o.  G:........|........|g.......|...ggg..  B:........|........|........|........
bar  94  K:........|X.......|........|........  S:........|S.......|........|S.......  H:X...X.X.|S.o...x.|..x.XxX.|S.o.....  G:........|..g.....|g....g.g|......g.  B:b.......|........|........|........
bar  95  K:X.......|X.......|........|........  S:........|S.......|........|S.......  H:x...X.X.|S.o.x.x.|x...XoX.|x...o.o.  G:........|........|gg......|...gg...  B:........|...b...b|b.b.b...|........
bar  96  K:X.......|X.......|........|........  S:........|S.......|........|S.......  H:X...X.X.|S.o.x.x.|o.x.XxX.|S.o...o.  G:........|..g.....|g......g|......Gg  B:........|........|....b...|........
```

### Bars 97-104  (200.6 s - 217.3 s)  OUTRO: sample only, no drums
- band RMS: sub -49.2 | 150-400 -25.9 | 400-1.5k -28.5 | 1.5-5k -44.1 | >8k -82.6
- counts: kicks 0 (0.00/bar), main claps 0, programmed hats (X/x) 0, open-type 0
- timing vs 32nd grid (ms, + = late; kick from its click where unmasked): kick +0.0 (sd 0.0, n=0) | clap +0.0 (sd 0.0, n=0) | hats +0.0 (sd 0.0, n=0)

```
bar  97  K:........|........|........|........  S:........|........|........|........  H:-.......|........|........|........  G:........|........|........|........  B:........|........|........|........
bar  98  K:........|........|........|........  S:........|........|........|........  H:........|........|........|........  G:........|........|........|........  B:........|........|........|........
bar  99  K:........|........|........|........  S:........|........|........|........  H:........|........|........|........  G:........|........|........|........  B:........|........|........|........
bar 100  K:........|........|........|........  S:........|........|........|........  H:........|........|........|........  G:........|........|........|........  B:........|........|........|........
bar 101  K:........|........|........|........  S:........|........|........|........  H:........|........|........|........  G:........|........|........|........  B:........|........|........|........
bar 102  K:........|........|........|........  S:........|........|........|........  H:........|........|........|........  G:........|........|........|........  B:........|........|........|........
bar 103  K:........|........|........|........  S:........|........|........|........  H:........|........|........|........  G:........|........|........|........  B:........|........|........|........
bar 104  K:........|........|........|........  S:........|........|........|........  H:........|........|........|........  G:........|........|........|........  B:........|........|........|........
```

## 3. Kick pattern by section (answer: yes, it changes)

Kick = the E1 808-kick only (bass retriggers excluded, see 1.2). Read the modal odd/even bar lines in section 2 for the exact per-section loop; summary:
- Intro (1-8): one kick on beat 1 of odd bars only (bars 1, 3, 5, 7); even bars have no kick.
- A (9-16): `1, 2&` (slots 0, 12) every bar. The 808 bass enters under it.
- A2 (17-24): odd bars `1, 2&`; even bars `1, 2&, 3&, 4e` (first appearance of the full even-bar figure); bar 24 has no kick, no clap and no bass.
- B (25-40), the main loop: odd bars `1, 2&`; even bars `1, 2&, 3&, 4e`; a soft (half-velocity, E1-pitched) beat-2 kick appears under the clap in some even bars (32, 36; measured also in 28): optional. Bar 40: four-on-the-floor `1, 2, 3, 4` with no clap (the turnaround into C).
- C (41-56): odd bars `1, 2&` (51: `1` only; 55: `2&` only); even bars `1, 2&, 3&, 4e` (44 and 52 drop the `2&`); bar 48 `1, 2&, 3&`; bar 56: no kick.
- D (57-72): every bar `1, 2&` (59: `1` only) with a soft `3&` in 64, 66, 68: the loop is thinned to its two main hits here; bar 72: a soft beat-2 hit only.
- E (73-88): odd bars `1, 2&`; even bars `1, (2 soft), 2&, 3&, 4e`; bar 88: soft `1`, `3&`, `4e` only (drop-out).
- F (89-96): `1, 2` (slots 0, 8) every bar, i.e. the kick doubles the clap on beat 2 for the last 8 bars (bar 92 adds a soft `3&`).

## 4. Snare placement, swing and microtiming (bars 1-96)

- Clap on **beats 2 and 4 of every bar** from bar 1 to bar 96 except the drop-out/variation bars 24, 40, 56 (bar 56 keeps beat 4 inside its fill), 72 and 88. There is no halftime (beat-3-only) section.
- hats X/x: mean +0.8 ms, sd 3.8 ms (n=685); on 8th slots -0.1 ms (n=370); on 'e'/'a' 16th slots +1.8 ms (n=305); on 32nd off-slots +4.0 ms (n=10)
- clap S: mean +1.9 ms, sd 6.1 ms (n=190); on 8th slots +2.1 ms (n=187); on 'e'/'a' 16th slots -4.7 ms (n=3); on 32nd off-slots +0.0 ms (n=0)
- kicks (unmasked click, n in brackets): mean +0.1 ms, sd 9.7 ms (n=168); on 8th slots -0.2 ms (n=150); on 'e'/'a' 16th slots +2.2 ms (n=18); on 32nd off-slots +0.0 ms (n=0)
- Folding all >9 kHz transient rises (n=4331) into one beat gives peaks only at 0.00, 0.25, 0.50 and 0.75 of the beat (0.0, 130, 261, 391 ms); nothing at the triplet positions 0.33/0.67. Combined with the 'e/a' slots not being late relative to the 8th slots: **no swing, no shuffle, no humanization**. Program everything dead on a straight 16th grid. (Kick timing is taken from the attack click where it is unmasked; the clap's internal transients at +13-15/+38-44 ms are part of the sample.)

## 5. Rolls, fills, drop-outs (all at 8-bar phrase ends)

- **Bar 24** (end of A2, into B): no kick, no clap, bass drops to -40 dB; only the sample's ghost hats remain; a 1.5-5 kHz riser climbs from -50 to -28 dBFS across the second half of the bar (noise/reverse swell into bar 25).
- **Bar 40** (end of B, into C): kick on every beat (1, 2, 3, 4), no clap, closed hats at -16..-20 on every 8th (slots 0-28), 2e/2a/3e/4e ghosts at -28..-33: a one-bar 'open-up'/turnaround.
- **Bar 48** (end of C1): clap roll at the end: beat 4 (-8), 4e (-8), 4& (-8) (slots 24, 26, 28). Kick `1, 2&, 3&` (no 4e).
- **Bar 56** (end of C2, into D): no kick, bass fades out over the bar, hats drop to -28..-35; a sustained buzzing mid/high tone enters at slot 2 and the 1.5-5 kHz band rises -31 -> -20 dBFS across the bar (riser); clap build `3&` (-15 dBFS), `4` (-7), `4e` (-10..-12), `4&` (-8), `4a` (-9) (slots 20, 24, 26, 28, 30). The 4-6 ms periodicity in that bar is a tone's harmonics beating, not a beat-repeat.
- **Bar 72** (end of D2, into E): clap dropped, kick only a soft beat-2 hit, bass holds, hats only the sample's ghosts: a one-bar breath.
- **Bar 88** (end of E2, into F): same device: clap dropped, kick reduced to soft `1`, `3&`, `4e`, hats thin to -28..-37.
- **Bar 96** (last drum bar): kick `1, 2` as in the rest of F, clap on 2 and 4, then everything stops at bar 97 (sub -48 dB, >8k -61 dB).
- Hat 'rolls': the only 32nd-level hat activity is the sample's own ghost hi-hat (1.6). The programmed hats never roll; they densify by adding 16ths (2& 2a from bar 33, 3e from bar 57, 2e and 4a pickups from bar 73).

## 6. Build sheet (what to program)

- 115.000 BPM, 4/4, straight 16ths, no swing, no humanize. 96 bars of drums = 12 x 8-bar phrases; drop-out/fill bar is always bar 8 of a phrase (24, 40, 48, 56, 72, 88).
- Kick: 808-style, E1, ~200 ms, 90->41 Hz sweep in 40 ms, hard click. Main loop: odd bars `1, 2&`; even bars `1, 2&, 3&, 4e`; soft (half-velocity) `2` under the clap in some even bars (32, 36 and most even bars of E: 74, 78, 80, 84); optional. Intro: beat 1 of odd bars only. A: `1, 2&`. Bar 40: `1 2 3 4`. D: thinned to `1, 2&`. F: `1, 2`. The odd-bar sub hits on `2`, `3&`, `4e` belong to the 808 bass part (B0/C1 retriggers), not the kick.
- Clap: layered clap, body at 600-1500 Hz, peak -7 dBFS, on 2 and 4 everywhere; fills in bars 48 and 56 as listed.
- Closed hat (-16 dB accents): `1& 1a 3& 3a` in every section; beat-1 hat on even bars (-18); open-type/crash on beat 1 of odd bars (-23 peak, 300 ms plateau).
  - A, A2, B1 (9-32): accents only (plus the beat-1 hats).
  - B2 (33-40): + `2&` (-17), `2a` (-16), `3e` (-16): the 16ths of beats 2 and 3 fill in at full velocity.
  - C (41-56): drop beat-1 hats; hats become two 5-note 16th runs `1& 1a 2 2e 2&` and `3& 3a 4 4e 4&`, all at -16 (the 2/4 slots are under the clap).
  - D (57-72): accents + `2& 2a 3e` at -24 (8 dB under the accents) and a -24 hat on beat 2 under the clap.
  - E/F (73-96): accents + `2e` (-31), `2&` (-24/-25), `2a` (-24), `3` (-25..-28), `3e` (-23), a 32nd after `3&` (slot 21, -29), `4` (-22/-23), `4&`/`4a` ghosts (-32..-35).
- Do not program the -37..-48 dB 32nd hats; they are in the sample.

## 7. Confidence / sources

- Grid (115.000 BPM, 0.277 s): measured, high. Snare on 2&4, hat accents, kick loop, section boundaries: measured, high. Kick = single E1 808-kick sample: measured on isolated hits, high. Kick vs 808-bass split in dense bars: measured, medium (overlapping sub band). Open-type hit = open hat vs crash vs noise: location/level measured (high), identity inferred from its 300 ms plateau (medium). G-line hits = sampled chops: inferred from spectrum (no HF, low-mid heavy, no clap fingerprint), medium. Soft beat-2 kick vs bass retrigger in even bars: by sub pitch (41 vs 46 Hz), medium. Ghost 32nd hats = inside the sample: inferred from their persistence in drop-out bars, high.
- No external source was needed for the drums; the only external fact used is the Royksopp 'Remind Me' sample credit given in the brief.
