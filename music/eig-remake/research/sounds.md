# EVERYWHERE I GO [REMIND ME] (BNYX x Kid Cudi) — instrumental sound-design fingerprint

Source: `refs/eig_inst.wav` (44.1 kHz stereo, 3:37.3). Every number below is **measured** on that file unless tagged `[web]` or `[inferred]`. Scripts and raw tables live next to this file (`*.py` / `*.txt`); `common.py` holds the grid.

Confidence tags: **H** = direct measurement, stable across repeats; **M** = measurement with an interpretation step (what the layer *is*); **L** = plausible but not verified.

**Bar numbering:** this file counts bars from **0** (bar 0 downbeat = 0.265 s). The sibling files in this folder (`structure.md`, `drums.md`, `bass.md`, `grid.json`) count from **1** with bar 1 at 0.277-0.291 s — the same bars, so `their bar = my bar + 1` (my drop 1 = bars 24-39 = their 25-40; my outro 96-101 = their 97-102). Tempo (115.000) and bar length agree with all of them.

---

## 0. Global measurements (correct the brief)

| Item | Value | Conf | How |
|---|---|---|---|
| Tempo | **115.000 BPM** (beat 0.52174 s, bar 2.08696 s, 16th 130.4 ms) | H | Onset-envelope autocorrelation at 4/8/16/32-bar lags: 115.000 / 114.999 / 114.998 / 114.998. The brief's 114.84 drifts 0.3 s by the end of the track; do not use it. |
| Drum grid downbeat | **T0 = 0.265 s** (bar n starts at 0.265 + n·2.08696) | H | Isolated intro kicks onset at 4.439 / 8.613 / 12.787 / 16.969 s; first hit of the file at 0.278 s. |
| Sample grid | chord changes land **+22…+35 ms after** the drum grid | M | chroma-flux onsets at bar boundaries (bars 1-16: median -11…-15 ms vs 0.302 s). The sampled layer is simply late/loose vs the programmed drums; quantise drums, nudge sample +25 ms. |
| Length | music 0.278 s → hard digital cut at **215.3 s**; 103 bars + 1 partial | H | end envelope: -17 dB sustained then -67 dB at 215.41 s. No reverb tail at the end (abrupt stop). |
| Chord loop | **Bm – F#m – C – Em**, one chord per bar, 4-bar cycle, unchanged for the whole song | H | basic-pitch MIDI + partial lists; chords change on the downbeat. Reads as B minor (i – v – ♭II – iv); the brief's "E minor" chroma reading is the same pitch set. |
| Tuning | **sampled layer +14 cents** (A ≈ 443.6 Hz); kick/808/pad-2/glide-bass ≈ A440 (±5 c) | H | every sample partial sits at +13…+16 c (B2 124.50, F#2 93.27, C3 131.90, E2 83.13 …); 808 fundamentals at -14…+5 c. +14 c = a 0.81 % speed change (e.g. ~114.1 → 115 BPM) if the sample was re-pitched `[inferred, L]`. |
| Loudness / master | RMS -8.9…-9.6 dBFS in drops, -15.8 intro, -18.5 outro; peaks **hard-clipped at 0 dBFS** (20 672 samples > 0.999, 5 235 clipped runs, longest 20 samples); crest 9 dB in drops | H | `k_noise.txt` |
| Stereo overall | L/R corr 0.917; side −13.6 dB vs mid; sub < 120 Hz is mono (side −27 dB) | H | `analyse.py` |
| Vinyl noise | **none** (0 crackle clicks/s in 3-16 kHz during the drumless outro; noise floor of the file is digital silence −80 dBFS) | H | `k_noise.txt` |
| Vocal textures / hums | **none detected** in the instrumental (pyin 80-600 Hz on mid and side, bars 56-88: voiced probability < 0.15, no 4-7 Hz vibrato energy) | M | `q4_vocal.txt`. Cudi's humming/choral vocals mentioned in press `[web]` are on the vocal version only. |
| Delay echoes | **none** (envelope autocorrelation of clap, hat, pad and side bands shows only the rhythmic self-similarity; no isolated 8th/dotted-8th/quarter repeat) | H | `j_space.txt`, `c2_sideecho.txt` |
| Sidechain pumping | only light ducking: ≤ 3-4 dB dip 40-100 ms after kicks in bars 56-72, none measurable in drop 1 → limiter/clipper behaviour, not a slow pump | M | `k3_pump.txt` |

Web context `[web]`: single released 30 Jan 2026 (Lyfestyle/Field Trip/Capitol), on BNYX's album *GENESIS FM* (May 2026); press describes a "juiced-up sample of Röyksopp's Remind Me", "humming keys, rubbery bass, snapping percussion, and choral vocals" and "clap back beats", Cudi "between wistful warmth and robotic vocoder" — sources: https://www.universalmusic.ca/?p=123123 , https://music.mxdwn.com/2026/02/news/kid-cudi-bnyx-team-up-for-collaborative-new-single-everywhere-i-go-remind-me/ , https://www.universalmusic.ca/?p=124078 . Röyksopp "Remind Me" (2002, vocal Erlend Øye) exists as album version 3:40 and Someone Else's Radio Remix 4:03 — https://en.wikipedia.org/wiki/Remind_Me_(R%C3%B6yksopp_song) . **Which Röyksopp version/section is sampled and the original's BPM were not verified from a human source** (songbpm-type sites excluded per rules).

---

## 1. Layer inventory

| # | Layer | Where (bars, drum grid) | Peak/level | Tuning | Width (side−mid) | Conf |
|---|---|---|---|---|---|---|
| 1 | SAMPLE-BASS (Röyksopp root note, octave 2) | 0-23, 26/28/30… (C & some Bm bars of drop 1), 40-101 | −17 dBFS sustained | +14 c | −14.7 dB | H |
| 2 | SAMPLE-PAD (stacked-triad chord, 7.6 Hz vibrato) | same as 1; **−16 dB in drop 1 (24-39)**; low-passed ~2 kHz in outro 96-101 | −17 dBFS | +14 c | −15 dB (intro) | H |
| 3 | SAMPLE-LEAD (melody line from the same sample) | 24-39 only | peaks −16 dBFS per note | +14 c | −12 dB | M |
| 4 | SAMPLE-SUB (octave-down of the sample bass) | 8-15 | −30 dBFS | +14 c | mono | M |
| 5 | KICK (sub kick, ~41 Hz) | every 2 bars 0-7; 2/bar 8-15; 2-4/bar 16-95 | **0 dBFS** (clips) | fixed ~41 Hz | −31 dB (mono) | H |
| 6 | 808 (chord-root sine, heavily saturated) | 16-23 octave-up @ −21 dB; 24-39, 56-95 full @ −4…−11 dB | −4 dBFS peak | A440 ±15 c | −36 dB (mono) | H |
| 7 | GLIDE-BASS (portamento melodic bass, wide) | 40-55 (replaces full 808) | −8…−13 dBFS | ≈A440 (−5 c) | −10 dB above 90 Hz, mono below | M |
| 8 | PAD-2 (second chord synth, no vibrato, unison) | 56-101 (incl. outro at −5 dB) | ~−8 dB below SAMPLE-PAD | 0 c (±3.5 c unison) | −3…−6 dB in oct 5-6 | M |
| 9 | CLAP (4-flam) + wide reverb | beats 2 & 4, bars 0-95 (not 23, 39, 55, 71, 87) | −9 dBFS | — | body −18 dB, tail −2 dB | H |
| 10 | HAT closed (main) | 0-95 | −19.5 dBFS, no velocity variation | — | −15 dB | H |
| 11 | HAT downbeat variant | 16th 0 | −20 dBFS | — | −21 dB | M |
| 12 | PERC-2 (soft, dark, wide hat/shaker) | 72-95 on 16ths 5-9, 13-15 | −26…−29 dBFS | — | −7 dB | M |
| 13 | KNOCK (16th-2 low-mid perc) | 0-95 | −16 dBFS | ~350-440 Hz noisy | −9.5 dB | M |
| 14 | REVERSE SWELL FX | last 2 s before bars 24, 56, 96 | rises −26 → −14 dB (side) | fixed partials | L/R corr ≈ 0 (fully wide) | H |

Not present: vinyl noise, vocal hums, discrete delays, risers with pitch sweeps, white-noise risers (the swells are tonal/noisy reverse textures), filter sweeps on the pad.

---

## 2. Per-layer fingerprints and recipes

### 2.1 SAMPLE-BASS — Röyksopp root note (octave 2)

Measured (intro bars 0-3, outro 96-101):
* Pitches: B2 124.50 Hz (+14 c), F#2 93.27 (+14 c), C3 131.90 (+14 c), E2 83.13 (+14 c). One note per bar, sustained the whole bar, no gap at chord changes (level continuous within ±3 dB across bar lines; no attack transient — the apparent stab at 0.278 s is the kick).
* Level −17 dBFS; it is the loudest partial of the sample (0 dB ref in partial lists).
* **No vibrato** (B2: 2.6 c pk-pk residual; C3: 4 c). Mono-ish (side −14.7 dB).
* Harmonics: 2nd (B3 249.0 Hz) at −8 dB in outro / 0 dB in intro (where it coincides with the pad's B3), 3rd weak.

Recipe (Faust / pedalboard):
```
osc  = sine(f0*1.0081) + 0.4*sine(2*f0*1.0081)      // or triangle, LPF 400 Hz 12 dB/oct
env  = gate (legato, no release gap); attack 10 ms, release 10 ms
gain = -17 dBFS ; pan centre; stereo: tiny width (side -15 dB) via 8 ms Haas at -12 dB or none
```
Notes per bar: B2 | F#2 | C3 | E2 (then add +14 c).

### 2.2 SAMPLE-PAD — the "Remind Me" chord synth

Measured:
* Voicing (partials with their levels relative to the bar's loudest partial, intro/outro):
  * Bm: B2 0, B3 0, D4 −4/−5, F#4 −4/−5, B4 −3/−10, D5 −7/−12, F#5 −10/−14 (A5 −14 and C#6 −17 appear only when PAD-2 is in).
  * F#m: F#2 −1.5, F#3 −4.5, A3 −4, C#4 −2/−5, F#4 0, A4 −2/−2.6, C#5 −3.4, E5 −16.
  * C: C3 0, G3 −3, C4 −3.6, E4 −2/−3, G4 −3/−5, C5 −2.5/−6, E5 −8.6, G5 −14.
  * Em: E2 −3/−4, E3 −2/−9, G3 −2/−3, B3 0, E4 0/−5, G4 −2, B4 −7/−12, E5 −5, B5 −10.
  → root (oct 2) + close triad in oct 3-4 + triad again in oct 4-5, top octave 8-12 dB down. Harmonic (flatness ≈ 0.03 in 300-4 k).
* **Vibrato: sinusoidal, 7.5-7.7 Hz, ±11-12 cents (≈24 c pk-pk), coherent across all chord tones** (instantaneous-frequency traces of 373/444/559 Hz partials are in phase; FM sidebands at ±7.67 Hz grow +6 dB/octave with partial frequency, exactly as constant-cents FM predicts: −19 dB at 249 Hz, −13 dB at 498 Hz, −9 dB at 746 Hz). Rate equals the 16th-note rate at 115 BPM (7.667 Hz) — set the LFO to sync 1/16. The bass root (2.1) does not carry it.
* Fixed resonance/extra partial at **~425.6 Hz (A4 −57 c)** at −12…−15 dB, present in F#m and Em bars regardless of chord (carries the same ±7.7 Hz sidebands) — a quirk of the source; optional.
* Spectral envelope (intro, drums excluded by band choice): flat 160-640 Hz, −4 dB/oct above ~700 Hz; 95 % energy below 1.7-1.9 kHz; partials above 1 kHz ≤ −17 dB. **Outro adds a low-pass: 3 kHz is −21.8 dB and 6 kHz −42 dB relative to 1 kHz (vs −7.9/−13.6 dB in the intro) → ~2 kHz cutoff, ≈24 dB/oct.**
* Amplitude: constant within ±1 dB across a bar (no gate, no tremolo: per-16th depth 8-11 dB in the outro is the beating against PAD-2; intro modulation spectrum has no 7.67 Hz AM peak). Chord changes are hard legato cuts (< 20 ms).
* Stereo: side −15 dB in 150-6 k (intro), L/R corr 0.96; **no L/R pitch offset (0.0 c)**, no Haas delay.
* Level: −17 dBFS; reduced ~16 dB in drop 1 (bars 24-39) except on C bars (26, 30, 34, 38) and alternate Bm bars (28, 36) where it returns to full — i.e. drop 1 uses a chopped/alternating version.

Recipe:
```
voice(f) = (saw(f)*0.5 + pulse(f, 0.5)*0.5)   // mellow; or 2 detuned saws ±4 c
chord    = sum over voicing above, top octave at -10 dB
vib      = f * 2^( 0.0115 * sin(2*pi*7.667*t) / 12 )   // ±11.5 c, applied to all chord voices, not the bass
filter   = LPF 24 dB/oct, cutoff 1.4 kHz, Q 0.7 (intro/drop) ; cutoff 2.0 kHz with extra 24 dB/oct LPF at 2 kHz in outro
env      = legato gate, attack 15 ms, release 15 ms (no re-trigger at chord change)
detune   = +14 cents global (multiply all f by 1.00812)
stereo   = narrow: mid + side at -15 dB (e.g. mono → 2-voice chorus depth 0.5 ms, rate 0.3 Hz, mix 15 %)
gain     = -17 dBFS (chord sum)
```

### 2.3 SAMPLE-LEAD — melody from the same sample (drop 1 only)

Measured (basic-pitch + partial lists, bars 24-31; same +14 c tuning and the same 7.6 Hz ±11 c vibrato as the pad → same synth):
* Note envelope: onset −30 → −18 dB in ~40 ms (attack ≈ 35 ms), flat sustain ≈ 250 ms, fast release (−16 dB within ~50 ms) → note length ≈ 2 16ths (260 ms). Peak −16…−18 dBFS at the fundamental. Side −12 dB.
* 4-bar phrase, 16th positions in brackets (M; pitch names from basic-pitch, ±1 note possible on the shorter notes):
  * bar 24 (Bm): F#4 [6] G4 [9] E4 [14]
  * bar 25 (F#m): F#4 [2]
  * bar 26 (C): E4 [6] D4 [9] F#4 [14]
  * bar 27 (Em): G4 [0] F#4 [5-6] E4 [8] D4 [13-14]
  * bar 28 (Bm): D4 [6] C#4 [9] D4 [11] A4 [14]
  * bar 29 (F#m): C#4 [2]
  * bars 30-31 = bars 26-27. Repeats through bar 39.

Recipe: the 2.2 voice, monophonic, attack 35 ms / decay 0 / sustain 1 / release 40 ms, LPF 1.6 kHz, +14 c, vibrato as 2.2, −17 dBFS.

### 2.4 SAMPLE-SUB (bars 8-15)

Octave-down copies of the root at +14 c: B1 62.2 Hz, F#1 ~46.6, C2 65.9, E2 83.1 at −30 dBFS, sustained, mono. Recipe: sine at f0/2 ×1.0081, −30 dBFS, legato. `[M]`

### 2.5 KICK

Measured on the four isolated intro kicks (bars 2/4/6/8) and drop hits:
* Pitch envelope (instantaneous frequency of the 25-110 Hz band): 130 Hz @3 ms → 95-100 Hz @10-20 ms → 62 Hz @30 ms → 44 Hz @40 ms → 42-43 Hz @50-80 ms → **40-41 Hz settled** (≈E1, 41.2 Hz; −30…−50 c). Exponential sweep, time constant ≈ 15 ms.
* Amplitude: perc-band attack 13-21 ms; sub-band peak at +22…+34 ms after onset; from the peak: −6 dB @ 90-98 ms, −12 dB @ 135-141, −20 dB @ 173-182, −30 dB @ 193-207, −40 dB @ 220-233 ms → not exponential: slow first 100 ms then fast (two-stage). Total ≈ 230 ms.
* Spectrum: first 15 ms is the sweep plus a low-mid thump (120-400 Hz dominant at −4 dB rel total; 400-800 Hz −14; 800-1.5 k −20; 1.5-3 k −23), 15-40 ms 50-120 Hz, after 40 ms pure 20-50 Hz sine. **No bright click: < −40 dB above 2 kHz in the first 10 ms, < −60 dB above 4 kHz in the first 30 ms.** Any top end on the downbeat is the hat (2.10/2.11). (`drums.md` reports the same 100-3000 Hz attack rise; its 90→41 Hz sweep and 200-220 ms length match 2.5.)
* Level: 0 dBFS (into the clipper), mono (side −31 dB).
* Timing: onset 37 ms before the sample's chord-change grid = on the drum grid.

Recipe:
```
f(t)   = 41 + 90*exp(-t/0.015)          // Hz
kick   = sin(2*pi*integral f) * env
env    = hold 1.0 for 60 ms, then exp decay tau 35 ms (reaches -40 dB at ~230 ms); attack 3 ms
drive  = soft clip 0 dB into master clipper (it is the loudest element)
click  = optional 120-800 Hz thump, 10 ms, -12 dB (no HF click layer); mono
```

### 2.6 808 (chord-root bass, saturated)

Measured on sustained notes (bars 24-27, 33, 56-57, 88):
* Fundamentals: B0 30.6-30.8 Hz, C1 32.4-33.3, E1 41.2-41.5, F#1 45.5-46.8 (≈A440 ±15 c; i.e. **not** tuned to the +14 c sample). Build (bars 16-23) uses B1 61.6 / F#1 46.1 / C2 65.3 / E1 at −21 dBFS.
* Envelope: attack ≈ 15-25 ms to peak (−4 dBFS), then **sustain with ≤ 1-6 dB/s decay (T60 > 10 s) until the next note cuts it** (monophonic re-trigger); no audible release gap.
* Harmonic series (dB rel H1, B0 note): H2 −3…−10, H3 −15…−18, H4 −6…−16, H5 −19…−22, H6 −8…−18, H8 −7…−17, H10 −13…−21, H12 −10…−14, H16 −15…−29, continuing to **H40 (≈1.2 kHz) at −25…−35 dB**. Even harmonics average −9…−16 dB vs odd −21…−23 dB → asymmetric (even-order) saturation; envelope ≈ −5.5 dB/oct over H2-H10. These harmonics land on 0 c chord tones (B0×8 = B3, ×5 = D#3 −14 c, ×9 = C#4) and are what fills the mids in the drops.
* Mono (side −36 dB, L/R corr 1.000). Peak −4 dBFS.
* No pitch glide between notes (f0 constant within ±1 Hz over a note); the only sweep is the kick.

Recipe:
```
src   = sine(f0)
sat   = asymmetric waveshaper: y = tanh(2.5*x + 0.35*x^2)  (even-heavy) → then tanh(1.5*y)
      target: H2 -5 dB, H3 -17 dB, H4 -12 dB, H6 -15 dB, H8 -15 dB, roll-off -5.5 dB/oct, harmonics audible to 1.2 kHz
post  = HPF 25 Hz; LPF 2 kHz 6 dB/oct
env   = attack 20 ms, decay ∞ (or 30 s), release 10 ms, mono legato (new note cuts old)
gain  = -4 dBFS peak ; mono
notes = B0 | F#1 | C1 | E1 (drops); B1 | F#1 | C2 | E1 at -21 dB (build 16-23)
```

### 2.7 GLIDE-BASS (bars 40-55)

Measured (side-channel pyin 45-500 Hz at 1/32 notes, mid-channel pyin, side spectra):
* Replaces the full 808 (808 sustain drops to −15…−17 dB in this section; the B0 note is still there quietly at −15 dB).
* Register 50-150 Hz fundamentals; continuous portamento (pitch moves 30-50 c per 1/32 note between targets). 4-bar phrase, repeats ×4 (bars 40-43 = 44-47 = 48-51 = 52-55), approximate targets:
  * bar 40 (Bm): B1 → (slide up) C2 → C#2 → D2 → (slide down) C#2 → C2 → B1 (the whole bar is one slow up-and-down slide B1…D2…B1)
  * bar 41 (F#m): A1 → F#1 → (G#1 passing) A1 → E1
  * bar 42 (C): A1/A2 with E2/E3 alternating (A – E – A – E – A)
  * bar 43 (Em): E2 → D2 → E2 → A1 → B1
* Stereo: fundamental mono (side −25 dB at 60-90 Hz), harmonics wide (side −10 dB at 90-300 Hz, L/R xcorr 0.94 at 0 ms lag → chorus-type width, no delay).
* Level −8…−13 dBFS; sustained notes with ~2 s decay-to-−20 dB where unbroken.

Recipe:
```
osc    = saw(f) + saw(f*1.004) + saw(f*0.996)  (3-voice unison ±7 c) ; sub sine(f) mono at -6 dB
glide  = portamento 120-180 ms (exponential), legato
filter = LPF 24 dB/oct 500 Hz, resonance 0.2 ; drive 3 dB
stereo = unison voices panned ±60 %; sub mono; HPF the wide part at 90 Hz
env    = A 20 ms, S 1, R 150 ms ; gain -10 dBFS
```
(Melody pitches M; the slide shape in bar 40 is H.)

### 2.8 PAD-2 (second chord layer, bars 56-101)

Measured (outro, where it is unmasked; drops 56-95):
* Tuning 0 c (A440). **No vibrato** (sidebands at ±7.67 Hz are −35…−41 dB in the outro, vs −15…−20 dB on the sample partials).
* Unison detune: high partials split into triplets 2.7-3.9 Hz apart (F#6 1476.7/1480.6/1483.3; G6 1565.1/1568.5/1570.9) → **3 voices, ±3.5 cents**.
* Voicing includes the thirds (A3/A4 in F#m, E4/E5 in C) and extensions (A5, C#6 over Bm = 7th and 9th at −14…−17 dB).
* Level ≈ −5 dB (outro) to −8…−12 dB (bars 56-95) below SAMPLE-PAD per chord tone; **brighter**: its octave-6 partials are 8-18 dB louder than the sample's; harmonic-stem centroid rises from ~850 Hz (bars 0-31) to 1100-1350 Hz (bars 72-95).
* Width: side −3…−6 dB in octaves 5-6 (L/R corr of the outro 0.69-0.90 vs 0.96 intro; xcorr lag 0 ms) → unison/chorus width, no Haas.
* Beats against the +14 c sample at 0.81 % of frequency (2 Hz at 250 Hz, 5 Hz at 600 Hz): this slow shimmer is the signature of bars 56-101. Keep both layers, do not tune them together.

Recipe:
```
voice(f) = saw(f) + saw(f*2^(3.5/1200)) + saw(f*2^(-3.5/1200)), voices panned L/C/R
chord    = root oct3 + triad oct4 + triad oct5 + 7th/9th oct5-6 at -12 dB (Bm9, F#m7, Cmaj9, Em9)
filter   = LPF 12 dB/oct 3.5 kHz (brighter than the sample)
env      = legato, attack 30 ms, release 50 ms ; no LFO
gain     = sample level -8 dB (bars 56-95), -5 dB (outro)
```
`[M]` for the extensions (they could also be 808 harmonics in the drops; in the outro they are real).

### 2.9 CLAP (backbeat) + reverb

Measured on 144 hits at beats 2 and 4 (bars 24-95):
* Attack: onset→peak 44 ms with **4 sub-transients in the first 40 ms** (flam count median 4) → multi-layer clap; peak −9 dBFS.
* Spectrum: 0-20 ms centroid 3.5 kHz, flatness 0.67; 20-80 ms centroid 4.3 kHz, flatness 0.74; band levels (rel total, 20-80 ms): 600-1.2 k −7, **1.2-2.5 k −3 (strongest)**, 2.5-5 k −8, 5-10 k −11, 10-16 k −19; spectral peaks 1.24-1.33 k, 1.6-1.8 k, 2.17 k, 2.77 k, 3.13 k, 4.0 k.
* Body decay (150-12 k): −6 dB @ 7 ms, −12 @ 26, −20 @ 53 ms; then a plateau at **−28…−38 dB rel peak from 75 to 450 ms = reverb tail**, slope −23 dB/s → **T60 ≈ 2.6 s**, pre-delay ≈ 25-30 ms (side channel lags the body by 27 ms in cross-correlation).
* Stereo: body mono (side −18 dB in 1.5-6 k for the first 100 ms), **tail fully wide (side −1…−3 dB)**.
* Timing: peak +19 ms after the 16th (because of the 44 ms attack) — i.e. on the drum grid.
* Absent on bars 23, 39, 55, 71, 87 (transition bars).

Recipe:
```
clap  = 4 noise bursts at 0, 10, 20, 32 ms (each: white noise, BPF 1.6 kHz Q 0.7 + BPF 3.1 kHz Q 1 mixed, 8 ms decay)
      + body burst at 32 ms: noise BPF 1.3-2.5 kHz, decay 40 ms (to -20 dB at 53 ms)
reverb = plate/hall, pre-delay 25 ms, T60 2.6 s, send -28 dB, 100 % wide, HPF 400 Hz, LPF 8 kHz
gain  = -9 dBFS ; mono body
```

### 2.10 HAT (main closed hat)

Measured (hits > −32 dB, all sections):
* Spectrum (first 30 ms, perc stem): centroid 7.3-7.5 kHz (9.5 kHz when the clap bleed is excluded); peaks **3.4-4.0 kHz** and **12.4 kHz**, secondary 4.6 k, 6.2-6.7 k; 12-16 k only −17…−19 dB rel total; nothing above 16 kHz (−49…−60 dB).
* Decay: −6 dB @ 1-4 ms, −12 @ 22, −20 @ 37-40, **−30 @ 53-54 ms** (dead by 80 ms) → very short closed hat.
* Level −19.5 dBFS, **velocity spread p10-p90 < 3.5 dB** (machine-static). Stereo side −15 dB. Timing +16 ms after the drum grid (slightly lazy).
* Downbeat variant (16th 0): peaks 6.6-8.5 kHz, decay −20 dB @ 73 ms, side −21 dB (a different, longer, narrower hat sample) `[M]`.

Recipe:
```
hat  = white noise → HPF 3 kHz 12 dB/oct → peak EQ +6 dB @ 3.7 kHz Q 2, +4 dB @ 12.4 kHz Q 3 → LPF 16 kHz
env  = attack 1 ms, exp decay reaching -30 dB at 54 ms (tau ≈ 16 ms)
gain = -19.5 dBFS, fixed velocity; pan centre with 15 % width
downbeat hat: same, EQ +6 dB @ 7.5 kHz, tau 25 ms, mono, -20 dBFS
```

### 2.11 PERC-2 (soft dark wide hat/shaker, bars 72-95)

Hits on 16ths 5-9 and 13-15 at −26…−29 dBFS: centroid 6.2 kHz, strong 1-3 kHz (−1 dB rel > 1 k), decay −20 dB @ 22 ms, −30 @ 74 ms, side −7 dB (wide). Recipe: noise BPF 2-8 kHz (centre 4 kHz, Q 0.5), tau 25 ms, stereo-spread (L/R decorrelated noise), −27 dBFS. `[M]`

### 2.12 KNOCK (16th-position-2 low-mid perc)

71 hits (bars 24-95, also present bars 0-15 at −16 dBFS; absent in outro): attack 28 ms, 300-600 Hz dominant (−2.5 dB rel total in the first 30 ms), peaks 436 Hz / 417 Hz / 937 Hz; zero-crossing pitch ≈ 350 Hz (F4) ±30 Hz; flatness 0.5-0.57 (noisy); decay −12 dB @ 28 ms; side −9.5 dB; 3-8 k and > 8 k present at −10…−13 dB. Recipe: short noise burst BPF 420 Hz Q 2 mixed with a 350 Hz sine ping (tau 20 ms), plus a −12 dB click; attack 10 ms, tau 15 ms, −16 dBFS, 30 % width. `[M]`

### 2.13 REVERSE SWELL FX (into bars 24, 56, 96)

* Side-channel 300-4 kHz rises from −26…−29 dB to −14 dB over the last ~2 s before the downbeat (≈ +12 dB), peaks 0.22 s before the drop, gone at the downbeat (−46 dB within 100 ms); side 2-8 kHz rises −68 → −27 dB.
* **Fully decorrelated** (L/R corr 0.05-0.37 in 300-4 k). Flatness 0.44-0.65 (noisy-tonal). Same fixed partials each time: 735 Hz, 974 Hz, 1074 Hz, 1176-1186 Hz, 1315 Hz (side > mid by 5-15 dB) → one reused sample (a reversed, pitched texture), not a synth riser (no pitch sweep, no noise sweep).
* Recipe: reverse a 2 s chord/crash with reverb, HPF 300 Hz, width 100 %, fade-in curve exponential +12 dB, stop at the downbeat; add the fixed partials via a ringing filter bank at 735/974/1074/1181/1315 Hz if matching the colour matters.

---

## 3. Patterns (16th grid, position 0 = downbeat on the drum grid)

```
pos:            0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
KICK   intro    K . . . . . . . . . .  .  .  .  .  .   (only every 2nd bar: bars 0,2,4,6 = Bm and C bars)
KICK   8-15     K . . . . . K . . . .  .  .  .  .  .
KICK   16-95    K . . . . . K . . . k  .  .  k  .  .   (k = present in alternate/odd bars → 4 kicks/bar)
808    24-39,56-95  . . . . B . . B . . B  .  .  B  .  .   (B = chord root, each note sustains to the next)
808    16-23    sustained octave-up root at -21 dB, whole bar
CLAP            . . . . C . . . . . .  .  C  .  .  .
HAT    0-39     h . h h (c) . . . . . h  h  (c) .  .  .  (plus the downbeat variant at 0)
HAT    40-55    . . h h h h h . . . h  h  h  h  h  .   (16th rolls into both backbeats)
HAT    56-71    h . h h . . h h . h h  h  .  .  .  .
HAT/PERC-2 72-95  h . h h . p p p p p h  h  .  p  p  p  (p = PERC-2 at -26 dB)
KNOCK           . . x . . . . . . . .  .  .  .  .  .
LEAD   24-39    see 2.3
```
Timing offsets relative to the drum grid: kick onset 0 (peak +25 ms), hat peak +16 ms, clap peak +56 ms (onset +12), knock peak +16 ms, sample chord changes +22…+35 ms. For a faithful feel: drums quantised, sample layer nudged +25 ms.

Bar 88-95 variation (H): the 808 holds the downbeat note and lets it decay (−27 dB by beat 3) with two short hits on 16ths 5 and 7; kicks 2/bar.

---

## 4. Arrangement map (bars on the drum grid; t = 0.265 + 2.087·bar)

| Bars | t | What is playing | Mix RMS |
|---|---|---|---|
| 0-7 | 0.3-17.0 | SAMPLE bass+pad, hats, claps, knock, kick every 2 bars (first kick at 0.278 s) | −14.5 / −17.5 alternating |
| 8-15 | 17.0-33.7 | + kick 2/bar, SAMPLE-SUB (−30 dB) | −13.1 |
| 16-22 | 33.7-48.3 | + 808 octave-up sustained (−21 dB); 4 kicks on odd bars | −12.8 / −10.8 |
| 23 | 48.3-50.4 | drums out, sample only, reverse swell | −19.3 |
| 24-39 | 50.4-83.7 | DROP 1: 808 full (B0/F#1/C1/E1), kicks, hats/claps, SAMPLE-LEAD melody, pad −16 dB (full on C bars and bars 28/36); hats double from bar 32 | −9.0 / −10.1 |
| 40-54 | 83.7-115.0 | GLIDE-BASS section: 808 quiet (−16 dB), hat 16th rolls, pad full | −9.7 / −11.3 |
| 55 | 115.0-117.1 | transition, reverse swell | −13.5 |
| 56-70 | 117.1-148.4 | DROP 2: 808 full, kicks 2/bar, PAD-2 enters (0 c), brighter (centroid ~1.05 kHz) | −9.5 |
| 71 | 148.4-150.5 | drums out (3 hats) | −10.1 |
| 72-86 | 150.5-181.8 | loudest: PAD-2 up, PERC-2 added, 4 kicks on odd bars, centroid 1.15-1.35 kHz | −8.4 / −9.2 |
| 87 | 181.8-183.9 | drums out | −9.4 |
| 88-95 | 183.9-200.6 | wind-down: 808 lighter pattern, kicks 2/bar | −11.2 / −9.9 |
| 95 → 96 | 198.5-200.6 | reverse swell | |
| 96-101 | 200.6-213.1 | OUTRO: no drums; SAMPLE low-passed ~2 kHz + PAD-2 at −5 dB; hard cut at 215.3 s | −18…−19 |

No gradual filter movement inside sections (per-bar harmonic centroid is flat within each block); brightness steps up per section (850 → 780 → 1100 → 650 → 1050 → 1250 → 950 Hz).

---

## 5. Caveats

* "Sample" layers (2.1-2.4) are inferred to be one sampled source because they share the +14 c offset, the identical 7.6 Hz ±11 c vibrato and the same stereo signature; which Röyksopp version/section was used is unverified `[L]`. The partial lists are exact regardless of provenance.
* Drop-1 "0 c chord tones" are the saturated 808's harmonics (H4-H16 land on B3/B4/D#3/C#4 etc.), **not** a pad; PAD-2 proper starts at bar 56 (thirds at 0 c appear only from there and in the outro).
* basic-pitch pitches for the lead (2.3) and the glide-bass targets (2.7) are M-confidence; rhythm positions are H.
* All drum timings measured on the HPSS percussive stem of a hard-clipped master; absolute spectral balances above 10 kHz are affected by the clipper.
