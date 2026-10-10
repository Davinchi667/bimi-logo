# EVERYWHERE I GO [REMIND ME] (BNYX feat. Kid Cudi) - 808 / bass, measured from the instrumental

Source: `refs/eig_inst.wav` (44.1 kHz stereo, 3:37.3) plus a fresh 4-stem Demucs htdemucs separation of it (`eig/research/demucs4/htdemucs/eig_inst/{bass,drums,other,vocals}.wav`). Nothing was listened to; every number below is a measurement (scripts listed at the end). "dBFS" for the 808 means the peak of a 20-120 Hz band envelope on the Demucs bass stem; kick levels are on the Demucs drums stem or the mix as stated. Confidence tags: H = direct measurement with a cross-check, M = measurement with one plausible alternative reading, L = inference.

## 0. Grid (H) - same correction as drums.md

Tempo **115.000 BPM**, bar 1 beat 1 = **0.277 s** (first transient in the file). The brief's 114.84 BPM / 0.813 s puts "beat 1" on beat 2 and drifts 2.7 ms per bar. Cross-check in this task: phase concentration of 958 sub-band (25-90 Hz) onsets peaks at 114.99 BPM, t0 = 0.285 s (`bass_grid.py`); loud 808 hits sit on the 16th grid with median -8 ms, sd 3 ms (`bass_timing.py`); kick clicks sit at +2 ms (sd 1 ms). 1 beat = 521.7 ms, 1 bar = 2.087 s, 16th = 130.4 ms. Slot names: 1 1e 1& 1a 2 2e 2& 2a 3 3e 3& 3a 4 4e 4& 4a. Bar numbers below are on this grid (bar N starts at 0.277 + (N-1) x 2.087 s); sections start on 8-bar boundaries: intro 1-8, verse 1a 9-16, verse 1b 17-23 (+24 break), hook 1 25-40, verse 2 41-54 (+55-56 break), hook 2 57-72, bridge 73-88, hook 3 89-96, outro 97-104.

## 1. What is actually down there: four low layers, not one (H on existence, M on which is which)

