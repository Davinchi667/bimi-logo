# EVERYWHERE I GO [REMIND ME] (BNYX / Kid Cudi) — instrumental: structure & transitions

Source: `refs/eig_inst.wav` (44.1 kHz stereo, 3:37.34). Everything below is **measured** from that file unless marked otherwise. No listening was involved; descriptions such as "808", "kick", "hats", "pad" are inferences from band/transient behaviour and are labelled with confidence.

## 0. Grid correction (read this first)

| item | given by harness | measured here | evidence |
|---|---|---|---|
| tempo | 114.84 BPM | **115.00 BPM** (beat 0.52174 s, bar 2.08696 s) | grid search of onset-envelope score over 114.5-115.5 BPM x phase peaks at 115.00; the 114.84 grid drifts to +134 ms by 80-100 s, the 115.00 grid stays within ±2 ms over the whole track |
| first downbeat | 0.813 s | **0.290 s** (= 0.812 - one beat) | 0.812 s is a beat, but the bar line is one beat earlier: chroma (harmonic) change entering that beat phase is 0.156 vs 0.020-0.059 for the other three; basic-pitch note onsets 215 vs 58-111; low-band energy 360 vs 168-237; every detected section boundary then lands on bar 8n+1 |
| bar count | ~104 | 104 bars (bar 104 = 215.247 s is the cut point) | |

All bar numbers below use **bar 1 = 0.290 s, bar n starts at 0.290 + (n-1) x 2.08696 s**. To convert from the harness grid: harness-bar n starts one beat (0.52 s) later than my bar n.

Consistency: `grid.json` (115.00 BPM, downbeat 0.291 s), `drums.md` (115.000 BPM) and `bass.md` (115.000 BPM, bar 1 at 0.277 s) in this folder reached the same grid independently; their bar numbers equal mine (first-downbeat phase differs by <= 14 ms, i.e. the same bars). Section labels differ only in naming (bass.md calls 25-40 "hook 1", 41-54 "verse 2", 57-72 "hook 2", 73-88 "bridge", 89-96 "hook 3"); the boundaries are identical.

Confidence: high (measured). The file starts with 50 ms of digital silence, then a 240 ms lead-in at -17 dBFS before the first downbeat hit (first > -30 dBFS sample at 0.278 s).

## 1. Section table

Loudness: K-weighted (ITU BS.1770 filters, no gating) per bar, averaged per section. Integrated loudness bars 1-103: **-10.2 LUFS**, sample peak 0.00 dBFS (brick-wall limited). Loudest section bars 73-87 (-8.0 LUFS); loudest bar 84 (-7.5 LUFS). **Bar 1 = -13.2 LUFS = 5.3 dB under the loudest section mean (5.7 dB under the loudest bar; 6.2 dB in plain RMS).** Intro mean (bars 1-8) -13.8 LUFS = 5.9 dB under the peak section.

