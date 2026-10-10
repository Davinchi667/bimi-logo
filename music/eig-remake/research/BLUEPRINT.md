# PRODUCTION BLUEPRINT — "EVERYWHERE I GO [REMIND ME]" (BNYX × Kid Cudi × Röyksopp), instrumental rebuild — revision 2

Written as lead producer from the 10 research reports plus the verification verdicts, then revised against the gap/unsupported-claim audit (every audited item is resolved below; `bp_rev_measure.txt` holds the new measurements). Where reports disagreed, the verified/corrected value is used and the loser is noted. Every number is tagged: **[M]** = measured on `refs/eig_inst.wav` (and stems/previews) by the research scripts in this folder, **[W]** = web source (URL in §10), **[D]** = my design decision where the record cannot be measured, **[ASSUMED]** = a value nothing measures, stated so the build has one. Confidence: H / M / L.

Reference files: `refs/eig_inst.wav` (official instrumental rip, 44.1 kHz), `refs/everywhere.wav` (vocal version = instrumental delayed 18.3 ms, no drift [M,H]), `refs/bp/eig_inst_basic_pitch.mid`.

---

## 0. Corrections to the brief (read first)

| Item | Brief said | Use instead | Evidence |
|---|---|---|---|
| Tempo | 114.84 BPM | **115.000 BPM** (beat 521.74 ms, bar 2086.96 ms, 16th 130.43 ms, 32nd 65.22 ms) | onset autocorrelation at 4/8/16/32-bar lags, per-band phase fits, 88-bar template fit (residual 1 ms); 114.84 drifts 2.7 ms/bar = half a beat by bar 100 [M,H], independently confirmed by three verifiers |
| First downbeat | 0.813 s | **0.278 s** on the drum grid (kick click / clap; `drums.md`, `bass.md`); 0.813 s is bar 1 beat 2. Bar n starts at **0.278 + (n−1)·2.08696 s**. The tonal layers (pad, bed-bass, riff) sit a further **+19 ms** late, i.e. their bar line is at 0.297 s (see §1.1 — this is the only offset, do not add it twice) | claps then fall on 2 & 4, chords change on beat 1, every section boundary lands on bar 8n+1 [M,H] |
| Length | ~104 bars, 3:37 | **104 bars = 13 × 8**, stop on the bar-105 line (217.33 s). `eig_inst.wav` is cut one bar short (hard cut at 215.238 s = bar-104 line); the official releases are 217.0–217.2 s [W: iTunes/Deezer/MusicBrainz durations]. **Bar 104 is therefore not measured**: it is rendered as a copy of bar 100 (Em, same level and filter) [ASSUMED, supported only by the official duration] | [M,H] + [W] |
| Key | E minor (provisional) | Pitch set **{B C# D E F# G A} + C** (no G#/D#/F/A#). Loop **Bm · F#m · C · Em**, label it **B minor i–v–♭II–iv** (sections all start on Bm). Same notes as "E minor v–ii–VI–i" — the label changes nothing in the remake; a bare Krumhansl fit of the four triads prefers E minor (0.79 vs 0.67), so the tonic is genuinely ambiguous [M]. Kick is tuned to E1. | [M,H] on notes; tonic label [M]. Source-loop label is itself disputed: Hooktheory's single-version entry reads i7–v7–**VII7**–iv7 (D#m, C#7 = ♭VII), its album entry "I V6 bVII vi" in F major (E♭ major, final Dm), while the guitar sheets give ♭IImaj7 (E♭maj7) [W]. The measured BNYX bar 3 is **C major** = ♭II of B minor; in the album preview the third chord carries E♭/G/B♭ [M]. Both readings are quoted; the remake uses what is measured on the record (C major). |
| Tuning | — | Two tunings coexist: the "sample"/pad/riff/bed-bass layer is **+14 cents sharp** (A ≈ 443.6 Hz); 808, kick, SUB, PAD-2 are **A440 (±5 c)**. Keep the split: the 0.81 % beating (2–5 Hz in 250–600 Hz) is part of the sound. | [M,H]: every pad partial +13…+16 c; 808 B0 30.85 Hz = −1 c |
| Master | RMS −10.7, crest 10.7 | integrated **−10.3 LUFS**, sample peak 0.00 dBFS hard-clipped (~20 000 full-scale samples, runs to 20–50), true peak +0.46 dBTP, RMS −10.5 dBFS, 57.0 % of energy < 60 Hz, 68.8 % < 120 Hz | [M,H] `master_out.txt` |

---

## 1. Tempo, key, chord loop, bass line

### 1.1 Grid
- 115.000 BPM, 4/4, straight 16ths, **zero swing** (hats +0.8 ms mean, sd 3.8; 'e/a' 16ths +1.8 ms; clap +1.9 ms; kick click +0.1 ms; folding all HF onsets on the beat shows energy only at 0/¼/½/¾) [M,H].
- 104 bars. Harmonic rhythm: one chord per bar, change on beat 1. 4-bar loop × 26. Every section starts on the Bm bar (bar 8n+1 ≡ loop position 1).
- **Two time origins, one offset.** Drum grid: bar n at 0.278 + (n−1)·2.08696 s (kick clicks +0.1 ms, claps +1.9 ms). Tonal grid: chroma-flux (chord-change) peaks sit a median **+19 ms** (IQR 10–29) after those bar lines [M,H], so the pad/bed-bass/riff bar line is at **0.297 s** in the file. In the DAW: quantise drums and 808 to the grid and delay the SAMPLE-PAD, BED-BASS/BED-SUB and LEAD-RIFF tracks by **+19 ms**. (Revision note: the earlier text added +20 ms on top of a 0.29 s grid, double-counting ~12 ms; the 0.29 s figure was a tonal-grid reading.)

### 1.2 Chord loop and voicings (MIDI numbers)

| Loop pos | Chord | 808 root (drops) | SAMPLE-PAD standing stack (+14 c), level re loudest partial, bars 9–23 median | Close-triad core | PAD-2 (A440, bars 57–104; upper voices also 35–40, see §3.7) |
|---|---|---|---|---|---|
| 1 | **Bm** | B0 = 23 (30.87 Hz) | B2 47 (−4), B3 59 (0), D4 62 (−2…−3), F#4 66 (−1…−3), B4 71 (−2…−10), D5 74 (−4…−25, see 1.2b), F#5 78 (−10…−16); colour A5 81 (−24, 7th) | 59 62 66 | 47 · 59 62 66 · 71 74 78 · 81 (7th) 85 (9th) |
| 2 | **F#m** | F#1 = 30 (46.25 Hz) | F#2 42 (−2), F#3 54 (−5…−13), A3 57 (−2…−4), C#4 61 (−1…−4), F#4 66 (0), A4 69 (−4…−15, see 1.2b), C#5 73 (−3…−8); colour E5 76 (−14…−17, 7th) | 57 61 66 | 42 · 54 57 61 · 66 69 73 · 76 (7th) |
| 3 | **C** | C1 = 24 (32.70 Hz) | C3 48 (−3…−7), G3 55 (−1…−3), C4 60 (0), E4 64 (−2…−3), G4 67 (0…−14, see 1.2b), C5 72 (−2…−7); colour D5 74 (−11…−15, 9th), E5 76 (−6…−12) | 55 60 64 | 48 · 60 64 67 · 72 76 79 · 71 (7th) 74 (9th) |
| 4 | **Em** | E1 = 28 (41.20 Hz) | E2 40 (−4), E3 52 (−4…−14), G3 55 (−1…−3), B3 59 (−2…−3), E4 64 (0), G4 67 (−5 or absent, see 1.2b), B4 71 (0 or −16, see 1.2b), E5 76 (−8…−16); colour D5 74 (−11…−14, 7th), F#5 78 (−14…−19, 9th) | 55 59 64 | 40 · 52 55 59 · 64 67 71 · 74 (7th) 78 (9th) |

- Inner voice of the pad descends chromatically **D4 → C#4 → C4 → B3** (62 61 60 59) — the ‑3 st transposition of the Röyksopp F–E–E♭–D line. Top voice F#4 F#4 E4 E4. [M,H]
- **7ths and 9ths, resolved.** In the 80–500 Hz register (octaves 2–4) the +14 c pad is a **bare triad**: 7th/9th ≥ 38 dB down (`mt7c_voicing.txt`). In **octave 5** it carries colour tones at −11…−17 dB: D5 over C (9th), D5 + F#5 over Em (7th, 9th), E5 over F#m (7th), A5 over Bm (7th, only −24) (`rp4_voicing_pad2.txt` section B, bars 1–24). The chroma readings "Bm(add9) / Cadd9 / Em9" and the Em9 template fit (0.78 > Em7 0.73) come from those octave-5 tones **plus the 808/808-HARM harmonic series**: C#4 = 9·B0 (277.8 Hz) and 6·F#1 (277.5), D4 = 9·C1 (294.3), F#4 = 9·E1 (370.8) — all three 9ths are exactly H9/H6 of the bar's root, at 0 c (`refute_808web/harm_test.txt`). So: program the pad as bare triads in oct 2–4 plus the octave-5 colour tones at the listed levels; do not add 9ths in oct 3–4 before bar 57 (where PAD-2 supplies real 7ths/9ths, §3.7) [M,H].
- The pad is **legato, not re-triggered**: partial envelopes flat within 2–3 dB across a bar, max per-beat dip 0.7 dB; chord changes are hard legato cuts (< 20 ms) [M,H]. (One report said "re-triggered every beat"; refuted — the per-16th articulation basic-pitch saw is the 16th-rate vibrato.)
- Source: Röyksopp "Remind Me" (Melody A.M. album version, ≈122.5 BPM, Dm7 | Am7 | E♭maj7 | B♭(/G) per cifraclub chart + measured Deezer preview) pitched **−3 st** (Dm → Bm; BNYX's bed bass B2/F#2/C3/E2 = the album's D3/A2/E♭3/G2 note for note) and time-stretched independently to 115 (ratio 0.939; not a resample, which would give 103 BPM) [M,H][W]. BNYX's bed is nevertheless a **re-voiced** bare-triad pad (7ths/9ths ≥ 38 dB down in oct 2–4 vs 2–8 dB down on the record) with a tempo-synced LFO the record does not have → build it as a synth, do not look for a loop [M,H].

#### 1.2b SAMPLE-PAD upper-octave voicing, bar by bar (bars 1–24) [M,H, `rp5_topvoice_retrig.txt` section A, levels in dB re the bar's loudest partial]
The octave-3/4 triad and the octave-2 root are identical in every bar. Only the octave-4/5 voices change, and they change per bar, not per section:

| Loop pos | Voice | 1–4 | 5–8 | 9–12 | 13–16 | 17–20 | 21–24 | Rule |
|---|---|---|---|---|---|---|---|---|
| Bm | B4 | −2 | −7 | −1 | −0 | −2 | −10 | always on, −1…−10 |
| Bm | D5 | −10 | −14 | −20 | −23 | −4 | −3 | weak in 1–16 (−10…−23), full (−3…−4) in 17–24 |
| Bm | F#5 | −10 | −18 | −12 | −10 | −14 | −14 | on, −10…−18 |
| F#m | A4 | −1 | −2 | −5 | −6 | −15 | −14 | full in 1–8, −5 in 9–16, **off (−15) in 17–24** |
| F#m | C#5 | −4 | −4 | −3 | −8 | −4 | −6 | always on |
| C | C5 | −3 | −3 | −2 | −7 | −5 | −7 | always on |
| C | E5 | −26 | −9 | −8 | −10 | −13 | −7 | **off in bar 3 only** (−26); on (−7…−13) from bar 7 |
| C | G4 | −2 | −3 | −12 | +0 | −2 | −2 | on, except bar 11 (−12) |
| Em | B4 | −12 | +0 | −1 | −16 | −0 | −3 | **alternates by phrase: on in bars 8, 12, 20, 24; off in bars 4, 16** |
| Em | G4 | −2 | −10 | −25 | −5 | −22 | −11 | **inverse of B4: on in bars 4, 16; off in 12, 20; −10 in 8, 24** |
| Em | E5 | −22 | −4 | −12 | −8 | −16 | −10 | **full only in bar 8** (−4); −8…−22 elsewhere |
| Em | E3 (root oct 3) | −9 | −16 | −5 | −14 | −4 | −10 | alternates −4…−16 |

Bars 25–40: see §3.5 duck lane. Bars 41–56 and 57–104: the stack is the 9–24 median (column 4 of the §1.2 table) [M,M: `rp4` section D shows the same per-chord partial set at full level]. Program these as per-bar velocity/level overrides on the four octave-4/5 voice tracks.

### 1.3 Bass / 808 line — bar by bar

Pitches (MIDI / Hz): B0 23 / 30.87 · C1 24 / 32.70 · E1 28 / 41.20 · F#1 30 / 46.25 · A1 33 / 55.0 · B1 35 / 61.74 · C#2 37 / 69.30 · D2 38 / 73.42 · E2 40 / 82.41 · C#1 25 / 34.65 · A0 21 / 27.5.
Slot = 16th position **0–15, zero-indexed everywhere in this document** (0 = beat 1, 4 = beat 2, 8 = beat 3, 12 = beat 4; "e/&/a" = +1/+2/+3, so 1e = slot 1, 2e = slot 5, 3& = slot 10, 4e = slot 13). Lengths in 16ths. Levels are peak dBFS of the 20–120 Hz band on the bass stem; loud 808 hit = −4 dBFS = the **0 dB reference for every level in this document**.
**No glides anywhere** (cycle-by-cycle tracking: every pitch change completes within one cycle, 161/161 changes < 45 ms; the +33 c "bends" basic-pitch wrote are the kick's E1 tail under quiet beat-1 notes) [M,H]. Downward moves in verse 2 are 30–45 ms steps — program them as separate notes, no portamento.

**Note-off / voice rules for the 808 (monophonic, one voice) [M,H on the measured lengths; D on the rule]:**
1. A new 808 note cuts the previous one within one cycle (release 10 ms). This covers every overlap in the tables: the H-odd slot-13 note runs into the next bar and is cut by that bar's slot-0/1 quiet root; the F#1 pickup (len 3) is cut by the next bar's first note; in hook 3 the pickup is held until the B0 on slot 4.
2. On H-even bars the quiet root sits at **slot 1, not 0** — measured at 1e on 6 of 8 even bars — because the kick owns slot 0 and the 808 and kick never coincide (0 of 47 within 40 ms). Keep it at slot 1.
3. The slot-7 note on H-even bars uses the **808-HOLD** envelope (§3.2): it decays to −12 dB re peak over 300 ms and holds there until its note-off at **slot 16 (the bar line)**, or at slot 13 on E bars where the F#1 pickup cuts it. This hold *is* the measured −16 dBFS "floor" (`bass.md`: settles at −16 ± 2 dBFS from ~300 ms to the bar end). The separate SUB layer exists only in bars 17–23 (§3.3).

Four low layers plus one harmonic send exist [M,H]:

| Layer | Bars | Notes | Tuning | Level re 808 | Character |
|---|---|---|---|---|---|
| BED-BASS (root of the pad, octave 2) | 1–104 (ducked with the pad in 25–40) | B2 F#2 C3 E2 (47 42 48 40) one per bar, whole bar | +14 c | −21 dB (−25 dBFS sine amplitude; the 80–160 Hz band sits −7 dB under the pad's total in drum-free bars) [M,M: two readings, −17 dBFS in `sounds.md` and −25…−29 dBFS in the section-map verification; the pad-relative figure is the one to match] | sine + octave at −8 dB, no vibrato, mono-ish |
| BED-SUB (octave-down copy of BED-BASS) | 9–16 at −26 dB; 17–24 at **−30 dB [ASSUMED]** (it is masked by SUB there and cannot be separated) | B1 F#1 C2 E1 (35 30 36 28), whole bar | +14…+16 c | −26 / −30 dB | pure sine, mono |
| SUB (sustained sub synth) | **17–23 only** | B1 F#1 C2 E1 (35 30 36 28), gated to the bar, no decay, attack 20 ms | A440 ±1 c | −17 dB (−21 dBFS amplitude; `refute_808web/layer_test.txt` reads B1/C2 at −22 dBFS in bars 21/23) | clean sine, H2 −11 dB, H3 −28 dB |
| 808 (rhythmic) | 25–96 | roots B0 F#1 C1 E1 + F#1 pickups; melodic riff in 41–56 | A440 ±5 c | 0 dB (loud), −8 dB (quiet beat-1 notes) | see §3.2 |
| 808-HARM (parallel harmonic send on the 808) | 25–96, every 808 note | the root's H3–H10 at 0 c | A440 | H3 −18, H5 −21, H6 −18, H7 −27, H8 −16, H9 −20…−29, H10 −20 dB re the 808 fundamental at the hit | see §3.2b — this is what produces the measured 0 c series on **odd (B/C) bars** as well as even bars (154/185/216/247/278/309 Hz on B bars, 131/164/196/262/327/392/523 Hz on C bars at −27…−42 dBFS) |

**Cell patterns** (used in the table below; q/X/H/P are 808 notes, K kick):

```
slot:        0  1  2  3 | 4  5  6  7 | 8  9 10 11 |12 13 14 15
H-odd  808:  q  .  .  . | X  .  .  X | .  .  X  . | .  X  .  .     X = loud root, len 3, each cut by the next; slot-13 note runs to the next bar's slot 0/1 note
       kick: K  .  .  . | .  .  K  . | .  .  .  . | .  .  .  .     q = quiet root −8 dB re X, len 4
H-even 808:  .  q  .  . | X  .  .  H | .  .  .  . | .  P  .  .     H = loud root with the 808-HOLD envelope, note-off at slot 16 (slot 13 on E bars)
       kick: K  .  .  . | .  .  K  . | .  .  K  . | .  K  .  .     P = F#1 pickup (E bars only), −6 dB, len 3 (cut by the next bar's first note)
H2-all 808:  q  .  .  . | X  .  .  X | .  .  X  . | .  X  .  .     (E bars: slot 13 = F#1 instead of E1)
       kick: K  .  .  . | .  .  K  . | .  .  .  . | .  .  .  .
H3-B   808:  (previous F#1 pickup held) | q@4 B0, len 12 (decays, no hold)      kick 0, 4
H3-F#  808:  q@0 F#1 len 16 (decays) — bars 94: q@0 len 1 + q@4 len 12          kick 0, 4
H3-C   808:  q@0 C1 len 16 — bar 95: q@5 len 11                                 kick 0, 4
H3-E   808:  q  .  .  . | q  .  .  . | .  .  X  . | .  P  .  .     q = E1 −9 dB, X = E1 loud, P = F#1 loud (−1 dB); bar 96: q@1, q@5, X@10, P@13
       kick: K  .  .  . | K  .  .  . | .  .  .  . | .  .  .  .
```
Hook-3 quiet roots: −12…−13 dBFS on the bass stem (= −8…−9 dB re ref; one verifier reads −8…−10 dBFS on the mix), decay −12…−17 dB/s, gone to −37 dBFS by beat 4 [M,H].

Verse-2 riff (4-bar phrase, played identically in 41–44, 45–48, 49–52, 53–56; peaks −5 dB re the hook hits; grace notes g at −11 dB, length 1) [M,H on pitches/slots after verification; the first note is B1, not B0]:

```
V2-1 (Bm):  1:B1(2)  3:g C#1(1)  4:C#2(3)  7:D2(2)  9:g C#1(1)  10:C#2(2)  12:B0(2, −24 dB re ref = faint; one verifier reads B1 here)  14:B1(2 → into next bar)
V2-2 (F#m): 1:A1(3)  4:F#1(3)  7:A1(3)  10:A1 weak −9 dB (3)  14:E2(1)  15:E1(1)
V2-3 (C):   1:A1(2)  3:g E1(1)  4:E2(3)  7:A1(2)  9:g E1(1)  10:E2(2)  12:A0 quiet −11 dB(1)  14:A1(2)
V2-4 (Em):  1:E2(2)  3:g E1(1)  [rest 4–6]  7:E2(2)  9:g E1(1)  10:D2(2)  12:E1(2)  14:A1(2 pickup)
kick V2: odd bars 0, 6 ; even bars 0, 6, 10, 13
```
Verse-2 patch details (resolving the open points): slot-4 note of V2-2 is **F#1** (46 Hz) with its octave at −6 dB (one verifier reads it as F#2 because the octave dominates in the mix; the bass stem f0 is 46 Hz) [M,M]. Grace notes **retrigger the main envelope** (they are separate note-ons at −11 dB; the following main note re-attacks within 1–3 cycles) [M,H]. Timbre: same patch, output −5 dB, **plus a fixed LPF 12 dB/oct at 160 Hz** so that H3 reads 8–12 dB weaker than in the hooks (−26…−32 dB re H1) [M,M]. (The riff never plays C under the C chord → that bar sounds as C6/Am7. The pad stays C.)
**V2-SIDE (octave-up double)** [M,M]: the **main notes only** (not the grace notes, not the A0) of V2-1…V2-4 one octave up — B2 C#3 D3 C#3 B1 B2 | A2 F#2 A2 A2 E3 E2 | A2 E3 A2 E3 A2 | E3 E3 D3 E2 A2 — same slots and lengths as the main notes [grace-note exclusion ASSUMED]; two saw voices detuned **±25 c** (side peaks C#3 −25/+25 c, E3 −28/+1 c in `i_wide.txt`), HPF 90 Hz, LPF 500 Hz, **side channel only** (mid −∞; measured side/mid 90–180 Hz −10.5 dB); level **−12 dB re the riff (−21 dBFS) in 41–48, −6 dB re the riff (−15 dBFS) from bar 49** (side/mid 2–6 k −26 → −19.5 dB). Glide: **none** by default (bass stem: hard steps) — one verifier reads continuous pitch motion in this side layer (talkbox-like); if you want that reading, add a 30–45 ms downward-only glide on the side voices only [D, contested].

**Full bar table** (chord loop position: 1 = Bm, 2 = F#m, 3 = C, 4 = Em; "kick" slots are 16ths):

| Bars | Loop pos | Low layers playing | 808 pattern | Kick |
|---|---|---|---|---|
| 1, 3, 5, 7 | 1, 3 | BED-BASS only | none | 0 (bar 1 included: the downbeat event is the kick, §3.1) |
| 2, 4, 6, 8 | 2, 4 | BED-BASS only | none | none |
| 9–16 | 1-2-3-4 ×2 | BED-BASS + BED-SUB | none | 0, 6 |
| 17, 19, 21, 23 | 1, 3 | BED-BASS + BED-SUB (faint) + SUB (B1 / C2 whole bar) | none (SUB only) | 0, 6 |
| 18, 20, 22 | 2, 4, 2 | BED-BASS + BED-SUB (faint) + SUB (F#1 / E1 / F#1) | none | 0, 6, 10, 13 (bar 20: 0, 6, 10, **13** — `drums.md` grid; the earlier "12" was a typo) |
| 24 | 4 | BED-BASS only (SUB off) | none; optional F#1 pickup at slot 15, −23 dB [M,L] | none |
| 25, 27, 29, 31, 33, 35, 37, 39 | 1, 3 | 808 (B0 / C1) + 808-HARM + BED-BASS ducked with the pad (§3.5 lane) | **H-odd** | 0, 6 |
| 26, 30, 34, 38 | 2 | 808 F#1 (+HOLD) + 808-HARM | **H-even** (no pickup) | 0, 6, 10, 13 |
| 28, 32, 36 | 4 | 808 E1 (+HOLD) + 808-HARM | **H-even** + P = F#1 @13 (bars 28/36 read @14) | 0, 6, 10, 13 + **soft E1 kick k@4** under the clap on **28, 32, 36** (`drums.md` 1.1 lists 28/32/36; §5 now agrees) |
| 40 | 4 (fill) | 808 E1 + 808-HARM | **q@1, q@5, X@7, X@10, F#1@13** (0-indexed: 1e, 2e, 2a, 3&, 4e — `bass_bars.txt` bar 40). Not "on every beat": the beats carry the kick. The "roll on nearly every 16th" readings are kick + 808 summed (sub onsets at 0,1,4,5,7,8,10,12,13) | 0, 4, 8, 12 (four-on-the-floor), no clap |
| 41, 45, 49, 53 | 1 | 808 riff + V2-SIDE; BED-BASS full | **V2-1** | 0, 6 (51: 0 only) |
| 42, 46, 50, 54 | 2 | " | **V2-2** | 0, 6, 10, 13 |
| 43, 47, 51, 55 | 3 | " | **V2-3** | 0, 6 (55: 6 only) |
| 44, 48, 52 | 4 | " | **V2-4** | 0, 6, 10, 13 (44/52 drop the 6; 48: 0, 6, 10) |
| 56 | 4 (pre-drop) | 808 riff V2-4 continues at its normal level (bass stem −18.4 dB vs −18…−20 in verse 2: **no 808 gain automation**), B0 pickup at slot 14–15 (+35 c, 0.78 s); the "sub pull" is the **kick being removed** (drum stem −40 dB in the bar) | V2-4 | **none** |
| 57–71 | all | 808 (+HOLD not used: every bar is retriggered) + 808-HARM; BED-BASS full | **H2-all** (E bars: F#1 @13) | 0, 6 (59: 0 only; soft k@10 on 64, 66, 68) |
| 72 | 4 | 808 alone + 808-HARM (drums out) | **q@1, X@4, X@7, X@10, F#1@13** (1e, 2, 2a, 3&, 4e; loudest bass bar, −12.3 dB stem RMS) | **soft k@4 only** (the "kick roll XXXX…" of the structure report was this 808 roll heard in the sub band; `drums.md` bar 72: one soft beat-2 hit) |
| 73, 75, 77, 79, 81, 83, 85, 87 | 1, 3 | 808 + 808-HARM + BED-BASS | **H-odd** | 0, 6 (73, 83: 0 only) |
| 74, 78, 82, 86 | 2 | 808 (+HOLD) + 808-HARM | **H-even** | 0, 6, 10, 13 |
| 76, 80, 84 | 4 | " | **H-even** + F#1 @13 | 0, 6, 10, 13 (+ soft k@4 on 80, 84) |
| 88 | 4 | 808 alone + 808-HARM | as bar 72 (q@1 X@4 X@7 X@10 F#1@13) | soft k@0, k@10, k@13 |
| 89, 93 | 1 | 808 + 808-HARM | **H3-B**: previous F#1 held through slots 0–3, B0 q@4 (len 12; bar 93: F#1 re-hit q@1 then B0 q@4) | 0, 4 |
| 90, 94 | 2 | " | **H3-F#** (F#1 q@0 len 16; 94: q@0 short + q@4) | 0, 4 (94: 4 only) |
| 91, 95 | 3 | " | **H3-C** (C1 q@0; 95: C1 q@5) | 0, 4 |
| 92, 96 | 4 | " | **H3-E** (E1 q@0, q@4, X@10, F#1 X@13; 96: q@1, q@5, X@10, X@13) | 0, 4 (+ soft k@10 on 92) |
| 97–104 | all | BED-BASS only (+14 c), low-passed with the pad | none | none |

Hook-3 kick is on **beats 1 and 2 = slots 0 and 4** (`drums.md` "F (89–96): 1, 2 every bar", `bass.md`, three verifiers). Slot 8 is beat 3; the earlier "0 and 8 (doubles the clap)" was wrong.

---

## 2. Arrangement — bar by bar

Timestamps are file positions on the drum grid (bar n = 0.278 + (n−1)·2.08696 s); for a render starting at 0.0 s subtract 0.278 s. Loudness = K-weighted bar-mean LUFS [M,H]. Rule applied: something audibly changes at every 8-bar line, and every drop is made of (sub re-entry + width collapse + new layer), never "drums come in" alone.

| # | Bars | Start (file) | Len | Name | Layers playing | What changes at the boundary (and inside) | LUFS |
|---|---|---|---|---|---|---|---|
| 1 | 1–8 | 0:00.28 | 8 | Intro | SAMPLE-PAD (with the 1.2b upper voices), BED-BASS, clap 2&4, HAT-A (2-bar loop: open-type on odd downbeats, closed hat on even downbeats), knock, kick on beat 1 of odd bars only | Track opens ON the downbeat with the **kick** (the 0.277 s "full-band stab" is the kick sample starting from digital silence: its 40 ms band profile is identical to the isolated bar-3 kick, `bp_rev_measure.txt` §1), no fade-in, no HPF opening. Even bars have no sub at all (−23 dB). The 7.3–8.1 kHz "tonal ping on beats 3–4 of even bars" of the arrangement report is, on the corrected grid, the **odd-bar beat-1 open-type hit** (peaks 6.6/7.3/7.75/8.5 kHz, 300 ms plateau; §3.10) — no separate ping exists. Cudi hum lives here in the vocal version (see §4.3). | −13.8 (odd −13.3 / even −14.5) |
| 2 | 9–16 | 0:16.97 | 8 | Verse 1a | + kick 1 & 2& every bar, + BED-SUB (octave-down bed bass, −26 dB) | Additive, no fill before it: sub band +8.8 dB and now present in every bar; hat/clap unchanged. **No 32nd hat layer yet** (odd-32nd slots −70…−90 dBFS, `bp_rev_measure.txt` §2). No fade of any hat across 9–22: even-bar beat-1 hat −21 dBFS and odd-bar open-type −19/−25 dBFS are constant in every bar 1–23 (§9 of the same file) — the arrangement report's "intro tick fading −25 → −36 dB" was an old-grid reading and is dropped. | −12.6 |
| 3 | 17–24 | 0:33.67 | 8 | Verse 1b / build | + SUB (A440 whole-bar roots, −17 dB), + **HAT-32** ghost layer (§3.10b: 16ths 6/8/9/13/14 at −35…−40 dBFS and 32nds between them at −42…−49, width −15 dB), even-bar kick figure 1 2& 3& 4e, width > 2 kHz −20 → −17 dB | Bar 17: sustained sub enters (first A440 element against the +14 c bed), kick density 2 → 4 on even bars, odd/even loudness alternation 1–1.4 dB. The verification's "8–16 kHz hits on 3, 3e, 4e, 4& (−50 dB)" and "1.5–5 kHz percussion on 1, 1e, 2, 3, 3a, 4e (−33 dB)" are HAT-32 (whose sample has 1–3 kHz content, §3.10b) plus the even-bar kick clicks — no further layer. **Bar 24 = drop-out**: kick, clap, hats, SUB all out; pad continues; HAT-32 keeps running as near-continuous 32nds at −37…−43 dBFS (all slots except 2e–2a and 3&–3a); wide reversed tonal swell (§3.13: side 500–1.5 kHz −41 → −18 dBFS = +23 dB over the bar, L/R corr 0.86 → 0.01), no brightening; optional −23 dB F#1 pickup on slot 15. | −11.8; bar 24 −14.6 |
| 4 | 25–32 | 0:50.36 | 8 | Drop 1 / Hook 1a | 808 (B0!) + 808-HARM, kick H-odd/H-even, clap, HAT-A (accents only), HAT-32, knock (loudest here), **LEAD RIFF** exposed, SAMPLE-PAD ducked −10…−19 dB per bar (§3.5 lane), 808-HOLD floor on even bars | **THE drop**: sub +16 dB bar-to-bar (+40 dB from last 16th of 24), RMS +7.4 dB, width collapses −15 dB at the downbeat (swell cut dead), B and C roots fall an octave (B1→B0, C2→C1), 808 becomes the dotted-8th pulse, pad thins to let the riff through, the riff starts (WhoSampled's "sample at 0:50" [W]). The duck is a **gain change, not a re-voicing**: every pad voice drops (B3 −10…−15, A3 −18…−20, C4 −13…−19, G3 −5…−6 re verse 1), and the voices that read "full" (D4/F#4 in alternate Bm bars, E4 in C bars) are the riff's own notes on the same pitches (`bp_rev_measure.txt` §8). The chroma "F#5 (no third)" reading is the ducked A3 (−19 dB) sitting under the 808's F#1 harmonics. | −10.2 (odd −11.0 / even −9.5) |
| 5 | 33–40 | 1:07.06 | 8 | Hook 1b | as 4 + HAT-A2 adds 2& 2a 3e at full level (second closed-hat sample, +13 ms), **WIDE bus ON in 35–36 and 39–40** (§3.8: side/mid 500–4 k −12.5 → −6 in 35/36, −4.3 in 39, −2 in 40); riff thinned from bar 33 (§4.1) | Hats double (the brief's "hats double at 1:07.7"); first appearance of the wide upper-structure layer: side peaks D5/E5/B5/G5/C5 in ±15 c triplets around **0 c** (`bp_rev_measure.txt` §5) = PAD-2's octave-5 voices through the WIDE chorus, two sections before PAD-2's lower voices enter. **Bar 40 = turnaround**: clap out, kick four-on-the-floor 0 4 8 12, 808 q@1 q@5 X@7 X@10 F#1@13, HAT-A on every 8th (slots 0 2 4 … 14 at −20 dBFS) with HAT-32 ghosts at 5/7/9/13, WIDE bus at its 35–39 level (side/mid 500–4 k −2 dB, 2–6 k −0.8 dB: the 2–6 kHz width comes from the WIDE chorus plus the removal of the mono accents, not from a swell — bar 40 has **no swell**), no sweep, no dip. | −10.2; bar 40 −9.5 |
| 6 | 41–48 | 1:23.75 | 8 | Verse 2a | SAMPLE-PAD full, 808 **melodic riff** (−5 dB) + V2-SIDE, kick, clap, HAT-A 16th runs (1& 1a 2 2e 2& / 3& 3a 4 4e 4&, i.e. slots 2 3 4 5 6 / 10 11 12 13 14), knock, no beat-1 hat on even bars, **no HAT-32**, WIDE bus OFF | Wide layer leaves (narrowest point: side/mid > 2 k −20…−22 dB), 808 goes up an octave and melodic, hats become two 5-note runs per half-bar, 120–250 Hz +2.8 dB, centroid up (2500–2650 Hz, hats). Bar 48: clap fill 4 4e 4& (slots 12 13 14, −8 dBFS each), kick 0 6 10. | −10.4 |
| 7 | 49–56 | 1:40.44 | 8 | Verse 2b | as 6; V2-SIDE +6 dB (side/mid 2–6 k −26 → −19.5 dB) | Only the side channel changes (riff double louder); keep it, it is the record's own 8-bar move. **Bar 56 = pre-drop**: kick out (this is the "sub pull": the kick band vanishes while the 808 riff plays on at its normal level), **LP-CLAP on beat 2** (§3.9b: the clap sample through a 400 Hz low-pass, −6 dBFS peak in 120–400 Hz, no sub, no HF), clap build c@10 X@12 9@13 X@14 X@15 (§5), bright **filter-opening riser** (§3.14), reversed swell again (side 500–1.5 k −43 → −19 dBFS, L/R corr 0.7); no loudness dip. | −10.4 |
| 8 | 57–64 | 1:57.14 | 8 | Drop 2 / Hook 2a | 808 H2-all (full pulse every bar) + 808-HARM, kick 0 6 only, clap 2&4 **every bar** (bar 57: beat-4 clap only), HAT-A accents + even-bar beat-1 hat, HAT-B 2& 2a 3e (slots 6 7 9) at −24 dBFS + under-clap slot 4 at −24, HAT-32 (width −10), SAMPLE-PAD full (+3 dB vs hook 1), **PAD-2 enters in full** (lower voices A440, no vibrato, −8 dB under the pad), LEAD thinned, WIDE bus every 2 bars (ON 57, 59–60, 63–64), knock gone | Sub +9.4 dB, RMS +3.4 dB, width −7 dB at the downbeat; 250–500 Hz and 1–2 kHz +2.5 dB (two pads now beating at 0.81 %); the 808 takes over the even-bar pulse from the kick (kick thins to 0, 6 everywhere). | −9.3 |
| 9 | 65–72 | 2:13.84 | 8 | Hook 2b | as 8 + soft k@10 on 64/66/68, riff variant a with the A3→A4 leap (65), WIDE bus ON 67–68, 71 | Lead riff second-pass variants; soft kick ghost; otherwise identical (the record's quietest boundary — if you want more, bring the WIDE bus ON for all of 65–72 [D]). **Bar 72 = transition**: hats and clap out (HAT-32 stays, slots 0/8/16/24 (32nds) at −27…−30), **one soft kick k@4**, 808 roll q@1 X@4 X@7 X@10 F#1@13 (loudest bass bar), swell reused (side 500–1.5 k −27 → −19 dBFS: same absolute swell, higher floor), WIDE bus ON (side/mid 2–6 k ≈ 0 dB because the mono accents are gone). | −9.3; bar 72 −9.0 |
| 10 | 73–80 | 2:30.53 | 8 | Bridge / PEAK a | everything of 8 + **LEAD RIFF +7 dB with octave-up double** and **CHORAL = PAD-2 octave-5/6 voices on the WIDE bus with the §3.6b lane**, HAT-B densest (slots 5 6 7 8 9 10½ 12 13 14 15 = the measured 2e 2& 2a 3 3e 4 4e 4& 4a set; the "PERC-2" of the sound report is this same dark-hat sample), kick H-odd/H-even figure back, 808 H-odd/H-even, WIDE bus ON throughout, PAD-2 +2 dB | Loudest section (−8.0). Entry is additive (RMS +0.8 dB): hats back (+10 dB > 6 k), all mids 250 Hz–4 kHz +2 dB, side/mid 500–4 k −4…−5 dB continuously, centroid +29 %. The "G-line" low-mid chops of `drums.md` (2e/3/3e/3a/4e/4a, loudest 4a at −9 dBFS in 150–1.5 kHz, > 9 kHz −32) are the **riff's own notes** (their peaks are G3/C4/E4/F#4/G4/E5 at +4…+26 c, `bp_rev_measure.txt` §11) — not a percussion layer and not PERC-2 (−27 dBFS, centroid 6.2 kHz). In the vocal version Cudi's "oohs" sit here (one phrase per loop) — see §4.3. | −8.0 |
| 11 | 81–88 | 2:47.22 | 8 | PEAK b | as 10; odd-bar HAT-A slot 2 dropped (keeps 3), **full clap on beat 3 (slot 8) of bars 77 and 81** (`drums.md` S-line, clap fingerprint ≥ −12 dBFS; level −3 dB re the backbeat clap [M,M]; there are no ghost claps anywhere), riff var-b in 85 drops C#4, CHORAL lane rises into 85 beat 3 and 87–88 (§3.6b) | Bar 84 is the loudest bar (−7.5). **Bar 88 = transition** (hats/clap out, HAT-32 stays, 808 roll as 72, soft kicks k@0 k@10 k@13; **no swell** — side 500–1.5 k flat −29…−21). | −8.0; bar 88 −7.9 |
| 12 | 89–96 | 3:03.91 | 8 | Hook 3 / post-drop | 808 half-bar only (H3) + 808-HARM, kick on beats 1 & 2 (slots 0, 4), clap 2&4, HAT-A/HAT-B as 73–80 (not the 81–88 variant: slot 2 is back on odd bars), HAT-32, pads, CHORAL sustained across whole bars (lane +3…+7 dB), riff thinned (var-b shape, long E4 over C) | 808 and kick vanish from the second half of every bar (sub decays to −33 dB re ref by beat 4), except Em bars 92 and 96 which restore E1@10 + F#1@13; the wide pad is exposed in the empty half-bars (side/mid −13 → −5.6 dB inside bar 89); 120–250 Hz −4.6 dB. **Last clap = bar 96 slot 12** (clap band −9.3 dBFS there, `rf3_hats.txt`; one verifier reads it absent — the fingerprint test says present); last hat bar 96 slot 15. Optional reversed swell into 97 (side 500–1.5 k −28 → −18, corr with bar 24 0.66) [M,L]. | −9.5 (92/96 −8.8) |
| 13 | 97–104 | 3:20.61 | 8 | Outro | SAMPLE-PAD + BED-BASS + PAD-2 (−5 dB under the pad, same low-pass; its upper voices on the WIDE bus: side/mid 400–2 k −4…−10 dB); nothing else | **Hard cut** on the bar line: 808, kick, hats, clap all off in one step (sub −43 dB, > 6 k −30 dB, RMS −7.8 dB); the master low-pass (§3.5c) **sweeps closed across bar 97** (fc 3.5 kHz → 2.0 kHz; 6 kHz −15 → −32 dB re bar 96 by the bar end, which is also why the HAT-32/PERC band decays −39 → −63 dBFS over bar 97 — no extra layer), then **static 98–102** (18 dB/oct at 2.0 kHz: 1.6 k −3, 2–3.2 k −8, 4 k −16.5, 6.3–8 k −28, 12.7 k −44 dB re unfiltered), **bar 103: second step** (adds 12 dB/oct at 1.0 kHz: a further −11 dB at 1–2 k, −20 at 2–4 k, −22 at 4–8 k; centroid 440 Hz). The "60–120 Hz −12 dB at bar 103" needs **no mechanism**: bar 103 is a C bar whose bass is C3 (132 Hz); every C/Bm outro bar reads −48…−65 dBFS in 60–120 Hz while F#m/Em bars read −25…−28 (`bp_rev_measure.txt` §6). Bar 104 = Em, a copy of bar 100 [ASSUMED]. **Hard digital cut (< 2 ms, no fade) on the bar-105 line at 3:37.33.** | −15.9 (103: −17.0) |

Transition summary: one-bar events at bars 24, 40, 56, 72, 88 (always loop position 4 = the Em bar). Swell FX in 24, 56, 72 (and optionally 96); none in 40 and 88. No crash cymbals anywhere (the odd-bar open-type hat is the same at section starts as elsewhere, sd 0.3 dB), no gated silence, no sidechain pump, no delays, no vinyl noise, no pad filter sweeps except bar 56 and the outro steps [M,H].

Loudness contour to hit (bar-mean LUFS): 1–8 −13.8 · 9–16 −12.6 · 17–23 −11.8 · 24 −14.6 · 25–39 −10.2 · 40 −9.5 · 41–55 −10.4 · 56 −10.4 · 57–71 −9.3 · 72 −9.0 · 73–87 −8.0 (84: −7.5) · 88 −7.9 · 89–96 −9.5 · 97–103 −15.9. Integrated −10.3 LUFS.

---

## 3. Sound layers — synthesis recipes

Level convention: 0 dB = peak of a loud 808 hit (= −4 dBFS on the bass stem). Width = side-minus-mid in dB (−∞ = mono). **Width mechanism used throughout**: a mono source plus an independent-noise (or chorus) copy on the side channel at ratio r gives side/mid = 20·log10(r): r = 0.18 → −15 dB, 0.32 → −10 dB, 0.45 → −7 dB, 0.56 → −5 dB. Env times in ms. Recipes are Faust/DawDreamer-style; pedalboard for effects. Register in MIDI. Each recipe ends with a **Check** = the measurement a render must reproduce.

### 3.1 KICK — fixed-pitch sub kick tuned E1 [M,H]
- Pitch (zero-crossing on isolated intro kicks, `b_kick2.txt`): 130 Hz @ 3 ms → 97 @ 15 → 63 @ 30 → 44 @ 40 → 42 @ 50–100 → **41 Hz (E1 −20 c)** from 100 ms. Same pitch under every chord. One sample throughout; the bar-1 downbeat is this kick (§2 row 1).
- Amplitude, **breakpoints from the sub-band envelope, re its peak** (peak at +22…+34 ms after the click): 0 dB @ 30 ms → −6 dB @ 94 ms (90–98) → −12 @ 138 (135–141) → −20 @ 178 (173–182) → −30 @ 205 (202–207) → −40 @ 226 (220–233). Two-stage: −6 dB over the first 64 ms after the peak (slow), then −34 dB over the next 88 ms (fast). Use these points directly as a breakpoint envelope; an exponential cannot reproduce the knee.
- Spectrum: body mildly symmetric-saturated (H3 −15 dB, H2 −38 dB, H4 −46); 120–400 Hz thump in the first 15 ms (−4 dB re total); click 1–8 kHz at −11…−14 dBFS gone in 16–35 ms; nothing above 4 kHz after 30 ms.
- Level **+4 dB** (0 dBFS, the loudest element, into the clipper). Mono (side −31 dB).
```
f(t)   = 41*2^(-20/1200) + 90*exp(-t/0.015)                        // Hz; 130 Hz at 3 ms, 41 Hz from ~100 ms
body   = sin(2*pi*∫f) -> tanh(1.3*x)                                // gives H3 ≈ -15 dB
env    = breakpoints (ms, dB): (0,-inf) (3,-6) (30,0) (94,-6) (138,-12) (178,-20) (205,-30) (226,-40) (240,-inf), linear-in-dB segments
thump  = bandpassed noise 120-800 Hz, 10 ms, -12 dB ; click = noise HPF 1 kHz, 5 ms, -12 dB
out    = (body*env + thump + click) -> softclip -> 0 dBFS ; mono
```
Velocity: full hits 0 dBFS (v 127); the "soft" E1 kick k under the clap on beat 2 (bars 28/32/36/80/84) and the drop-out-bar kicks (72, 88) = −6 dB (v 90 on the §5 scale).
**Check**: sub-band −20 dB at 173–182 ms, −40 dB at 220–233 ms; f0 42 ± 1 Hz at 80 ms.

### 3.2 808 — chord-root sub with phase-locked octave [M,H after correction]
- Pitches: B0 30.87 / F#1 46.25 / C1 32.70 / E1 41.20 Hz, A440 within ±5 c (cycle-by-cycle median −1 c). **Not** +14 c.
- Waveform of the hits: sine + **octave at −6 dB (range −3…−10), phase-locked (relative phase −159°)**, the hit's own H3 ≤ −24 dB. Ratio does not change with level → fixed waveform, **not** saturation. The 0 c H3–H10 series measured in the mix is a separate send (§3.2b) and is not produced by distorting the hits.
- Attack: full amplitude within one cycle (13–25 ms), no click (1–8 kHz < −40 dBFS at onsets).
- Decay (**808-HIT** envelope): log-linear **−28 dB/s** for the first 300 ms (−6 dB @ 160 ms, −10 dB @ 290–390 ms), then −12…−17 dB/s; −20 dB only at 0.75–1.0 s. Retriggered every 391 ms (3 16ths) in the hooks, so each note is cut at about −10…−12 dB. Monophonic legato: new note cuts the old within one cycle, no release gap (§1.3 rule 1).
- **808-HOLD** envelope (the slot-7 note of H-even bars only): same attack; decays at −28 dB/s to **−12 dB re peak at 300 ms, then sustains at −12 dB** (= −16 dBFS, the measured floor) until note-off at the bar line (slot 16) or at the slot-13 pickup on E bars; release 20 ms. Hook 3 has no held notes, hence no floor there [M,H on the floor level and its absence in hook 3; D on implementing it as a sustain stage rather than a separate layer — the two are indistinguishable in a mix].
- Levels: loud hits 0 dB (−4 dBFS), quiet beat-1 notes −8 dB, hook-3 roots −8…−9 dB (−12…−13 dBFS stem; a mix reading gives −8…−10 dBFS), verse-2 riff −5 dB (grace notes −11 dB). Mono (side −36 dB, L/R corr 1.000).
```
f0      = midi2hz(note)                                     // A440
osc     = sin(2*pi*f0*t) + 0.5*sin(2*pi*2*f0*t + pi*(-159/180))   // octave -6 dB, locked phase
envHIT  = attack 15 ms ; decay 10^(-28*t/20) for t<0.3 s then 10^(-(8.4 + 14*(t-0.3))/20) ; release 10 ms on retrigger
envHOLD = attack 15 ms ; decay to -12 dB over 0.3 s ; sustain -12 dB ; release 20 ms at note-off (slot 16, or slot 13 on E bars)
post    = HPF 24 Hz (keep the 30.87 Hz fundamental!) ; LPF 6 dB/oct @ 400 Hz
gain    = -4 dBFS peak ; mono ; no glide, no pitch env
```
Verse-2 variant: same patch, output −5 dB, **plus LPF 12 dB/oct at 160 Hz** (H3 8–12 dB weaker: −26…−32 dB re H1); grace notes are separate note-ons at −11 dB that retrigger envHIT; the V2-SIDE double is specified in §1.3.
**Check**: H2 −6 ± 3 dB, H3 ≤ −24 dB on an isolated hit; −10 dB at 290–390 ms; even-bar held note −16 dBFS from 0.3 s to the bar line.

### 3.2b 808-HARM — the root's 0 c harmonic series (parallel send, bars 25–96) [M,H on the series; D on the mechanism]
Measured in the mix on **odd (B/C) bars as well as even bars**: B0 bars carry 154.3 / 185.2 / 216.1 / 247.0 / 277.8 / 308.6 Hz (= 5·…10·30.87, within −14 c) at −27…−40 dBFS; C1 bars 131 / 164 / 196 / 262 / 327 / 392 / 523 Hz at −27…−42 dBFS (`refute_808web/layer_test.txt`, `harm_test.txt`). Levels re the 808 fundamental at the hit: H3 −18, H4 −16…−19, H5 −21, H6 −18, H7 −27, H8 −16, H9 −20…−29, H10 −20, H12 −26; nothing distinct above ~400 Hz; evens ~5 dB above odds. The series is present whenever the 808 is sounding (continuous retriggers on odd bars, the held note on even bars) and **decays faster than the fundamental** when nothing retriggers (hook 3: H5–H10 fall to −45…−66 dBFS while H1 is at −33). It is not the SUB (which is clean) and not pad tones (they are +14 c).
Recipe: a parallel channel fed by the 808 voice: `x -> tanh(4x) + 0.3*x^2 -> HPF 80 Hz 12 dB/oct -> LPF 420 Hz 24 dB/oct -> own envelope`, with the envelope following the 808 note-ons but decaying at **−45 dB/s** (−20 dB at 440 ms); set the send gain so that H3 of a loud B0 hit reads −18 dB re the 808's H1 in the mix. Mono. Fills the mids at 0 c and is what makes the chroma read "Bm9 / Cadd9 / Em9".
**Check**: on a B bar with no PAD-2 (bars 25–40), 0 c partials at 154/185/247/309 Hz at −30 ± 5 dBFS during the dotted-8th pulse.

### 3.3 SUB — sustained whole-bar root, bars 17–23 only [M,H]
- B1 61.70 / F#1 46.27 / C2 65.39 / E1 41.21 Hz (A440, 0 ±1 c). Gated to the bar: starts on beat 1 (attack 10–90 % ≈ 20 ms), no decay (slope +2.5 dB/s), ends at the bar line (release 20 ms).
- Spectrum: **clean** — H2 −11 dB, H3 −28 dB, nothing else above −40 (`layer_test.txt` bars 18/20/21/23: H5–H10 at −45…−68 dBFS). The full harmonic series seen under the hooks belongs to 808-HARM (§3.2b), not to this layer; the earlier single recipe that tried to serve both spectra is withdrawn.
- Level −17 dB (−21 dBFS). Mono. Off from bar 24; the hook even-bar floor is the 808-HOLD note (§3.2).
```
osc = sin(2*pi*f0*t) + 0.28*sin(4*pi*f0*t) + 0.04*sin(6*pi*f0*t)   // H2 -11 dB, H3 -28 dB, no saturation
env = gate per bar, A 20 ms, R 20 ms ; gain -21 dBFS ; bars 17-23
```

### 3.4 BED-BASS and BED-SUB (the Röyksopp-derived root voice) [M,H]
- B2 124.50 / F#2 93.27 / C3 131.90 / E2 83.13 Hz = +14 c. Whole bar, legato, no vibrato (±0.3 c), no attack transient. H2 −8 dB, H3 weak. Width −15 dB (r = 0.18).
- Level **−25 dBFS** (−21 dB re ref); check it as "80–160 Hz band = −7 dB re the pad's total in a drum-free bar" (`f_pad.txt`). In drop 1 (25–40) it follows the pad duck lane (§3.5a). Full in 41–104 [M,M: `rp4` section D shows the root partials at their verse level in 41–96 and the outro]. BED-SUB = same note one octave down, −26 dB in 9–16, −30 dB in 17–24 [ASSUMED], off from 25.
```
osc  = sin(2*pi*f) + 0.4*sin(4*pi*f) , f = midi2hz(n)*2^(14/1200)
env  = legato gate, A 10 ms, R 10 ms (no gap at chord change)
pan  = centre ; width: + 0.18 x independent-noise-modulated copy on the side (or chorus 0.5 ms / 0.3 Hz / 15 %) => side -15 dB
```

### 3.5 SAMPLE-PAD — "humming keys" (the signature bed) [M,H]
- Voicing: §1.2 column 4 (root oct 2, close triad oct 3–4, same triad oct 4–5 at −3…−10 dB, octave-5 colour tones at −11…−17 dB) with the per-bar upper-voice table 1.2b. All partials **+14 c**.
- **Vibrato: sinusoidal pitch LFO at exactly the 16th rate (7.667 Hz at 115 BPM), ±11.5 c (24 c pk-pk), applied to all chord voices coherently, phase-locked to the grid (phase −134° at every downbeat), free-running carriers.** Not on the bed bass. This is what reads as "humming". [M,H]
- **Per-voice harmonic content (the oscillator choice, reconciled with the measured envelope)**: isolated chord-tone partials (`rf8_padhf.txt`, `rf6_outro_hats.txt`: F#4 and E4 voices in bars 2/6/22/23) read **H3 −21…−24 dB, H5 −28…−30 dB, H7 ≈ −35 dB re H1**, with H2/H4/H6 supplied by the octave-doubled voices (B4 is "H2" of B3 at −2…−10 dB), not by the waveform. That is a **triangle** (H3 −19, H5 −28, H7 −34) with a gentle roll-off, not a saw through a 24 dB/oct filter (which would put H3 at −9.5 dB before filtering and give a far steeper slope above the cutoff). The flat 160–640 Hz / −4 dB/oct-above-700 Hz envelope of the summed stack and "95 % of energy below 1.8 kHz" follow from triangle voices spread over octaves 2–5.
- Amplitude: constant within ±1 dB across the bar; legato, chord changes < 20 ms, no retrigger.
- Stereo: side −15 dB (r = 0.18), L/R corr 0.96, no L/R pitch offset, no Haas.
- Level: −13 dB (−17 dBFS for the chord sum) in intro/verses/hook 2/outro; +2 dB in 73–88; drop 1 per the lane below. Register: MIDI 40–81.
- Optional colour [M,M]: a fixed tone cluster at **413–426 Hz (G#4 −9…+42 c, A4 −27 c)** at −12…−15 dB re the loudest partial on **F#m and Em bars only** (`f_pad.txt` intro bars 2/4 and outro bar 100; absent on Bm/C bars) — a resonance of the source. Implement as a 420 Hz peaking EQ (+8 dB, Q 8) on the pad, enabled on loop positions 2 and 4, or leave it out.
```
voice(f) = tri(f)                                   // triangle; octave voices supply the even partials
f_mod    = f * 2^(14/1200) * 2^( 0.0115/12 * sin(2*pi*7.667*t + phi) )   // phi so that phase = -134 deg at bar lines
chord    = sum(voice(f_mod_i) * level_i)            // levels from §1.2 / 1.2b
filter   = LPF 12 dB/oct, fc 2.0 kHz, Q 0.7         // gentle; the triangle already gives the measured slope
env      = legato gate, A 15 ms, R 15 ms
stereo   = mono -> + 0.18 x side copy (chorus 0.5 ms / 0.3 Hz / 15 %) => side -15 dB
gain     = -17 dBFS ; delay the whole track +19 ms vs the drum grid
```
**Check (per voice, on a single rendered voice at F#4 +14 c)**: H3 −22 ± 2 dB, H5 −29 ± 2 dB re H1. **Check (stack)**: in a drum-free bar, band levels re the loudest band: 80–160 −7, 160–320 −5, 320–640 −4, 640–1.3 k −10, 1.3–2.6 k −13 dB (`f_pad.txt` intro).

#### 3.5a Drop-1 duck lane (bars 25–40), gain in dB re the verse level, applied to SAMPLE-PAD and BED-BASS together [M,H, `rp4_voicing_pad2.txt` section D "pad" column vs the 1–24 mean of 60.5 dB]
| 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| −15 | −19 | −12 | −13.5 | −12.5 | −12 | −10 | −14 | −14 | −18.5 | −12 | −16 | −15 | −14 | −11 | −12 |

These readings include the riff's notes that fall on pad pitches, so the pad itself may be 2–4 dB lower on the var-a/var-b Bm bars; the duck is a **gain change** (all voices fall together, §2 row 4). Full level returns at bar 41. The "F#5 (no third)" chroma of hook 1 needs no voicing edit.

#### 3.5c Outro low-pass — one filter spec per step [M,H, `rf6_outro_hats.txt` band table, `outro2_out.txt` per-8th sweep]
Applied to the whole tonal bus (SAMPLE-PAD + BED-BASS + PAD-2 + WIDE):
- **Bar 97, sweep**: LPF 18 dB/oct, fc exponential **3.5 kHz → 2.0 kHz** across the bar (per-8th 6 kHz level re bar 96: −15, −20, −20, −26, −25, −27, −28, −32 dB).
- **Bars 98–102, static**: LPF **18 dB/oct at 2.0 kHz** (3-pole). Third-octave targets re the unfiltered bed: 1.6 k −3, 2–3.2 k −8, 4 k −16.5, 5 k −24, 6.3–8 k −28, 12.7 k −44 dB; band targets re intro bars: 1–2 k −3…−6, 2–4 k −7, 4–6 k −19…−23, 6–10 k −34, 10–16 k −41 dB. (The earlier narrow-band figures "3 kHz −22 / 6 kHz −42 re 1 kHz" measured individual partials against the 1 kHz partial and are superseded by these band figures.)
- **Bar 103, second step**: add LPF **12 dB/oct at 1.0 kHz** in series. Band targets re bars 98–102: 1–2 k −11, 2–4 k −20, 4–8 k −22 dB; centroid 440 Hz.
- Bar 104: as 103 [ASSUMED]. No change below 500 Hz at any step.

### 3.6 LEAD RIFF — the interpolated Röyksopp top line ("chopped vocal" in press; measured: pad-synth voice, no formants) [M,H]
- Same +14 c tuning, **no LFO**. Measured spectrum of isolated notes (`rf5_riff_timbre.txt` B): **H2 −12…−18, H3 −26…−29, H4 −33 dB** (G4/E4 in bars 27/28). A saw+pulse through 12 dB/oct at 500 Hz gives H2 −10 / H3 −16 / H4 −22 and is withdrawn. Matching voice: **triangle + an octave sine at −14 dB**, through LPF 12 dB/oct at 700 Hz → H2 −14, H3 −26, H4 −30, H5 −37.
- Gated notes: attack 35 ms, flat sustain, release ≈ 50 ms; lengths per note in §4.1. Monophonic, legato off (each chop re-attacks; a new note-on cuts the previous note). Side −12 dB (r = 0.25).
- Level −13 dB (−17 dBFS peaks) in 25–40 and 57–72; **+7 dB and octave-doubled from bar 73, +9 dB from bar 81, through bar 96** (fundamental of the C-bar E4 chop: 0 dB in 27/31, +7…+10 dB in 75–87, `mtR_choir_refute3.txt`; riff-note levels −21…−25 → −13…−20 dB in `rf5`). The 4th partial strengthens in 73–96 (−3…−5 dB re H1 vs −25 in hook 1) — that is the octave double's H2.
- Register MIDI 61–69 (C#4–A4). Notes in §4.1.
```
voice  = tri(f) + 0.2*sin(2*pi*2f*t), f = midi2hz(n)*2^(14/1200) ; LPF 12 dB/oct fc 700 Hz
env    = A 35 ms, D 0, S 1, R 50 ms ; mono, legato off (each chop re-attacks)
bridge = + octave-up copy (same voice, f*2) at -6 dB, LPF fc 1.2 kHz ; output +7 dB (73-80) / +9 dB (81-96) ; side widened to -6 dB (chorus 2 ms / 0.4 Hz / 40 %)
```
**Check**: isolated G4 note: H2 −14 ± 3, H3 −27 ± 2, H4 −31 ± 3 dB re H1.

#### 3.6b CHORAL layer (bars 73–96) — what it is and its lane [M,H on the measurements; M on the split]
The instrumental's "choral vocals" (press) is **not** a sung stack: it is the LEAD RIFF at +7…+9 dB with its octave double **plus PAD-2's octave-5/6 voices on the WIDE bus swelling in half-bar stabs**. Pitch set {D, E, F#, G, A} in E4–A5 with octave doubling, 2–3 pitch classes at a time, rises on beats 1 and 3, running to bar 96 beat 4 (`mtR_choir_refute*.txt`, `i_wide.txt`: side peaks E5/A5/C#6 over F#m, C5/D5/E5/G5 over C, D5/E5/B5/F#6 over Em = the chord's triad + 7th/9th in octaves 5–6).
Notes per bar for the CHORAL send (PAD-2's voices restricted to MIDI 64–81, legato, one chord per bar): **Bm: D5 F#5 A5 B5 (+ C#6 at −6 dB) · F#m: E5 F#5 A5 C#6 · C: D5 E5 G5 C6 · Em: D5 E5 F#5 G5 B5** [M on pitch classes; the exact voice set ASSUMED from the side-channel peaks].
**Amplitude lane** (half-bar values, dB re the 73–80 base; measured as the Demucs vocal-stem RMS per half bar, `bp_rev_measure.txt` §3 — this stem holds riff + choral together, so the lane is the target for their **sum** on a vocal-stem split; the riff's share is its §3.6 gain, the rest goes on the CHORAL send): 
73: 0 / +6 (peak +10 at beat 3) · 74: 0 / −2 · 75: −1 / −1 · 76: 0 / −1 · 77: −2 / +2 (+6 at 4&) · 78: +1 / 0 · 79: −1 / −2 · 80: −1 / −1 · 81: −1 / +4 (+8 at beat 3) · 82: +1 / +1 · 83: +2 / +6 · 84: +6 / +3 · 85: +3 / +6 (+8 at beat 3 and at 4&) · 86: +4 / +1 · 87: +3 / +5 · 88: +5 / +6 · 89: +3 / +7 (+9.5 at beat 3) · 90: +4 / +4 · 91: +1 / +5 · 92: +4 / +3 · 93: +2 / +6 (+8 at beat 3) · 94: +4 / +5 · 95: +1 / +5 · 96: +5 / +6 · 97: −4 / −15 (fades under the closing LPF, gone by bar 98).
Base: CHORAL send −16 dB re ref (−20 dBFS) in 73–80 [D, sets the −26…−30 dBFS stem base]. From bar 89 the layer is **sustained across whole bars** (both halves +1…+7) rather than riff-gated — this is the "choral layer fills beats 1–2" of hook 3.

### 3.7 PAD-2 — second chord synth [M,H on existence from bar 57; M on detail; its upper voices alone are heard in 35–36, 39–40]
- A440 (0 ±2 c), **no vibrato**, legato. **Unison: 3 voices ±3.5…4 c** — confirmed in the outro upper octave (F#6 at −4/+1/+4 c, G6 at −3/+1/+3 c, C#6 at −4/+4 c, `f_pad.txt`); in 57–60 the cluster is smeared by 808 harmonics, so the outro is the evidence.
- **Partial-level table** (0 c partials in the outro, dB re the SAMPLE-PAD's loudest partial in the same bar — the only drum-free, 808-free place PAD-2 can be read; `f_pad.txt` OUTRO):

| Chord | oct 3–4 | oct 5 | oct 6 (3-voice unison, wide) |
|---|---|---|---|
| Bm | B3 −8, D4 −15, F#4 −9 | B4 −10, D5 −13, F#5 −14.5, **A5 −14 (7th)** | **C#6 −17 (9th)**, F#6 −17 |
| F#m | C#4 −7, F#4 −12 | A4 −16, C#5 −14 | C#6 −11 (E5 7th not resolved: ≤ −18 [ASSUMED]) |
| C | C4 −5, G4 −8 | C5 −10, E5 −14, G5 −14.5 | G6 −11 (B5 7th / D6 9th ≤ −18 [ASSUMED]) |
| Em | B3 −5.5, E4 −10, G4 −16 | B4 −13, **D5 −15 (7th)**, E5 −11 | B5 −10.5 (F#6 9th ≤ −18 [ASSUMED]) |

So 7ths sit at −14…−15 and 9ths at −17 re the sample's loudest partial (≈ −9…−12 dB re PAD-2's own loudest voice). Root in octave 3 (B2/F#2/C3/E2 doubling) ≤ −20 [ASSUMED]. Voices per octave in the outro: the table (2–3 per octave in 3–5, 1–2 in octave 6).
- **Width per octave** (side − mid, outro): octaves 3–4 **−15…−19 dB** (as narrow as the sample, r = 0.15), octave 5 −11…−14 (r = 0.22), octave 6 **−7…−12** (r = 0.35). The earlier "wider and brighter, side −3…−6" applied to the WIDE-bus send, not to PAD-2's direct output; one verifier's "side −15…−22" is the direct output and is correct for the fundamentals.
- Filter: no PAD-2 partial is measured above 1.6 kHz (G6/F#6 fundamentals at −11…−17); set LPF 12 dB/oct at **2.5 kHz [ASSUMED]** (the earlier 3.5 kHz was a guess too). Outro: it passes through the same §3.5c low-pass steps as the pad.
- Level: −21 dB (8 dB under the pad) in 57–72, −19 dB in 73–96, −18 dB (5 dB under the pad) in the outro. Register MIDI 47–82.
- Beats against the +14 c pad at 0.81 % (2 Hz at 250 Hz, 5 Hz at 600 Hz): keep both tunings.
```
voice(f) = saw(f) + saw(f*2^(3.5/1200)) + saw(f*2^(-3.5/1200)) panned L/C/R   // ±3.5 c unison
chord    = oct3-4 voices + oct5 voices + oct6 voices at the table levels (7th -14, 9th -17 re the sample's loudest partial)
filter   = LPF 12 dB/oct fc 2.5 kHz ; env A 30 ms R 50 ms legato
stereo   = per-octave side ratio r: oct 3-4 0.15, oct 5 0.22, oct 6 0.35
sends    = oct 5-6 voices -> WIDE bus (§3.8) from bar 35 ; CHORAL lane (§3.6b) from bar 73
outro    = same LPF steps as §3.5c
```
**Check**: in bar 100 (Em) the 0 c partials B3 / E4 / E5 / B5 read −5.5 / −10 / −11 / −10.5 dB re the +14 c pad's loudest partial; F#6/G6 show a ±3.5 c triplet.

### 3.8 WIDE bus — the side-channel 500 Hz–4 kHz tonal layer [M,H on behaviour; M on identity]
- Source: **PAD-2's octave-5/6 voices (triad + 7th + 9th)** through a 3-voice chorus at **±15 c** (the side peaks come in triplets −17 / +1 / +15 c around 0 c, `bp_rev_measure.txt` §5), 100 % wet, L/R inverted → fully decorrelated side energy. Chroma of the side channel E/F#/B = the upper voices of F#m/Bm/Em (A5/C#6/E5/F#5/B5). Before bar 57 only these upper voices exist (nothing of PAD-2's lower stack is measurable in 35–56), so the bus is fed by the same PAD-2 oct-5/6 note set from **bar 35**, with PAD-2's direct (lower) output starting at bar 57.
- **Send-level lane** (ON = send at −20 dB re ref; the per-bar side/mid target for 500 Hz–4 kHz is the check, `rv2_width.txt`, `i_wide.txt`, `rv2_width` section means): OFF bars 1–34 (−12…−19) · **35–36 ON** (−6) · 37–38 OFF (−11…−12.5) · **39 ON** (−4.3) · **40 ON** (−2) · 41–55 OFF (−14, the narrowest point) · **56 ON from beat 3** (−2.8 bar mean) · 57 ON (−9) · 58 OFF (−7.4 — PAD-2's own upper voices alone) · 59–60 ON (−5 / −4.2) · 61–62 OFF (−7.7 / −8.5) · 63–64 ON (−5 / −4.5) · 65–66 OFF (−8.3 / −6.6) · 67–68 ON (−5) · 69–70 OFF (−8 / −8.8) · 71–72 ON (−5.8 / −2) · **73–96 ON** (−4…−5; 2–6 kHz ≈ 0 dB in 72/88 where the mono accents are absent) · 97–104 ON (survives the low-pass; side/mid 400–2 k −4…−10, outro 1–4 kHz −2…−4).
- The 500 Hz–4 kHz width readings in the "OFF" bars of 57–72 (−7…−9) are PAD-2's own octave-6 voices at r = 0.35; the ON bars add the bus.
**Check**: side/mid 500 Hz–4 kHz per bar within ±2 dB of the lane values.

### 3.9 CLAP (backbeat) + the only reverb [M,H on the clap; M on the tail]
- 4-flam layered clap: sub-transients at **0, 13, 25 and 44 ms** at **−8, −4, −6 and 0 dB** re the peak (the peak is the last one: onset→peak 44 ms; envelope −5 dB at 5 ms, −8 at 10–20 ms, 0 at 44, `d_snare.txt`, `drums.md` 1.3). Spectrum 20–80 ms: centroid 4.3 kHz, flatness 0.74; **1.2–2.5 kHz strongest** (−3 dB re total), 600–1.2 k −7, 2.5–5 k −8, 5–10 k −11, 10–16 k −19; peaks 1.3 k, 1.7 k, 2.2 k, 2.8 k, 3.1 k, 4.0 k. Body decay −6 @ 7, −12 @ 26, −20 @ 53 ms after the peak.
- **Tail — two measurements disagree and the spec picks one**: on the mix the 1.5–6 kHz tail plateaus at −28…−38 dB re peak from 75–450 ms with slope −23 dB/s (T60 ≈ 2.6 s, side −1…−3 dB, `j_space.txt`); on the Demucs drum stem the clap's own tail is short (−43 dB at 100 ms, −57 at 200 ms, slope −34 dB/s → T60 1.75 s, `rf3_hats.txt` I), the long wide tail being mostly non-drum bleed. **Spec: plate, T60 1.8 s, pre-delay 25 ms, HPF 400 Hz, LPF 8 kHz, return EQ flat between, send −30 dB, 100 % wide.** Accept the render when the mix-level tail check passes (below); raise T60 toward 2.4 s only if it does not.
- Level −5 dB (−9 dBFS). On beats 2 and 4 of every bar 1–96 except 24, 40, 72, 88 and bar 57 (beat 4 only); bar 56 = build (§5); bar 48 = fill; extra full clap on beat 3 of bars 77 and 81 at −3 dB re the backbeat clap.
```
clap   = Σ_k noise burst at {0,13,25,44} ms with gains {-8,-4,-6,0} dB: (BPF 1.6 kHz Q 0.7 + BPF 3.1 kHz Q 1), 8 ms decay each
       + body from 44 ms: noise BPF 1.3-2.5 kHz, decay to -20 dB at 53 ms ; body mono (side -18 dB, r = 0.13)
reverb = plate, pre-delay 25 ms, T60 1.8 s, HPF 400, LPF 8 k, send -30 dB, width 100 %
```
**Check (mix level)**: 1.5–6 kHz envelope after a backbeat clap: −21 dB @ 50 ms, −30…−34 @ 75–100 ms, −28…−36 @ 150–300 ms, side/mid of the tail −1…−3 dB.

#### 3.9b LP-CLAP (bar 56 beat 2 only) [M,H on the event; recipe ASSUMED]
Beat 2 of bar 56 carries a 120–400 Hz hit at **−6 dBFS peak** with no sub (20–60 Hz −29 dB re total), no HF (1.5–5 k −20, > 5 k −29 dB re total), peaks around D3/E3/C4 (`bp_rev_measure.txt` §7), while the clap band is empty (−17.9 dBFS). Recipe: the §3.9 clap sample through **LPF 24 dB/oct at 400 Hz, +6 dB**, no reverb send, mono. (Its 120–400 Hz body then matches the normal clap's 200–600 Hz level of −12 dBFS raised by 6 dB.)

### 3.10 HATS [M,H]
- **HAT-A (main closed hat)**: peaks 3.4–4.0 kHz and 12.4 kHz, centroid ~9.5 kHz, −6 dB @ 1–4 ms, −20 @ 37–40, −30 @ 54 ms (dead by 80 ms). Velocity spread < 3.5 dB (machine-static). Width **−15 dB = r 0.18** (mono sample + 18 % independent-noise copy on the side; L/R lag 0).
- **HAT-A2 (second closed hat, bars 33–40 additions)**: same level, centroid 10.1 kHz with its peak at 8.7–10.2 kHz (vs 12.4 kHz), placed **+13 ms** after the grid relative to HAT-A (`rf3_hats.txt` F).
- **OPEN (odd-bar beat-1 hit)**: on beat 1 of every odd bar 1–95, identical in every section (not a crash). Peak **−23 dBFS** (−22…−25), plateau **−27 dBFS at 100 ms** sloping to −31 at 250 ms (verifier −24…−27 plateau; `drums.md` −30.5…−31.1 in the 60–250 ms window), −6 dB @ 276, −20 @ 307 ms. Spectrum (re the > 1 kHz total): **6–9 kHz −5 (strongest), 1–3 k −5.7, 3–6 k −11.5, 9–12 k −7.1, 12–16 k −8.2**; peaks 6.6 / 7.3 / 7.75 / 8.5 kHz; i.e. broadband noise with a +5 dB shelf centred 7.5 kHz, bandwidth ≈ 1.3 octaves (`rf3_hats.txt` pos 0). Identity (open hat vs short crash/noise) stays M: the spectrum/envelope is what is specified. Mono (side −21).
- **Even-bar beat-1 closed hat**: HAT-A at −20…−21 dBFS (absent in 41–56).
- Levels re ref: HAT-A accents −12 (−16 dBFS); even-bar beat-1 −16/−17 (−20/−21 dBFS); HAT-A at −20 dBFS in bar 40 (every 8th).
- **Hat under the clap (slots 4 / 12)**: unverifiable where the clap plays. Spec: **none in 1–40 and 73–96** [ASSUMED]; **HAT-A at full level in 41–56** (the measured 5-note runs include the 2/4 slots); **HAT-B at −24 dBFS in 57–72** (measured at bar 57 where the clap is absent).
```
hatA = white noise -> HPF 3 kHz 12 dB/oct -> peak +6 dB @ 3.7 kHz Q 2, +4 dB @ 12.4 kHz Q 3 -> LPF 16 kHz ; env A 1 ms, exp tau 16 ms ; side r 0.18
hatA2= as hatA with the 12.4 kHz peak moved to 9.5 kHz ; +13 ms
open = white noise -> shelf +5 dB 6-9 kHz (peak @ 7.5 kHz Q 1.2) -> HPF 1 kHz 6 dB/oct ; env A 1 ms, plateau 300 ms (-27 dBFS @ 100 ms, -31 @ 250 ms), release 30 ms ; mono
```

#### 3.10b HAT-B — the dark hat (added 16ths 57–72 = "PERC-2" 73–96 = the HAT-32 ghost layer) [M,H on spectra and positions; M on their being one sample]
One sample explains three things the reports listed separately: the hook-2 added 16ths ("soft hits 6,7,8,9": centroid 6.24 kHz, 1–3 k strongest, 3–6 k −7.6, 6–9 k −12.9, 9–12 k −17.5, 12–16 k −22.8 dB, side −7.0), the bridge "PERC-2" (centroid 6.25 kHz, same band shape, side −6.6), and the −35…−49 dBFS 32nd-note ghost layer (same 1–3 kHz content, which is the verification's "1.5–5 kHz percussion" in bars 17–23). Decay −12 dB @ 9–26 ms, −20 @ 22–75 ms, −30 @ 74–181 ms (two readings; use τ 25 ms). Recipe: decorrelated L/R noise → BPF 1.5–8 kHz (centre 4 kHz, Q 0.5) → peak +4 dB @ 2.2 kHz; **mono/side blend r = 0.45 (−7 dB)** in 73–96, r = 0.32 (−10 dB) in 57–72, r = 0.18 (−15 dB) for the ghost layer in 17–55.
Reference level: v 127 = **−22 dBFS** (its loudest use, the bridge beat-4 hit). Uses, by section (16th slots unless marked ½ = the following 32nd):
- **HAT-32 ghost layer** [M,H; width −15 in 17–55, −10 in 57–71, −6.5 in 73–96; absent in 1–16 and 41–56 per the verification]: **bars 17–39**: 16th slots 6, 8, 9, 13, 14 at −35…−40 dBFS, 32nd slots 7½, 8½, 13½, 14½ at −42…−49 dBFS; **from bar 33** add 5, 5½, 6½ at −49…−51. **Bars 57–71**: 5½, 6½, 7½, 8½, 10½, 13½, 14½ at −42…−52. **Bars 73–96**: 5½, 6½, 7½, 8½, 10½, 13½, 14½ at −32…−43. **Drop-out bars**: 24 = every 32nd slot except 2e–2a (9–14) and 3&–3a (19–20) at −37…−43; 40 = slots 5, 7, 9, 13 (16ths) at −27…−31 plus 32nds at −39…−49; 72 = beats 0/4/8/12 at −27…−30, the rest −40…−52; 88 = slots 0, 3, 4, 5, 7, 8, 10, 11, 12, 15 at −24…−31 (plus 32nds −36…−43); 96 = full bridge pattern; 97 = the layer is cut at the bar line and only the closing LPF's tail is heard (−39 → −63). (`bp_rev_measure.txt` §2, `rf3_hats.txt`, `rf8_padhf.txt`.)
- **Hook-2 added hats (57–72)**: slots 6, 7, 9 at −24 dBFS (v 113); slot 4 under the clap −24 (v 113); slot 14 −37 (v 53) on odd bars.
- **Bridge / hook 3 (73–96) "PERC-2"**: slot 5 −31 (v 76), 6 −24 (113), 7 −24 (113), 8 −26 (101), 9 −23 (120), 10½ −29 (86), 12 −22 (127, under the clap), 13 −38 (50), 14 −33 (67), 15 −35 (60). (The earlier §3.11 "16ths 5–9, 13–15" is this set.)

### 3.11 (merged into 3.10b)

### 3.12 KNOCK — low-mid perc on 1& (bars 1–54) [M,M]
300–600 Hz dominant (peaks 436/417/937 Hz), zero-crossing pitch ≈ 350 Hz, flatness 0.5–0.57, attack 10–28 ms, −12 dB @ 28 ms, side −9.5 dB (r = 0.33). Level −12 dB (−16 dBFS) in 25–40, −16 dB elsewhere; **last knock bar 54** (stem level −17…−24 in 49–54, −62 in 55, −72 in 56; residual −31…−39 in 57–62 is 15 dB down and is ignored) (`rf3_hats.txt` E). Recipe: noise BPF 420 Hz Q 2 + 350 Hz sine ping (τ 20 ms) + −12 dB click; τ 15 ms; side ratio 0.33.

### 3.13 REVERSE SWELL FX (bars 24, 56, 72; optional 96) [M,H]
Fully decorrelated (L/R corr 0.05–0.37 at its peak), noisy-tonal (flatness 0.44–0.65), **fixed partials 735 / 974 / 1074 / 1181 / 1315 Hz** in all three bars (`swell_out.txt`). No pitch sweep, no brightening (centroid flat 1.4–1.7 kHz). **Chosen recipe (the "reverse a chord/crash" alternative is withdrawn — no sample is specified by any measurement)**: white noise, independent L and R seeds → bank of 5 resonators at the partials (Q 30, equal gains) summed with the raw noise at −12 dB → HPF 300 Hz, LPF 4 kHz.
Envelope [M,H]: exponential rise over the whole bar, **side-channel 500 Hz–1.5 kHz from −41 dBFS at the bar start to −18 dBFS at the last 20 ms (+23 dB, ≈ +11 dB/s)**, mid 2–8 kHz −57 → −32 dBFS; cut dead at the next downbeat (−46 dB within 100 ms). The same absolute envelope serves bars 56 (side −43 → −19, corr 0.89 with bar 24) and 72 (side −27 → −19: same peak, higher floor because PAD-2/WIDE are already playing; corr 0.84); bar 96 optional (−28 → −18, corr 0.66). The "+12 dB" and "+14 dB" figures of earlier reports were full-band/mid readings of the same event; the side-channel rise is the implementable number. Level at the peak: side −18 dBFS = −14 dB re ref.

### 3.14 BRIGHT RISER (bar 56 only) [M,H]
Centred above 6 kHz, wide 2–6 kHz; 2 k+ band −34.5 → −20.9 dBFS and 6 k+ −42 → −28 over the bar, mostly beats 3–4; centroid 1.1 → 3.0 kHz. Recipe: white noise → HPF sweeping 1 kHz → 8 kHz (exponential over 2.09 s) → level −35 → −21 dBFS; split: > 6 kHz mono; 2–6 kHz through the **WIDE bus chorus (§3.8, ±15 c, L/R inverted)** — not through the swell, which has no chorus.

### 3.15 Level/width/register summary

| Layer | Level re 808 hit | dBFS | Width (side−mid) / r | Register (MIDI) | Bars |
|---|---|---|---|---|---|
| KICK | +4 | 0 (clipped) | mono (−31) | 28 (E1) | 1–96 (bar 1 beat 1 included) |
| 808 loud / quiet / hook-3 roots | 0 / −8 / −8…−9 | −4 / −12 / −12…−13 | mono (−36) | 23–30 (riff 21–40) | 25–96 |
| 808-HOLD floor (slot-7 note, even bars) | −12 (sustain) | −16 | mono | 28–30 | even bars 26–40, 74–88 |
| 808-HARM send | H3 −18 re 808 H1 | −27…−42 (partials) | mono | — | 25–96 |
| SUB | −17 | −21 | mono | 28–36 | 17–23 |
| BED-BASS / BED-SUB | −21 / −26 (−30 in 17–24) | −25 / −30 | −15 (r 0.18) / mono | 40–48 / 28–36 | 1–104 / 9–24 |
| SAMPLE-PAD | −13 (lane §3.5a in 25–40, −11 in 73–88) | −17 | −15 (r 0.18) | 40–81 | 1–104 |
| LEAD RIFF | −13 (−6 from 73, −4 from 81) | −17 (−10 / −8) | −12 (−6 from 73) | 61–69 (+ 73–81 double) | 25–40, 57–96 |
| PAD-2 direct | −21 / −19 / −18 | −25 / −23 / −22 | oct 3–4 −16, oct 5 −12, oct 6 −8 | 47–82 | 57–104 |
| WIDE bus (PAD-2 oct 5–6 via ±15 c chorus) | −20 send | — | fully decorrelated | 76–88 | lane §3.8 (35–36, 39–40, 56–57, 59–60, 63–64, 67–68, 71–104) |
| CHORAL (PAD-2 oct 5–6, lane §3.6b) | −16 + lane | −20 + lane | via WIDE | 74–81 | 73–96 |
| CLAP / LP-CLAP | −5 / −2 | −9 / −6 (120–400 Hz) | body −18, tail −2 / mono | — | 1–96 / bar 56 beat 2 |
| HAT-A / HAT-A2 / even beat-1 | −12 / −12 / −16 | −16 / −16 / −20 | −15 (r 0.18) | — | 1–96 / 33–40 / even bars ≤ 40, 57–96 |
| OPEN | −19 peak / −23 plateau | −23 / −27 | mono | — | odd bars 1–95 |
| HAT-B (dark hat): hook-2 adds / PERC-2 / HAT-32 | −20 / −18…−31 / −31…−45 | −24 / −22…−35 / −35…−49 | −10 / −7 / −15→−6.5 | — | 57–72 / 73–96 / 17–39, 57–96 |
| KNOCK | −12…−16 | −16…−20 | −9.5 (r 0.33) | — | 1–54 |
| SWELL / RISER | −14 (side peak) / −17 | −18 / −21 | ≈ 0 (decorrelated) / centred > 6 k, wide 2–6 k | — | 24, 56, 72, (96) / 56 |

---

## 4. Riff and vocal-texture plans

### 4.1 Lead riff — MIDI notes, every bar that has one (16th slots; lengths in 16ths from basic-pitch, ±0.5 16th on soft tails) [M,H pitches, M lengths; `rf4_riff.txt`]
**Voice rules**: monophonic, legato off; a note holds for its listed length and is cut earlier by any new note-on. There is **no cross-bar tie**: the "held tail" of each Bm bar is a **new note-on at slot 0–2 of the following F#m bar** (F#4 after var a, C#4 after var b), with its own length; the slot-14 note of the Bm/C bar simply ends at its length (it never reaches slot 16 except E4@15 in bar 33, len 1.1). Bars not listed are **rests** (every F#m bar that is not listed, and 38, 78, 94). 8-bar phrase = two passes of the loop; var a on odd passes, var b on even passes.

**Drop 1 (25–40)** — full in 25–32, already thinned in 33–40 (one verifier's reading, confirmed by the note list):
| Bar | Chord | Notes (MIDI@slot(len)) |
|---|---|---|
| 25 | Bm a | F#4 66@6(1.3) · G4 67@9(1.8) · E4 64@14(1.9) |
| 26 | F#m | F#4@2(1.2) then rest |
| 27 | C | E4@6(2.9) · D4 62@9(1.5) · F#4@14(2.0) |
| 28 | Em | G4@0(3.0) · F#4@5(1.1) · F#4@6(1.3) · E4@8(2.1) · D4@13(2.1) |
| 29 | Bm b | D4@6(2.9) · C#4 61@9(1.4) · D4@11(1.9) · A4 69@14(2.0) |
| 30 | F#m | C#4@0(2.3) · C#4@2(1.4) then rest |
| 31 | C | E4@6(2.8) · D4@9(1.3) · F#4@14(2.0) |
| 32 | Em | G4@0(1.5) · G4@2(1.6) · F#4@5(2.0) · E4@8(2.0) · D4@13(2.1) |
| 33 | Bm a | F#4@6(1.3) · G4@9(1.3) · E4@15(1.1) |
| 34 | F#m | F#4@1(2.2) then rest |
| 35 | C | E4@6(2.9) · F#4@14(1.8) |
| 36 | Em | E4@8(1.8) only |
| 37 | Bm b | D4@6(2.9) · C#4@9(1.2) · D4@11(1.9) · A4@14(1.9) |
| 38 | F#m | **rest** |
| 39 | C | E4@6(2.9) · E4@11(1.4) · F#4@14(1.4) |
| 40 | Em | E4@8(2.1) only |

**Hook 2 (57–72)**, thinned:
57: G4@9(1.7) E4@14(1.5) · 58: F#4@4(1.9) · 59: E4@6(1.2) E4@12(1.4) · 60: E4@0(2.0) E4@6(1.1) E4@8(2.1) E4@10(1.5) · 61: D4@2(1.1) D4@6(3.6) A4@14(1.1) · 62: F#4@13(1.6) · 63: E4@5(3.7) E4@11(2.2) · 64: E4@0(1.7) E4@6(2.0) E4@8(2.7) · 65: F#4@7(1.3) A4@8(1.1) E4@14(1.3) · 66: F#4@0(2.0) F#4@3(3.5) F#4@8(1.0) · 67: E4@6(1.3) F#4@14(1.3) · 68: E4@0(1.6) E4@4(3.0) E4@7(1.0) E4@8(2.9) · 69: D4@6(3.3) D4@11(1.9) · 70: F#4@8(1.3) F#4@13(2.3) · 71: E4@5(1.4) E4@7(1.3) F#4@14(1.5) · 72: E4@0(2.0) E4@4(3.9) E4@8(2.1) E4@10(1.1).

**Bridge (73–88)**, busier version (+7/+9 dB, octave double, §3.6):
73: F#4@6(1.8) G4@9(1.4) F#4@11(2.0) E4@14(1.8) · 74: F#4@0(3.7) · 75: E4@6(2.0) E4@8(1.2) E4@9(1.1) E4@11(2.5) F#4@14(1.7) · 76: G4@0(2.0) E4@8(2.0) D4@12(1.9) · 77: D4@6(2.9) C#4@9(1.2) D4@11(2.7) A4@14(1.5) · 78: **rest** · 79: E4@6(2.7) E4@11(2.8) F#4@14(1.5) · 80: E4@8(2.0) E4@10(1.8) · 81: F#4@6(2.0) G4@9(1.1) F#4@11(1.3) E4@14(1.6) · 82: F#4@0(3.5) · 83: E4@6(2.1) E4@8(1.1) D4@9(1.1) E4@11(2.8) F#4@14(1.8) · 84: G4@0(2.5) E4@8(1.2) D4@12(3.1) · 85: D4@6(2.6) D4@11(3.1) A4@14(1.8) (C#4 dropped) · 86: F#4@12(3.3) · 87: E4@6(1.9) E4@8(1.8) D4@9(1.3) E4@11(1.1) E4@12(1.4) F#4@14(1.5) · 88: G4@0(3.1) F#4@4(1.2) E4@8(4.0) D4@12(1.6) D4@13(1.1).
(The Em bars of the bridge are 76, 80, 84, 88 — 80 is the "E4@8 only" type like 36/40; 76/84/88 carry the G4@0 … D4@12 shape.)

**Hook 3 (89–96)**, thinned, over the sustained CHORAL layer:
89: F#4@6(1.0) E4@14(1.1) · 90: F#4@0(1.3) · 91: E4@6(2.4) E4@8(2.6) E4@11(2.8) · 92: E4@9(1.1) · 93: D4@5(1.1) D4@6(3.0) C#4@9(1.3) D4@11(2.7) · 94: **rest** · 95: C4 60@5(1.4) E4@6(2.1) E4@8(2.0) D4@9(1.1) E4@11(2.6) F#4@14(1.5) · 96: E4@8(1.1).

In 1–24, 41–56 and the outro the riff track is **silent** (the register is the pad; basic-pitch's notes there are pad voices split by the vibrato). MIDI reference: `refs/bp/eig_inst_basic_pitch.mid` and `rf4_riff.txt`.

### 4.2 Kid Cudi's hook (vocal version only) — for an optional "hum-lead" texture [M,H pitch classes; M on register detail]
Same riff **one octave down (MIDI 49–57, C#3–A3)**, slightly straightened. The vocal-stem pitch distribution for the sung hook sits **D3–G3 (5th–95th percentile), centred F#3/E3; C#3 and A3 are < 3 % outliers** (`mtR_choir_refute3.txt`), so write the A3 and C#3 of the shapes below as short grace/passing tones and the held tones as D3/E3/F#3:
- Bm var a: (F#3@6) A3@8 (grace) G3@9 F#3@11–12 E3@14 → F#3 held ≈ 1 beat into the F#m bar.
- Bm var b: D3 repeated slots 3–7 (2–4 hits), C#3@9 (short), D3@11, A3@14 (grace) → D3/C#3 ≈ 1–1.3 beats (mostly D3).
- F#m bar: held tail then rest.
- C bar: E3 (often anticipated from slot 0–4), E3@6, D3@9 (sometimes), E3@11, F#3@14 → G3.
- Em bar: **G3@0 F#3@4 E3@8 D3@12**, one per beat (3–4 16ths each) — the most consistent line.
Present in bars 25–40, 57–72, 89–104 (+12…+15 dB excess in the C3–B3 octave); verse-type long notes in 9–24 and 41–56 (A3 held over F#m, C3 held over C); ≈ none in 73–88.

### 4.3 Hum / "ooh" textures — synthesis plan (no words; the official instrumental has none [M,H], so these are an optional layer, default −6 dB below where the voice sits) [D]
Measured facts to copy: Cudi's intro hum is monophonic, pitch-stable to 1–5 c frame-to-frame (same as his sung notes, so NOT hard-tuned/vocoded by measurement; the vocoder description is press-only [W]), register D3–A3, strong octave-above energy. The bridge "oohs" exist **only in the vocal version** (full stem +4…+13 dB over the instrumental stem at 2:34.7, 2:43.2, 2:51.5, 2:59.3); the instrumental's "choral" layer is §3.6b. VOX-CHOIR below is therefore modelled on the vocal version, not on the instrumental, and is off by default.

**VOX-HUM** (intro) — contour from the vocal stem (`mtR_choir_refute3.txt`, file time): A3 2.78–3.09 s → G3 3.2 → E3 4.1 → F#3 4.4 → E3 5.1–5.4 → **D3 5.5–6.3** → **E3 7.0–7.7** → F#3 8.5; ad-lib climb G3 (11.0) A3 (12.0) C#4 (13.0) B3 (14.0–15.2) landing on the tonic.
```
source   = pulse train / glottal (Rosenberg) at f0, 0.5 % jitter, vibrato 5 Hz ±6 c starting 300 ms into each note
formants = closed-mouth "mm": F1 250 Hz (BW 60, 0 dB), F2 1000 Hz (BW 120, -18 dB), F3 2500 Hz (BW 200, -30 dB), nasal zero at 1.0 kHz (-15 dB); LPF 1.5 kHz 12 dB/oct
layers   = unison + octave-up copy at -10 dB (measured "strong octave-above energy")
env      = A 120 ms, R 250 ms, legato between notes with 40 ms pitch steps (no long glide)
level    = -20 dB re 808 (-24 dBFS) ; mono, 10 % width ; plate reverb 1.6 s, send -20 dB
```
**VOX-HOOK** (if used, bars 25–40, 57–72, 89–104): the §4.2 line through the same voice with an "oo" vowel (F1 300, F2 870, F3 2240), unison + octave-up −8 dB, level −12 dB re 808, side −12 dB. Rhythm in 57–72 and 89–104: the hook-1 shapes of §4.2 reused unchanged [ASSUMED — the vocal-stem rhythm there was not transcribed].
**VOX-CHOIR** (bridge 73–88, four phrases, vocal-version model): 3-voice stack, top voice with explicit durations [ASSUMED from the 1–2 s hold and one-note-per-beat reading]: **E4 1.5 s → D4 0.5 s → F#4 0.5 s → G4 0.5 s → F#4 0.5 s → E4 1.0 s → A4 (or C#5 on the 4th phrase) 0.5 s**, total ≈ 5 s; middle voice a diatonic 3rd below; bass support E3–A3 one octave below the top; vowel "oh" (F1 570, F2 840, F3 2410) for the first 1.0 s, **morphing to "oo" over the following 0.5 s** and staying "oo"; each voice 2 detuned copies ±8 c with independent 0.3 Hz drift; chorus 15 ms / 0.3 Hz / 50 % for width (side −6 dB); level −16 dB re 808; fade in over bar 73 and over 87–88. Phrases start on the C bar of each loop (bars 75, 79, 83, 87).

---

## 5. Drum programming per section

16th grid, slots 0–15 (0 = beat 1, 4 = beat 2, 8 = beat 3, 12 = beat 4). **One row per layer per bar type.** Everything quantised; apply +1 ms to hats on e/a 16ths, +2 ms to claps, +13 ms to HAT-A2, 0 to kicks. No swing, no humanize.

**Velocity ↔ level (one formula for every layer)**: `level_dB_re_layer_reference = 40 · log10(v / 127)`, so v 127 = 0, 113 = −2, 101 = −4, 90 = −6, 80 = −8, 71 = −10, 64 = −12, 57 = −14, 50 = −16, 45 = −18, 40 = −20, 36 = −22, 32 = −24, 28 = −26, 25 = −28, 23 = −30, 20 = −32, 18 = −34, 16 = −36, 14 = −38, 13 = −40, 11 = −42, 10 = −44, 9 = −46, 8 = −48. **Layer references (v 127 =)**: KICK 0 dBFS · CLAP −9 dBFS · HAT-A −16 dBFS · HAT-A2 −16 dBFS · OPEN −23 dBFS peak · HAT-B −22 dBFS · KNOCK −16 dBFS. Symbols: **X** = 127, **9** = 113, **x** = 90, **o** = 64, **-** = 45, **.** = rest; HAT-B and HAT-32 rows give explicit `slot:velocity` lists (½ = the 32nd after that 16th).

```
Slot:               0 1 2 3 | 4 5 6 7 | 8 9 10 11 | 12 13 14 15

INTRO (1-8)
 odd  KICK          X . . . | . . . . | . . . . | . . . .          (bars 1,3,5,7 — bar 1 included)
 odd  OPEN          X . . . | . . . . | . . . . | . . . .
 even KICK          . . . . | . . . . | . . . . | . . . .
 even HAT-A         x . . . | . . . . | . . . . | . . . .          (even-bar beat-1 closed hat, v 90 = -20 dBFS)
 both CLAP          . . . . | X . . . | . . . . | X . . .
 both HAT-A         . . X X | . . . . | . . X X | . . . .          (accents 1& 1a 3& 3a; plus the even-bar x at 0)
 both KNOCK         . . x . | . . . . | . . . . | . . . .          (v 90 = -20 dBFS)
 both HAT-B/32      none

V1a (9-16)        as INTRO except KICK on every bar:
 both KICK          X . . . | . . X . | . . . . | . . . .

V1b (17-23)
 odd  KICK          X . . . | . . X . | . . . . | . . . .
 even KICK          X . . . | . . X . | . . X . | . X . .
 others           as V1a
 both HAT-32        6:50 8:45 9:40 13:45 14:40 | 7½:32 8½:28 13½:32 14½:25        (= -35..-40 dBFS on the 16ths, -42..-49 on the 32nds; width -15)

BAR 24            KICK/CLAP/HAT-A/OPEN/KNOCK: none
      HAT-32        every 32nd slot except 9-14 and 19-20 (32nd numbering) at v 40-45 (-37..-43 dBFS) ; SWELL §3.13

HOOK1a (25-32)
 odd  KICK          X . . . | . . X . | . . . . | . . . .          (808 fills 4,7,10,13 — not drums)
 even KICK          X . . . | k . X . | . . X . | . X . .          k = soft kick v 90 on bars 28, 32 (and 36 in H1b) only
 odd  OPEN          X at 0 ; even HAT-A x at 0
 both CLAP          . . . . | X . . . | . . . . | X . . .
 both HAT-A         . . X X | . . . . | . . X X | . . . .
 both KNOCK         . . X . | . . . . | . . . . | . . . .          (v 127 = -16 dBFS, loudest here)
 both HAT-32        as V1b

HOOK1b (33-40)    as HOOK1a plus:
 both HAT-A2        . . . . | . . X X | . X . . | . . . .          (second hat sample, v 127, +13 ms)
 both HAT-32        as V1b plus 5:27 5½:25 6½:25

BAR 40            KICK          X . . . | X . . . | X . . . | X . . .
                  CLAP          none
                  HAT-A         x . x . | x . x . | x . x . | x . x .     (every 8th, v 90 = -20 dBFS; no OPEN, no HAT-A2)
                  HAT-B         5:71 7:64 9:64 13:64                       (-27..-31 dBFS) ; HAT-32 32nds at v 20-28
                  KNOCK         . . X . | . . . . | . . . . | . . . .
                  808           q@1 q@5 X@7 X@10 F#1@13 (§1.3) ; WIDE bus ON ; no swell

VERSE2 (41-56)
 odd  KICK          X . . . | . . X . | . . . . | . . . .          (51: slot 0 only ; 55: slot 6 only)
 even KICK          X . . . | . . X . | . . X . | . X . .          (44, 52: no slot 6 ; 48: 0, 6, 10)
 odd  OPEN          X at 0 ; even: NO beat-1 hat
 both CLAP          . . . . | X . . . | . . . . | X . . .
 both HAT-A         . . X X | X X X . | . . X X | X X X .          (two 5-note runs incl. the 2/4 slots under the clap, all v 127)
 both HAT-B         1:50 7:50 8:50 9:50 15:50                       (-37 dBFS ghosts [M,M]: fill the >6 kHz onset detector's 13-16/16 reading)
 both KNOCK         . . X . | . . . . | . . . . | . . . .          (bars 41-54 only)
 both HAT-32        none (absent in 41-56)

BAR 48            CLAP          . . . . | X . . . | . . . . | X X X .     (roll 4 4e 4&, -8 dBFS = v 113 each)
                  KICK          X . . . | . . X . | . . X . | . . . .

BAR 56            KICK          none
                  LP-CLAP       . . . . | X . . . | . . . . | . . . .     (§3.9b, beat 2)
                  CLAP          . . . . | . . . . | . . x . | X 9 X X     (3& -15 dBFS = v 90 ; 4 -7 = v 127 ; 4e -11 = v 113 ; 4& -8 = v 127 ; 4a -9 = v 127)
                  HAT-A         0:71 1:45 3:45 4:64 6:64 7:64 9:64 | 12:127 13:127 14:127 15:90   (-27..-37 dBFS in the first half; the 6-16 kHz band of the second half is the riser, not hats)
                  KNOCK         none (last knock bar 54)
                  RISER §3.14 + SWELL §3.13 ; WIDE bus ON from beat 3 ; 808 riff unchanged

HOOK2 (57-72)
 both KICK          X . . . | . . X . | . . . . | . . . .          (59: 0 only ; 64/66/68: + k at 10)
 odd  OPEN          X at 0 ; even HAT-A x at 0
 both CLAP          . . . . | X . . . | . . . . | X . . .          (every bar; bar 57: slot 12 only)
 both HAT-A         . . X X | . . . . | . . X X | . . . .
 both HAT-B         4:113 6:113 7:113 9:113 | odd bars + 14:53          (-24 dBFS adds 2& 2a 3e + under-clap beat 2; width -10)
 both HAT-32        5½:30 6½:30 7½:25 8½:28 10½:28 13½:28 14½:25         (-42..-52 dBFS)
 both KNOCK         none

BAR 72            KICK          . . . . | k . . . | . . . . | . . . .     (one soft kick, v 90)
                  CLAP/HAT-A/OPEN/HAT-B: none
                  HAT-32        0:71 4:71 8:71 12:71 (-27..-30 dBFS on the beats) + 32nds at v 20-28
                  808 roll q@1 X@4 X@7 X@10 F#1@13 ; SWELL ; WIDE bus ON

BRIDGE (73-88)
 odd  KICK          X . . . | . . X . | . . . . | . . . .          (73, 83: 0 only)
 even KICK          X . . . | k . X . | . . X . | . X . .          k = soft kick v 90 on 80, 84 only
 odd  OPEN          X at 0 ; even HAT-A x at 0
 both CLAP          . . . . | X . . . | . . . . | X . . .          + full clap at 8 (v 101, -3 dB) on bars 77 and 81
 odd  HAT-A         . . X X | . . . . | . . X X | . . . .          73-79 ; 81-87: . . . X | . . . . | . . X X | . . . .  (slot 2 dropped)
 even HAT-A         . . X X | . . . . | . . X X | . . . .
 both HAT-B         5:76 6:113 7:113 8:101 9:120 10½:86 12:127 13:50 14:67 15:60   ("PERC-2": -31 -24 -24 -26 -23 -29 -22 -38 -33 -35 dBFS; width -7)
 both HAT-32        5½:40 6½:36 7½:50 8½:40 13½:36 14½:40        (-32..-43 dBFS)

BAR 88            KICK          k . . . | . . . . | . . k . | . k . .     (soft kicks v 90 at 0, 10, 13)
                  CLAP/HAT-A/OPEN: none
                  HAT-B         0:76 3:64 4:64 5:64 7:71 8:71 10:64 11:64 12:64 15:71   (-24..-31 dBFS) + HAT-32 32nds at v 28-36
                  808 roll as bar 72 ; no swell ; WIDE bus ON

HOOK3 (89-96)
 both KICK          X . . . | X . . . | . . . . | . . . .          (beats 1 and 2 = slots 0, 4 ; 94: 4 only ; 92: + k at 10)
 odd  OPEN          X at 0 ; even HAT-A x at 0
 both CLAP          . . . . | X . . . | . . . . | X . . .          (last clap = bar 96 slot 12)
 both HAT-A         . . X X | . . . . | . . X X | . . . .          (the 73-80 pattern, slot 2 present on odd bars)
 both HAT-B         as BRIDGE
 both HAT-32        as BRIDGE ; last hat = bar 96 slot 15

OUTRO (97-104)    nothing (the 6-16 kHz decay across bar 97 is the closing low-pass, not a hit)
```
OPEN: beat 1 of **every odd bar 1–95** (bar 24 is even; bars 41–55 and 57–87 keep it). Even-bar beat-1 HAT-A (v 90) except bars 41–56.

Kick summary (the thing that changes most): intro 1 of odd bars (incl. bar 1) · 9–16 `1 2&` · 17–56 and 73–88 2-bar cell (odd `1 2&`, even `1 2& 3& 4e`) · 40 four-on-the-floor · 57–72 `1 2&` everywhere (808 takes the pulse) · 89–96 `1 2` (slots 0, 4) · 97+ none.

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
| Spectral centroid (full mix, per bar) | intro 2000–2500 Hz (odd/even alternation), drop 1 1700–2100, verse 2 2000–2650, drop 2 1850–2360, bridge 2080–2570, hook 3 2300–2800, outro 750–1136 → bar 103 441 Hz; whole track 1839 Hz | brightness steps per section, never sweeps (except bar 56 and the bar-97 LPF close) |
| Harmonic-stem centroid | ≈ 850 Hz (bars 1–32) → 1100–1350 Hz (73–96): PAD-2 is what brightens the mids | |
| Stereo | sub < 60 Hz side/mid −37.6 dB; < 120 Hz −27.4; < 200 Hz −23 (sub strictly mono). 60–120 Hz: mono in drops, −17 intro, −14.5 verse 2 (V2-SIDE). Full-band L/R corr 0.96–0.98 bars 1–32, 0.95 verse 2, 0.88–0.93 drops 2/3, 0.82 post-drop/outro; 0.50 bar 24, 0.70 bar 56 | |
| Width per bar, 500 Hz–4 kHz side/mid | the §3.8 lane: 1–34 −12…−19 · 35/36 −6 · 39 −4.3 · 40 −2 · 41–55 −14 · 56 −2.8 · 57–72 alternating −4…−9 · 73–96 −4…−5 · outro −2…−4 (1–4 kHz) | automation lane for the WIDE bus |
| Clap reverb | the only reverb: plate T60 1.8 s (spec) / 1.75–2.6 s (measured range, §3.9), pre-delay 25 ms, side −2 dB on the tail | |
| Absent | delays, vinyl crackle (noise floor = digital silence), sidechain pump, section crashes, gated silence, HPF intro opening | |
| Loudness contour | see §2 (intro 5.9 dB under the peak section; biggest step bar 24 → 25 = +7.4 dB RMS) | |
| Ending | hard digital cut at the bar-105 line, no fade, no tail | |

Suggested chain: stems → bus (no compression) → clipper at 0 dBFS driven so that the kick clips (~20 000 clipped samples over the track) → ceiling 0.0 dBFS sample peak. Check: 57 % < 60 Hz, −10.3 LUFS integrated, bar contour within ±0.5 dB of §2.

---

## 7. What makes this track feel the way it does — ranked

1. **The 808 pulse lives between the kicks.** Kick on 1 and 2&, 808 on 2 · 2a · 3& · 4e (a dotted-8th chain starting on the backbeat and landing on the next downbeat; inter-hit spacing 391 ms), and the two never coincide (0 of 47 loud 808 hits within 40 ms of a kick in hook 1; the even-bar quiet root is even nudged to 1e for it). On even bars the kick takes the 3& 4e pulse and the 808 holds. At 115 BPM with a clap on 2 and 4 and straight 16ths this is a dance/house bounce, not halftime trap — the "rubbery bass" of the press release and r/hiphopheads' "Random Access Memories" comparison [M,H; W].
2. **Sub-first mastering.** 57 % of the energy is below 60 Hz; the 808 sits at B0 (30.9 Hz) with a phase-locked octave and a 0 c harmonic send that fills the mids, the E1 kick is the loudest element and is hard-clipped at 0 dBFS; the drop at bar 25 is a +40 dB sub step plus a 15 dB width collapse rather than a drum entry. Death Oblivion's 25:10 808-to-kick ratio is the documentary echo of this [M,H; W].
3. **Röyksopp's loop, re-voiced and detuned.** Bm · F#m · C · Em (the album's Dm7 Am7 E♭maj7 B♭/G down 3 st) played as bare close triads with the chromatic inner line D–C#–C–B and the Neapolitan C, +14 c sharp against an A440 low end; a 16th-synced ±11.5 c pitch LFO makes the pad "hum". From bar 35 (upper voices) and bar 57 (full) a second A440 pad beats against it at 0.81 % — the shimmer of the second half [M,H; W cifraclub/Hooktheory].
4. **The hook is an interpolated instrumental chop, phrased like a voice.** 8-bar riff in C#4–A4, dark (H3 −27 dB, no formants), gated 35/250/50 ms, every phrase ending on a note that is re-struck on the next downbeat and the F#m bar left as a breath; Cudi sings the same line an octave down. From bar 73 it is doubled/brightened +7–9 dB and, with PAD-2's upper voices swelling on the WIDE bus, becomes the "choral" peak [M,H].
5. **Two-bar cells inside eight-bar phrases.** Odd and even bars differ everywhere (open-type hat on odd downbeats, kick figure, 808 scheme, 1–1.4 dB loudness alternation); every section lands on bar 8n+1; the only fills are the Em bar at the end of a phrase (24, 40, 56, 72, 88) with 808/kick rolls and a reused reversed swell — never a crash, never a silence [M,H].
6. **Width is an arrangement parameter.** Mono below 120 Hz always; the intro and verse 2 are nearly mono (L/R corr 0.96–0.98, side −19…−22 dB), a tonal wide layer toggles on in 2-bar stretches (35–36, 39–40, 57–71) and then stays on for the peak (side −4…−5 dB); the swells are the only fully decorrelated moments (corr 0.5) [M,H].
7. **Brightness by steps, not sweeps.** Each section has its own fixed centroid; the single filter-opening riser is bar 56; the outro is a stepped 18 dB/oct 2 kHz → +1 kHz low-pass with a hard digital cut on the bar-105 line [M,H].
8. **Dry, clean, digital.** No delays, no vinyl noise, no sidechain pump; the only space is the clap's short wide plate at −30 dB. Everything else is close and mono-ish, which is why the few wide elements read so strongly [M,H].

---

## 8. Build order (suggested)
1. Grid + chord/bass MIDI (§1) at 115.000, 104 bars, t0 = 0.278 s; drum MIDI (§5) from `drums_measured.mid` as a cross-check.
2. KICK, 808 (HIT + HOLD envelopes), 808-HARM send, SUB, BED-BASS (§3.1–3.4): verify sub share, the 808/kick never-coincide rule, the even-bar −16 dBFS floor and the 0 c H3–H10 series on a B bar.
3. SAMPLE-PAD with synced LFO, +14 c and the 1.2b voice table (§3.5, +19 ms); LEAD RIFF (§3.6, §4.1); PAD-2 (§3.7) upper voices from bar 35 on the WIDE bus, full from bar 57.
4. Clap+plate, LP-CLAP, HAT-A/A2, OPEN, HAT-B (adds / PERC-2 / HAT-32), knock (§3.9–3.12); swells/riser (§3.13–3.14) on bars 24/56/72/(96).
5. Automation: pad duck lane (§3.5a), WIDE-bus lane (§3.8), CHORAL lane (§3.6b), outro LPF steps (§3.5c), hard cut.
6. Master: clipper to 0 dBFS, −10.3 LUFS, contour of §2; compare per-bar band RMS with `bar_band_rms.txt` and `bars.csv`, run every **Check** line in §3.
7. Optional VOX textures (§4.3) muted by default.

## 9. Open items / confidence notes
- Whether the odd-bar beat-1 hit is an open hat or a short crash/noise sample (envelope/spectrum only) — M; its spectrum and plateau are specified, which is what the render needs.
- The even-bar −16 dBFS floor: implemented as the 808-HOLD sustain stage; a separate sustained layer would measure the same — M.
- 808-HARM as a parallel saturation send is a mechanism chosen to reproduce the measured 0 c series; the record may use a layered harmonic sample instead — M on mechanism, H on the target spectrum.
- HAT-B being one sample for the hook-2 adds, PERC-2 and the HAT-32 ghosts (same centroid/band shape/width family) — M; levels and positions are H.
- The reversed swell into bar 97 and the bar-24 808 pickup — L.
- Verse-2 grace notes one octave below (C#1, E1 before C#2/E2) — M; V2-SIDE doubling only the main notes — ASSUMED; a glide in V2-SIDE — contested (D: none).
- Provenance of the riff timbre (synth line vs processed vocal) is unverified; the recipe copies the measured spectrum either way.
- Lengths of riff notes ±0.5 16th (soft tails).
- The CHORAL/riff split of the §3.6b lane (the vocal stem holds both) — M.
- BED-BASS absolute level (−17 vs −25…−29 dBFS readings; the pad-relative check is authoritative) — M.
- Clap tail T60 (1.75 vs 2.6 s) — M; spec 1.8 s with the mix-level check.
- PAD-2 cutoff (2.5 kHz) and its 7ths in F#m/C bars — ASSUMED; PAD-2's unison and widths are H in the outro only.
- Bar 104 content — ASSUMED (copy of bar 100); only its existence is supported (official duration).
- Section names: "hook/verse/bridge" follow the vocal version's lyric timing [W LRCLIB]; the instrumental's own boundaries are identical.

## 10. Sources
Measured: scripts and outputs in this folder (`drums.md`, `bass.md`, `bass_bars.txt`, `harmony.md`, `structure.md`, `sounds.md`, `arrangement.json`, `resolved.json`, `grid.json`, `master_out.txt`, `bar_band_rms.txt`, `rv2_width.txt`, `rv2_drums.txt`, `rf3_hats.txt`, `rf4_riff.txt`, `rf5_riff_timbre.txt`, `rf6_outro_hats.txt`, `rf8_padhf.txt`, `rp4_voicing_pad2.txt`, `rp5_topvoice_retrig.txt`, `mt7c_voicing.txt`, `mtR_choir_refute2/3.txt`, `refute_808web/layer_test.txt`, `refute_808web/harm_test.txt`, `b_kick2.txt`, `d_snare.txt`, `j_space.txt`, `swell_out.txt`, `outro2_out.txt`, `i_wide.txt`, `f_pad.txt`, `mt5_findings.json`, `mt7_findings.json`, `mt11_v2riff_verdict.md`, `bars.csv`, `drums_hits.json`, `bass_notes.json`, `demucs4/`, and the revision measurements `bp_rev_measure.py` → `bp_rev_measure.txt`).
Web: Universal Music Canada press release https://www.universalmusic.ca/press-releases/bnyx%ef%b8%8f-and-kid-cudi-share-collaboration-everywhere-i-go-remind-me ("humming keys, rubbery bass, snapping percussion, choral vocals"; writers BNYX, Mescudi, Øye, Berge, Brundtland; 30 Jan 2026) · mxdwn https://music.mxdwn.com/2026/02/02/news/kid-cudi-bnyx-team-up-for-collaborative-new-single-everywhere-i-go-remind-me/ ("strong 808s", "clap back beats", "chopped up vocal track") · HipHopCanada https://hiphopcanada.com/bnyx-kid-cudi-everywhere-i-go-single/ (vocoder) · Apple Music single https://music.apple.com/us/album/everywhere-i-go-remind-me-single/1871603512 (3:37, Röyksopp credited) · WhoSampled https://www.whosampled.com/sample/1406730/ (sample from 0:50; page CAPTCHA-walled, snippet only) · Hooktheory single version https://www.hooktheory.com/theorytab/view/royksopp/remind-me-%28single-version%29 (D# minor, 126, i7–v7–VII7–iv7) and album version https://www.hooktheory.com/theorytab/view/royksopp/remind-me-%28album-version%29 (F major, 122, I V6 bVII vi) · cifraclub chart https://www.cifraclub.com/royksopp/remind-me/zpgkkt.html (Dm7 Am7 E♭maj7 B♭; snippet) · Wikipedia Remind Me https://en.wikipedia.org/wiki/Remind_Me_(R%C3%B6yksopp_song) · Wikipedia Bnyx https://en.wikipedia.org/wiki/Bnyx (Ableton) · Equipboard https://equipboard.com/pros/bnyx (Serum) · SoSouthern / ProducerGrind kit listings (808:kick ratio) · LRCLIB https://lrclib.net/api/get/28081080 (lyric timing, used only for section naming) · Reddit threads 1qqwe0d / 1qqwvuj (listener comparisons) · Deezer previews 109713896 (album), 3120990 (radio edit), 3794993062 (BNYX) for pitch/tempo cross-checks.
