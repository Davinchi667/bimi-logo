# EVERYWHERE I GO (REMIND ME) — harmony & melody research

Target: instrumental rebuild of BNYX x Kid Cudi "EVERYWHERE I GO (REMIND ME)" (samples Röyksopp "Remind Me").
Everything below is either **measured** on the supplied wavs (scripts in this folder) or cited with a URL.
Confidence tags: HIGH / MED / LOW.

Files measured:
- `refs/eig_inst.wav` (instrumental, 3:37.34, 44.1 kHz)
- `refs/everywhere.wav` (full version with Cudi, same length)
- `refs/bp/eig_inst_basic_pitch.mid` (basic-pitch of the instrumental, 1663 notes)
- 30-second official previews pulled from the public Deezer API (track 3794993062 = BNYX release, 109713896 = Röyksopp album version, 3120990 = Röyksopp radio edit) — used only for pitch/tempo/chord cross-checks.

---

## 0. TL;DR for the person programming it

| Item | Value | Conf. |
|---|---|---|
| Tempo | **115.00 BPM** (bar = 2.08702 s, beat = 0.52176 s, 16th = 130.4 ms). The earlier 114.84 was frame-quantised; it drifts 2.7 ms/bar and is 284 ms late by bar 100. | HIGH (measured, 88-bar fit, residual 1 ms) |
| First downbeat | **0.2912 s** in `eig_inst.wav` (= old 0.813 s minus one beat). Chord changes, 808 and kick land here; claps on beats 2 & 4. | HIGH (measured) |
| Key / loop | **B minor**, 4-bar loop, one chord per bar, changes on beat 1: **\| Bm \| F#m \| C \| Em \|** (i – v – bII – iv). Krumhansl on whole-track chroma prefers E minor (0.556 vs 0.442) — same pitch set, different tonic reading. | HIGH for the chords, MED for naming the tonic |
| 808 roots | **B1 – F#1 – C2 – E1** (61.7 / 46.2 / 65.4 / 41.2 Hz) with an octave double (B2/F#2/C3/E2). Intro (bars 1–8) has only the octave-2 bass; the sub enters at bar 9. | HIGH |
| Pad voicing (closed, re-triggered every beat) | Bm: B3 D4 F#4 · F#m: A3 C#4 F#4 · C: G3 C4 E4 · Em: G3 B3 E4. Inner voice D4→C#4→C4→B3 (chromatic descent), top F#4 F#4 E4 E4. Intro adds a top voice A4 / C#5 / C5 / B4–E5. | HIGH |
| Sample lead ("chopped vocal" riff) | 8-bar phrase, register C#4–A4, mostly on 16th offbeats (slots 6, 9, 11, 14). See §4 tables. | HIGH for notes, MED for exact lengths |
| Kid Cudi hook | **The same riff one octave down (C#3–A3)**, slightly re-rhythmed (Em bar = G3 F#3 E3 D3 on the four beats). See §5. | HIGH that it exists and its pitches; MED on fine rhythm |
| Tuning | Sample layer (pad + lead chops) is **+14 cents sharp** of A440 (E4 = 332.4 Hz, G4 = 395.2 Hz); 808 and the breakdown keys are ≈ 0 c. The official Deezer preview shows the same, so the wav is at release pitch and speed. | HIGH |
| Original (Röyksopp) | Dm7 \| Am7 \| Ebmaj7 \| Bb at ≈122.5 BPM (chord chart + measured preview). BNYX = that loop **pitched down 3 semitones**; only the 4th-bar bass differs (E instead of G → Em7 instead of G/Bb). | MED-HIGH |

---

## 1. Grid correction (affects every other sub-task)

**Measured.** Self-correlation of the onset envelope (16-bar template vs whole track, 88 peaks, hop 128) gives bar = 2.08702 ± 0.00003 s → **114.996 BPM** (call it 115.00). Fit residual: std 1.0 ms, max 2.1 ms (`tempo_refine.py`, `tempo_out.txt`).

Downbeat phase (`phase_check.py`, `phase_out.txt`), folded over the refined bar with 0.813 s as phase reference:
- Pad (harmonic, 200–1200 Hz) onsets cluster at old-grid 16th slots 0.00, 4.00, 8.00, 12.00 (n ≈ 500 each, offsets −1…+8 ms) → the pad is re-triggered on every beat and the beat phase of the old grid is right.
- Chord change (chroma flux peak, 64-slot fold) at old slot 11.75–12.0 = old **beat 4**.
- Kick transient (percussive 40–150 Hz) densest at old slot 11.75; clap/snare (percussive 1–4 kHz) at old 7.75 and 15.75; i.e. relative to the chord change the claps sit 2 beats before/after → beats 2 and 4 of a bar that starts at the chord change.
- First audible transient at 0.253–0.283 s ≈ 0.291 s.

Therefore: **downbeat = 0.813 − 0.52176 = 0.2912 s**, bar numbering unchanged (new bar N starts one beat before old bar N). Bar N start time = 0.2912 + (N−1)·2.08702 s. The file holds 104 bars (bar 104 = 215.25 s → end 217.34 s).

For the full version (`everywhere.wav`) add **+807 samples (+18.3 ms)**: cross-correlation lag is 806–809 samples at every 30 s window, tempo identical (`align_out.txt`). Downbeat there = 0.3095 s.

Any 16th-level table computed on the old grid is wrong by ~1 slot from bar 30 and ~2 slots from bar 70. All tables below use the corrected grid (`grid.json`).

---

## 2. Chord loop and key

### 2.1 Per-bar chord fits (HPSS harmonic part, CQT chroma, 36 bins/oct, templates triads/7ths/9ths/sus/5)
Full table: `final_harmony_out.txt`. Best-fit chord root by loop position over all 103 bars (basic-pitch bass pitch-class, duration-weighted): **B ×26, F# ×26, C ×26, E ×25 — unanimous.**

| Loop bar | Chord (best fits across the song) | Chroma, bars 1–96 folded (C C# D D# E F F# G G# A A# B) | Bass (basic-pitch) | Notes |
|---|---|---|---|---|
| 1 | **Bm** — fits Bm9 ×11, Bmadd9 ×6, Bm ×5, B5 ×3 | B 1.0, F# 0.73–0.84, D 0.60–0.77, C# 0.40–0.68 | B1 (+B2) | C# = add9 colour from the pad/sample; intro and outro read as plain B5/Bm |
| 2 | **F#m** (thin third) — F#5 ×16, F#m ×6, F#m9 ×4 | F# 1.0, C# 0.47–0.54, A 0.30–0.36 | F#1 (+F#2) | the A (minor 3rd) is present but weak; never reads as F# major in the full sections |
| 3 | **C** (add9 / 6) — Cadd9 ×14, C ×5, C6 ×4, C5 ×3 | C 1.0, G 0.39–0.56, E 0.51–0.59, D/A ≈ 0.2–0.3 | C2 (+C3) | bars 41–56 fit C6/Am7 (A added) |
| 4 | **Em** (7/9) — Em9 ×14, Em ×6, Em7 ×3 | E 1.0, G 0.28–0.58, B 0.41–0.64, F# 0.12–0.8 (beat 4) | E1 (+E2) | F#/D on beat 4 = the sample's pickup into the next Bm |

Beat-level fold (bars 1–96): all four beats of each bar carry the same chord → **harmonic rhythm = 1 chord per bar, change on beat 1** (HIGH).

### 2.2 Key
- Krumhansl–Schmuckler on the whole-track harmonic chroma: E minor 0.556, B minor 0.442, F# minor 0.381 (measured). Per-8-bar: E min wins in 9 of 13 blocks, B min in 2 (bars 17–24, 97–104), F# min in the thin breakdown (25–40).
- Musical reading: the loop starts on Bm, the bass B is the longest/loudest root, and the source loop (§2.3) is i–v–bII–VI in D minor. **Read it as B minor: i – v – bII – iv.** The C major chord is the Neapolitan (bII) — that is the "colour" of the progression and the reason no single diatonic mode fits (C natural and C# both occur: global chroma C 0.80, C# 0.67).
- Equivalent E-minor reading if you prefer: v – ii – VI – i. Either way the notes to program are identical. (Tonic naming: MED.)

### 2.3 Relation to Röyksopp "Remind Me"
- Chord chart (cifraclub, human-made): **Dm7 | Am7 | Ebmaj7 | Bb** repeating. Source: https://www.cifraclub.com/royksopp/remind-me/zpgkkt.html?locale=en (page returns 403 to scripted fetch; chords taken from the search-result snippet). Hooktheory has no "Remind Me" entry (https://www.hooktheory.com/theorytab/artist/royksopp-). MED.
- Measured on the official 30-s album preview (Deezer 109713896): ≈122.5 BPM; chord per second: Dm9 | Am7 | Cm7/Cm9 | Gm9 repeating; Krumhansl says C major/A minor/F major (ambiguous, 30 s only). "Cm7" and "Gm9" are what a template fitter returns for Ebmaj7 and Bb when C and G are the strongest low notes — consistent with the chart. MED.
- Transpose the original down 3 semitones: Dm7→**Bm7**, Am7→**F#m7**, Ebmaj7→**Cmaj7**, Bb→**G** (Bb/G = Gm7 → **Em7**). BNYX's measured loop Bm | F#m | C | Em therefore = the original loop pitched down a minor third, with E (not G) under the last chord. The inner chromatic line of the original (F–E–Eb–D over Dm7–Am7–Ebmaj7–Bb) becomes D4–C#4–C4–B3 in BNYX's pad (measured, §3). HIGH that the loop matches; the "−3 semitones" direction assumes the chart's key.
- Tempo is not a resample of the original: 122.5 × 2^(−3/12) = 103 BPM ≠ 115. The sample is chopped and re-triggered on the grid (press describes "a repeating chopped up vocal track", https://music.mxdwn.com/2026/02/02/news/kid-cudi-bnyx-team-up-for-collaborative-new-single-everywhere-i-go-remind-me/).

### 2.4 Tuning (measured, zero-padded FFT per bar, `grid.json` bars)
| Element | Bars | Measured | Offset from A440 |
|---|---|---|---|
| Pad/choir + lead chops | 3, 11, 15, 43, 59, 63, 91, 99 (C bars); 4, 12, 60, 76, 100 (Em bars) | C3 131.89, G3 197.63, C4 263.78, E4 332.38, G4 395.2, B3 249.0 Hz | **+14 c** (±1) |
| Lead note windows | bar 27 E4, bar 28 G4, bar 25 G4 | 332.2 / 395.2 / 395.0 Hz | +13 / +14 / +13 c |
| 808 | bars 11, 15, 28, 32, 60, 76 | C2 65.7–65.9 Hz, E2 82.1–82.5 Hz | ≈ 0 to +13 c (808 glides; treat as in tune) |
| Breakdown keys (bars 25–40) | 27, 31, 35 | C3 130.80, G3 196.24, C4 261.7 Hz | **0 c** |
| Official Deezer preview (aligned to our bar 23.88) | bar 24 / bars 27–36 | same values: +14 c in bar 24, 0 c keys in 27–36; bar period 2.0875 s (114.97 BPM) | wav = release pitch & speed |

Practical: if you rebuild the choir/lead from a sampler, detune that layer **+14 cents** against an in-tune 808 to match the record. The breakdown (bars 25–40) uses an in-tune keys/bass element plus the +14 c lead chops.

---

## 3. Pad / choir layer (what basic-pitch sees in F3–F#4 and above)

Mode per 16th over the 4 loops of bars 9–24 (`fm.txt`, "PAD F3-F#4"): closed triads held across the bar, re-articulated at slots 0, 5–6, 9, 12–13 (onsets at every beat per the phase analysis — the layer "pumps" on each beat).

| Loop bar | Notes (MIDI) | Hz (as recorded, +14 c) | Intro extra top voice (bars 1–8) |
|---|---|---|---|
| 1 Bm | B3 D4 F#4 (59 62 66) | 249 / 296 / 372 | A4 (69) from slot 15 of bar 1 into bar 2 → Bm7 |
| 2 F#m | A3 C#4 F#4 (57 61 66) | 222 / 279 / 372 | C#5 (73) around slots 7–8 |
| 3 C | G3 C4 E4 (55 60 64) | 198 / 264 / 332 | C5 (72) sustained slots 5–11, E5 at 15 |
| 4 Em | G3 B3 E4 (55 59 64) | 198 / 249 / 332 | B4 (71) slots 0–9, E5 (76) at 5 and 14–15 |

Voice-leading: top F#4 → F#4 → E4 → E4; middle D4 → C#4 → C4 → B3; bottom B3 → A3 → G3 → G3. HIGH.
In the breakdown (bars 25–40) this layer is largely absent (8-bar key correlation drops to 0.30–0.35, chord fits fall to F#5/Cadd9/Em9 at 0.7–0.8) and an in-tune keys/bass element plus the lead chops remain. In the outro (97–104) the stack returns with very high partials/voices (B5, C6, E5, G5 sustained, F#6) — densest section of the MIDI (17 notes/bar ≥ C4).

---

## 4. Sample lead riff (the "chopped vocal" hook in the instrumental)

Register MIDI 61–69 (C#4–A4), centre E4–G4. Pitch set: C# D E F# G A (B natural minor). Clearest where the pad is thin: B1 (bars 25–40) and D2 (73–88); also present in D1 (57–72) and E (89–96). In A1 (9–24) and C1 (41–56) the same register is filled by the pad voicings, so the riff is not separately resolvable there (it may be mixed in).

Slots are 16ths within the bar (0 = beat 1, 4 = beat 2, 8 = beat 3, 12 = beat 4). Lengths in 16ths (basic-pitch note durations; the chop tails are soft, so ±0.5).

### 4.1 The 8-bar phrase (two passes of the 4-bar loop; only the Bm bar differs)

**Loop bar 1 (Bm), variant a — bars 25, 33, 73, 81 (odd passes)**

| Slot | Beat | Note | MIDI | Len (16ths) | Seen in |
|---|---|---|---|---|---|
| 6 | 2.5 | F#4 | 66 | 1.3–2.0 | 25, 33, 73, 81 |
| 9 | 3.25 | G4 | 67 | 1.1–1.8 | 25, 33, 73, 81 |
| 11 | 3.75 | F#4 | 66 | 1.3–2.0 | 73, 81 only (absent in 25, 33) |
| 14 | 4.5 | E4 | 64 | 1.1–1.9 | 25, 33, 73, 81 |
| 16 (= next bar 0) | 1 of bar 2 | F#4 | 66 | 2.2–3.7 | 26, 34, 74, 82 (tail note over F#m) |

**Loop bar 1 (Bm), variant b — bars 29, 37, 77, 85 (even passes)**

| Slot | Beat | Note | MIDI | Len | Seen in |
|---|---|---|---|---|---|
| 6 | 2.5 | D4 | 62 | 2.6–2.9 | 29, 37, 77, 85 |
| 9 | 3.25 | C#4 | 61 | 1.2–1.4 | 29, 37, 77 (85: D4 held instead) |
| 11 | 3.75 | D4 | 62 | 1.9–3.1 | 29, 37, 77, 85 |
| 14 | 4.5 | A4 | 69 | 1.5–2.0 | 29, 37, 77, 85 |
| 16 (= next bar 0) | 1 of bar 2 | C#4 | 61 | 2.3 (+1.4 re-articulation at slot 2) | 30, 78 |

**Loop bar 2 (F#m):** only the tail note above (slots 0–3), then **rest**.

**Loop bar 3 (C) — bars 27, 31, 35, 39, 75, 79, 83, 87**

| Slot | Beat | Note | MIDI | Len | Seen in |
|---|---|---|---|---|---|
| 6 | 2.5 | E4 | 64 | 2.0–2.9 | all 8 |
| 8 | 3 | E4 | 64 | 1.1–1.8 | 75, 83, 87 (re-articulation) |
| 9 | 3.25 | D4 | 62 | 1.1–1.5 | 27, 31, 83, 87 (75/79: E4 instead) |
| 11 | 3.75 | E4 | 64 | 2.5–2.8 | 39, 75, 79, 83, 87 (absent in 27, 31, 35) |
| 14 | 4.5 | F#4 | 66 | 1.4–2.0 | all 8 |
| 16 (= next bar 0) | 1 of bar 4 | G4 | 67 | 1.5–3.1 | see bar 4 |

**Loop bar 4 (Em) — bars 28, 32, 76, 84, 88**

| Slot | Beat | Note | MIDI | Len | Seen in |
|---|---|---|---|---|---|
| 0 | 1 | G4 | 67 | 1.5–3.0 | 28, 32, 76, 84 (87→88 tail: G4@15.8 ×3.1) |
| 5 | 2.25 | F#4 | 66 | 1.1–2.0 | 28 (4.7 & 5.8), 32 (4.9), 88 (3.9) |
| 8 | 3 | E4 | 64 | 2.0–4.0 | 28, 32, 76, 84, 88 |
| 12–13 | 4–4.25 | D4 | 62 | 1.6–3.1 | 28 (13.5), 32 (13.3), 76 (12.0), 84 (11.8), 88 (11.7, 13.3) |

Melodic shape: a: F#4 G4 (F#4) E4 → F#4 held; b: D4 C#4 D4 A4 → C#4 held; C bar: E4 (E4) D4 (E4) F#4 → G4; Em bar: G4 F#4 E4 D4 (stepwise descent). Bar 2 of the loop is empty except the held tail — the breath in the phrase.

### 4.2 Variation between sections (MED)
- B1 (25–40) and D2 (73–88): phrase as above; D2 adds the slot-11 F#4 in variant a and the slot-8/11 E4 re-articulations in the C bar (busier chops).
- D1 (57–72): sparser; C-bar E4 at slots 5–8 and 11–12, Em-bar E4 long (slots 0–10) — the lead reads as sustained E4 rather than chopped.
- E (89–96): variant-b shape (D4 C#4 D4 E4 F#4) in bar 1, long E4 over C, little else.
- A1/C1/intro/outro: not resolvable from the pad (see §3).
So: **one 8-bar riff, re-used verbatim in the hook sections, thinned in D1/E, buried under the choir in verse-type sections.**

### 4.3 Chop rhythm summary (for a sampler)
Onsets predominantly at 16th slots **6, 9, 11, 14** (beat 2-and, 3-e, 3-a, 4-and) in loop bars 1 and 3, and **0, 5, 8, 12/13** in loop bar 4; nothing new in loop bar 2. Durations 1–3 16ths with soft tails. Note that every phrase ends with a note that carries across the barline into the next chord (slot 16).

---

## 5. Kid Cudi's vocal melody (from full − instrumental)

### 5.1 Method and caveats (all measured)
- Alignment: full = instrumental delayed 807 samples (18.3 ms), identical tempo, no drift (lag 806–809 at 30/60/…/200 s).
- Straight subtraction does not cancel above 120 Hz: magnitude coherence inst↔full is 0.71 in 20–120 Hz but only 0.13–0.28 in 120–500 Hz and 0.04–0.11 above (`vocal2_out.txt`, `vocal_pitch_out.txt`). The two files are different renders/encodes (LTAS of the full is +2–3 dB in the mids and extends to 20 kHz where the instrumental is cut at 16 kHz). Phase-sensitive subtraction is therefore useless; I used **magnitude spectral subtraction with a per-bin, per-8-bar gain** (`vocal3.py` → `vocal_ss.wav`) and then basic-pitch on that residual (`bp_vocal/vocal_ss_basic_pitch.mid`), cross-checked with a CQT excess-salience contour (`vocal4_out.txt`). Band-limited pyin on the full mix fails (never >50 % voiced frames) because the band is polyphonic — not evidence against the vocal.
- Where the vocal is: excess energy of the full over the instrumental per octave band (`vocal4_out.txt`): **C3–B3 band +12…+15 dB in bars 25–40, +5…+12 dB in 57–72, +10…+15 dB in 89–97**; ≈0…+4 dB in 41–56 and 9–24; ≈0 in 73–88 and the intro. The residual's duration-weighted pitch histogram peaks at E3 (37 s), F#3 (28 s), D3 (20 s), G3 (12 s), A3 (11 s): **Cudi's hook lives in C#3–A3.**

### 5.2 The hook (bars 25–40, 57–72, 89–104) — same 8-bar structure as the sample riff, one octave down
Mode tables and per-bar listings: `fm.txt` ("VOCAL C3-B3"). Slots as in §4.

**Loop bar 1 (Bm), variant a — bars 25, 33, 57, 65, 89, 97**

| Slot | Beat | Note | MIDI | Len | Evidence |
|---|---|---|---|---|---|
| 6 | 2.5 | F#3 | 54 | 1.3–3 | 33, 57, 65, 89 |
| 8 | 3 | A3 | 57 | ≈1 | 25, 33, 89, 97 (pickup/grace) |
| 9 | 3.25 | G3 | 55 | 1.5–2.2 | 25, 57, 89, 97 |
| 11–12 | 3.75–4 | F#3 | 54 | 1.5–3.0 | 25, 33, 57, 65, 89, 97 |
| 14 | 4.5 | E3 | 52 | 1.1–1.7 | all |
| 16 (= bar 2 slot 0) | 1 | F#3 held | 54 | 2.8–4.8 | 26, 34, 66, 90 |

**Loop bar 1 (Bm), variant b — bars 29, 37, 61, 69, 93, 101**

| Slot | Beat | Note | MIDI | Len | Evidence |
|---|---|---|---|---|---|
| 3–7 | 1.75–2.75 | D3 (repeated 2–4×) | 50 | 1.1–2.5 each | 29 (2.7, 5.6, 6.7), 37 (2.8, 4.0, 5.6, 6.6), 61 (4.1, 6.6), 69 (6.6), 93 (6.5), 101 (6.5) |
| 9 | 3.25 | C#3 | 49 | ≈1.1 | 29, 61, 69, 93, 101 |
| 11 | 3.75 | D3 | 50 | 1.1–1.9 | all |
| 14 | 4.5 | A3 | 57 | 1.4–1.9 | all |
| 16 (= bar 2 slot 0) | 1 | C#3 held | 49 | 3.9–5.3 | 30, 62, 94, 102 |

**Loop bar 2 (F#m):** the held tail (F#3 after variant a, C#3 after variant b, ≈ 1–1.3 beats), then rest; occasional F#3 pickup at slots 9–14 (34, 58).

**Loop bar 3 (C) — bars 27, 31, 35, 39, 59, 63, 67, 71, 91, 95, 99, 103**

| Slot | Beat | Note | MIDI | Len | Evidence |
|---|---|---|---|---|---|
| 0–4 | 1–2 | E3 (anticipation / held from pickup) | 52 | 2–3.3 | 31, 39, 59, 67, 71 |
| 6 | 2.5 | E3 | 52 | 1.6–2.9 | all 12 |
| 9 | 3.25 | D3 | 50 | 1.1–1.2 | 27, 59, 99 (others stay on E3) |
| 11 | 3.75 | E3 | 52 | 2.0–2.6 | all |
| 14 | 4.5 | F#3 | 54 | 1.1–1.7 | all |
| 16 (= bar 4 slot 0) | 1 | G3 | 55 | 3.2–4.1 | see bar 4 |

**Loop bar 4 (Em) — bars 28, 32, 36, 40, 60, 64, 68, 72, 92, 96, 100** (most consistent line in the song)

| Slot | Beat | Note | MIDI | Len | Evidence |
|---|---|---|---|---|---|
| 0 | 1 | G3 | 55 | 3.1–3.7 | 28, 32, 36, 68, 72, 96, 100 |
| 4 | 2 | F#3 | 54 | 2.0–4.1 | all 11 |
| 8 | 3 | E3 | 52 | 1.9–4.1 | all 11 |
| 12 | 4 | D3 | 50 | 2.1–4.2 | all 11 |

Shape: variant a = (F#3) A3 G3 F#3 E3 → F#3 held; variant b = D3 D3 (D3) C#3 D3 A3 → C#3 held; C bar = E3 E3 (D3) E3 F#3 → G3; Em bar = **G3 F#3 E3 D3 on the beats**. Intervals are all steps except the A3 leap (up a 5th from D3) and the drop to the held C#3. Range C#3–A3 (minor 6th). This is the sample riff (§4) transposed down an octave, with the Em bar straightened onto the beats and the C bar anticipated — i.e. Cudi hums/sings the Röyksopp hook an octave below the chopped sample. HIGH on pitches, MED on exact slot lengths (basic-pitch on a residual).

### 5.3 Other sections (LOW–MED; different material, probably sung verses)
- Bars 9–24: residual contour (counts 2–4 of 4 loops) F#3/A3 over Bm, A3 G3 F#3 E3 over F#m, E3 C3 D3 over C, G3 A3 E3 D3 over Em — hook-like but weaker (+0…+3 dB excess).
- Bars 41–56: long F#3/E3/D3 over Bm, **A3 held slots 5–12 over F#m**, **C3 held slots 1–7 over C**, E3 then F#3 over Em (+0…+4 dB). Different rhythm (long notes) — reads as a verse.
- Bars 73–88: sparse F#3 held (slots 1–7) over Bm and F#m, C3/E3/D3 over C, E3/G3/F#3 over Em (≈0 dB excess). Press describes vocoder/talkbox passages; this section has the least added vocal energy and some excess in C4–B4 (vocoder band?) — LOW.
- Outro (97–104): hook continues; extra excess in C4–B4 (+9 / +6.6 dB in bars 99–100) suggests an octave-up double or choir there (LOW).

---

## 6. Section map (corrected grid; bar N starts at 0.2912 + (N−1)·2.08702 s)

| Bars | Time | Harmony | Instrumental content (measured) | Vocal (full version) |
|---|---|---|---|---|
| 1–8 | 0:00.3–0:17.0 | loop ×2, B5/Bm plain | choir pad with top voice (A4/C#5/C5/B4–E5), octave-2 bass only, no sub | ≈ none |
| 9–24 | 0:17.0–0:50.4 | loop ×4 | sub 808 enters (B1…), full pad re-triggered per beat, lead buried | weak (verse-like) |
| 25–40 | 0:50.4–1:23.8 | loop ×4, pad thin | **lead riff exposed** (§4), in-tune keys/bass element, 808 | **hook, strong** |
| 41–56 | 1:23.8–1:57.2 | loop ×4, C reads C6/Am7 | full pad, lead buried | moderate, long notes (verse) |
| 57–72 | 1:57.2–2:30.6 | loop ×4 | lead riff (thinned), pad medium | **hook, strong** |
| 73–88 | 2:30.6–3:03.9 | loop ×4 | lead riff (busiest chops), pad medium | weak / vocoder (LOW) |
| 89–96 | 3:03.9–3:20.6 | loop ×2 | lead (variant-b shape), pad | **hook, strong** |
| 97–104 | 3:20.6–3:37.3 | loop ×2, B5/Bm plain | densest choir stack, high partials | hook + octave double (LOW) |

Section boundaries are inferred from note density, chord-fit strength and vocal excess (MED); the harmony never changes.

---

## 7. Sources
- Measured: scripts in this folder — `chroma_chords.py`, `grid_check.py`, `tempo_refine.py`, `phase_check.py`, `final_harmony.py`, `final_melody.py`, `midi_melody.py`, `riff_sections.py`, `align_vocal.py`, `vocal2.py`, `vocal3.py`, `vocal4.py`, `vocal_pitch.py`, `bp_vocal_read.py`, `preview_analyse.py`; outputs `*_out.txt`, `fm.txt`, `grid.json`, `chroma_bars.json`, `bass_bars.json`, `vocal_contour_16ths.json`, `bp_vocal/vocal_ss_basic_pitch.mid`, `vocal_ss.wav`, `harm.wav`; previews in `dl/`.
- Universal Music Canada press release (release date 30 Jan 2026; label Lyfestyle Corporation / Field Trip / Capitol; "humming keys, rubbery bass, snapping percussion, and choral vocals"; Cudi "between wistful warmth and robotic vocoder"): https://www.universalmusic.ca/?p=123123 — writers listed in the related press-release search snippet as BNYX, Erlend Øye, Kid Cudi, Svein Berge, Torbjørn Brundtland (MED).
- mxdwn review ("strong 808s and a repeating chopped up vocal track", "clap back beats", "talkbox vocals"): https://music.mxdwn.com/2026/02/02/news/kid-cudi-bnyx-team-up-for-collaborative-new-single-everywhere-i-go-remind-me/
- Röyksopp "Remind Me" background (writers Berge/Brundtland/Øye, vocal Erlend Øye, album version on Melody A.M. 2001, single = Someone Else remix, 4:04): https://en.wikipedia.org/wiki/Remind_Me_(R%C3%B6yksopp_song)
- Röyksopp chord chart Dm7 | Am7 | Ebmaj7 | Bb: https://www.cifraclub.com/royksopp/remind-me/zpgkkt.html?locale=en (snippet; direct fetch 403).
- Hooktheory (no Remind Me entry): https://www.hooktheory.com/theorytab/artist/royksopp-
- Previews: Deezer API tracks 3794993062 (BNYX), 109713896 (Röyksopp album), 3120990 (radio edit). WhoSampled and Genius pages were blocked (403) — not used.
- Not used on purpose: songbpm/tunebat-type sites (no human verification).