| # | bars | time | len | role (inferred) | LUFS mean (bar min..max) | RMS dBFS | what changes at the start of it |
|---|---|---|---|---|---|---|---|
| 1 | 1-8 | 0:00.29-0:16.99 (0.290-16.986 s) | 8 | Intro: sample loop + backbeat + one 808 note per 2 bars | -13.8 (-14.6..-13.2) | -15.8 | Track opens on the downbeat hit (-5.6 dBFS in the first 100 ms). 2-bar sample loop, clap-type accent on beats 2 and 4 (400 Hz-2 kHz, 16ths 5 and 13), 2-bar hat loop with a ~250 ms bright hit on odd-bar downbeats, a single 808 note (sub -7 dBFS) on beat 1 of ODD bars only, with a 60-120 Hz kick doubling it. Even bars have no sub at all (sub band 23 dB lower). |
| 2 | 9-16 | 0:16.99-0:33.68 (16.986-33.682 s) | 8 | A: 808 pattern enters (every bar) | -12.6 (-12.7..-12.4) | -13.1 | Sub band +8.8 dB vs the intro average and now constant every bar; 808 plays beat 1 + the "and" of 2 (16ths 1,7) every bar, kick doubles both hits; RMS +2.8 dB, LUFS +1.2. Nothing leaves. No fill or riser in bar 8 (bar 8 is identical to bar 6 within 0.5 dB); the only lead-in is a soft 808 pickup on the last 16th of each bar (-31 dBFS, 23 dB below the downbeat note). |
| 3 | 17-23 | 0:33.68-0:48.29 (33.682-48.290 s) | 7 | B: kick/hat layer thickens (build) | -11.8 (-12.6..-11.0) | -11.8 | Kick (60-120 Hz) onsets 2 -> 5-7/bar with ghost kicks on odd bars; 808 becomes a 2-bar phrase (even bars add hits on the "and" of 3 and the "e" of 4: 16ths 11, 14); 2 kHz-band onsets +3/bar; width above 2 kHz rises from -20 to -17 dB side/mid (first appearance of a wide high element); even bars 1.0-1.4 dB louder than odd bars. 7 bars because bar 24 is the drop-out bar. |
| 4 | 24-24 | 0:48.29-0:50.38 (48.290-50.377 s) | 1 | PRE-DROP bar (drop-out + wide reversed swell) | -14.6 (-14.6..-14.6) | -17.4 | 808, kick and hats all removed (sub -45 dBFS, 60-120 Hz -34, >6 kHz -47..-56); the sample (120 Hz-2 kHz) keeps playing at its usual level. A wide, TONAL (flatness 0.10) reversed swell in 500 Hz-4 kHz rises +14 dB across beats 2-4 (2k+ band -45.6 -> -31.7 dBFS), side/mid goes -9.6 -> -2.8 dB, L/R correlation 0.50 (near-decorrelated), centroid does NOT rise (1.4-1.7 kHz: it is not a bright noise riser). 808 pickup on the last 16th (-26.8 dBFS). No silence gap. Quietest bar since the intro: -14.6 LUFS, 4.3 dB under bar 23. |
| 5 | 25-39 | 0:50.38-1:21.68 (50.377-81.682 s) | 15 | DROP 1 (first full arrangement) | -10.2 (-11.0..-9.1) | -9.5 | THE biggest single drop of the track: RMS -17.4 -> -10.0 dBFS (+7.4 dB) and -14.6 -> -11.0 LUFS (bar 26: -9.8); sub band +16 dB bar-to-bar (+40 dB from the last 16th of 24 to the downbeat); the swell is cut dead at the downbeat (side/mid -5.2 -> -19.8 dB, i.e. the mix snaps back to near-mono). 808 becomes continuous (notes on beats 1, 2, 2.5, 3.5, 4.25 = 16ths 1,5,7,11,14, sub held at -10..-19 dBFS all bar); kick dense (10-13 onsets/bar); hats unchanged. 2-bar loudness alternation 1.2 dB (even bars louder). Sub-events: bar 33 the hat pattern adds 16ths 8 and 10 (>6 kHz +3 dB on even bars); bars 35-36 and 39 switch on a wide tonal 500 Hz-4 kHz layer (side/mid 1-4 kHz -15 -> -5..-8 dB) for 2-bar stretches. |
| 6 | 40-40 | 1:21.68-1:23.77 (81.682-83.769 s) | 1 | transition bar: hats out, wide wash, 808 on every beat | -9.5 (-9.5..-9.5) | -8.8 | Hats removed (>6 kHz flat at -31..-37 dBFS with none of the loop's gaps) and replaced by a fully decorrelated wash (2-6 kHz side/mid -0.2 dB); 808 switches to a roll with a note on every beat (16ths 1,5,9,13 at -6..-8 dBFS plus 8, 11); kick roll `XXXX|XXXx|XxXx|XXXX`. Loudness does not dip (-9.5 LUFS). No sweep (centroid flat). |
| 7 | 41-55 | 1:23.77-1:55.07 (83.769-115.073 s) | 15 | VERSE-type section (narrow, busy drums, darker) | -10.4 (-11.0..-9.9) | -10.5 | The wide layer LEAVES: side/mid above 2 kHz falls to -20..-22 dB (narrowest point of the track); sustained 400 Hz-2 kHz content between the backbeats drops ~3 dB (clap accents stay); 808 goes back to the sparse 2-bar phrase of bars 17-23 (beat 1 + and-of-2, with 11/14 on even bars) with ghost notes, sub -3 dB on odd bars (2-bar alternation 1.5 dB); kick very dense (9-14 onsets/bar), hat pattern changes (16ths 6-7 added), 2 kHz onsets 10-14/bar (busiest hats of the track); a wide low-mid layer appears (120-250 Hz +2.8 dB, side/mid there -10.5 dB vs -17). Bar 48 has the only mid-section fill: 2-6 kHz +7 dB in beat 4 (`XXX.` in the mid/hat rows). -10.4 LUFS. |
| 8 | 56-56 | 1:55.07-1:57.16 (115.073-117.160 s) | 1 | PRE-DROP bar 2 (bright riser / filter opening) | -10.4 (-10.4..-10.4) | -12.6 | Sub pulled (808 notes only at -17 dBFS, ~10 dB under normal), kick thinned, a 120-400 Hz hit on beat 2 (-12.5 dBFS). Riser: 2k+ band -34.5 -> -20.9 dBFS and 6k+ -42 -> -28 over the bar (+14 dB, mostly beats 3-4), **centroid 1.1 -> 3.0 kHz (x2.7)** = the one true bright/filter-opening sweep in the track; its >6 kHz part is centred (side/mid -19..-36 dB) while its 2-6 kHz part is wide (-6..-15 dB). Loudness does not dip (-10.4 LUFS, RMS -12.6, crest 12.7 dB). No silence gap. |
| 9 | 57-71 | 1:57.16-2:28.46 (117.160-148.464 s) | 15 | DROP 2 | -9.3 (-9.7..-8.9) | -9.3 | Sub returns (+9.4 dB; 808 continuous as in Drop 1); 250-500 Hz +2.5 dB and 1-2 kHz +2.5 dB vs Drop 1 (sample/chords louder); hat pattern `XXxx|X.xx|.xxx|X...` (16ths 7-8 and 10-12 added vs Drop 1); the wide tonal layer comes back and toggles every 2 bars: ON in 57, 59-60, 63-64, 67-68, 71 (side/mid >2 kHz -7..-10 dB), OFF in 58, 61-62, 65-66, 69-70 (-12..-15 dB); the 2-bar loudness alternation shrinks to 0.4 dB. -9.3 LUFS (+1.1 vs Drop 1). Entry from 56: +3.4 dB RMS, +9.4 dB sub, side/mid -7.7 -> -14.5. |
| 10 | 72-72 | 2:28.46-2:30.55 (148.464-150.551 s) | 1 | transition bar: hats out, wash, dotted-8th 808 roll | -9.0 (-9.0..-9.0) | -9.6 | Hats removed (>6 kHz flat -42..-53 dBFS, 6k onsets 10 -> 2), the remaining 1-4 kHz content is fully wide (side/mid -1..+2 dB); 808 plays a dotted-8th roll (16ths 1,5,8,11,14 at -10.5..-11 dBFS); kick roll `XXXX|XXXX|XXXX|Xx..`. No sweep (centroid ~1.2 kHz flat), no loudness dip (-9.0 LUFS). |
| 11 | 73-87 | 2:30.55-3:01.86 (150.551-181.855 s) | 15 | DROP 3 / PEAK (loudest section) | -8.0 (-8.4..-7.5) | -8.5 | -8.0 LUFS (loudest bar 84 = -7.5). Vs Drop 2: 250-500 Hz +2.4 dB, 500 Hz-1 kHz +1.3..+3, 1-2 kHz +2, 2-4 kHz +2 dB — the mid-range layers become continuous (`XXXX` in both the 150-400 and 400 Hz-2 kHz rows); wide tonal layer on for the whole section (side/mid 500 Hz-4 kHz -4..-5 dB, L/R corr 0.88); hats add 16th 15 on odd bars; 808/kick as Drop 1-2. Entry from 72 is additive, not a "drop": RMS +0.8 dB only, >6 kHz +10 dB (hats back), centroid +29%. |
| 12 | 88-88 | 3:01.86-3:03.94 (181.855-183.942 s) | 1 | transition bar (same recipe as 72) | -7.9 (-7.9..-7.9) | -9.0 | Hats out, wash wide (2-6 kHz side/mid -6..0, >6 kHz -6..+3 dB), dotted-8th 808 roll (1,5,8,11,14), kick roll. -7.9 LUFS. |
| 13 | 89-96 | 3:03.94-3:20.64 (183.942-200.638 s) | 8 | POST-DROP: half-bar drums | -9.5 (-9.8..-8.7) | -10.5 | 808 reduced to beats 1 and 2 only (16ths 1, 5 at -7 dBFS, then it decays to -37 dBFS by beat 4), kick only in the first half of each bar (sub onsets 5 -> 2, kick onsets 7 -> 2-4 per bar); every 4th bar (92, 96) restores the full 808/kick bar (-8.7..-8.9 vs -9.6..-9.8 LUFS); hats, sample and wide layer continue; 120-250 Hz -4.6 dB. The empty second half of each bar exposes the wide pad (side/mid -13 -> -5.6 dB within bar 89). -9.5 LUFS. |
| 14 | 97-103 | 3:20.64-3:35.25 (200.638-215.247 s) | 7 | OUTRO: low-passed sample only, hard cut | -15.9 (-17.0..-15.2) | -18.2 | HARD CUT at the bar line — no riser, no fill, no gap, no crash: 808/kick/hats all removed in one step (0-60 Hz -43 dB, >6 kHz -30 dB, RMS -7.8 dB, centroid -63%). The sample's 120 Hz-2 kHz content stays at its normal level (-21..-24 dBFS per 16th) but low-passed: >6 kHz at -72 dBFS, 2k+ at -40 dBFS, centroid ~700 Hz (vs ~2.1 kHz in the drops). Bar 97 carries the decaying tail of the previous section (>6 kHz -51 -> -65 dBFS over the bar); bars 98-102 are static (-18 ± 0.7 dBFS RMS, -15.9 LUFS); bar 103 steps the low-pass down again (2k+ -62 dBFS, centroid 423 Hz, 400 Hz-2 kHz -6 dB). What is left above 2 kHz is mostly side (side/mid 2-8 kHz 0..+2.5 dB: reverb/width, not centre content). Audio stops with a hard cut (<10 ms, -18 -> -45 dBFS) at **215.238 s**, 9 ms before the bar-104 line; residual -45..-95 dBFS tail to 217.34 s. |

Phrase logic: every structural boundary sits on bar 8n+1 (9, 17, 25, 41, 57, 73, 89, 97); the three "drops" are each preceded by a one-bar transition (24, 56 before a drop; 40, 72, 88 between full sections). Intro length: 8 bars / 16.7 s before the 808 pattern, 24 bars / 50.1 s before the first full drop (bar 25 at 50.377 s = 0:50.38).

## 2. Loudness contour (bar-mean LUFS, K-weighted)

```
bars  1-8   -13.8   (bar 1 -13.2; even bars ~0.6 dB quieter than odd)
bars  9-16  -12.6
bars 17-23  -11.8   (odd -12.0..-12.6 / even -11.0..-11.2)
bar  24     -14.6   <- dip (drop-out bar)
bars 25-39  -10.2   (odd -11.0..-10.3 / even -9.9..-9.1)
bar  40      -9.5
bars 41-55  -10.4   (odd -10.5..-11.0 / even -9.9..-10.3)
bar  56     -10.4   (no dip: riser fills the level)
bars 57-71   -9.3
bar  72      -9.0
bars 73-87   -8.0   <- peak (bar 84 -7.5)
bar  88      -7.9
bars 89-96   -9.5   (bars 92, 96 -8.9/-8.7)
bars 97-103 -15.9   (static; bar 103 -17.0); hard cut at 215.238 s
```
Plain RMS (stereo, dBFS): intro -15.8, 9-16 -13.1, 17-23 -11.8, bar 24 -17.4, Drop 1 -9.5, Verse -10.5, bar 56 -12.6, Drop 2 -9.3, Drop 3 -8.5, post-drop -10.5, outro -18.2. Peak is 0.00 dBFS in every section except the outro (-5.1).

## 3. Transition anatomy (what to program)

| into bar | time | type | preceding-bar fill / riser | gap? | at the downbeat |
|---|---|---|---|---|---|
| 9 | 16.986 | additive entry | none (bar 8 = loop as usual; 808 pickup -31 dBFS on last 16th) | none | 808 pattern + kick start; no crash |
| 17 | 33.682 | additive entry | none | none | kick/hat density up; no crash |
| 24 | 48.290 | drop-out bar | — | none | 808, kick, hats removed; wide reversed tonal swell +14 dB over beats 2-4, no brightening; 808 pickup -26.8 dBFS on last 16th |
| **25** | **50.377** | **THE drop** | bar 24 swell | none (no gated silence; see note) | sub +40 dB in the sub band, RMS +7.4 dB, width collapses -15 dB (swell cut dead); continuous 808 starts |
| 40 | 81.682 | transition bar | — | none | hats out, decorrelated wash, 808 on every beat, kick roll |
| 41 | 83.769 | section change (no level jump) | bar 40 roll | none | wide layer gone (side/mid >2k -14 dB), 808 back to sparse phrase, hats busier; RMS -2.3 dB vs 40 |
| 48->49 | 100.46 | phrase fill | beat 4 of 48: 2-6 kHz +7 dB, hat/mid `XXX.` | none | continues |
| 56 | 115.073 | pre-drop bar | — | none | sub pulled 10 dB, kick thinned, 120-400 Hz hit on beat 2, bright centred riser: 2k+/6k+ +14 dB, centroid 1.1 -> 3.0 kHz |
| **57** | **117.160** | drop 2 | bar 56 riser | 1 x 8 ms dip 160 ms before (not audible-scale) | sub +9.4 dB, RMS +3.4 dB, width -7 dB; continuous 808 |
| 72 | 148.464 | transition bar | — | none | hats out, wash fully wide, dotted-8th 808 roll (1,5,8,11,14), kick roll; no sweep |
| 73 | 150.551 | peak section | bar 72 roll | none | hats back (+10 dB >6k), mids +2 dB everywhere 250 Hz-4 kHz, wide layer stays on; RMS only +0.8 dB |
| 88 | 181.855 | transition bar | — | none | as 72 |
| 89 | 183.942 | thinning | bar 88 roll | none | 808/kick cut to first half of each bar |
| 97 | 200.638 | hard cut to outro | none (bar 96 is a normal full bar) | none | 808/kick/hats removed; sample low-passed (~2-4 kHz corner inferred from 2k+ -40 / 6k+ -72 dBFS) |
| 103 | 213.160 | second low-pass step | — | — | 2k+ -62 dBFS, centroid 423 Hz |
| 104 | 215.247 | END | — | — | hard cut at 215.238 s (<10 ms), no fade |

Notes from the measurements:
- **No crash cymbals / no section-start accents.** The bright ~250 ms hit on every odd-bar downbeat (>6 kHz -23.6 dBFS decaying to -28 over 240 ms) is identical at section starts and at ordinary odd bars (std 0.3 dB). It is part of the 2-bar loop. Even-bar downbeats have only a short hat (>6 kHz falls to -58 dBFS within 90 ms).
- **No gated silence before any drop.** A strict search (>=8 ms, >=12 dB below the local 90th percentile, within -200/+100 ms of each section downbeat) finds nothing at 41, 73, 97, and only the natural low points of the sparse preceding bar at 9/17/25 (those bars are 20+ dB quieter than the -3.4 dBFS downbeat hit); 1 x 8 ms dips at 57 and 89. Drops are made by the sub re-entering and the width collapsing, not by a gap.
- **Filter sweeps:** the only multi-beat centroid ramp is inside bar 56 (x2.7 within one bar). The outro is a stepped low-pass (one step at bar 97, a second at bar 103), not a sweep. There is no high-pass opening in the intro (bars 1-8 >6 kHz level equals the drops' within 0.5 dB).
- **Fills:** the arrangement uses 808 rolls (bars 40, 72, 88) and one hat/mid fill (beat 4 of bar 48) rather than snare rolls. There is no fill before 9, 17, 73, 89 or 97.
- **808 pickup:** the last 16th of each bar carries sub energy in every section from bar 9 on (-31 dBFS in 9-23, -18 in the drops where the 808 sustains, -27 in 89-96) — a ghost note/tail leading into the next downbeat.

## 4. Layer behaviour by section (step-sequencer view)

Patterns are per 16th (beats separated by |). X = strong, x = weak. Thresholds: sub<60 Hz whole-16th RMS > -12 / -22 dBFS; kick 60-120 Hz first-60 ms > -20/-26; snr 150-400 Hz > -18/-23; mid 400 Hz-2 kHz > -20/-24; hat >6 kHz > -30/-38. Representative bars (odd/even pairs show the 2-bar loop):


```
intro            bar   1  sub Xx..|....|....|....  kick X...|....|....|....  snr xxxx|xxxx|xxxx|xxxx  mid x.xx|X...|..x.|X...  hat XXxx|X...|..xx|X...
intro            bar   2  sub ....|....|....|....  kick x...|....|....|....  snr xxxx|xxxx|xxxx|xxxx  mid x.x.|X...|xxXx|X...  hat x.xx|X...|..xx|X...
A 9-16           bar   9  sub Xx..|..Xx|....|....  kick X...|..X.|....|....  snr xxxx|xxxx|xxxx|xxxx  mid ..X.|X...|..x.|X...  hat XXxx|X...|..xx|X...
A 9-16           bar  10  sub Xx..|..Xx|....|....  kick X...|..X.|....|....  snr xxxx|xxxx|xxxx|x.xx  mid x.X.|X...|..Xx|X...  hat x.xx|X...|..xx|X...
B 17-23          bar  17  sub Xx..|..Xx|....|....  kick X...|..X.|....|....  snr xxxx|xxxx|xxxx|xxxx  mid xxxx|X..x|xxxx|Xxxx  hat XXxx|X...|..xx|X...
B 17-23          bar  18  sub Xx..|..Xx|..Xx|.Xx.  kick X...|..X.|..X.|.X..  snr xxxx|xxxx|xxxx|x.xx  mid xxxx|X...|x..x|Xx..  hat x.xx|X...|..xx|X...
pre-drop         bar  24  sub ....|....|....|....  kick ....|....|....|....  snr xxxx|xxxx|xxxx|x.xx  mid xx.x|....|x..x|xxxx  hat ....|....|....|....
Drop 1           bar  25  sub Xxxx|XxXX|xxXx|xXxx  kick Xxxx|XxXx|xxxx|.x..  snr ..x.|..xx|.x.x|x.xx  mid xxxx|X...|X.xx|Xx..  hat XXxx|X...|..xx|X...
Drop 1           bar  26  sub Xxxx|XxXx|xxXx|xXxx  kick Xxxx|XXXX|XXXx|xX..  snr x.x.|.xxx|.xx.|....  mid x.x.|X...|X.xx|Xx..  hat x.xx|X...|..xx|X...
Drop 1 from 33   bar  33  sub Xxxx|XxXx|xxXx|xXxx  kick X...|XxXX|xxXx|xXxx  snr ..x.|.xxx|.xxx|xxxx  mid xxXx|X..x|XxXX|Xxx.  hat XXxx|X.xX|.Xxx|X...
Drop 1 from 33   bar  34  sub Xxxx|XxXx|xxXx|xXxx  kick XXXX|x.XX|XxXX|XXXX  snr .x..|x...|.x..|x...  mid xxXx|X..x|X.xX|Xx..  hat x.xx|X.XX|.Xxx|X...
Drop 1 wide (35) bar  35  sub Xxxx|XxXx|xxXx|xXxx  kick Xxxx|xxXX|XXXx|xXXx  snr ..x.|xxxx|xxxx|xxxx  mid xxXX|X.xx|xXXX|Xxxx  hat XXxx|X.XX|.Xxx|X...
bar 40           bar  40  sub Xxx.|XxxX|XxXx|Xxxx  kick XXXX|XXXx|XxXx|XXXX  snr xxx.|xxxx|xxx.|xxxx  mid xxXx|.xxx|x.Xx|.xxx  hat x.xx|x.xx|x.xx|x.xx
Verse            bar  41  sub Xx.x|..Xx|.x..|xxx.  kick XXx.|XXXX|X.XX|x.Xx  snr xxxx|xxxx|xxxx|xxXx  mid ....|X...|....|X...  hat XXxx|Xxx.|..xx|Xxx.
Verse            bar  42  sub Xx..|xxXx|..Xx|.Xxx  kick XXx.|XXXX|xXXx|xXXX  snr xXxx|xxxx|xxxx|xXXx  mid ....|X...|....|X...  hat ..xx|Xxx.|..xx|Xxx.
bar 48 fill      bar  48  sub Xx.x|..Xx|.xXx|xxx.  kick XXx.|..XX|x.Xx|XxXx  snr xXxx|Xx.X|xxxx|xxxx  mid ....|X...|....|XXX.  hat ..xx|Xxx.|..xx|XXX.
bar 56           bar  56  sub ...x|....|.x..|xxxx  kick .Xxx|...X|xxXX|X.X.  snr xXxX|Xx.X|xXX.|xxX.  mid .x..|x...|..Xx|XxXX  hat ....|x...|..X.|XXXX
Drop 2           bar  57  sub Xxxx|XxXx|xxXx|xXxx  kick X...|XxXX|xxXx|xXxx  snr xxxx|xxxX|xXxx|xxxx  mid xxxx|XxxX|Xxxx|XXXx  hat XXxx|X.xx|.xxx|X...
Drop 2           bar  58  sub Xxxx|XxXx|xxXx|xXxx  kick XxxX|x.XX|XXXX|xXXX  snr xXxx|XXxX|xxXX|xxxx  mid xxxx|XxxX|xxxX|XXxx  hat x.xx|X.xx|.xxx|X...
bar 72           bar  72  sub Xxxx|XxxX|xxXx|xXxx  kick XXXX|XXXX|XXXX|Xx..  snr xXxx|XXxX|XXXx|XxxX  mid XxXx|XxxX|XxXX|XXXX  hat x...|x...|....|....
Drop 3           bar  73  sub Xxxx|XxXx|xxXx|xXxx  kick Xxx.|XxXX|xxxx|.x..  snr xxxx|xxXX|XxxX|XxXX  mid xxXx|XXXX|XXXX|XXXX  hat XXxx|Xxxx|xxxx|X.x.
Drop 3           bar  74  sub Xxxx|XxXx|xxXx|xXxx  kick Xxxx|XXXX|XXXX|XX..  snr xXXx|xxxX|Xxxx|xxxx  mid XXXx|XXXX|XxXX|XXXX  hat x.xx|X.xx|.xxx|X...
bar 88           bar  88  sub Xxxx|XxxX|xxXx|xXxx  kick XXXX|XXXX|xxX.|.XXx  snr XXxx|XXXX|XXXX|XXXx  mid XXXX|XXXX|XXXX|XXXX  hat x..x|x...|x...|x...
post-drop        bar  89  sub Xxxx|Xxxx|....|....  kick XXXX|Xxxx|xxx.|....  snr xxxx|xxxx|.x.x|...x  mid xXXx|XXXX|XXXX|XXXX  hat XXxx|X.xx|xxxx|X.x.
post-drop        bar  90  sub Xxx.|Xxx.|....|....  kick XXxx|XXXX|XxXx|x...  snr xxx.|xxxx|.xxx|x.xx  mid XxXX|XXXx|XxXX|XXXX  hat x.xx|X.xx|.xxx|X...
post-drop        bar  92  sub Xxx.|Xxxx|.xXx|xXxx  kick Xxxx|XxXX|XXXX|xXXX  snr xxx.|.xx.|x.x.|xxxx  mid XxXx|XXXx|XxXX|XXXX  hat x.xx|X.xx|xxxx|X...
outro            bar  97  sub ....|....|....|....  kick ....|....|....|....  snr ....|x.x.|....|....  mid xxxx|xxxx|.xxx|x.x.  hat ....|....|....|....
outro            bar  98  sub ....|....|....|....  kick xxxx|....|....|.x..  snr xxxx|.xxx|xx.x|xxxx  mid xx.x|.x.x|xxxx|.x.x  hat ....|....|....|....
outro            bar 103  sub ....|....|....|....  kick ....|....|....|....  snr xxxx|xxxx|xxxx|xxxx  mid ....|....|....|....  hat ....|....|....|....
```

Constant elements (bars 1-96): the 2-bar hat/perc loop (odd bar `XXxx|X...|..xx|X...`, even bar `x.xx|X...|..xx|X...` until bar 32; busier variants after), the backbeat accent on beats 2 and 4 in 400 Hz-2 kHz, the sample's 120-400 Hz bed (`xxxx|xxxx|xxxx|xxxx` in every bar 1-102). The 808 pattern is what changes most between sections (see the table above). basic-pitch's lowest note per bar cycles over 4 bars in the drops (MIDI 23/30/24/28 ~ B0/F#1/C1/E1) and reads 38/30 in the verse — a 4-bar bass cycle (low confidence: basic-pitch octave errors are common below 50 Hz; the sub-band energy itself is the reliable part).

## 5. Stereo / wide-layer facts

- Sub (<60 Hz) is mono everywhere (side/mid -36..-43 dB). 60-120 Hz is mono in the drops (-25..-35 dB) but wider in the intro (-17) and the verse (-14.5).
- The "wide layer" that defines Drop 2/3 and the post-drop lives in **500 Hz-4 kHz**, is tonal (side-channel spectral flatness 0.14-0.19), with side-channel chroma dominated by E, F#, B (E-minor chord tones): a pad / vocal-chop type element, not noise or hats. Side/mid in 1-4 kHz: intro -19, Drop 1 -15..-18, Drop 1 bars 35/36/39 -5..-8, Verse -20..-22 (gone), Drop 2 alternating -7 / -12, Drop 3 and post-drop -4..-5, outro -2..-4 (it survives the low-pass).
- Full-band L/R correlation: 0.96-0.98 in bars 1-32, 0.95 verse, 0.88-0.93 Drop 2/3, 0.82-0.83 post-drop/outro; 0.50 in bar 24 and 0.70 in bar 56 (the swells are the widest moments).
- Transition bars 40/72/88: 2-6 kHz side/mid at about 0 dB (fully decorrelated wash) once the hats are removed.

## 6. Vocal version cross-check (low confidence)

`refs/everywhere.wav` lines up with the instrumental at +20 ms (envelope correlation 0.81-0.94, no drift) but is not phase-coherent (sample-level correlation 0.59), so it cannot be subtracted. Per-bar 1-4 kHz energy of the full version minus the instrumental (after a +0.5 dB gain reference from bars 1-8): ~0 dB in bars 1-24 and 73-96; +1 to +3.5 dB in bars 27-72 (odd bars of Drop 1, bars 40, 43-44, 49-55, 59-71 odd, 72); +5 to +21 dB in 97-103 (the full version's outro is NOT the low-passed instrumental outro; it has extra content, and +8 dB in the sub band). Treat as "voice is probably present somewhere in 27-72 and in the outro, probably absent in 1-24 and 73-96" — not a transcription-grade result.

## 7. Per-bar layer map (1-bar resolution)

Band levels are Butterworth-band RMS in dBFS over the whole bar (mid channel). Onsets = detected transients per bar per band (sub / 60-120 / 120-400 / 400-2k / 2-6k / >6k; masked when the band is near-silent). S/M = side/mid energy ratio in dB (full band / above 2 kHz). cent = spectral centroid (Hz). vox = full-version minus instrumental 1-4 kHz energy (dB, see §6). 808 = sub<60 Hz step pattern.

| bar | t0 | LUFS | RMS | sub | 60-120 | 120-400 | 400-2k | 2-6k | >6k | onsets s/k/l/m/h/t | cent | S/M | S/M>2k | vox | 808 pattern |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 0:00.29 | -13.2 | -14.7 | -19.6 | -31.2 | -20.5 | -22.1 | -30.7 | -31.7 | 4/0/0/3/4/6 | 2435 | -18.3 | -20.6 | -0.6 | `Xx..|....|....|....` |
| 2 | 0:02.38 | -14.0 | -16.6 | -44.3 | -24.8 | -21.5 | -21.8 | -31.0 | -34.5 | 14/1/1/5/6/8 | 1997 | -16.4 | -18.9 | +0.3 | `....|....|....|....` |
| 3 | 0:04.46 | -13.5 | -15.0 | -19.6 | -33.3 | -21.1 | -22.5 | -31.1 | -31.7 | 5/1/1/5/4/6 | 2463 | -17.7 | -20.1 | -0.2 | `Xx..|....|....|....` |
| 4 | 0:06.55 | -14.5 | -17.2 | -41.0 | -26.3 | -20.5 | -23.8 | -31.0 | -34.5 | 13/1/1/8/6/8 | 2034 | -14.2 | -19.3 | +0.3 | `....|....|....|....` |
| 5 | 0:08.64 | -13.6 | -15.0 | -19.4 | -31.1 | -20.6 | -24.2 | -30.9 | -31.6 | 5/0/0/6/4/6 | 2499 | -16.8 | -19.9 | -0.5 | `Xx..|....|....|....` |
| 6 | 0:10.72 | -14.0 | -16.7 | -44.5 | -25.0 | -21.3 | -21.7 | -31.0 | -34.5 | 11/2/1/4/6/8 | 1975 | -16.1 | -19.2 | +0.6 | `....|....|....|....` |
| 7 | 0:12.81 | -13.2 | -14.6 | -19.4 | -33.2 | -20.3 | -21.9 | -31.0 | -31.7 | 5/1/0/4/4/6 | 2398 | -19.5 | -20.3 | +0.3 | `Xx..|....|....|....` |
| 8 | 0:14.90 | -14.6 | -17.3 | -42.1 | -26.3 | -22.6 | -21.4 | -31.2 | -34.6 | 9/1/1/5/6/8 | 2070 | -13.8 | -18.3 | -0.2 | `....|....|....|....` |
| 9 | 0:16.99 | -12.6 | -13.2 | -16.5 | -24.6 | -20.8 | -22.9 | -30.8 | -31.7 | 2/4/2/7/5/7 | 2438 | -18.8 | -20.3 | +1.8 | `Xx..|..Xx|....|....` |
| 10 | 0:19.07 | -12.7 | -13.1 | -16.5 | -24.1 | -21.1 | -22.3 | -31.0 | -34.6 | 2/2/2/7/7/9 | 1921 | -19.0 | -18.6 | +1.1 | `Xx..|..Xx|....|....` |
| 11 | 0:21.16 | -12.4 | -13.0 | -16.5 | -24.5 | -20.0 | -22.0 | -30.9 | -31.7 | 2/6/2/5/5/7 | 2377 | -19.3 | -20.3 | +0.1 | `Xx..|..Xx|....|....` |
| 12 | 0:23.25 | -12.7 | -13.1 | -16.4 | -24.6 | -20.6 | -22.0 | -31.1 | -34.6 | 2/2/2/6/7/9 | 1937 | -19.1 | -19.2 | +1.5 | `Xx..|..Xx|....|....` |
| 13 | 0:25.33 | -12.6 | -13.2 | -16.4 | -24.8 | -20.9 | -22.8 | -30.9 | -31.6 | 2/3/2/6/5/7 | 2429 | -18.5 | -19.9 | +0.3 | `Xx..|..Xx|....|....` |
| 14 | 0:27.42 | -12.7 | -13.2 | -16.5 | -24.2 | -20.9 | -23.2 | -31.0 | -34.4 | 2/2/2/8/7/9 | 1954 | -18.7 | -18.6 | -0.5 | `Xx..|..Xx|....|....` |
| 15 | 0:29.51 | -12.5 | -13.0 | -16.4 | -24.6 | -20.0 | -23.2 | -30.9 | -31.7 | 2/5/2/7/5/7 | 2378 | -20.7 | -20.0 | +2.2 | `Xx..|..Xx|....|....` |
| 16 | 0:31.59 | -12.7 | -13.2 | -16.4 | -24.7 | -20.3 | -23.4 | -30.9 | -34.7 | 2/2/2/8/7/9 | 1937 | -18.5 | -19.2 | +1.5 | `Xx..|..Xx|....|....` |
| 17 | 0:33.68 | -12.0 | -12.7 | -16.5 | -23.0 | -20.2 | -21.8 | -30.6 | -31.5 | 2/5/2/4/8/8 | 2548 | -21.5 | -18.5 | -0.0 | `Xx..|..Xx|....|....` |
| 18 | 0:35.77 | -11.2 | -10.8 | -13.3 | -21.6 | -20.5 | -22.5 | -30.7 | -34.4 | 4/7/4/9/10/9 | 2033 | -21.2 | -16.9 | +1.2 | `Xx..|..Xx|..Xx|.Xx.` |
| 19 | 0:37.85 | -12.2 | -12.8 | -16.5 | -21.9 | -20.0 | -23.0 | -30.5 | -31.7 | 2/4/2/8/8/8 | 2572 | -19.8 | -17.6 | +0.3 | `Xx..|..Xx|....|....` |
| 20 | 0:39.94 | -11.0 | -10.6 | -12.9 | -21.5 | -20.3 | -22.2 | -30.5 | -34.6 | 4/4/4/8/10/9 | 1988 | -20.6 | -17.0 | +0.9 | `Xx..|..X.|..Xx|.Xx.` |
| 21 | 0:42.03 | -12.3 | -12.8 | -16.5 | -23.0 | -20.4 | -22.7 | -30.4 | -31.7 | 2/3/2/6/8/8 | 2590 | -20.2 | -17.3 | +1.6 | `Xx..|..Xx|....|....` |
| 22 | 0:44.12 | -11.2 | -10.9 | -13.3 | -21.6 | -20.2 | -23.1 | -30.7 | -34.5 | 4/4/4/10/10/9 | 2013 | -20.4 | -17.0 | +1.0 | `Xx..|..Xx|..Xx|.Xx.` |
| 23 | 0:46.20 | -12.6 | -13.1 | -16.4 | -22.9 | -21.2 | -23.3 | -30.6 | -31.7 | 1/4/1/9/8/8 | 2588 | -18.3 | -17.8 | +0.3 | `Xx..|..Xx|....|....` |
| 24 | 0:48.29 | -14.6 | -17.4 | -38.3 | -29.4 | -21.5 | -23.8 | -36.1 | -43.5 | 1/1/1/2/4/5 | 1507 | -5.2 | -0.0 | +0.2 | `....|....|....|....` |
| 25 | 0:50.38 | -11.0 | -10.0 | -12.0 | -21.1 | -20.4 | -22.6 | -30.8 | -31.8 | 5/8/5/10/8/8 | 2082 | -19.8 | -17.1 | +0.9 | `Xxxx|XxXX|xxXx|xXxx` |
| 26 | 0:52.46 | -9.8 | -9.2 | -11.5 | -17.7 | -20.2 | -22.7 | -30.7 | -34.7 | 5/7/6/12/10/9 | 1778 | -20.9 | -16.4 | -0.7 | `Xxxx|XxXx|xxXx|xXxx` |
| 27 | 0:54.55 | -11.0 | -10.1 | -12.2 | -19.2 | -20.1 | -22.9 | -30.9 | -31.8 | 5/7/8/11/8/8 | 2109 | -20.2 | -16.4 | +3.1 | `Xxxx|XxXx|xxXx|xXxx` |
| 28 | 0:56.64 | -9.7 | -9.0 | -11.2 | -18.0 | -19.7 | -22.3 | -30.9 | -34.8 | 5/6/13/11/10/9 | 1714 | -20.5 | -16.9 | +0.3 | `Xxxx|XxXx|xxXx|xXxx` |
| 29 | 0:58.73 | -11.0 | -10.0 | -12.1 | -20.9 | -20.3 | -21.8 | -30.8 | -31.9 | 5/8/11/11/8/8 | 2072 | -20.4 | -17.1 | +1.7 | `Xxxx|XxXx|xxXx|xXxx` |
| 30 | 1:00.81 | -9.9 | -9.2 | -11.5 | -17.9 | -20.6 | -22.4 | -30.6 | -34.7 | 5/5/6/11/10/9 | 1784 | -21.7 | -16.4 | -0.0 | `Xxxx|xxXx|xxXx|xXxx` |
| 31 | 1:02.90 | -10.8 | -10.1 | -12.4 | -18.4 | -19.8 | -22.8 | -30.6 | -31.8 | 5/6/9/12/8/8 | 2083 | -20.3 | -16.4 | +3.2 | `Xxxx|XxXx|xxXx|xXxx` |
| 32 | 1:04.99 | -9.7 | -9.0 | -11.1 | -18.8 | -19.6 | -22.5 | -30.9 | -34.6 | 5/7/9/12/10/9 | 1741 | -20.5 | -17.3 | +2.7 | `Xxxx|XxXx|xxXx|xXxx` |
| 33 | 1:07.07 | -10.6 | -9.9 | -12.2 | -20.2 | -20.3 | -21.2 | -30.4 | -31.1 | 5/7/7/11/8/10 | 2391 | -19.7 | -16.1 | +1.9 | `Xxxx|XxXx|xxXx|xXxx` |
| 34 | 1:09.16 | -9.6 | -9.0 | -11.4 | -17.9 | -20.4 | -21.3 | -30.4 | -33.2 | 5/5/10/10/10/11 | 2118 | -21.0 | -15.5 | -0.6 | `Xxxx|XxXx|xxXx|xXxx` |
| 35 | 1:11.25 | -10.3 | -9.9 | -12.3 | -19.6 | -20.3 | -20.0 | -29.7 | -31.0 | 5/7/8/10/3/9 | 2476 | -14.4 | -8.6 | +2.4 | `Xxxx|XxXx|xxXx|xXxx` |
| 36 | 1:13.33 | -9.1 | -8.7 | -11.2 | -17.6 | -20.2 | -19.6 | -29.9 | -33.1 | 5/8/11/9/2/11 | 2137 | -15.6 | -7.2 | +0.3 | `Xxxx|XxXx|xxXx|xXxx` |
| 37 | 1:15.42 | -10.6 | -9.9 | -12.2 | -20.7 | -20.6 | -20.0 | -30.4 | -31.0 | 5/8/15/8/8/10 | 2401 | -18.7 | -16.0 | +3.3 | `Xxxx|XxXx|xxXx|xXxx` |
| 38 | 1:17.51 | -9.5 | -9.0 | -11.3 | -17.8 | -20.7 | -20.5 | -30.4 | -33.3 | 5/6/6/8/10/11 | 2115 | -20.4 | -15.7 | +0.5 | `Xxxx|XxXx|xxXx|xXxx` |
| 39 | 1:19.59 | -10.3 | -9.9 | -12.3 | -19.6 | -20.1 | -20.9 | -29.8 | -30.8 | 4/7/6/9/3/9 | 2529 | -13.9 | -8.4 | +3.1 | `Xxxx|XxXx|xxXx|xXxx` |
| 40 | 1:21.68 | -9.5 | -8.8 | -11.1 | -18.0 | -19.7 | -22.3 | -34.7 | -33.4 | 5/7/9/8/0/11 | 2369 | -15.0 | -4.3 | +5.8 | `Xxx.|XxxX|XxXx|Xxxx` |
| 41 | 1:23.77 | -10.8 | -11.1 | -15.1 | -19.0 | -18.2 | -24.4 | -31.1 | -31.1 | 4/9/13/10/10/9 | 2668 | -14.2 | -20.1 | +0.8 | `Xx.x|..Xx|.x..|xxx.` |
| 42 | 1:25.86 | -9.9 | -9.6 | -12.4 | -18.2 | -18.3 | -23.9 | -31.3 | -33.6 | 6/14/11/13/14/11 | 2000 | -17.4 | -20.8 | +1.9 | `Xx..|xxXx|..Xx|.Xxx` |
| 43 | 1:27.94 | -10.6 | -11.1 | -15.0 | -19.5 | -18.3 | -22.0 | -31.2 | -31.2 | 5/8/9/8/10/9 | 2544 | -16.0 | -21.9 | +2.6 | `Xx.x|..Xx|.x..|..x.` |
| 44 | 1:30.03 | -10.0 | -9.7 | -12.5 | -18.4 | -18.2 | -24.0 | -31.2 | -33.7 | 7/10/11/16/13/12 | 2076 | -17.5 | -20.9 | +2.8 | `Xx.x|..Xx|.xXx|xXx.` |
| 45 | 1:32.12 | -10.7 | -11.1 | -15.2 | -19.3 | -18.5 | -22.3 | -31.0 | -31.2 | 4/7/14/7/10/9 | 2664 | -15.3 | -22.1 | +1.6 | `Xx.x|..Xx|.x..|xx..` |
| 46 | 1:34.20 | -9.9 | -9.6 | -12.4 | -18.2 | -18.8 | -22.6 | -31.4 | -33.6 | 6/13/13/10/14/10 | 2003 | -17.6 | -21.1 | +0.4 | `Xx..|xxXx|..Xx|.Xxx` |
| 47 | 1:36.29 | -10.8 | -11.1 | -15.0 | -19.4 | -18.7 | -23.1 | -31.1 | -31.3 | 5/9/9/10/10/9 | 2602 | -15.2 | -21.8 | +0.7 | `Xx.x|..Xx|.x..|..x.` |
| 48 | 1:38.38 | -10.3 | -10.4 | -13.5 | -20.0 | -18.3 | -22.3 | -28.3 | -32.9 | 6/11/10/12/14/11 | 2263 | -16.5 | -23.7 | +0.8 | `Xx.x|..Xx|.xXx|xxx.` |
| 49 | 1:40.46 | -10.5 | -11.0 | -15.2 | -19.2 | -18.3 | -21.4 | -31.0 | -31.2 | 4/9/13/8/8/9 | 2579 | -15.7 | -19.6 | +3.5 | `Xx.x|..Xx|.x..|xx..` |
| 50 | 1:42.55 | -9.9 | -9.7 | -12.4 | -18.6 | -18.9 | -22.7 | -31.0 | -33.5 | 6/12/12/10/12/12 | 2049 | -17.4 | -18.8 | +2.4 | `Xx..|xxXx|..Xx|.Xxx` |
| 51 | 1:44.64 | -11.0 | -12.0 | -17.2 | -19.8 | -18.1 | -22.4 | -31.1 | -31.2 | 4/8/9/7/8/9 | 2634 | -14.7 | -19.4 | +2.6 | `Xx.x|..xx|.x..|..x.` |
| 52 | 1:46.72 | -10.0 | -9.8 | -12.5 | -18.7 | -18.6 | -22.1 | -30.9 | -33.6 | 7/9/11/8/11/11 | 2075 | -16.9 | -18.8 | +2.3 | `Xx.x|..Xx|.xXx|xXx.` |
| 53 | 1:48.81 | -10.6 | -11.0 | -15.1 | -19.2 | -18.8 | -22.0 | -30.8 | -31.1 | 4/8/14/10/8/9 | 2628 | -15.2 | -19.5 | +1.8 | `Xx.x|..Xx|.x..|xx..` |
| 54 | 1:50.90 | -9.9 | -9.6 | -12.4 | -18.4 | -18.7 | -23.1 | -31.0 | -33.5 | 6/13/12/11/12/9 | 2053 | -17.3 | -18.6 | +3.6 | `Xx..|xxXx|..Xx|.Xxx` |
| 55 | 1:52.99 | -10.7 | -11.1 | -14.9 | -20.1 | -18.4 | -22.4 | -31.0 | -31.2 | 3/8/9/6/8/9 | 2565 | -15.7 | -18.9 | +3.2 | `Xx.x|..Xx|.x..|..x.` |
| 56 | 1:55.07 | -10.4 | -12.7 | -22.5 | -20.7 | -17.5 | -21.6 | -26.5 | -32.6 | 6/7/11/7/11/10 | 2196 | -7.7 | -10.0 | +0.3 | `...x|....|.x..|xxxx` |
| 57 | 1:57.16 | -9.5 | -9.3 | -12.1 | -20.2 | -18.0 | -20.1 | -30.2 | -31.5 | 5/7/6/4/3/3 | 2360 | -14.5 | -9.5 | +1.4 | `Xxxx|XxXx|xxXx|xXxx` |
| 58 | 1:59.25 | -9.0 | -9.2 | -12.6 | -17.4 | -17.9 | -20.1 | -30.8 | -34.4 | 5/6/6/5/6/11 | 1870 | -15.0 | -13.5 | -0.7 | `Xxxx|XxXx|xxXx|xXxx` |
| 59 | 2:01.33 | -9.4 | -9.4 | -12.4 | -19.7 | -18.0 | -19.9 | -29.9 | -31.7 | 5/7/6/6/2/9 | 2197 | -12.0 | -7.8 | +2.5 | `Xxxx|XxXx|xxXx|xXxx` |
| 60 | 2:03.42 | -9.1 | -9.2 | -12.4 | -17.4 | -18.6 | -20.0 | -29.9 | -34.3 | 5/8/12/6/2/10 | 1938 | -12.5 | -6.7 | -0.2 | `Xxxx|XxXx|xxXx|xXxx` |
| 61 | 2:05.51 | -9.7 | -9.5 | -12.2 | -20.9 | -18.1 | -20.0 | -30.7 | -31.8 | 5/7/10/6/6/10 | 2092 | -14.5 | -14.9 | +2.3 | `Xxxx|XxXX|xxXx|xXxx` |
| 62 | 2:07.59 | -9.1 | -9.3 | -12.7 | -18.0 | -18.1 | -20.3 | -30.8 | -34.5 | 5/4/6/9/6/11 | 1851 | -13.9 | -13.9 | -0.1 | `Xxxx|XxXx|xxXx|xXxx` |
| 63 | 2:09.68 | -9.4 | -9.5 | -12.5 | -19.3 | -17.7 | -19.7 | -30.1 | -31.6 | 5/8/5/2/2/9 | 2218 | -12.9 | -7.8 | +3.2 | `Xxxx|XxXx|xxXx|xXxx` |
| 64 | 2:11.77 | -9.1 | -9.3 | -12.5 | -18.0 | -18.0 | -20.1 | -30.1 | -34.3 | 5/5/7/6/2/10 | 1945 | -12.7 | -6.5 | +2.5 | `Xxxx|XxXx|xxXx|xXxx` |
| 65 | 2:13.85 | -9.7 | -9.5 | -12.3 | -21.3 | -17.8 | -20.5 | -30.0 | -31.3 | 5/6/12/9/7/9 | 2347 | -13.9 | -13.2 | +1.5 | `Xxxx|XxXx|xxXx|xXxx` |
| 66 | 2:15.94 | -9.3 | -9.6 | -12.8 | -18.4 | -18.8 | -20.7 | -30.4 | -34.4 | 5/6/9/10/5/11 | 1951 | -14.1 | -12.4 | +0.0 | `Xxxx|XxXx|xxXx|xXxx` |
| 67 | 2:18.03 | -9.1 | -9.2 | -12.4 | -18.5 | -18.0 | -19.8 | -29.7 | -31.5 | 5/7/10/6/3/10 | 2304 | -11.5 | -7.7 | +2.9 | `Xxxx|XxXx|xxXx|xXxx` |
| 68 | 2:20.12 | -8.9 | -9.1 | -12.3 | -18.4 | -17.7 | -19.7 | -29.6 | -34.0 | 5/8/10/6/2/10 | 2002 | -12.4 | -6.3 | +0.5 | `Xxxx|XxXx|xxXx|xXxx` |
| 69 | 2:22.20 | -9.7 | -9.4 | -12.3 | -20.2 | -18.2 | -20.1 | -30.2 | -31.5 | 5/8/12/8/6/10 | 2302 | -14.2 | -13.0 | +2.4 | `Xxxx|XxXx|xxXx|xXxx` |
| 70 | 2:24.29 | -8.9 | -9.1 | -12.6 | -17.0 | -18.1 | -20.5 | -30.3 | -34.2 | 5/6/9/8/6/10 | 1893 | -14.2 | -12.0 | -0.2 | `Xxxx|XxXx|xxXx|xXxx` |
| 71 | 2:26.38 | -9.4 | -9.4 | -12.4 | -19.9 | -18.1 | -19.2 | -29.3 | -31.6 | 5/6/7/4/2/10 | 2311 | -12.4 | -8.0 | +2.4 | `Xxxx|XxXx|xxXx|xXxx` |
| 72 | 2:28.46 | -9.0 | -9.6 | -13.6 | -18.2 | -17.4 | -19.6 | -33.0 | -41.6 | 5/6/8/1/0/2 | 1306 | -10.1 | -0.1 | +4.3 | `Xxxx|XxxX|xxXx|xXxx` |
| 73 | 2:30.55 | -8.2 | -8.8 | -12.7 | -21.4 | -16.3 | -17.5 | -28.2 | -30.9 | 5/8/8/5/4/2 | 2569 | -11.9 | -5.5 | +0.4 | `Xxxx|XxXx|xxXx|xXxx` |
| 74 | 2:32.64 | -7.9 | -8.3 | -11.5 | -17.6 | -17.6 | -18.2 | -27.8 | -33.8 | 5/7/7/5/5/6 | 2093 | -12.7 | -4.6 | -0.5 | `Xxxx|XxXx|xxXx|xXxx` |
| 75 | 2:34.72 | -8.2 | -8.8 | -12.6 | -19.8 | -15.4 | -18.9 | -28.2 | -31.3 | 4/8/8/10/5/9 | 2411 | -11.2 | -6.2 | -0.4 | `Xxxx|XxXx|xxXx|xXxx` |
| 76 | 2:36.81 | -7.7 | -8.2 | -11.6 | -18.1 | -15.8 | -18.8 | -28.1 | -33.7 | 5/7/13/4/4/6 | 2077 | -12.6 | -4.8 | -0.3 | `Xxx.|XxXx|xxXx|xXxx` |
| 77 | 2:38.90 | -8.4 | -8.9 | -12.4 | -21.3 | -16.2 | -18.0 | -28.3 | -31.2 | 5/7/13/5/7/8 | 2392 | -11.8 | -6.1 | +0.5 | `Xxxx|XxXx|xxXx|xXxx` |
| 78 | 2:40.99 | -8.0 | -8.3 | -11.5 | -17.7 | -17.2 | -18.8 | -27.9 | -33.9 | 5/6/10/7/5/6 | 2086 | -12.1 | -4.4 | -0.1 | `Xxxx|XxXx|xxXx|xXxx` |
| 79 | 2:43.07 | -8.3 | -8.8 | -12.5 | -18.8 | -15.7 | -18.7 | -28.1 | -31.3 | 5/8/10/7/4/9 | 2422 | -11.9 | -6.1 | -0.6 | `Xxxx|XxXx|xxXx|xXxx` |
| 80 | 2:45.16 | -7.8 | -8.2 | -11.7 | -19.1 | -15.7 | -18.5 | -28.0 | -33.8 | 5/7/10/7/4/5 | 2092 | -12.8 | -4.7 | -0.4 | `Xxxx|XxXx|xxXx|xXxx` |
| 81 | 2:47.25 | -8.1 | -8.7 | -12.5 | -21.0 | -16.4 | -17.5 | -28.4 | -31.1 | 5/7/12/5/5/5 | 2443 | -11.8 | -6.3 | +0.1 | `Xxxx|XxXx|xxXx|xXxx` |
| 82 | 2:49.33 | -7.9 | -8.3 | -11.5 | -17.6 | -18.5 | -18.0 | -28.0 | -33.6 | 5/5/10/6/4/5 | 2127 | -11.6 | -4.3 | +0.2 | `Xxxx|XxXx|xxXx|xXxx` |
| 83 | 2:51.42 | -8.3 | -8.9 | -12.7 | -19.7 | -16.1 | -18.1 | -28.3 | -31.2 | 5/7/7/3/6/6 | 2426 | -10.8 | -6.1 | -0.9 | `Xxxx|XxXx|xxXx|xXxx` |
| 84 | 2:53.51 | -7.5 | -8.1 | -11.7 | -18.1 | -16.0 | -17.7 | -28.0 | -33.5 | 5/11/14/7/4/5 | 2101 | -11.8 | -4.9 | -0.7 | `Xxxx|XxXx|xxXx|xXxx` |
| 85 | 2:55.59 | -8.1 | -8.7 | -12.3 | -20.7 | -16.6 | -16.9 | -28.3 | -31.3 | 4/8/13/6/7/6 | 2369 | -11.5 | -6.2 | +0.9 | `Xxxx|XxXx|xxXx|xXxx` |
| 86 | 2:57.68 | -8.0 | -8.4 | -11.8 | -17.7 | -17.5 | -18.6 | -27.9 | -33.9 | 5/6/8/8/5/5 | 2098 | -11.0 | -4.5 | +0.7 | `Xxxx|XxXx|xxXx|xXxx` |
| 87 | 2:59.77 | -8.1 | -8.8 | -12.7 | -20.5 | -15.8 | -17.0 | -28.3 | -31.2 | 5/7/9/4/6/5 | 2431 | -11.8 | -6.0 | -0.3 | `Xxxx|XxXx|xxXx|xXxx` |
| 88 | 3:01.85 | -7.9 | -9.0 | -14.1 | -17.8 | -16.1 | -17.0 | -29.9 | -38.5 | 5/4/6/2/2/2 | 1622 | -10.4 | -1.9 | -0.3 | `Xxxx|XxxX|xxXx|xXxx` |
| 89 | 3:03.94 | -9.6 | -10.8 | -15.1 | -21.2 | -20.0 | -18.1 | -28.5 | -31.1 | 2/2/10/4/6/6 | 2768 | -10.3 | -6.1 | +1.0 | `Xxxx|Xxxx|....|....` |
| 90 | 3:06.03 | -9.7 | -10.9 | -15.5 | -19.0 | -20.3 | -18.8 | -28.0 | -33.9 | 2/2/4/7/4/5 | 2454 | -9.6 | -4.1 | -0.5 | `Xxx.|Xxx.|....|....` |
| 91 | 3:08.12 | -9.7 | -10.7 | -14.9 | -20.6 | -19.2 | -18.4 | -28.5 | -31.3 | 2/4/8/4/5/6 | 2752 | -10.5 | -5.7 | +1.7 | `Xxxx|Xxx.|....|....` |
| 92 | 3:10.20 | -8.9 | -9.6 | -13.1 | -18.2 | -20.2 | -17.9 | -28.2 | -33.4 | 4/4/11/7/5/5 | 2327 | -10.7 | -4.3 | -0.7 | `Xxx.|Xxxx|.xXx|xXxx` |
| 93 | 3:12.29 | -9.8 | -11.0 | -15.3 | -21.8 | -20.1 | -17.7 | -28.4 | -31.2 | 2/2/14/3/5/6 | 2799 | -10.4 | -5.9 | +1.5 | `Xxx.|Xxx.|....|....` |
| 94 | 3:14.38 | -9.8 | -10.8 | -15.0 | -19.1 | -21.2 | -18.6 | -28.1 | -34.0 | 2/3/4/5/3/4 | 2457 | -10.4 | -4.4 | -0.2 | `Xxxx|Xxxx|....|....` |
| 95 | 3:16.46 | -9.7 | -10.8 | -15.0 | -20.9 | -19.0 | -18.7 | -28.3 | -31.3 | 2/4/13/7/5/6 | 2767 | -10.3 | -5.6 | +1.3 | `Xxx.|Xxxx|....|....` |
| 96 | 3:18.55 | -8.7 | -9.4 | -13.0 | -19.1 | -19.6 | -18.0 | -28.2 | -34.0 | 3/2/8/2/2/3 | 2298 | -9.8 | -3.2 | +1.1 | `Xxxx|Xxx.|..Xx|xXxx` |
| 97 | 3:20.64 | -15.6 | -18.1 | -61.7 | -35.2 | -23.1 | -23.1 | -39.8 | -55.6 | 0/0/1/0/0/0 | 1136 | -6.9 | -0.8 | +5.1 | `....|....|....|....` |
| 98 | 3:22.72 | -15.4 | -17.7 | -56.6 | -26.5 | -21.4 | -23.3 | -41.4 | -70.7 | 0/0/1/0/5/0 | 753 | -12.4 | -1.3 | +0.8 | `....|....|....|....` |
| 99 | 3:24.81 | -16.0 | -18.4 | -67.2 | -42.1 | -21.5 | -24.3 | -38.6 | -72.5 | 0/1/0/0/0/0 | 821 | -9.6 | -2.8 | +7.9 | `....|....|....|....` |
| 100 | 3:26.90 | -16.0 | -18.3 | -52.2 | -29.1 | -21.2 | -24.4 | -39.4 | -73.1 | 0/0/1/2/1/0 | 748 | -10.0 | -2.1 | +5.3 | `....|....|....|....` |
| 101 | 3:28.99 | -15.2 | -17.5 | -66.6 | -35.7 | -20.9 | -22.3 | -40.7 | -73.2 | 0/1/1/0/1/0 | 761 | -12.2 | -1.6 | +8.5 | `....|....|....|....` |
| 102 | 3:31.07 | -16.1 | -18.4 | -56.8 | -26.3 | -22.7 | -23.6 | -41.5 | -72.6 | 0/0/3/0/3/0 | 753 | -9.8 | -1.0 | +3.4 | `....|....|....|....` |
| 103 | 3:33.16 | -17.0 | -19.1 | -63.2 | -42.1 | -20.8 | -28.6 | -62.7 | -94.8 | 0/1/0/0/0/0 | 441 | -12.9 | -8.7 | +20.7 | `....|....|....|....` |
| 104 | 3:35.25 | — | -72.3 | -72.2 | -71.4 | -74.3 | -86.7 | -108.8 | -108.5 | 0/0/3/1/0/0 | 3599 | -13.2 | -8.4 | — | `....|....|....|....` |

## 8. Files

- `bars.csv` / `bars.json` — per-bar features (band power, onsets, stereo, centroid, intra-bar slopes, chroma, basic-pitch density, dropouts)
- `steps.npz` — 16-step layer levels per bar (sub/kick/snr/mid/hat)
- `transitions.json` — 16th-note band levels for bars 8, 9, 16, 17, 24, 25, 40, 41, 56, 57, 72, 73, 88, 89, 96, 97
- `bar_lufs.npy`, `vocal_rel.npy`, `boundaries.json`
- scripts: `features.py`, `boundaries.py`, `transitions.py`, `steps.py`, `vocal.py`, `vocal2.py`, `loud.py`, `wide.py`, `sweeps.py`, `write_md.py`

## 9. Method notes / caveats

- Section boundaries = bars where >=2 of {six band levels (>=3 dB, 2-bar means), band onset counts (>=2.5/bar), RMS (>=2 dB), centroid (>=18 %), side/mid (>=3 dB)} jump. Raw detector output is in `boundaries.json`; the 2-bar toggling of the wide layer in bars 33-40 and 57-71 trips it every 2 bars, which I classify as a layer toggle inside a section, not a boundary.
- "808", "kick", "hats", "clap", "pad" are names for band/transient behaviour (sub<60 Hz sustained notes; 60-120 Hz 60 ms attacks; >6 kHz transients; 400 Hz-2 kHz accents on 2 and 4; tonal wide 500 Hz-4 kHz layer). Instrument identity is inferred, medium confidence.
- The 2-bar loop (odd/even bar difference in >6 kHz, centroid and in the intro's sub) and the 8-bar phrase grid are both robust (every section change lands on bar 8n+1).
- Master is limited to 0.00 dBFS; crest factor 8-9 dB in the drops, 15-17 dB in the intro.
