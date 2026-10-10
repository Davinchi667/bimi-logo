# PRODUCTION BLUEPRINT — "EVERYWHERE I GO [REMIND ME]" (BNYX × Kid Cudi × Röyksopp), instrumental rebuild

Written as lead producer from the 10 research reports plus the verification verdicts. Where reports disagreed, the verified/corrected value is used and the loser is noted. Every number is tagged: **[M]** = measured on `refs/eig_inst.wav` (and stems/previews) by the research scripts in this folder, **[W]** = web source (URL in §10), **[D]** = my design decision where the record cannot be measured. Confidence: H / M / L.

Reference files: `refs/eig_inst.wav` (official instrumental rip, 44.1 kHz), `refs/everywhere.wav` (vocal version = instrumental delayed 18.3 ms, no drift [M,H]), `refs/bp/eig_inst_basic_pitch.mid`.

---

## 0. Corrections to the brief (read first)

| Item | Brief said | Use instead | Evidence |
|---|---|---|---|
| Tempo | 114.84 BPM | **115.000 BPM** (beat 521.74 ms, bar 2086.96 ms, 16th 130.43 ms, 32nd 65.22 ms) | onset autocorrelation at 4/8/16/32-bar lags, per-band phase fits, 88-bar template fit (residual 1 ms); 114.84 drifts 2.7 ms/bar = half a beat by bar 100 [M,H], independently confirmed by three verifiers |
| First downbeat | 0.813 s | **0.28–0.29 s** (0.813 s is bar 1 beat 2). Bar n starts at 0.29 + (n−1)·2.08696 s in the file | claps then fall on 2 & 4, chords change on beat 1, every section boundary lands on bar 8n+1 [M,H] |
| Length | ~104 bars, 3:37 | **104 bars = 13 × 8**, stop on the bar-105 line (217.33 s). `eig_inst.wav` is cut one bar short (hard cut at 215.238 s = bar-104 line); the official releases are 217.0–217.2 s [W: iTunes/Deezer/MusicBrainz durations] | [M,H] + [W] |
| Key | E minor (provisional) | Pitch set **{B C# D E F# G A} + C** (no G#/D#/F/A#). Loop **Bm · F#m · C · Em**, label it **B minor i–v–♭II–iv** (sections all start on Bm; the source is i–v–♭II in D/D# minor). Same notes as "E minor v–ii–VI–i" — the label changes nothing in the remake. Kick is tuned to E1. | [M,H] on notes; tonic label [M]. Hooktheory single version D#m i7-v7-VII7-iv7 [W] |
| Tuning | — | Two tunings coexist: the "sample"/pad/riff/bed-bass layer is **+14 cents sharp** (A ≈ 443.6 Hz); 808, kick, SUB, PAD-2 are **A440 (±5 c)**. Keep the split: the 0.81 % beating (2–5 Hz in 250–600 Hz) is part of the sound. | [M,H]: every pad partial +13…+16 c; 808 B0 30.85 Hz = −1 c |
| Master | RMS −10.7, crest 10.7 | integrated **−10.3 LUFS**, sample peak 0.00 dBFS hard-clipped (~20 000 full-scale samples, runs to 20–50), true peak +0.46 dBTP, RMS −10.5 dBFS, 57.0 % of energy < 60 Hz, 68.8 % < 120 Hz | [M,H] `master_out.txt` |

---

## 1. Tempo, key, chord loop, bass line

### 1.1 Grid
- 115.000 BPM, 4/4, straight 16ths, **zero swing** (hats +0.8 ms mean, sd 3.8; 'e/a' 16ths +1.8 ms; clap +1.9 ms; kick click +0.1 ms; folding all HF onsets on the beat shows energy only at 0/¼/½/¾) [M,H].
- 104 bars. Harmonic rhythm: one chord per bar, change on beat 1. 4-bar loop × 26. Every section starts on the Bm bar (bar 8n+1 ≡ loop position 1).
- The pad/bed/riff layer sits **+20 ms late** vs the drum grid (chroma-flux peaks median +19 ms, IQR 10–29) [M,H]. Quantise drums and 808 to the grid; delay the pad, bed-bass and lead-riff tracks by 20 ms.

### 1.2 Chord loop and voicings (MIDI numbers)

| Loop pos | Chord | 808 root (drops) | SAMPLE-PAD stack (+14 c), level re loudest partial | Close-triad core | PAD-2 (A440, bars 57–104) |
|---|---|---|---|---|---|
| 1 | **Bm** (reads Bm/Bm(add9)) | B0 = 23 (30.87 Hz) | B2 47 (−2), B3 59 (0), D4 62 (−4), F#4 66 (−3), B4 71 (−3…−9), D5 74 (−12), F#5 78 (−10…−22) | 59 62 66 | 47 · 59 62 66 · 71 74 78 · 69 73 (7th, 9th at −12 dB) |
| 2 | **F#m** (thin 3rd; reads F#5/F#m) | F#1 = 30 (46.25 Hz) | F#2 42 (−1.5), F#3 54 (−4), A3 57 (−4), C#4 61 (−2), F#4 66 (0), A4 69 (−2), C#5 73 (−3) | 57 61 66 | 42 · 54 57 61 · 66 69 73 · 64 (7th) |
| 3 | **C** (reads Cadd9 / C6) | C1 = 24 (32.70 Hz) | C3 48 (0), G3 55 (−3), C4 60 (−4), E4 64 (−2), G4 67 (−3), C5 72 (−2…−6), E5 76 (−8) | 55 60 64 | 48 · 60 64 67 · 72 76 79 · 71 74 (7th, 9th) |
| 4 | **Em** (reads Em7/Em9, Bm-over-E) | E1 = 28 (41.20 Hz) | E2 40 (−3), E3 52 (−2…−9), G3 55 (−2), B3 59 (0), E4 64 (0), G4 67 (−2), B4 71 (−7…−12), E5 76 (−5) | 55 59 64 | 40 · 52 55 59 · 64 67 71 · 62 66 (7th, 9th) |

- Inner voice of the pad descends chromatically **D4 → C#4 → C4 → B3** (62 61 60 59) — the ‑3 st transposition of the Röyksopp F–E–E♭–D line. Top voice F#4 F#4 E4 E4. [M,H]
- The pad is **legato, not re-triggered**: partial envelopes flat within 2–3 dB across a bar, max per-beat dip 0.7 dB; chord changes are hard legato cuts (< 20 ms) [M,H]. (One report said "re-triggered every beat"; refuted — the per-16th articulation basic-pitch saw is the 16th-rate vibrato.)
- Source: Röyksopp "Remind Me" (Melody A.M. album version, ≈122.5 BPM, Dm7 | Am7 | E♭maj7 | B♭(/G) per cifraclub chart + measured Deezer preview) pitched **−3 st** (Dm → Bm; BNYX's bed bass B2/F#2/C3/E2 = the album's D3/A2/E♭3/G2 note for note) and time-stretched independently to 115 (ratio 0.939; not a resample, which would give 103 BPM) [M,H][W]. BNYX's bed is nevertheless a **re-voiced** bare-triad pad (7ths/9ths ≥ 38 dB down vs 2–8 dB down on the record) with a tempo-synced LFO the record does not have → build it as a synth, do not look for a loop [M,H].

### 1.3 Bass / 808 line — bar by bar

Pitches (MIDI / Hz): B0 23 / 30.87 · C1 24 / 32.70 · E1 28 / 41.20 · F#1 30 / 46.25 · A1 33 / 55.0 · B1 35 / 61.74 · C#2 37 / 69.30 · D2 38 / 73.42 · E2 40 / 82.41 · C#1 25 / 34.65 · A0 21 / 27.5.
Slot = 16th position 0–15 (0 = beat 1, 4 = beat 2, 8 = beat 3, 12 = beat 4; "e/&/a" = +1/+2/+3). Lengths in 16ths. Levels are peak dBFS of the 20–120 Hz band on the bass stem; loud 808 hit = −4 dBFS = the **0 dB reference for every level in this document**.
**No glides anywhere** (cycle-by-cycle tracking: every pitch change completes within one cycle, 161/161 changes < 45 ms; the +33 c "bends" basic-pitch wrote are the kick's E1 tail under quiet beat-1 notes) [M,H]. Downward moves in verse 2 are 30–45 ms steps — program them as separate notes, no portamento.

Four low layers exist [M,H]:

| Layer | Bars | Notes | Tuning | Level re 808 | Character |
|---|---|---|---|---|---|
| BED-BASS (root of the pad, octave 2) | 1–104 (quieter in drops) | B2 F#2 C3 E2 (47 42 48 40) one per bar, whole bar | +14 c | −13 dB (−17 dBFS) | sine + octave at −8 dB, no vibrato, mono-ish |
| BED-SUB (octave-down copy of BED-BASS) | 9–16 (faint under 17–24) | B1 F#1 C2 E1 (35 30 36 28), whole bar | +14…+16 c | −26 dB (−30 dBFS) | pure sine, mono |
| SUB (sustained sub synth) | 17–23, and the −16 dB "floor" under hook even bars 25–40 / 73–88 | B1 F#1 C2 E1 (35 30 36 28), gated to the bar, no decay, attack 20 ms | A440 ±1 c | −17 dB (−21 dBFS) | sine, H2 −11 dB, H3 −28 dB |
| 808 (rhythmic) | 25–96 | roots B0 F#1 C1 E1 + F#1 pickups; melodic riff in 41–56 | A440 ±5 c | 0 dB (loud), −8 dB (quiet beat-1 notes) | see §3.3 |

**Cell patterns** (used in the table below):

```
slot:        0  1  2  3 | 4  5  6  7 | 8  9 10 11 |12 13 14 15
H-odd  808:  q  .  .  . | X  .  .  X | .  .  X  . | .  X  .  .     X = loud root (len 3, each cut by the next; the slot-13 note runs into next bar's beat 1)
       kick: K  .  .  . | .  .  K  . | .  .  .  . | .  .  .  .     q = quiet root −8 dB re X, len 4
H-even 808:  .  q  .  . | X  .  .  H | .  .  .  . | .  P  .  .     H = loud root HELD to bar end (settles to −12 dB floor = SUB layer)
       kick: K  .  .  . | .  .  K  . | .  .  K  . | .  K  .  .     P = F#1 pickup (E bars only), −6 dB, len 3 (into next bar)
H2-all 808:  q  .  .  . | X  .  .  X | .  .  X  . | .  X  .  .     (E bars: slot 13 = F#1 instead of E1)
       kick: K  .  .  . | .  .  K  . | .  .  .  . | .  .  .  .
H3-BFC 808:  q  .  .  . | q  .  .  . | .  .  .  . | .  .  .  .     q = −8…−11 dB, long decay (no floor), gone by beat 4
       kick: K  .  .  . | K  .  .  . | .  .  .  . | .  .  .  .
H3-E   808:  q  .  .  . | q  .  .  . | .  .  X  . | .  P  .  .     X = E1 loud, P = F#1 loud (−1 dB)
       kick: K  .  .  . | K  .  .  . | .  .  .  . | .  .  .  .
```

Verse-2 riff (4-bar phrase, played identically in 41–44, 45–48, 49–52, 53–56; peaks −5 dB re the hook hits; grace notes g at −11 dB, length 1) [M,H on pitches/slots after verification; the first note is B1, not B0]:

```
V2-1 (Bm):  1:B1(2)  3:g C#1(1)  4:C#2(3)  7:D2(2)  9:g C#1(1)  10:C#2(2)  12:B0(2)  14:B1(2 → into next bar)
V2-2 (F#m): 1:A1(3)  4:F#1(3)  7:A1(3)  10:A1 weak −9 dB (3)  14:E2(1)  15:E1(1)
V2-3 (C):   1:A1(2)  3:g E1(1)  4:E2(3)  7:A1(2)  9:g E1(1)  10:E2(2)  12:A0 quiet −11 dB(1)  14:A1(2)
V2-4 (Em):  1:E2(2)  3:g E1(1)  [rest 4–6]  7:E2(2)  9:g E1(1)  10:D2(2)  12:E1(2)  14:A1(2 pickup)
kick V2: odd bars 0, 6 ; even bars 0, 6, 10, 13
```
(The riff never plays C under the C chord → that bar sounds as C6/Am7. The pad stays C.) A wide, ±25 c-detuned **octave-up double** of this riff (B2/C#3/D3 … 124–147 Hz) sits in the side channel at about −12 dB re the riff [M,M]; it gets ~6 dB louder from bar 49.

**Full bar table** (chord loop position: 1 = Bm, 2 = F#m, 3 = C, 4 = Em; "kick" slots are 16ths):

| Bars | Loop pos | Low layers playing | 808 pattern | Kick |
|---|---|---|---|---|
| 1, 3, 5, 7 | 1, 3 | BED-BASS only | none | 0 |
| 2, 4, 6, 8 | 2, 4 | BED-BASS only | none | none |
| 9–16 | 1-2-3-4 ×2 | BED-BASS + BED-SUB | none | 0, 6 |
| 17, 19, 21, 23 | 1, 3 | BED-BASS + SUB (B1 / C2 whole bar) | none (SUB only) | 0, 6 |
| 18, 20, 22 | 2, 4, 2 | BED-BASS + SUB (F#1 / E1 / F#1) | none | 0, 6, 10, 13 (bar 20: 0, 6, 10, 12) |
| 24 | 4 | BED-BASS only (SUB off) | none; optional F#1 pickup at slot 15, −23 dB [M,L] | none |
| 25, 27, 29, 31, 33, 35, 37, 39 | 1, 3 | 808 (B0 / C1) + BED-BASS at −16 dB (full on 27, 29, 31, 35, 37, 39) | **H-odd** | 0, 6 |
| 26, 30, 34, 38 | 2 | 808 F#1 + SUB floor F#1 | **H-even** (no pickup) | 0, 6, 10, 13 |
| 28, 32, 36 | 4 | 808 E1 + SUB floor E1 | **H-even** + P = F#1 @13 (bars 28/36 read @14) | 0, 6, 10, 13 (+ soft E1 kick @4 under the clap, −6 dB) |
| 40 | 4 (fill) | 808 E1 | q@1, q@5, X@7, X@10, F#1@13 | 0, 4, 8, 12 (four-on-the-floor), no clap |
| 41, 45, 49, 53 | 1 | 808 riff + octave double; BED-BASS full | **V2-1** | 0, 6 (51: 0 only) |
| 42, 46, 50, 54 | 2 | " | **V2-2** | 0, 6, 10, 13 |
| 43, 47, 51, 55 | 3 | " | **V2-3** | 0, 6 (55: 6 only) |
| 44, 48, 52 | 4 | " | **V2-4** | 0, 6, 10, 13 (44/52 drop the 6; 48: 0, 6, 10) |
| 56 | 4 (pre-drop) | 808 riff V2-4 continues, −10 dB sub pull in beats 1–2, B0 pickup at slot 15 | V2-4 | **none** |
| 57–71 | all | 808 + SUB floor; BED-BASS full | **H2-all** (E bars: F#1 @13) | 0, 6 (59: 0 only; soft @10 on 64, 66, 68) |
| 72 | 4 | 808 alone (drums out) | q@1, X@4, X@7, X@10, F#1@13 (loudest bass bar) | soft @4 only |
| 73, 75, 77, 79, 81, 83, 85, 87 | 1, 3 | 808 + BED-BASS | **H-odd** | 0, 6 (73, 83: 0 only) |
| 74, 78, 82, 86 | 2 | 808 + SUB floor | **H-even** | 0, 6, 10, 13 |
| 76, 80, 84 | 4 | " | **H-even** + F#1 @13 | 0, 6, 10, 13 (+ soft @4 on 80, 84) |
| 88 | 4 | 808 alone | as bar 72 | soft 0, 10, 13 |
| 89, 93 | 1 | 808 | previous F#1 tail held through slots 0–3, B0 q@4 | 0, 8 |
| 90, 94 | 2 | 808 | **H3-BFC** (F#1 q@0, q@4) | 0, 8 (94: 8 only) |
| 91, 95 | 3 | 808 | **H3-BFC** (C1 q@0) | 0, 8 |
| 92, 96 | 4 | 808 | **H3-E** (E1 q@0, q@4, X@10, F#1 X@13) | 0, 8 (+ soft @10 on 92) |
| 97–104 | all | BED-BASS only (+14 c), low-passed with the pad | none | none |

---

## 2. Arrangement — bar by bar

Timestamps are file positions (bar n = 0.29 + (n−1)·2.08696 s); for a render starting at 0.0 s subtract 0.29 s. Loudness = K-weighted bar-mean LUFS [M,H]. Rule applied: something audibly changes at every 8-bar line, and every drop is made of (sub re-entry + width collapse + new layer), never "drums come in" alone.

| # | Bars | Start (file) | Len | Name | Layers playing | What changes at the boundary (and inside) | LUFS |
|---|---|---|---|---|---|---|---|
| 1 | 1–8 | 0:00.29 | 8 | Intro | SAMPLE-PAD (with top octave), BED-BASS, clap 2&4, hats (2-bar loop: open-type on odd downbeats), knock, kick on beat 1 of odd bars only | Track opens ON the downbeat with the kick (−3 dBFS full-band stab), no fade-in, no HPF opening. Even bars have no sub at all (−23 dB). Cudi hum lives here in the vocal version (see §4.3). | −13.8 (odd −13.3 / even −14.5) |
| 2 | 9–16 | 0:16.99 | 8 | Verse 1a | + kick 1 & 2& every bar, + BED-SUB (octave-down bed bass, −26 dB), + faint 32nd hat layer | Additive, no fill before it: sub band +8.8 dB and now present in every bar; hat/clap unchanged. | −12.6 |
| 3 | 17–24 | 0:33.68 | 8 | Verse 1b / build | + SUB (A440 whole-bar roots, −17 dB), even-bar kick figure 1 2& 3& 4e, extra soft 1.5–5 kHz chop hits, width > 2 kHz −20 → −17 dB | Bar 17: sustained sub enters (first A440 element against the +14 c bed), kick density 2 → 4 on even bars, odd/even loudness alternation 1–1.4 dB. **Bar 24 = drop-out**: kick, clap, hats, SUB all out; pad continues; wide reversed tonal swell +14 dB over beats 2–4 (L/R corr → 0.5), no brightening; optional −23 dB F#1 pickup on slot 15. | −11.8; bar 24 −14.6 |
| 4 | 25–32 | 0:50.38 | 8 | Drop 1 / Hook 1a | 808 (B0!), kick H-odd/H-even, clap, hats (accents only), knock (loudest here), **LEAD RIFF** exposed, SAMPLE-PAD ducked −16 dB except C bars and bars 29/37, SUB floor on even bars | **THE drop**: sub +16 dB bar-to-bar (+40 dB from last 16th of 24), RMS +7.4 dB, width collapses −15 dB at the downbeat (swell cut dead), B and C roots fall an octave (B1→B0, C2→C1), 808 becomes the dotted-8th pulse, pad thins to let the riff through, the riff starts (WhoSampled's "sample at 0:50" [W]). | −10.2 (odd −11.0 / even −9.5) |
| 5 | 33–40 | 1:07.07 | 8 | Hook 1b | as 4 + hats add 2& 2a 3e at full level (second hat sample, +13 ms late), wide tonal layer toggles ON in 35–36 and 39 (side/mid 500–4k −12 → −6 dB) | Hats double (the brief's "hats double at 1:07.7"); first appearance of the wide 500 Hz–4 kHz layer. **Bar 40 = turnaround**: clap out, kick four-on-the-floor 1 2 3 4, 808 on every beat (slots 1, 5, 7, 10, 13), hats on every 8th, wash fully wide (side/mid 2–6 k ≈ 0 dB), no sweep, no dip. | −10.2; bar 40 −9.5 |
| 6 | 41–48 | 1:23.77 | 8 | Verse 2a | SAMPLE-PAD full, 808 **melodic riff** (−5 dB) + wide octave double, kick, clap, hats 16th runs (1& 1a 2e 2& / 3& 3a 4e 4&), knock, no beat-1 hat on even bars | Wide layer leaves (narrowest point: side/mid > 2 k −20…−22 dB), 808 goes up an octave and melodic, hats become two 4-note runs per half-bar, 120–250 Hz +2.8 dB, centroid up (2500–2650 Hz, hats). Bar 48: clap fill 4 4e 4& (−8 dBFS each), kick 1 2& 3&. | −10.4 |
| 7 | 49–56 | 1:40.46 | 8 | Verse 2b | as 6; the riff's wide octave double +6 dB (side/mid 2–6 k −26 → −19.5 dB) | Only the side channel changes (riff double louder); keep it, it is the record's own 8-bar move. **Bar 56 = pre-drop**: kick out, sub pulled ~10 dB (riff keeps playing), 120–400 Hz hit on beat 2, clap build 3&(−11) 4(−3) 4e(−7) 4&(−4) 4a(−5) re ref, bright **filter-opening riser** (2 k+ and 6 k+ bands +14 dB, centroid 1.1 → 3.0 kHz, the only such sweep in the track), reversed swell again (L/R corr 0.7); no loudness dip. | −10.4 |
| 8 | 57–64 | 1:57.16 | 8 | Drop 2 / Hook 2a | 808 H2-all (full pulse every bar), kick 1 2& only, clap, hats (+2& 2a 3e at −8 dB), SAMPLE-PAD full (+3 dB vs hook 1), **PAD-2 enters** (A440, no vibrato, brighter, −8 dB under the pad), LEAD thinned, wide layer toggles every 2 bars (ON 57, 59–60, 63–64), knock gone, SUB floor on every bar | Sub +9.4 dB, RMS +3.4 dB, width −7 dB at the downbeat; 250–500 Hz and 1–2 kHz +2.5 dB (two pads now beating at 0.81 %); the 808 takes over the even-bar pulse from the kick (kick thins to 1, 2& everywhere). | −9.3 |
| 9 | 65–72 | 2:13.86 | 8 | Hook 2b | as 8 + soft 3& kick on 64/66/68, riff variant a with the A3→A4 leap (65), wide layer ON 67–68, 71 | Lead riff second-pass variants; soft kick ghost; otherwise identical (the record's quietest boundary — if you want more, bring the wide layer ON for all of 65–72 [D]). **Bar 72 = transition**: hats and clap out, kick roll `XXXX|XXXX|XXXX|Xx..` at −6 dB, 808 roll q@1 X@4 X@7 X@10 F#1@13 (loudest bass bar), swell reused, wash fully wide. | −9.3; bar 72 −9.0 |
| 10 | 73–80 | 2:30.55 | 8 | Bridge / PEAK a | everything of 8 + **LEAD RIFF +7…10 dB and octave-doubled/brighter** (the "choral" layer), PERC-2 (wide dark shaker 16ths), hats densest (2e 2& 2a 3e 4 4&), kick H-odd/H-even figure back, 808 H-odd/H-even, wide layer ON throughout, PAD-2 +2 dB | Loudest section (−8.0). Entry is additive (RMS +0.8 dB): hats back (+10 dB > 6 k), all mids 250 Hz–4 kHz +2 dB, side/mid 500–4 k −4…−5 dB continuously, centroid +29 %. In the vocal version Cudi's "oohs" sit here (one phrase per loop) — see §4.3. | −8.0 |
| 11 | 81–88 | 2:47.25 | 8 | PEAK b | as 10; odd-bar hat accent 1& dropped (keeps 1a), extra clap on beat 3 of bars 77/81 (−10 dB), riff var-b in 85 drops C#4, "choral" swell rises into 85 beat 3 and 87–88 | Bar 84 is the loudest bar (−7.5). **Bar 88 = transition** (same recipe as 72: hats/clap out, 808 roll, kick roll; no swell). | −8.0; bar 88 −7.9 |
| 12 | 89–96 | 3:03.94 | 8 | Hook 3 / post-drop | 808 half-bar only (H3), kick on beats 1 & 2 (doubles the clap), clap, hats as E, PERC-2, pads, riff thinned (var-b shape, long E4 over C) | 808 and kick vanish from the second half of every bar (sub decays to −33 dB re ref by beat 4), except Em bars 92 and 96 which restore E1@3& + F#1@4e; the wide pad is exposed in the empty half-bars (side/mid −13 → −5.6 dB inside bar 89); 120–250 Hz −4.6 dB. Last clap bar 96 beat 4; last hat bar 96 slot 15. Optional reversed swell into 97 [M,L]. | −9.5 (92/96 −8.8) |
| 13 | 97–104 | 3:20.64 | 8 | Outro | SAMPLE-PAD + BED-BASS through a **~2 kHz 24 dB/oct low-pass**, PAD-2 at −5 dB under the pad (also low-passed); nothing else | **Hard cut** on the bar line: 808, kick, hats, clap all off in one step (sub −43 dB, > 6 k −30 dB, RMS −7.8 dB); the LPF closes during bar 97 (6 kHz −15 → −32 dB across the bar), then static 98–102 (1.6 k −3, 2–3.2 k −8, 4 k −16.5, 6.3–8 k −28 dB re unfiltered). **Bar 103: second LPF step** (another −15…−20 dB above 1.5 kHz, centroid 440 Hz, 60–120 Hz −12 dB). Bar 104 = Em, same level. **Hard digital cut (< 2 ms, no fade) on the bar-105 line at 3:37.33.** | −15.9 (103: −17.0) |

Transition summary: one-bar events at bars 24, 40, 56, 72, 88 (always loop position 4 = the Em bar). No crash cymbals anywhere (the odd-bar open-type hat is the same at section starts as elsewhere, sd 0.3 dB), no gated silence, no sidechain pump, no delays, no vinyl noise, no pad filter sweeps except bar 56 and the outro steps [M,H].

Loudness contour to hit (bar-mean LUFS): 1–8 −13.8 · 9–16 −12.6 · 17–23 −11.8 · 24 −14.6 · 25–39 −10.2 · 40 −9.5 · 41–55 −10.4 · 56 −10.4 · 57–71 −9.3 · 72 −9.0 · 73–87 −8.0 (84: −7.5) · 88 −7.9 · 89–96 −9.5 · 97–103 −15.9. Integrated −10.3 LUFS.

---

## 3. Sound layers — synthesis recipes

Level convention: 0 dB = peak of a loud 808 hit (= −4 dBFS on the bass stem). Width = side-minus-mid in dB (−∞ = mono). Env times in ms. Recipes are Faust/DawDreamer-style; pedalboard for effects. Register in MIDI.

### 3.1 KICK — fixed-pitch sub kick tuned E1 [M,H]
- Pitch: 130 Hz at 3 ms → 95 Hz @ 10–20 ms → 62 @ 30 → 44 @ 40 → settles **40.5–41 Hz (E1 −20 c)** by 60 ms; exponential sweep τ ≈ 15 ms. Same pitch under every chord.
- Amplitude: attack 3 ms (perc band 13–21 ms to sub peak at +22…+34 ms); hold ≈ 60 ms; then −6 dB @ 92–105, −10 @ 126–135, −20 @ 179–199, −30 @ ~205, −40 @ 220–233 ms (two-stage: slow then fast). Total ≈ 230 ms.
- Spectrum: body mildly symmetric-saturated (H3 −15 dB, H2 −38 dB, H4 −46); 120–400 Hz thump in the first 15 ms (−4 dB re total); click 1–8 kHz at −11…−14 dBFS gone in 16–35 ms; nothing above 4 kHz after 30 ms.
- Level **+4 dB** (0 dBFS, the loudest element, into the clipper). Mono (side −31 dB).
```
f(t)   = 41 * 2^(-20/1200) + 90*exp(-t/0.015)              // Hz
body   = sin(2*pi*∫f) -> tanh(1.3*x)                        // gives H3 ≈ -15 dB
env    = ar(3 ms, hold 60 ms, exp decay tau 35 ms)          // -40 dB at ~230 ms
thump  = bandpassed noise 120-800 Hz, 10 ms, -12 dB ; click = noise HPF 1 kHz, 5 ms, -12 dB
out    = (body*env + thump + click) -> softclip -> 0 dBFS ; mono
```
Velocity: full hits 0 dBFS; the "soft" E1 kick under the clap on beat 2 (bars 28/32/36/80/84 etc.) = −6 dB.

### 3.2 808 — chord-root sub with phase-locked octave [M,H after correction]
- Pitches: B0 30.87 / F#1 46.25 / C1 32.70 / E1 41.20 Hz, A440 within ±5 c (cycle-by-cycle median −1 c). **Not** +14 c.
- Waveform of the hits: sine + **octave at −6 dB (range −3…−10), phase-locked (relative phase −159°)**, H3 ≤ −24 dB on its own, nothing above ~H12. Ratio does not change with level → fixed waveform, **not** saturation. (The "even-order saturation to H40" one report described is the sum of the SUB floor's harmonic series + pad tones sitting on 808 harmonics; do not distort the hits.)
- Attack: full amplitude within one cycle (13–25 ms), no click (1–8 kHz < −40 dBFS at onsets).
- Decay: log-linear **−28 dB/s** for the first 300 ms (−6 dB @ 160 ms, −10 dB @ 290–390 ms), then −12…−17 dB/s; −20 dB only at 0.75–1.0 s. Retriggered every 391 ms (3 16ths) in the hooks, so each note is cut at about −10…−12 dB. Monophonic legato: new note cuts the old within one cycle, no release gap.
- Levels: loud hits 0 dB (−4 dBFS), quiet beat-1 notes −8 dB, hook-3 roots −8…−11 dB, verse-2 riff −5 dB (grace notes −11 dB). Mono (side −36 dB, L/R corr 1.000).
```
f0      = midi2hz(note)                                     // A440
osc     = sin(2*pi*f0*t) + 0.5*sin(2*pi*2*f0*t + pi*(-159/180))   // octave -6 dB, locked phase
env     = attack 15 ms ; decay: 10^(-28*t/20) for t<0.3 s then 10^(-(8.4 + 14*(t-0.3))/20)  ; release 10 ms on retrigger
post    = HPF 24 Hz (keep the 30.87 Hz fundamental!) ; LPF 6 dB/oct @ 400 Hz
gain    = -4 dBFS peak ; mono ; no glide, no pitch env
```
Verse-2 variant: same patch, output −5 dB, plus a side-only double one octave up (saw, 3-voice unison ±25 c, HPF 90 Hz, LPF 500 Hz, −12 dB re the riff, width 100 %) [M,M].

### 3.3 SUB — sustained whole-bar root (bars 17–23 and the hook even-bar floor) [M,H]
- B1 61.70 / F#1 46.27 / C2 65.39 / E1 41.21 Hz (A440, 0 ±1 c). Gated to the bar: starts on beat 1 (attack 10–90 % ≈ 20 ms), no decay (slope +2.5 dB/s), ends at the bar line (release 20 ms).
- Spectrum: H2 −11 dB, H3 −28 dB; under the hooks it carries a weak full harmonic series on the root (H5–H10 at −25…−40 dBFS, 0 c) which fills the mids at 0 c — model it as a lightly saturated sine.
- Level −17 dB in 17–23; −12 dB as the hook even-bar floor (the held 2a note "settles" there). Mono.
```
osc = sin(2*pi*f0*t) -> tanh(1.8*x)  (H2 ≈ -11 dB after an asymmetric 0.15*x^2 term) ; LPF 12 dB/oct @ 500 Hz
env = gate per bar, A 20 ms, R 20 ms ; gain -21 dBFS (17-23) / -16 dBFS (hook even bars, from slot 7)
```

### 3.4 BED-BASS and BED-SUB (the Röyksopp-derived root voice) [M,H]
- B2 124.50 / F#2 93.27 / C3 131.90 / E2 83.13 Hz = +14 c. Whole bar, legato, no vibrato (±0.3 c), no attack transient. H2 −8 dB, H3 weak. Width −15 dB.
- Level −13 dB (−17 dBFS); in drop 1 (25–40) ducked to −29 dB except on bars 27, 29, 31, 35, 37, 39 (full). BED-SUB = same note one octave down, −26 dB, bars 9–16 only.
```
osc  = sin(2*pi*f) + 0.4*sin(4*pi*f) , f = midi2hz(n)*2^(14/1200)
env  = legato gate, A 10 ms, R 10 ms (no gap at chord change)
pan  = centre ; width: mono -> 15 % chorus (0.5 ms, 0.3 Hz) for side -15 dB
```

### 3.5 SAMPLE-PAD — "humming keys" (the signature bed) [M,H]
- Voicing: §1.2 column 4 (root oct 2, close triad oct 3–4, same triad oct 4–5 at −3…−10 dB; top octave 8–12 dB down). Bare triads: 7ths/9ths ≥ 38 dB down. All partials **+14 c**.
- **Vibrato: sinusoidal pitch LFO at exactly the 16th rate (7.667 Hz at 115 BPM), ±11.5 c (24 c pk-pk), applied to all chord voices coherently, phase-locked to the grid (phase −134° at every downbeat), free-running carriers.** Not on the bed bass. This is what reads as "humming". [M,H]
- Spectral envelope: flat 160–640 Hz, −4 dB/oct above ~700 Hz, 95 % of energy below 1.8 kHz; partials above 1 kHz ≤ −17 dB. LPF ≈ 1.4 kHz 24 dB/oct. A fixed resonance at ~425 Hz (A4 −57 c) at −12…−15 dB on F#m and Em bars (optional colour).
- Amplitude: constant within ±1 dB across the bar; legato, chord changes < 20 ms, no retrigger.
- Stereo: side −15 dB, L/R corr 0.96, no L/R pitch offset, no Haas.
- Level: −13 dB (−17 dBFS for the chord sum) in intro/verses/hook 2/bridge/outro; −29 dB in drop-1 bars 25, 26, 28, 30, 32, 33, 34, 36, 38, 40; +2 dB in 73–88. Outro: extra LPF 2 kHz 24 dB/oct (3 kHz −22 dB, 6 kHz −42 dB re 1 kHz); bar 103 a further step (≈1 kHz).
- Register: MIDI 40–78.
```
voice(f) = 0.5*saw(f) + 0.5*pulse(f, 0.5)          // or two saws ±4 c
f_mod    = f * 2^(14/1200) * 2^( 0.0115/12 * sin(2*pi*7.667*t + phi) )   // phi so that phase = -134 deg at bar lines
chord    = sum(voice(f_mod_i) * level_i)            // levels from the §1.2 table
filter   = LPF 24 dB/oct, fc 1.4 kHz, Q 0.7  ; outro: + LPF 24 dB/oct fc 2.0 kHz (bar 97 sweep 4k->2k over the bar; bar 103: fc 1.0 kHz)
env      = legato gate, A 15 ms, R 15 ms
stereo   = mono -> short chorus (0.5 ms, 0.3 Hz, 15 %) => side -15 dB
gain     = -17 dBFS ; delay the whole track +20 ms vs the drum grid
```

### 3.6 LEAD RIFF — the interpolated Röyksopp top line ("chopped vocal" in press; measured: pad-synth voice, no formants) [M,H]
- Same +14 c tuning, **no LFO**, fixed ~−12 dB/oct roll-off above 500 Hz (H2 −12…−18, H3 −26…−29, H4 −33 dB). Gated notes: attack 35 ms, flat sustain ≈ 250 ms, release ≈ 50 ms (notes ≈ 2 16ths). Monophonic. Side −12 dB.
- Level −13 dB (−17 dBFS peaks) in 25–40 and 57–72; **+7…+10 dB louder and brighter (strong 4th partial, octave-doubled) from bar 73 to 96** (this is the "choral" layer Demucs routes to vocals; press calls it choral vocals [W]).
- Register MIDI 61–69 (C#4–A4). Notes in §4.1.
```
voice  = 0.5*saw(f) + 0.5*pulse(f,0.5), f = midi2hz(n)*2^(14/1200) ; LPF 12 dB/oct fc 500 Hz (-12 dB/oct above)
env    = A 35 ms, D 0, S 1, R 50 ms ; mono legato off (each chop re-attacks)
bridge = + octave-up copy at -6 dB, LPF fc 1.2 kHz, output +8 dB, side widened to -6 dB (chorus 2 ms / 0.4 Hz / 40 %)
```

### 3.7 PAD-2 — second chord synth (bars 57–104) [M,H on existence, M on detail]
- A440 (0 ±2 c), **no vibrato**, 3-voice unison ±3.5 c (partial triplets 2.7–3.9 Hz apart at 1.5 kHz), legato. Includes thirds and 7ths/9ths (§1.2 column 6), bright: octave-6 partials 8–18 dB louder than the sample's; LPF 12 dB/oct 3.5 kHz.
- Width: upper partials wide (side −3…−6 dB in octaves 5–6), fundamentals as narrow as the sample.
- Level: −21 dB (8 dB under the pad) in 57–72, −19 dB in 73–96, −18 dB (5 dB under the pad) in the outro. Register MIDI 40–86.
- Beats against the +14 c pad at 0.81 % (2 Hz at 250 Hz, 5 Hz at 600 Hz): keep both tunings.
```
voice(f) = saw(f) + saw(f*2^(3.5/1200)) + saw(f*2^(-3.5/1200)) panned L/C/R
chord    = root oct3 + triad oct4 + triad oct5 + 7th/9th oct5-6 at -12 dB
filter   = LPF 12 dB/oct fc 3.5 kHz ; env A 30 ms R 50 ms legato ; outro: LPF follows the pad's 2 kHz/1 kHz steps
```

### 3.8 WIDE TONAL LAYER (side-channel 500 Hz–4 kHz, bars 35–36, 39, 40, 57–72 toggling, 73–96 on) [M,H on behaviour; M on identity]
Measured as a tonal, decorrelated layer (side flatness 0.14–0.19, chroma E/F#/B). Best reading: PAD-2's wide upper voices + the riff's chorus. Implement as a stereo-width send: the PAD-2 upper triad (oct 5) through a 100 %-wet 2-voice chorus (12 ms / 0.2 Hz, L/R inverted) at −20 dB, with an automation lane: ON 35–36, 39, 40, 57, 59–60, 63–64, 67–68, 71, 72–96 (continuous), 97–104 (survives the low-pass at −2…−4 dB side/mid). Target side/mid 500 Hz–4 kHz: intro −19, drop 1 −15…−18 (ON bars −6), verse −20…−22, drop 2 −7/−12 alternating, bridge −4…−5, post-drop −5, outro −2…−4.

### 3.9 CLAP (backbeat) + the only reverb [M,H]
- 4-flam layered clap: sub-transients at 0, 10, 20, 32 ms, onset→peak 44 ms. Spectrum 20–80 ms: centroid 4.3 kHz, flatness 0.74; **1.2–2.5 kHz strongest** (−3 dB re total), 600–1.2 k −7, 2.5–5 k −8, 5–10 k −11, 10–16 k −19; peaks 1.3 k, 1.7 k, 2.2 k, 2.8 k, 3.1 k, 4.0 k. Body decay −6 @ 7, −12 @ 26, −20 @ 53 ms.
- Reverb tail: plateau −28…−38 dB re peak from 75–450 ms, slope −23 dB/s → **T60 ≈ 2.6 s (1.8–2.6 across two measurements), pre-delay 25–30 ms, 100 % wide** (side −1…−3 dB), HPF 400 Hz, LPF 8 kHz. Body mono (side −18 dB).
- Level −5 dB (−9 dBFS). On beats 2 and 4 of every bar 1–96 except 24, 40, 72, 88; bar 56 = build (see §5); bar 48 = fill.
```
clap   = Σ_k noise burst at {0,10,20,32} ms: (BPF 1.6 kHz Q 0.7 + BPF 3.1 kHz Q 1), 8 ms decay
       + body at 32 ms: noise BPF 1.3-2.5 kHz, decay to -20 dB at 53 ms
reverb = plate, pre-delay 25 ms, T60 2.4 s, HPF 400, LPF 8 k, send -28 dB, width 100 %
```

### 3.10 HATS [M,H]
- Closed hat: peaks 3.4–4.0 kHz and 12.4 kHz, centroid ~9.5 kHz, −6 dB @ 1–4 ms, −20 @ 37–40, −30 @ 54 ms (dead by 80 ms). Velocity spread < 3.5 dB (machine-static). Side −15 dB.
- Beat-1 variants: **odd bars** = open-type hit (peak −19 dB re ref, plateau ≈ −26 dB for ~300 ms, −6 dB @ 276, −20 @ 307 ms; 6.6–8.5 kHz centre; mono) on beat 1 of every odd bar 1–95, identical in every section (not a crash); **even bars** = closed hat −15…−16 dB (absent in 41–56).
- Second hat sample from bar 33: same level, placed 13 ms late.
- Levels re ref: accents −12 (−16 dBFS); added 16ths −20 (−24 dBFS); 2e in 73–96 −27 (−31 dBFS); ghosts −33.
```
hat  = white noise -> HPF 3 kHz 12 dB/oct -> peak +6 dB @ 3.7 kHz Q 2, +4 dB @ 12.4 kHz Q 3 -> LPF 16 kHz ; env A 1 ms, exp tau 16 ms
open = same noise -> peak +6 dB @ 7.5 kHz ; env A 1 ms, plateau 300 ms at -26 dB, release 30 ms ; mono
```

### 3.11 PERC-2 — soft dark wide shaker (bars 73–96) [M,M]
Centroid 6.2 kHz, strong 1–3 kHz, −20 dB @ 22 ms, −30 @ 74 ms, side −7 dB. Level −23 dB (−27 dBFS). On 16ths 5, 6, 7, 8, 9, 13, 14, 15. Recipe: decorrelated L/R noise → BPF 2–8 kHz (centre 4 kHz, Q 0.5), τ 25 ms.

### 3.12 KNOCK — low-mid perc on 1& (bars 1–54) [M,M]
300–600 Hz dominant (peaks 436/417/937 Hz), zero-crossing pitch ≈ 350 Hz, flatness 0.5–0.57, attack 10–28 ms, −12 dB @ 28 ms, side −9.5 dB. Level −12 dB (−16 dBFS) in 25–40, −16 dB elsewhere; absent from bar 57. Recipe: noise BPF 420 Hz Q 2 + 350 Hz sine ping (τ 20 ms) + −12 dB click; τ 15 ms; 30 % width.

### 3.13 REVERSE SWELL FX (bars 24, 56, 72; optional 96) [M,H]
Fully decorrelated (L/R corr 0.05–0.37), noisy-tonal (flatness 0.44–0.65), fixed partials 735 / 974 / 1074 / 1181 / 1315 Hz; side 300 Hz–4 kHz rises ≈ +12 dB (−26 → −14 dBFS) over the last 2 s, peaks 0.22 s before the downbeat, cut dead at the downbeat (−46 dB within 100 ms). No pitch sweep, no brightening (centroid flat 1.4–1.7 kHz). Level −10 dB (−14 dBFS) at its peak. Recipe: reverse a 2 s chord/crash with reverb, HPF 300 Hz, ringing filter bank at the five partials (Q 30), width 100 % (independent L/R noise seeds), exponential fade-in +12 dB, hard stop at the bar line.

### 3.14 BRIGHT RISER (bar 56 only) [M,H]
Centred above 6 kHz, wide 2–6 kHz; 2 k+ band −34.5 → −20.9 dBFS and 6 k+ −42 → −28 over the bar, mostly beats 3–4; centroid 1.1 → 3.0 kHz. Recipe: white noise → HPF sweeping 1 kHz → 8 kHz (exponential over 2.09 s) → level −35 → −21 dBFS; mono above 6 kHz, 2–6 kHz through the swell's wide chorus.

### 3.15 Level/width/register summary

| Layer | Level re 808 hit | dBFS | Width (side−mid) | Register (MIDI) | Bars |
|---|---|---|---|---|---|
| KICK | +4 | 0 (clipped) | mono (−31) | 28 (E1) | 1–96 |
| 808 loud / quiet | 0 / −8 | −4 / −12 | mono (−36) | 23–30 (riff 21–40) | 25–96 |
| SUB | −17 (floor −12) | −21 / −16 | mono | 28–36 | 17–23, even bars 25–40, 73–88 |
| BED-BASS / BED-SUB | −13 / −26 | −17 / −30 | −15 / mono | 40–48 / 28–36 | 1–104 / 9–16 |
| SAMPLE-PAD | −13 (−29 ducked, −11 bridge) | −17 | −15 | 40–78 | 1–104 |
| LEAD RIFF | −13 (−5 from 73) | −17 (−9) | −12 (−6 from 73) | 61–69 (+ 73–81 double) | 25–40, 57–96 |
| PAD-2 | −21 / −19 / −18 | −25 / −23 / −22 | −3…−6 (oct 5–6) | 40–86 | 57–104 |
| CLAP | −5 | −9 | body −18, tail −2 | — | 1–96 |
| HAT closed / open-type | −12…−20 / −19 | −16…−24 / −23 | −15 / mono | — | 1–96 |
| PERC-2 | −23 | −27 | −7 | — | 73–96 |
| KNOCK | −12…−16 | −16…−20 | −9.5 | — | 1–54 |
| SWELL / RISER | −10 / −17 | −14 / −21 | ≈ 0 (decorrelated) / centred > 6 k | — | 24, 56, 72, (96) / 56 |

---

## 4. Riff and vocal-texture plans

### 4.1 Lead riff — MIDI notes (16th slots; lengths in 16ths) [M,H pitches, M lengths]
8-bar phrase = two passes of the loop; only the Bm bar differs (variant a on odd passes, b on even). Every phrase ends on a note that carries across the bar line (slot 16 = next bar's beat 1).

| Loop bar | Slot | Beat | MIDI | Note | Len | Notes |
|---|---|---|---|---|---|---|
| Bm var a (25, 33, 73, 81) | 6 | 2& | 66 | F#4 | 1.5 | |
| | 9 | 3e | 67 | G4 | 1.5 | |
| | 11 | 3a | 66 | F#4 | 1.5 | **bars 73, 81 only** |
| | 14 | 4& | 64 | E4 | 1.5 | |
| | 16 (next bar 0) | 1 | 66 | F#4 | 3 | held tail over F#m |
| Bm var b (29, 37, 77, 85) | 6 | 2& | 62 | D4 | 2.8 | |
| | 9 | 3e | 61 | C#4 | 1.3 | 85: D4 held instead |
| | 11 | 3a | 62 | D4 | 2.5 | |
| | 14 | 4& | 69 | A4 | 1.8 | the one leap |
| | 16 | 1 | 61 | C#4 | 2.3 | held tail (re-articulated at slot 2 in 30, 78) |
| F#m bar | 0–3 | 1 | (tail) | | | then **rest** — the breath of the phrase |
| C bar (27, 31, 35, 39, 75, 79, 83, 87) | 6 | 2& | 64 | E4 | 2.5 | |
| | 8 | 3 | 64 | E4 | 1.2 | 75, 83, 87 (re-articulation) |
| | 9 | 3e | 62 | D4 | 1.2 | 27, 31, 83, 87 |
| | 11 | 3a | 64 | E4 | 2.6 | 39, 75, 79, 83, 87 |
| | 14 | 4& | 66 | F#4 | 1.7 | |
| | 16 | 1 | 67 | G4 | 2–3 | = Em bar slot 0 |
| Em bar (28, 32, 76, 84, 88) | 0 | 1 | 67 | G4 | 2.5 | |
| | 5 | 2e | 66 | F#4 | 1.5 | |
| | 8 | 3 | 64 | E4 | 2.5 | |
| | 12–13 | 4 | 62 | D4 | 2 | |

Section use: 25–40 as listed (drop 1); 57–72 thinned (57: G4@9 E4@14; 59: E4@6, E4@12; 60: E4@0 E4@6 E4@8 E4@10; 61: D4@2 D4@6 A4@14; 63: E4@5 E4@11; 64: E4@0 E4@6 E4@8; 65: F#4@7 A4@8 E4@14; 67: E4@6 F#4@14; 68: E4@0 E4@4 E4@8; 69: D4@6 D4@11; 71: E4@5 E4@7 F#4@14; 72: E4@0 F#4@4 E4@8); 73–88 busier version (adds the slot-11 F#4 and the C-bar re-articulations; bar 36/40-type Em bars become G4@0 E4@8 D4@12); 89–96 thinned (89: F#4@6 E4@14; 90: F#4@0; 91: E4@6 E4@8 E4@11; 93: D4@5 D4@6 C#4@9 D4@11; 95: E4 long over C). In 1–24, 41–56 and the outro the riff is not separately present (the register is the pad). MIDI reference: `refs/bp/eig_inst_basic_pitch.mid` and `rf4_riff.txt`.

### 4.2 Kid Cudi's hook (vocal version only) — for an optional "hum-lead" texture [M,H pitches]
Same riff **one octave down (MIDI 49–57, C#3–A3)**, slightly straightened:
- Bm var a: (F#3@6) A3@8 (grace) G3@9 F#3@11–12 E3@14 → F#3 held ≈ 1 beat into the F#m bar.
- Bm var b: D3 repeated slots 3–7 (2–4 hits), C#3@9, D3@11, A3@14 → C#3 held ≈ 1–1.3 beats.
- F#m bar: held tail then rest.
- C bar: E3 (often anticipated from slot 0–4), E3@6, D3@9 (sometimes), E3@11, F#3@14 → G3.
- Em bar: **G3@0 F#3@4 E3@8 D3@12**, one per beat (3–4 16ths each) — the most consistent line.
Present in bars 25–40, 57–72, 89–104 (+12…+15 dB excess in the C3–B3 octave); verse-type long notes in 9–24 and 41–56 (A3 held over F#m, C3 held over C); ≈ none in 73–88.

### 4.3 Hum / "ooh" textures — synthesis plan (no words; the official instrumental has none [M,H], so these are an optional layer, default −6 dB below where the voice sits) [D]
Measured facts to copy: Cudi's hum is monophonic, pitch-stable to 1–5 c frame-to-frame (same as his sung notes, so NOT hard-tuned/vocoded by measurement; the vocoder description is press-only [W]), register D3–A3, strong octave-above energy; the bridge "oohs" are a 2–3-pitch-class stack, top voice E4–A4, one phrase per 4-bar loop at 2:34.7, 2:43.2, 2:51.5, 2:59.3 (file time), all diatonic to B minor.

**VOX-HUM** (intro, 2.8–8.6 s, then ad-lib 11–15 s) — contour: A3 (2.8–3.1) → G3 → E3 (4.1) → F#3 (4.4) → E3 (5.1–5.4) → **D3 (5.5–6.3)** → **E3 (7.0–7.6)** → F#3 (8.2–8.7); ad-lib climb G3 (11.0) A3 (12.0) C#4 (13.0) B3 (14.0–15.2) landing on the tonic.
```
source   = pulse train / glottal (Rosenberg) at f0, 0.5 % jitter, vibrato 5 Hz ±6 c starting 300 ms into each note
formants = closed-mouth "mm": F1 250 Hz (BW 60, 0 dB), F2 1000 Hz (BW 120, -18 dB), F3 2500 Hz (BW 200, -30 dB), nasal zero at 1.0 kHz (-15 dB); LPF 1.5 kHz 12 dB/oct
layers   = unison + octave-up copy at -10 dB (measured "strong octave-above energy")
env      = A 120 ms, R 250 ms, legato between notes with 40 ms pitch steps (no long glide)
level    = -20 dB re 808 (-24 dBFS) ; mono, 10 % width ; plate reverb 1.6 s, send -20 dB
```
**VOX-HOOK** (if used, bars 25–40, 57–72, 89–104): the §4.2 line through the same voice with an "oo" vowel (F1 300, F2 870, F3 2240), unison + octave-up −8 dB, level −12 dB re 808, side −12 dB.
**VOX-CHOIR** (bridge 73–88, four phrases): 3-voice stack = top E4 (hold 1–2 s) → D4 → F#4 → G4 → F#4 → E4, tail rising to A4 or C#5; middle voice a diatonic 3rd below; bass support E3–A3 one octave below the top; vowel "oh" (F1 570, F2 840, F3 2410) morphing to "oo"; each voice 2 detuned copies ±8 c with independent 0.3 Hz drift; chorus 15 ms / 0.3 Hz / 50 % for width (side −6 dB); level −16 dB re 808; swell in over bars 73 and 87–88. Phrases start on the C bar of each loop (bars 75, 79, 83, 87) and last ≈ 8 s.

---

## 5. Drum programming per section

16th grid, slots 0–15. Velocity scale (MIDI, from measured peak levels): 127 = 0 dBFS kick; clap 110 (−9 dBFS); hat accent 105 (−16 dBFS); hat −20 dBFS 90; −24 dBFS 78; −28 dBFS 65; −31 dBFS 55; −37 dBFS 40; open-type 85; PERC-2 60; knock 95 (−16 dBFS) / 80. Everything quantised; apply +1 ms to hats on e/a 16ths, +2 ms to claps, +13 ms to the second hat sample (33–40 additions), 0 to kicks. No swing, no humanize.

```
Legend: K kick  k soft kick (−6 dB)  C clap  c soft/ghost clap  O open-type hat  H hat accent  h added hat  . rest
Slot:                 0 1 2 3 | 4 5 6 7 | 8 9 10 11 | 12 13 14 15

INTRO 1–8      odd:  K/O . H H | C . . . | . . H H | C . . .          kick only on bars 1,3,5,7; O on odd bars
               even: h . H H | C . . . | . . H H | C . . .          h = closed hat 90
               knock on slot 2 every bar (80)

V1a 9–16       odd:  K/O . H H | C . K . | . . H H | C . . .
               even: K/h . H H | C . K . | . . H H | C . . .          (+ faint 32nd hats 40 appear on 8/9 and 13/14 from bar 17)

V1b 17–23      odd:  K/O . H H | C . K . | . . H H | C . . .
               even: K/h . H H | C . K . | . . K H | C K . .          kick 0,6,10,13; hats 2,3,10,11 (+ faint 32nd hats 40)
BAR 24:        no K, no C, no H ; swell only

HOOK1a 25–32   odd:  K/O . H H | C . K . | . . H H | C . . .          808 fills 4,7,10,13 (not drums)
               even: K/h . H H | C . K . | . . K H | C K . .          (+ k at slot 4 under the clap on 28, 32)
               knock slot 2 (95)

HOOK1b 33–40   odd:  K/O . H H | C . K h | . h H H | C . . .          h = second hat sample at full level (105), +13 ms
               even: K/h . H H | C . K h | . h K H | C K . .
BAR 40:        K . H . | K . H . | K . H h | K . H h    (kick 0,4,8,12; hats every 8th 90; NO clap; 808 every beat)

VERSE2 41–56   odd:  K/O . H H | C h H . | . . H H | C h H .          hats 2,3,5,6,10,11,13,14 at 105 (two 4-note runs); no even-bar beat-1 hat
               even: K . H H | C h K H | . . K H | C K h .            kick 0,6,10,13 (44/52: 0,10,13)
               knock slot 2 (95)
BAR 48:        K . H H | C h K . | . . K H | C C C .    clap roll 12,13,14 at 110
BAR 51: kick 0 only ; BAR 55: kick 6 only
BAR 56:        . . h . | . . h . | . . h c | C c C c    hats 65; clap build: slot 10 (80), 12 (115), 13 (95), 14 (110), 15 (105); NO kick; riser + swell

HOOK2 57–72    odd:  K/O . H H | h . K h | . h H H | C . h .          h on 4,7,9 at 78 (−24 dBFS); slot 14 ghost 40 (odd bars)
               even: K/h . H H | C . K h | . h H H | C . . .          kick 0,6 only (59: 0 ; soft 10 on 64,66,68)
               (bar 57: clap on 12 only — measured; keep)
BAR 72:        . . . . | k . . . | . . . . | . . . .    soft kick slot 4; hats/clap out; 808 roll q1 X4 X7 X10 F#1@13; swell

BRIDGE 73–88   odd:  K/O . H H | C h h h | h h H H | C . p p         kick 0,6 (73,83: 0 only); hats 2,3 (105), 5 (55), 6,7 (78), 8 (65), 9 (80), 10,11 (105), 12 (clap+hat 85), PERC-2 p on 5,6,7,8,9,13,14,15 (60)
               even: K . H H | C/k h h h | h h K H | C K p p         kick 0,6,10,13 (+ k at 4 on 80, 84)
               81–88: odd bars drop the slot-2 accent (keep 3); extra clap on slot 8 of bars 77, 81 (85)
BAR 88:        k . . . | . . . . | . . k . | . k . .    soft kicks 0,10,13; hats/clap out; 808 roll as 72; no swell

HOOK3 89–96    odd:  K/O . H H | K/C h h h | h h H H | C . p p        kick 0 and 8 (doubles the clap); hats as bridge
               even: K . H H | K/C h h h | h h H H | C . p p        (92: + soft 10 ; 94: 8 only)
               last clap = bar 96 slot 12 ; last hat = bar 96 slot 15

OUTRO 97–104   nothing
```
Open-type hat: beat 1 of **every odd bar 1–95** (even in bar-24-type? no: bar 24 has none; bars 41–55 keep it; 57–87 keep it). Even-bar beat-1 closed hat (90) except bars 41–56.

Kick summary (the thing that changes most): intro 1 of odd bars · 9–16 `1 2&` · 17–56 and 73–88 2-bar cell (odd `1 2&`, even `1 2& 3& 4e`) · 40 four-on-the-floor · 57–72 `1 2&` everywhere (808 takes the pulse) · 89–96 `1 2` · 97+ none.

---

## 6. Mix / master targets (measured on the reference)

| Target | Value | Notes |
|---|---|---|
| Integrated loudness | **−10.3 LUFS** (instrumental; vocal version ≈ −8.7…−9.3) | BS.1770-4 gated |
| Peaks | sample peak 0.00 dBFS, true peak +0.46 dBTP, **hard clipper** (~20 000 samples ≥ 0.999, runs up to 20–50 samples) | limiter/clipper is the only dynamics processing measurable; ducking ≤ 3–4 dB for < 100 ms after kicks in 56–72, none in drop 1 (no slow pump) |
| RMS / crest | −10.5 dBFS / 10.5 dB overall; drops −9…−9.5 dBFS, crest 8–9 dB; intro −15.8 dBFS, crest 15–17 dB; outro −18.2 dBFS | |
| Band energy shares (whole track) | 0–60 Hz **57.0 %** · 60–120 Hz 11.8 % · 120–400 Hz 18.5 % · 400 Hz–2 kHz 10.8 % · 2–6 kHz 1.2 % · 6 kHz+ 0.7 % | 30–60 Hz is +6.4 dB over 60–120 Hz: the B0 808 and E1 kick own the record |
| Per-bar band RMS (mono, dBFS): drops | sub < 80 Hz −11…−12 · 150–400 −18…−21 · 400–1.5 k −19…−23 · 1.5–5 k −26…−29 · > 8 k −34…−36 (odd bars 2 dB brighter > 8 k than even) | `bar_band_rms.txt` |
| … intro / outro | intro: sub −19 (odd) / −39 (even), 150–400 −21, 400–1.5 k −22, 1.5–5 k −28.5, > 8 k −34.6; outro: sub < −48, 150–400 −22, 400–1.5 k −23, 1.5–5 k −35, > 8 k −70…−78 | |
| Spectral centroid (full mix, per bar) | intro 2000–2500 Hz (odd/even alternation), drop 1 1700–2100, verse 2 2000–2650, drop 2 1850–2360, bridge 2080–2570, hook 3 2300–2800, outro 750–1136 → bar 103 441 Hz; whole track 1839 Hz | brightness steps per section, never sweeps (except bar 56) |
| Harmonic-stem centroid | ≈ 850 Hz (bars 1–32) → 1100–1350 Hz (73–96): PAD-2 is what brightens the mids | |
| Stereo | sub < 60 Hz side/mid −37.6 dB; < 120 Hz −27.4; < 200 Hz −23 (sub strictly mono). 60–120 Hz: mono in drops, −17 intro, −14.5 verse 2 (riff double). Full-band L/R corr 0.96–0.98 bars 1–32, 0.95 verse 2, 0.88–0.93 drops 2/3, 0.82 post-drop/outro; 0.50 bar 24, 0.70 bar 56 | |
| Width per band, 500 Hz–4 kHz side/mid | intro −19 · drop 1 −15…−18 (−6 in 35/36/39) · verse 2 −20…−22 · drop 2 −7 / −12 alternating · bridge −4…−5 · hook 3 −5 · outro −2…−4; transition bars 40/72/88 ≈ 0 dB in 2–6 kHz | automation lane for §3.8 |
| Clap reverb | the only reverb: T60 ≈ 2.4 s, pre-delay 25 ms, side −2 dB on the tail | |
| Absent | delays, vinyl crackle (noise floor = digital silence), sidechain pump, section crashes, gated silence, HPF intro opening | |
| Loudness contour | see §2 (intro 5.9 dB under the peak section; biggest step bar 24 → 25 = +7.4 dB RMS) | |
| Ending | hard digital cut at the bar-105 line, no fade, no tail | |

Suggested chain: stems → bus (no compression) → clipper at 0 dBFS driven so that the kick clips (~20 000 clipped samples over the track) → ceiling 0.0 dBFS sample peak. Check: 57 % < 60 Hz, −10.3 LUFS integrated, bar contour within ±0.5 dB of §2.

---

## 7. What makes this track feel the way it does — ranked

1. **The 808 pulse lives between the kicks.** Kick on 1 and 2&, 808 on 2 · 2a · 3& · 4e (a dotted-8th chain starting on the backbeat and landing on the next downbeat; inter-hit spacing 391 ms), and the two never coincide (0 of 47 loud 808 hits within 40 ms of a kick in hook 1). On even bars the kick takes the 3& 4e pulse and the 808 holds. At 115 BPM with a clap on 2 and 4 and straight 16ths this is a dance/house bounce, not halftime trap — the "rubbery bass" of the press release and r/hiphopheads' "Random Access Memories" comparison [M,H; W].
2. **Sub-first mastering.** 57 % of the energy is below 60 Hz; the 808 sits at B0 (30.9 Hz) with a phase-locked octave, the E1 kick is the loudest element and is hard-clipped at 0 dBFS; the drop at bar 25 is a +40 dB sub step plus a 15 dB width collapse rather than a drum entry. Death Oblivion's 25:10 808-to-kick ratio is the documentary echo of this [M,H; W].
3. **Röyksopp's loop, re-voiced and detuned.** Bm · F#m · C · Em (the album's Dm7 Am7 E♭maj7 B♭/G down 3 st) played as bare close triads with the chromatic inner line D–C#–C–B and the Neapolitan C, +14 c sharp against an A440 low end; a 16th-synced ±11.5 c pitch LFO makes the pad "hum". From bar 57 a second A440 pad beats against it at 0.81 % — the shimmer of the second half [M,H; W cifraclub/Hooktheory].
4. **The hook is an interpolated instrumental chop, phrased like a voice.** 8-bar riff in C#4–A4, dark (−12 dB/oct above 500 Hz, no formants), gated 35/250/50 ms, every phrase ending on a held note across the bar line and the F#m bar left empty as a breath; Cudi sings the same line an octave down. From bar 73 it is doubled/brightened +7–10 dB and becomes the "choral" peak [M,H].
5. **Two-bar cells inside eight-bar phrases.** Odd and even bars differ everywhere (open-type hat on odd downbeats, kick figure, 808 scheme, 1–1.4 dB loudness alternation); every section lands on bar 8n+1; the only fills are the Em bar at the end of a phrase (24, 40, 56, 72, 88) with 808/kick rolls and a reused reversed swell — never a crash, never a silence [M,H].
6. **Width is an arrangement parameter.** Mono below 120 Hz always; the intro and verse 2 are nearly mono (L/R corr 0.96–0.98, side −19…−22 dB), a tonal wide layer toggles on in 2-bar stretches (35–36, 39, 57–71) and then stays on for the peak (side −4…−5 dB); the swells are the only fully decorrelated moments (corr 0.5) [M,H].
7. **Brightness by steps, not sweeps.** Each section has its own fixed centroid; the single filter-opening riser is bar 56; the outro is a stepped 2 kHz → 1 kHz low-pass with a hard digital cut on the bar-105 line [M,H].
8. **Dry, clean, digital.** No delays, no vinyl noise, no sidechain pump; the only space is the clap's 2.4 s wide plate at −28 dB. Everything else is close and mono-ish, which is why the few wide elements read so strongly [M,H].

---

## 8. Build order (suggested)
1. Grid + chord/bass MIDI (§1) at 115.000, 104 bars; drum MIDI (§5) from `drums_measured.mid` as a cross-check.
2. KICK, 808, SUB, BED-BASS (§3.1–3.4): verify sub share and the 808/kick never-coincide rule.
3. SAMPLE-PAD with synced LFO and +14 c (§3.5); LEAD RIFF (§3.6, §4.1); PAD-2 (§3.7) from bar 57.
4. Clap+plate, hats, open-type, knock, PERC-2 (§3.9–3.12); swells/riser (§3.13–3.14) on bars 24/56/72/(96).
5. Automation: pad duck in drop 1, wide-layer lane (§3.8), outro LPF steps, hard cut.
6. Master: clipper to 0 dBFS, −10.3 LUFS, contour of §2; compare per-bar band RMS with `bar_band_rms.txt` and `bars.csv`.
7. Optional VOX textures (§4.3) muted by default.

## 9. Open items / confidence notes
- Whether the odd-bar beat-1 hit is an open hat or a short crash/noise sample (envelope/spectrum only) — M.
- The −16 dB floor under hook even bars: sustained SUB layer vs 808 sustain stage — modelled as SUB (hook 3 has no floor) — M.
- The reversed swell into bar 97 and the bar-24 808 pickup — L.
- Verse-2 grace notes one octave below (C#1, E1 before C#2/E2) — M (seen in the raw mix, absent before hook hits).
- Provenance of the riff timbre (synth line vs processed vocal) is unverified; the recipe copies the measured spectrum either way.
- Lengths of riff notes ±0.5 16th (soft tails).
- Section names: "hook/verse/bridge" follow the vocal version's lyric timing [W LRCLIB]; the instrumental's own boundaries are identical.

## 10. Sources
Measured: scripts and outputs in this folder (`drums.md`, `bass.md`, `harmony.md`, `structure.md`, `sounds.md`, `arrangement.json`, `resolved.json`, `grid.json`, `master_out.txt`, `bar_band_rms.txt`, `rv2_width.txt`, `rf4_riff.txt`, `rp4_voicing_pad2.txt`, `mt5_findings.json`, `mt7_findings.json`, `mt11_v2riff_verdict.md`, `mtR_choir_refute3.txt`, `bars.csv`, `drums_hits.json`, `bass_notes.json`, `demucs4/`).
Web: Universal Music Canada press release https://www.universalmusic.ca/press-releases/bnyx%ef%b8%8f-and-kid-cudi-share-collaboration-everywhere-i-go-remind-me ("humming keys, rubbery bass, snapping percussion, choral vocals"; writers BNYX, Mescudi, Øye, Berge, Brundtland; 30 Jan 2026) · mxdwn https://music.mxdwn.com/2026/02/02/news/kid-cudi-bnyx-team-up-for-collaborative-new-single-everywhere-i-go-remind-me/ ("strong 808s", "clap back beats", "chopped up vocal track") · HipHopCanada https://hiphopcanada.com/bnyx-kid-cudi-everywhere-i-go-single/ (vocoder) · Apple Music single https://music.apple.com/us/album/everywhere-i-go-remind-me-single/1871603512 (3:37, Röyksopp credited) · WhoSampled https://www.whosampled.com/sample/1406730/ (sample from 0:50; page CAPTCHA-walled, snippet only) · Hooktheory single version https://www.hooktheory.com/theorytab/view/royksopp/remind-me-%28single-version%29 (D# minor, 126, i7–v7–VII7–iv7) · cifraclub chart https://www.cifraclub.com/royksopp/remind-me/zpgkkt.html (Dm7 Am7 E♭maj7 B♭; snippet) · Wikipedia Remind Me https://en.wikipedia.org/wiki/Remind_Me_(R%C3%B6yksopp_song) · Wikipedia Bnyx https://en.wikipedia.org/wiki/Bnyx (Ableton) · Equipboard https://equipboard.com/pros/bnyx (Serum) · SoSouthern / ProducerGrind kit listings (808:kick ratio) · LRCLIB https://lrclib.net/api/get/28081080 (lyric timing, used only for section naming) · Reddit threads 1qqwe0d / 1qqwvuj (listener comparisons) · Deezer previews 109713896 (album), 3120990 (radio edit), 3794993062 (BNYX) for pitch/tempo cross-checks.