| layer | where | notes (per 4-bar loop Bm-F#m-C-Em) | tuning vs A440 | level | spectrum | behaviour |
|---|---|---|---|---|---|---|
| S = the Roksopp sample's own bass | every bar incl. outro | B2 / F#2 / C3 / E2 (124.5 / 93.3 / 131.9 / 83.1 Hz) | **+14 c** (same as every key/pad partial: all +14 c) | -27 to -38 dBFS (mix, 20-150 Hz) | fundamental + octave | continuous |
| S8 = octave-down copy of S | bars 9-16 (and faintly under 17-24) | B1 / F#1 / C2 / E1 (62.24 / 46.65 / 65.97 / 41.59 Hz) | **+14 to +16 c** (tracks the sample, so it is pitched with it: octaver / sub of the sample, not the 808) | -7 to -12 dB below S's fundamental, -32 to -36 dBFS | pure-ish | continuous |
| SUB = sustained sub synth | bars 17-23 (ends at break bar 24), and (M) the -16 dB "floor" under hook even bars | B1 / F#1 / C2 / E1 (61.70 / 46.27 / 65.39 / 41.21 Hz) | **-1 to +1 c** (A440, in tune with ET, 14 c flat of the sample) | -20 to -22 dBFS, whole-bar notes (2.09 s), no decay (slope +2.5 dB/s) | H2 -10 to -12 dB, H3 -25 to -31, nothing above | gated to the bar, starts on/just after beat 1 (attack 10-90% ~20 ms) |
| 808 = the rhythmic 808 | bars 25-96 (absent 1-24 and 97-104) | B0 / F#1 / C1 / E1 (30.6-30.8 / 46.1 / 32.6 / 40.9-41.2 Hz) in hooks/bridge; octave-up melodic line in verse 2 | **0 +/- 10 c** (A440; sustained windows read -4 to -14 c, first 100 ms 0 to +9 c) | loud hits -3 to -4 dBFS, quiet hits -9 to -13 dBFS | H2 -4 to -7 dB, H3 -16 to -20 dB (see section 3) | retriggered on a dotted-8th pulse, decays ~-29 dB/s |

Consequences for the remake (H on the numbers, the musical choice is yours): the 808 and the SUB are tuned to A440 while the sample and all keys are +14 cents sharp. That leaves the 808's 2nd harmonic 0.7-0.8 Hz below the sample's bass (E1 808 H2 82.4 Hz vs sample E2 83.1 Hz; F#1 H2 92.5 vs 93.3), i.e. slow beating in the 80-95 Hz region on every F# and E bar. Hook 2 adds a second chord layer that IS at A440 (bar 57: F#4 +1 c, B3 0 c, B4 -1 c alongside the +14 c sample partials; `bass_tuning.py`), so from hook 2 the 808 is in tune with that layer but still 14 c flat of the sample. To copy the record, leave the 808 at A440 and pitch the sample +14 c; to make it "cleaner", tune the 808 +14 c (not what the record does).

There is **no 808 in bars 1-24**: Demucs puts everything below 120 Hz of bars 1-16 into the drums stem (bass stem -83 dBFS), and the mix low-band pitch between kicks is S/S8 at +14 c. The sub in the intro and verse 1a is the kick only. What the earlier arrangement notes called "808 on beats 1 & 3 from bar 9" is the E-tuned kick on 1 and 2& on the corrected grid (drums.md agrees).

## 2. Kick (H) - measured on the four isolated hits (bars 1/3/5/7 beat 1 = 0.280, 4.454, 8.627, 12.800 s), `kick_measure.py`

- One sample throughout (drums.md); here only the isolated hits were measured so nothing is contaminated by 808 or clap.
- Level: 25-250 Hz band peak **-0.2 to +0.1 dBFS** (mono mix), i.e. the kick, not the 808, owns the top of the sub band. 250-1 kHz peak -6 to -8 dBFS at +0-1 ms. Click: 1-8 kHz peak **-11 to -14 dBFS** at the onset, down 20 dB within 16-35 ms.
- Pitch (Hilbert instantaneous frequency, 25-200 Hz band): 0-10 ms 65-85 Hz (noise/click), **10-30 ms 120-140 Hz, 30-40 ms 53-58 Hz, 40-60 ms 42-47 Hz, 60-150 ms 40-45 Hz**, i.e. a ~130 -> 41 Hz sweep completed in about 40 ms, then a steady body. Body FFT (30-220 ms): **f0 = 40.4-40.7 Hz = E1 -20 to -30 c** (E1 = 41.20 Hz). So the kick is tuned to E, the loop's iv/ "home" note, and is ~25 c flat of the 808's E1 and ~40 c flat of the sample's E.
- Body harmonics: H2 -34 to -42 dB, **H3 -14 to -16 dB**, H4 -44 to -49 dB: odd-harmonic, i.e. a mildly (symmetrically) saturated sine, not a clipped one.
- Envelope (25-250 Hz, re peak): -6 dB at 92-105 ms, -10 dB at 126-135 ms, **-20 dB at 179-199 ms**, -30 dB not reached before the clap/next event. Audible length ~200 ms. 10-90% rise is inside the first 10-20 ms (peak at +9 to +22 ms after the click, +42 ms on the first hit).

Kick-808 interaction: when a loud 808 hit and a kick coincide the kick dominates the first ~100 ms (0 dBFS vs -4). In the hooks they almost never coincide (0 of 47 loud hits in hook 1 within 40 ms of a kick); the kick holds 1 and 2&, the 808 holds 2, 2a, 3&, 4e. See section 4.

## 3. The 808 sound (bass stem), `bass_timbre.py`, `bass_notes3.py`, `bass_zc.py`

**Pitch set and tuning.** Hooks/bridge: B0 30.6-30.8 Hz, F#1 46.1-46.3, C1 32.5-32.9, E1 40.9-41.3 (root of each bar: B, F#, C, E - the 808 plays roots only, no 5ths or 3rds, except the F#1 pickup at 4e of every E bar). Per-note pyin medians of all 165 loud hits fall in the 0..+10 c bin for every pitch class (B0 n=48, C1 n=48, F#1 n=38, E1 n=31); long-window FFTs on sustained portions read -4 to -14 c. Call it **A440 within +/-10 c** (H). The SUB layer is at -1..+1 c (H). Verse-2 notes: A1 55.0 (-13..+5 c), E2 82.2-82.3 (-5 c), C#2 69.1 (-5 c), D2 73.0-73.4 (-10..0), B1 61.2-61.9, E1 41.1-41.3 (H).

**Harmonic structure (H on numbers, M on interpretation).** Loud hits, sustained 50-500 ms window: **H2 = -4.7 dB median in hook 1 (p10 -13, p90 -2.4), -5.8 hook 2, -6.8 bridge; H3 = -16 to -20 dB; H4 -17 to -22; H5-H8 -20 to -30 dB**. "THD-ish" (sum of H2..H8 over H1) = **-3 to -5 dB**, almost all of it the octave. The ratio does not change with level inside a note (bar 72 E1: H2 -5.4 dB at 50-350 ms vs -5.6 dB at 600-1000 ms; bar 88: -5.0 vs -3.3), so it is a fixed waveform / layered octave, **not dynamic saturation or clipping**. Odd harmonics are weak (H3 < -16 dB), so no symmetric distortion either. Simplest matching recipe: sine 808 + octave-up sine 4-7 dB lower (or a sampler 808 that already has a strong 2nd harmonic), H3 around -17 dB, gentle low-pass above. The H2 ratio varies hit-to-hit between -1 and -13 dB; the F#1 and C1 notes of hook 2 read -12 dB while B0/E1 read -3 to -6, which is what you would get if a separate octave-up SUB layer (B1/C2) is present on the B and C bars but doubles the fundamental on F#/E bars (M).

**Attack.** Loud hits: 6 ms-envelope 10-90% rise 36-44 ms (median 40 ms, n=165), 4 ms-envelope on clean single hits 13-25 ms: in other words one cycle of the fundamental, the fastest a 30-46 Hz tone can start; no fade-in, no click (bass stem 1-8 kHz stays below -40 dBFS at 808 onsets). Quiet hits read 75-120 ms, but every quiet hit sits on or right after a kick, so that number is kick masking rather than a slower attack (M).

**Decay / length.** Loud hit peak **-3.4 to -3.9 dBFS** (p10 -5.5, p90 -2.5). Slope over 30-300 ms after the peak: **-29 dB/s median (p10 -46, p90 -19)**, so **-20 dB re peak at ~330-350 ms** when it is not re-hit (bars 25, 72, 88 measured 332/354/352 ms). Hits are re-triggered every 3 16ths (391 ms), so the note is normally cut by the next hit at about -10 to -12 dB. When nothing re-triggers (hook 3) the tail keeps going: bar 89 B0 -15 -> -36 dB over 1.4 s (-17 dB/s), bar 90 F#1 -14 -> -35 dB over 1.9 s (-12 dB/s), i.e. a two-stage envelope: fast -29 dB/s for ~0.3 s, then ~-12 to -17 dB/s. In hooks 1/2 and the bridge the long F#1/E1 note on even bars does NOT keep falling: it settles at **-16 +/- 2 dBFS from ~300 ms after the 2a hit to the bar end (1.3 s)**, which is either the SUB layer holding the root or a sustain stage (M; hook 3, where the floor is absent, is the reason to prefer "separate sustained layer").

**Glides / pitch envelope: none on the hits (H).** Cycle-by-cycle zero-crossing tracking of clean loud hits: bar 25 B0 -2/0/-4 c over 0-300 ms, bar 27 C1 +9/-4/+1, bar 92 E1 -5/+5/-1, bar 92 F#1 +8/+5/0, bar 72 E1 -3/+2/+1/+2/-10. No pitch bends between notes (the pyin glide test - monotonic change >= 70 c inside a note - returns zero notes in 307). Two things that look like glides and are not: (a) quiet notes that start under a kick read +25 to +65 c sharp for the first 100-200 ms (bars 89, 93) and basic-pitch writes a +33 c bend at the start of those same notes; that is the kick's 41 Hz tail pulling the zero crossings, so treat it as kick leakage, not an 808 pitch envelope (M); (b) verse 2 bars 44/48/52/56 at 3&: E1 steps down to D1 (-200 c) inside <= 100 ms and back to E1 on beat 4; the step is complete within the first 100 ms window, so if it is a slide it is a very short one (M).

**Per-section 808 level (bass stem, 20-120 Hz RMS per bar):** verse 1b SUB -25 dB; hook 1 odd bars -13.4, even -14.5 to -15; verse 2 -18 to -20; hook 2 -13.2 to -13.8 (both odd and even, the most even section); bridge odd -13.5 to -14, even -15 to -16; hook 3 -18 to -20 on F#/B/C bars, -14.5 on E bars (the two loud hits); bars 72 and 88 (drums out) -12.3 / -12.6 (loudest bars, the 808 carries alone); bar 24 -41.7, bar 56 -18.4 (808 continues through the drum drop), bars 97-104 below -47 dB (no bass at all under the outro).

## 4. Patterns and the kick relationship, by section (H; counts are bars out of 8 in `bass_notes3.py` output)

Odd bars = B and C bars (roots B0, C1); even bars = F# and E bars (roots F#1, E1).

- **Verse 1a, bars 9-16:** no 808, no SUB. Kick 1 and 2& every bar. Sample bass S + octave-down S8 only.
- **Verse 1b, bars 17-23:** SUB enters at -20 dBFS, one whole-bar root per bar (B1, F#1, C2, E1 - note the B and C are an octave ABOVE the hook's B0/C1), starting on beat 1 (detected 1 or 1e, slow 20-80 ms rise), held gated to the bar line. Kicks 1, 2& (odd) / 1, 2&, 3&, 4e (even). Bar 24 = everything out except the sample.
- **Hook 1, bars 25-40:** the main design.
  - Odd (B/C) bars: 808 loud hits at **2, 2a, 3&, 4e** (8/8 bars each) = 16th positions 4, 7, 10, 13 = a dotted-8th pulse starting on beat 2 that lands on the next downbeat; measured inter-hit spacing 387-399 ms = 3 16ths. A quiet root note at beat 1 (-11 dBFS, 4/8 bars detected) sits under the beat-1 kick. Kick only on **1 and 2&**. The 808 therefore sits BETWEEN the kicks: 808 on the "a" and "e" positions, kick on the beat/"&".
  - Even (F#/E) bars: 808 loud hits at **2 and 2a** only (7/8, 6/8), the 2a note then held to the bar end (1.7 s, at the -16 dB floor); quiet root at 1e (6/8) under the beat-1 kick. Kick takes over the pulse: **1, 2&, 3&, 4e** (7-8/8). On E bars the last 808 note is an **F#1 at 4e** (bars 28, 32, 36, 40; -8 to -13 dBFS) = pickup into the next B bar.
  - Bar 40 (fill): kick 1, 2, 3, 4; 808 E1 at 1e(q), 2e(q), 2a, 3&, then F#1 at 4e.
  - Net 2-bar cell: odd bar "808 plays the dotted-8th pulse, kick marks 1 and 2&"; even bar "kick plays 1, 2&, 3&, 4e, 808 answers with 2, 2a and holds". That alternation is the groove; the hats add 16ths from bar 33 (drums.md) without changing it.
- **Verse 2, bars 41-54 (+55-56):** the same 808 drops ~6-9 dB (peaks -10 to -13 dBFS, nothing above -9) and plays a melodic 4-bar riff an octave up, with the kick at 1 and 2& (odd) / 1, 2&, 3&, 4e (even). 8th-grid reading from the stem (`bass_fine.py`, bars 41-44 = 45-48 = 49-52 = 53-56):
  - Bar 41 (Bm): B0 at 1e (0.4 beat, under/after the kick) - C#2 at 2 (0.5) - D2 at 2a (0.5) - C#2 at 3a (0.3) - B0 at 4e (0.15) - B1 at 4& (0.4).
  - Bar 42 (F#m over A): A1 at 1e (0.4) - F#1 at 2 (0.5) - A1 at 2a (0.5) - A1 at 3a (0.3) - E1 at 4& (0.4).
  - Bar 43 (Am): A1 at 1e (0.4) - E1 at 1a (short) - E2 at 2e/2 (0.4) - A1 at 2a (0.4) - E1 at 3e (0.6) - A1 at 4& (0.4).
  - Bar 44 (Em): E2 at 1e (0.4) - E1 at 1a (short) - **rest 2e-2a (bass stem -45 to -55 dBFS, the kick at 2& plays into silence)** - E2 at 2a/3 (0.4) - E1 at 3e -> D1 at 3& (-200 c step) - E1 at 4 - A1 at 4& (pickup).
  - Timing caveat: notes labelled 1e and 2a follow a kick (1, 2&) by one 16th; a note starting ON the kick would be masked for ~100 ms and surface at the same place, so those two could be on-the-kick (M). The 3e, 3a, 4, 4&, 4e notes are not near a kick and are solid.
- **Hook 2, bars 57-72:** 808 plays the full dotted-8th pulse **2, 2a, 3&, 4e on every bar** (odd 8/8, even 8/8 for 2, 3&, 4e and 7/8 for 2a), i.e. the even-bar kick pulse of hook 1 is handed to the 808; kicks reduce to **1 and 2&** on every bar. Quiet root on beat 1 on 3-4 bars of each parity. Bar 72 (drums out): 808 alone, 1e(q), 2, 2a, 3&, then F#1 4e, loudest bass bar.
- **Bridge, bars 73-88:** back to the hook-1 scheme (odd bars 808 2, 2a, 3&, 4e; even bars 808 2, 2a + kick 1, 2&, 3&, 4e), 808 ~1 dB quieter than hook 1 on even bars. Bars 87-88 drums out, 808 keeps the pulse (bar 88 = same as bar 72).
- **Hook 3, bars 89-96:** stripped. Kick on **1 and 2** of every bar (not 2&). 808 = quiet root notes only (-12 to -15 dBFS, long decay, no floor): B0 from beat 2 of bar 89/93 (beats 1-2 are the previous F#1 tail), F#1 at 1 and re-hit at 2 (bars 90/94), C1 at 1 (bars 91/95); on the E bars (92, 96) two loud hits return: **E1 at 3& (-5 / -4 dBFS) and F#1 at 4e (-5 dBFS)**. No 808 on beats 3-4 of the B, F#, C bars.
- **Outro 97-104:** no 808, no SUB, no kick; only the sample (its bass S at +14 c).

## 5. Bar-by-bar, bars 1-48 (generated from `bass_notes.json`; chord names from the chroma/annotation work in `arrangement.json` and `grid_check.txt`)

Slot = 16th position of the onset (loud hits are on the grid within +/-10 ms; q = quiet hit < -9 dBFS, timing +/-1 16th because of kick masking; ~ = onset found by pitch change, not level). Length = time to the next onset, or to -20 dB re peak if sooner.

| bar | section | chord | sample bass / sub layer (note, cents, dBFS 20-150 Hz) | 808 hits: slot:note(peak dBFS bass-stem 20-120, length to next onset/-20 dB); q = quiet (< -9 dB); ~ = pitch-change onset | kick slots |
|---|---|---|---|---|---|
| 1 | intro | Bm | B2+14c -34 | - | 1 |
| 2 | intro | F#m | F#2+14c -27 | - | - |
| 3 | intro | C | C3+14c -37 | - | 1 |
| 4 | intro | Em | E2+14c -29 | - | - |
| 5 | intro | Bm | B2+14c -34 | - | 1 |
| 6 | intro | F#m | F#2+14c -27 | - | - |
| 7 | intro | C | C3+14c -37 | - | 1 |
| 8 | intro | Em | E2+14c -29 | - | - |
| 9 | verse1a | Bm | B2+14c + B1+14c -34 (oct-down of sample) | - | 1 2& |
| 10 | verse1a | F#m | F#2+14c + F#1+15c -32 | - | 1 2& |
| 11 | verse1a | C | C3+14c + C2+15c -36 | - | 1 2& |
| 12 | verse1a | Em | E2+14c + E1+15c -34 | - | 1 2& |
| 13 | verse1a | Bm | B2+14c + B1+14c -34 (oct-down of sample) | - | 1 2& |
| 14 | verse1a | F#m | F#2+14c + F#1+15c -32 | - | 1 2& |
| 15 | verse1a | C | C3+14c + C2+15c -36 | - | 1 2& |
| 16 | verse1a | Em | E2+14c + E1+15c -34 | - | 1 2& |
| 17 | verse1b | Bm | B1 -1c -22 (A440 sub, held 2 s) | - | 1 2& |
| 18 | verse1b | F#m | F#1 +1c -22 | 1e~:F♯1q(-22dB,2088ms) | 1 2& 3& 4e |
| 19 | verse1b | C | C2 0c -21 | 1e~:C2q(-21dB,2134ms) | 1 2& |
| 20 | verse1b | Em | E1 0c -21 | 1e:E1q(-21dB,4114ms) | 1 2& 3& 4 |
| 21 | verse1b | Bm | B1 -1c -22 (A440 sub, held 2 s) | - | 1 2& |
| 22 | verse1b | F#m | F#1 +1c -22 | 1~:F♯1q(-22dB,2104ms) | 1 2& 3& 4e |
| 23 | verse1b | C | C2 0c -21 | 1e~:C2q(-24dB,2046ms) | 1 2& |
| 24 | break | Em | sample only, no sub | - | - |
| 25 | hook1 | Bm | - | 1:B0q(-11dB,500ms) 2:B0(-5dB,387ms) 2a:B0(-7dB,399ms) 3&:B0(-6dB,394ms) 4e:B0(-6dB,455ms) | 1 2& |
| 26 | hook1 | F#m | - | 1e:F♯1q(-13dB,454ms) 2:F♯1(-6dB,386ms) 2a:F♯1(-8dB,1698ms) | 1 2& 3& 4e |
| 27 | hook1 | C | - | 2:C1(-5dB,393ms) 2a:C1(-9dB,389ms) 3&:C1(-5dB,397ms) 4e:C1(-5dB,462ms) | 1 2& |
| 28 | hook1 | Em | - | 1e:E1q(-12dB,446ms) 2:E1(-5dB,388ms) 2a:E1q(-10dB,854ms) 4&:F♯1q(-11dB,380ms) | 1 2& 3& 4e |
| 29 | hook1 | Bm | - | 1:B0q(-11dB,465ms) 2:B0(-5dB,391ms) 2a:B0(-8dB,396ms) 3&:B0(-5dB,388ms) 4e:B0(-5dB,463ms) | 1 2& |
| 30 | hook1 | F#m | - | 1e:F♯1q(-12dB,453ms) 2:F♯1(-6dB,389ms) 2a:F♯1q(-9dB,1693ms) | 1 2& 3& 4e |
| 31 | hook1 | C | - | 2:C1(-5dB,392ms) 2a:C1(-8dB,394ms) 3&:C1(-6dB,388ms) 4e:C1(-5dB,917ms) | 1 2& |
| 32 | hook1 | Em | - | 2:E1(-6dB,328ms) 2a:E1(-8dB,849ms) 4e~:F♯1q(-11dB,853ms) | 1 2& 3& 4e |
| 33 | hook1 | Bm | - | 2:B0(-6dB,388ms) 2a:B0(-8dB,394ms) 3&:B0(-5dB,391ms) 4e:B0(-5dB,919ms) | 1 2& |
| 34 | hook1 | F#m | - | 2:F♯1(-6dB,384ms) 2a:F♯1(-8dB,1695ms) | 1 2& 3& 4e |
| 35 | hook1 | C | - | 2:C1(-6dB,392ms) 2a:C1(-8dB,394ms) 3&:C1(-5dB,392ms) 4e:C1(-5dB,464ms) | 1 2& |
| 36 | hook1 | Em | - | 1e:E1q(-12dB,447ms) 2:E1(-5dB,388ms) 2a:E1(-8dB,858ms) 4&~:F♯1q(-13dB,838ms) | 1 2& 3& 4e |
| 37 | hook1 | Bm | - | 2:B0(-5dB,389ms) 2a:B0(-8dB,397ms) 3&:B0(-6dB,391ms) 4e:B0(-5dB,466ms) | 1 2& |
| 38 | hook1 | F#m | - | 1e:F♯1q(-14dB,445ms) 2:F♯1(-5dB,392ms) 2a:F♯1(-8dB,1225ms) | 1 2& 3& 4e |
| 39 | hook1 | C | - | 1~:C1q(-12dB,469ms) 2:C1(-5dB,391ms) 2a:C1(-8dB,393ms) 3&:C1(-5dB,394ms) 4e:C1(-6dB,460ms) | 1 2& |
| 40 | hook1 | Em | - | 1e:E1q(-12dB,524ms) 2e:E1q(-12dB,321ms) 2a:E1(-6dB,387ms) 3&:E1(-6dB,388ms) 4e:F♯1(-8dB,444ms) | 1 2 3 4 |
| 41 | verse2 | Bm | - | 1e:B0q(-13dB,793ms) 2a:D2q(-13dB,930ms) 4&:B1q(-11dB,322ms) | 1 2& |
| 42 | verse2 | F#m/A | - | 1e:A1q(-18dB,62ms) 1e:A1q(-12dB,394ms) 2:F♯1q(-11dB,388ms) 2a:A1q(-12dB,918ms) 4&:E1q(-13dB,386ms) | 1 2& 3& 4e |
| 43 | verse2 | Am | - | 1e:A1q(-12dB,297ms) 1a:E2q(-12dB,391ms) 3e:E1q(-12dB,621ms) 4&:A1q(-10dB,288ms) | 1 2& |
| 44 | verse2 | Em | - | 1e:E2q(-13dB,301ms) 1a:E1q(-12dB,137ms) 3e:D1q(-12dB,394ms) 4:E1q(-13dB,181ms) 4&:A1q(-12dB,296ms) | 1 2& 3& 4 |
| 45 | verse2 | Bm | - | 1e:B1q(-21dB,62ms) 1e:B1q(-13dB,743ms) 2a:D2q(-13dB,929ms) 4&:B1q(-11dB,281ms) | 1 2& |
| 46 | verse2 | F#m/A | - | 1e:A1q(-12dB,423ms) 2:F♯1q(-11dB,386ms) 2a:A1q(-12dB,920ms) 4&:E2q(-13dB,179ms) 4a:E1q(-13dB,207ms) | 1 2& 3& 4 |
| 47 | verse2 | Am | - | 1e:A1q(-12dB,299ms) 1a:E2q(-12dB,483ms) 2a:A1q(-12dB,299ms) 3e:E1q(-12dB,397ms) 4:A0q(-15dB,223ms) 4&:A1q(-10dB,298ms) | 1 2& |
| 48 | verse2 | Em | - | 1e:E2q(-15dB,297ms) 1a:E1q(-12dB,149ms) 3e:D1q(-12dB,398ms) 4:E1q(-13dB,237ms) 4&:A1q(-11dB,388ms) | 1 2& 3& |

Reading the table: bars 49-56 repeat 41-48 (per-bar dominant stem notes B1/C#2/D2 | A1/F#1/E1 | A1/E2/E1 | E2/A1/E1 for both halves, `bass_stem_f0.py`); bars 57-72, 73-88 and 89-96 are summarised in section 4 and listed in full in `bass_bars.txt`.

## 6. Section summary (what to program)

| section | bars | 808 register / notes | 808 rhythm | kick | 808 level |
|---|---|---|---|---|---|
| intro | 1-8 | none (sample bass B2/F#2/C3/E2 +14 c only) | - | 1 of odd bars | - |
| verse 1a | 9-16 | none; sample + octave-down sample layer (B1/F#1/C2/E1 +15 c, -34 dBFS) | - | 1, 2& | - |
| verse 1b | 17-23 | SUB B1/F#1/C2/E1 at A440, whole bar, no decay, H2 -11 dB | one note on beat 1, held | 1, 2& (+3&, 4e even bars) | -21 dBFS |
| break | 24 | nothing | - | none | - |
| hook 1 | 25-40 | B0 / F#1 / C1 / E1 (+F#1 4e on E bars) | odd: 2 2a 3& 4e; even: 2 2a (held) | odd 1 2&; even 1 2& 3& 4e | hits -3 to -6, beat-1 note -11 to -13 |
| verse 2 | 41-56 | melodic riff: B0 C#2 D2 C#2 B0 B1 / A1 F#1 A1 A1 E1 / A1 E1 E2 A1 E1 A1 / E2 E1 (rest) E2 E1-D1 E1 A1 | 5-7 notes a bar on 1e 2 2a 3a/3e 4 4& (see 4) | odd 1 2&; even 1 2& 3& 4e | -10 to -13 |
| hook 2 | 57-72 | B0 / F#1 / C1 / E1 (+F#1 4e on E bars) | 2 2a 3& 4e every bar | 1 2& every bar | -3 to -6 |
| bridge | 73-88 | as hook 1 | as hook 1 | as hook 1 | hits -3 to -6 |
| hook 3 | 89-96 | roots only, quiet, long decay; E bars add E1 3& + F#1 4e loud | 1 (or 2) quiet; even E bars 3& 4e loud | 1, 2 every bar | -12 to -15 (loud hits -4 to -5) |
| outro | 97-104 | none | - | none | - |

Remake recipe in numbers (all measured above): 808 at A440 (or +14 c if you want it to match the sample), roots B0/F#1/C1/E1 (B0 = 30.87 Hz, so the sub needs to reach 30 Hz), sine fundamental with an octave at -5 dB and a 3rd harmonic at -17 dB, instant attack (<= 1 cycle), two-stage decay (-29 dB/s for 0.3 s then -12 to -17 dB/s), no glide, no pitch envelope, loud hits peaking 3-4 dB below the kick in the sub band, quiet beat-1 notes 8-10 dB below the hits; a separate sustained sub (SUB) on the roots B1/F#1/C2/E1 at -21 dBFS, gated to the bar, for bars 17-23 and (probably) under the hooks' even bars; kick = E1 (40.5 Hz body, 130 -> 41 Hz sweep in 40 ms, -20 dB at 180 ms, 3rd harmonic -15 dB, click -12 dBFS at 1-8 kHz); kicks on 1 and 2&, 808 on 2 2a 3& 4e.

## 7. Caveats

- The Demucs bass/drums split is the basis of the 808-vs-kick separation. Checks that it behaved: the drums stem contains the click and the 120 -> 41 Hz sweep, the bass stem contains no click (1-8 kHz < -40 dBFS at 808 onsets), the stems' onsets never coincide in the hooks, and the bass stem is empty (-83 dBFS) in bars 1-16 where the mix's low band is explained by the +14 c sample layers. The one known leak is the kick's E1 tail into the bass stem at -14 to -18 dBFS for ~150 ms after each kick, which is why beat-1/2 quiet notes are tagged M for timing and pitch.
- "Quiet beat-1 note" on even bars (1e) could be on the downbeat and masked; on odd bars it is measured on the downbeat.
- Whether the -16 dB floor on hook even bars is a sustained layer or a sustain stage of the 808 cannot be settled from a mix; hook 3 behaves like "no sustained layer", which is why the table calls it SUB.
- Chord names in the table come from the earlier chroma/annotation work (Bm-F#m-C-Em; verse 2 reads Bm | F#m/A | Am | Em), not re-measured here.
- The basic-pitch MIDI was used only as a cross-check: its sub-C3 notes agree with the stem on pitch classes (F#1 102, E1 65, B1 70, C1 33, B0 18 notes) and its 41 pitch-bend runs (all +33 c, at note starts in the hook odd bars) are the kick-leak effect described in section 3.

## 8. Files (all under `eig/research/`)

`bass.md` (this), `bass_notes.json` (every 808 onset: t, bar, slot, dev ms, note, cents, peak, length, H2, H3, attack, decay slope, kick distance; and every kick), `bass_bars.txt` (per-bar listing, all 104 bars), `bass_table48.md` (the table above), `bass_f0.npy` / `bass_stem_f0.npy` (pyin tracks: t, f0, voicing, sub/mid envelopes; 8 ms hop), `demucs4/` (stems), scripts: `bass_grid.py` (grid), `kick_measure.py` (kick), `bass_f0.py` / `bass_stem_f0.py` (pitch tracks), `bass_diag.py` / `bass_fine.py` (raw dumps), `bass_notes3.py` (segmenter), `bass_timing.py` (grid bias), `bass_timbre.py` (harmonics/envelopes), `bass_zc.py` (cycle-by-cycle pitch), `bass_tuning.py` (layer tuning), `bass_sample.py` (sample bass line), `bass_table.py` (table).
