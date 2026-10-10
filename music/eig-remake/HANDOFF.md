# EVERYWHERE I GO [REMIND ME] REMAKE — COMPLETE HANDOFF

For a new Claude Code chat with zero memory. Everything below is either measured from David's files, built and verified in code, or quoted from David. Where something is uncertain it says so.

**Repo (everything is here, clone it first):** https://github.com/Davinchi667/bimi-logo/tree/claude/keen-tesla-ingcx0/music/eig-remake

```
git clone -b claude/keen-tesla-ingcx0 https://github.com/Davinchi667/bimi-logo.git
cd bimi-logo/music/eig-remake
```

Layout of that folder:
- `HANDOFF.md` — this document (narrative + all source code pasted in full)
- `code/tools/` — synth.py, seq.py, master.py, measure.py, midiw.py, flpw.py (the toolkit)
- `code/eig/` — build_eig.py (the whole track), compare.py, fit_gains.py, remix.py
- `code/analyse.py` — reference-track analysis; `code/research_workflow.js` — the 50-agent research workflow script
- `research/` — the measured teardown reports: structure.md, harmony.md, sounds.md, bass*.md, drums*.md, BLUEPRINT.md (verified, revised), BLUEPRINT_v1_backup.md
- `deliver/` — `EIG_remake_115bpm_Bmin.mp3` (v1 master), `EIG_stems_part1_drums_bass.zip`, `EIG_stems_part2_music.zip` (19 FLAC stems + reference mix), `EIG_MIDI_parts.zip`
- `midi/` — the 9 MIDI parts unzipped; `out/` — gains.json (fitted stem gains), e808.json (every 808 note), eig_remake.mid (all parts in one file)

**NOT in the repo (David must re-upload to the new chat):** the reference audio. `eig_inst.wav` is the 44.1 kHz conversion of David's upload `BNYX__-_EVERYWHERE_I_GO_REMIND_ME_Audio_Instrumental.mp3` (instrumental, 3:37.3) and `everywhere.wav` is the visualizer rip with Kid Cudi's vocal. Both are needed for mastering (Matchering target) and for the compare scripts. Also not in the repo: the archive.org drum-sample packs (download commands in §2.9).

---

## 0. WHO, RULES, STATUS

David Oshinubi, 20, Ibadan. Judges by ear only; Claude cannot hear, so every judgement must be a measurement against his reference files. He has FL Studio and Logic. HARD RULE: never touch ClickUp (his agency work). Standing rules from his brief: something must change at every 8-bar boundary (his #1 complaint is tracks that sound the same start to finish); no piano- or guitar-led tracks; crest ~12 dB on his own tracks (he called brickwalled masters "too loud too fake") — but note this record itself is brickwalled at crest ~9 and he loves it; short intros; restraint over stacking; only artists he has named; Treblo is Sonauto not Suno.

STATUS: v1 of the remake was delivered (mp3 + stems + MIDI). David's verdict: it is "an exact copy", "the best", with "a few issues" he has NOT yet specified. v2 has not been built. The verified blueprint's refinement list (§5) is queued for v2 together with his issues.

---

## 1. MEASURED FACTS ABOUT THE ORIGINAL (from David's instrumental file)

All numbers below were measured by scripts on `eig_inst.wav` (the instrumental) unless marked [web]. Three independent teardown agents reached the same grid.

### 1.1 Grid
- **Tempo 115.000 BPM** (beat 0.52174 s, bar 2.08696 s, 16th 130.4 ms). An earlier 114.84 reading was frame-quantised and drifts 2.7 ms/bar; do not use it.
- **First downbeat (bar 1) = 0.290 s** in `eig_inst.wav` (drum grid 0.278–0.291 s depending on the method; the first transient is a kick at 0.278 s). Bar n starts at 0.290 + (n−1)·2.08696 s. **104 bars**; the audio hard-cuts at **215.238 s**, 9 ms before the bar-104 line. Bar numbering in this document = structure.md numbering (bar 1 = first downbeat). (sounds.md counts from 0; bass.md puts bar 1 at 0.277 s — same bars.)
- The sampled (tonal) layers sit **+22…+35 ms behind** the drum grid. v1 nudges them +25 ms.
- Full vocal version (`everywhere.wav`) = instrumental delayed 807 samples (+18.3 ms), identical tempo.

### 1.2 Key and chord loop
- **B minor. One 4-bar loop for the whole song, one chord per bar, change on beat 1: | Bm | F#m | C | Em | = i – v – ♭II – iv.** Bar 1 = Bm. The C major chord (Neapolitan) is the colour. Krumhansl on whole-track chroma prefers E minor (0.556 vs 0.442) — same pitch set, tonic label ambiguous; the notes are identical either way.
- Source: Röyksopp "Remind Me" loop Dm7 | Am7 | E♭maj7 | B♭ (≈122.5 BPM) pitched down 3 semitones, with E instead of G under the last chord. Tempo is not a resample (122.5·2^(−3/12) = 103 ≠ 115): the sample is chopped and re-triggered on the grid. [web + measured]
- **808 roots in the drops: B0 (30.7 Hz) / F#1 (46.2) / C1 (32.6) / E1 (41.2).** Build section (bars 17–23) uses an octave up: B1 / F#1 / C2 / E1 at −21 dBFS.

### 1.3 Tuning — the signature
- **The entire sample layer (pad, bass, lead chops) is +14 cents sharp of A440** (E4 = 332.4 Hz, G4 = 395.2 Hz). The kick, 808, SUB layer and the second pad (PAD-2) are at A440 (±5 c). Keep this: the beating between the +14 c sample and the in-tune PAD-2 (0.81 % of frequency: 2 Hz at 250 Hz, 5 Hz at 600 Hz) is the shimmer that defines bars 57–103. Do not tune them together.
- The kick is tuned to **E1 ≈ 40.5 Hz** (−25 c).

### 1.4 Layer inventory (what is actually in the instrumental)
| Layer | Where | Measured character |
|---|---|---|
| SAMPLE-BASS (Röyksopp root, octave 2) | all bars 1–103 | B2 124.5 / F#2 93.3 / C3 131.9 / E2 83.1 Hz (+14 c), −17 dBFS, sustained whole bar, no vibrato, 2nd harmonic −8 dB, side −15 dB |
| SAMPLE-SUB (octave-down of the above) | bars 9–16 | −30 dBFS, +14 c, mono |
| SAMPLE-PAD (the "Remind Me" chord synth) | all bars; ducked −10…−19 dB per bar in 25–40 except C bars and bars 29/37; low-passed in outro | root oct2 + closed triad oct3-4 + triad oct4-5 (top octave 8–12 dB down). **Vibrato sinusoidal 7.667 Hz (= 16th-note rate), ±11.5 cents, coherent across all chord tones**, not on the bass. Spectrum flat 160–640 Hz, −4 dB/oct above ~700 Hz, 95 % of energy below 1.9 kHz. Hard legato chord changes (<20 ms), amplitude constant within a bar. Narrow (side −15 dB), no L/R pitch offset. Voicings (MIDI): Bm 47 | 59 62 66 | 71 74 78; F#m 42 | 57 61 66 | 69 73 (76); C 48 | 55 60 64 | 67 72 76; Em 40 | 55 59 64 | 67 71 76. Inner voice D4→C#4→C4→B3 (chromatic descent). Intro adds a top voice: A4 (Bm, from 16th 15), C#5 (F#m, 16ths 7–8), C5 (C, 16ths 5–11) + E5 at 15, B4 (Em, 16ths 0–9) + E5 at 5 and 14–15. Blueprint revision: voice is closer to a **triangle** (H3 −22, H5 −29) than saw/pulse. |
| SAMPLE-LEAD (chopped-vocal riff) | exposed 25–40 and 73–88; thinned 57–72; variant-b shape 89–96; buried under the pad elsewhere | same +14 c and same 7.6 Hz vibrato as the pad (same source). Attack ≈35 ms, flat sustain ≈250 ms, release ≈50 ms; note length ≈2 16ths; peak −16…−18 dBFS; register C#4–A4. Notes in §1.6. |
| SUB (sustained sub synth) | bars 17–23 only | whole-bar roots B1/F#1/C2/E1 at A440, −21 dBFS, gated to the bar, 20 ms attack, H2 −11 dB |
| KICK | odd-bar beat 1 in 1–8; 1 & 2& from 9; densest in drops | pitch sweep 130 → 41 Hz in ~40 ms (τ ≈ 15 ms) then steady ~40.5 Hz (E1 −25 c); env: peak +9…+22 ms, −6 dB @ 92–105 ms, −20 dB @ 180–200 ms (two-stage); 0 dBFS (into the clipper), mono; click 1–8 kHz −11…−14 dBFS at onset; 120–400 Hz thump in the first 15 ms; **no bright click above 2 kHz** |
| 808 | bars 25–96 only (absent 1–24, 97–104) | sine + strong octave: H2 −5 dB (p10 −13, p90 −2.4), H3 −16…−20, H4 −17…−22, fixed waveform not dynamic saturation; attack = one cycle (13–25 ms); loud hits −3.4…−3.9 dBFS; decay **−29 dB/s for ~0.3 s then −12…−17 dB/s**; retriggered every 3 16ths (391 ms); mono; **no glides**; on hook even bars the 2a note holds at a **−16 dBFS floor** to the bar end |
| GLIDE / verse-2 bass | bars 41–56 | the 808 an octave up playing a melodic 4-bar riff (§1.6), −10…−13 dBFS peaks, harmonics wide (chorus-type, side −10 dB above 90 Hz), fundamental mono, portamento ~150 ms, LPF ~500 Hz; blueprint: 808 oct-up + a ±25 c side-channel double |
| PAD-2 (second chord synth) | bars 57–103 (outro at −5 dB) | A440, **no vibrato**, 3-voice unison ±3.5 c (partials split 2.7–3.9 Hz), brighter than the sample (LPF ~2.5–3.5 kHz), includes 7ths/9ths in oct 5–6 at −12…−17 dB, side −3…−6 dB in oct 5–6, ~−8 dB under the sample pad in 57–95 |
| WIDE layer | ON in 35, 36, 39; 57, 59–60, 63–64, 67–68, 71; all of 73–87; 89–103 | tonal, 500 Hz–4 kHz, side chroma E/F#/B; = PAD-2's oct-5/6 voices through a ±15 c chorus (blueprint) |
| CLAP | beats 2 & 4, bars 1–96, absent on 24, 40, 56, 72, 88 | 4 flams in the first 40 ms (0/10/20/32 ms), peak −9 dBFS, strongest band 1.2–2.5 kHz, body mono; reverb tail T60 ≈ 2.6 s (blueprint: 1.8 s), pre-delay 25–30 ms, tail fully wide, −28 dB under the body |
| HAT closed | 1–96 | peaks 3.4–4.0 kHz and 12.4 kHz, τ ≈ 16 ms (−30 dB @ 54 ms), −19.5 dBFS, **no velocity variation**, +16 ms late, side −15 dB; downbeat variant on odd bars: peaks 6.6–8.5 kHz, τ 25 ms, mono, −20 dBFS |
| HAT-32 ghost layer (blueprint) | 17–39 and 57–96 | 32nd-note ghosts at −35…−49 dBFS (−32…−43 in 73–96), width −15/−10/−6.5 by section |
| PERC-2 (dark wide hat) | 73–96 on 16ths 5–9 and 13–15 | centroid 6.2 kHz, strong 1–3 kHz, τ 25 ms, −26…−29 dBFS, side −7 dB |
| KNOCK | 16th slot 2 of every bar 1–96 (blueprint: ends bar 54) | noisy 300–600 Hz ping ≈350 Hz, attack 28 ms, −16 dBFS, side −9.5 dB |
| REVERSE SWELL | last ~2 s before bars 25, 57, 97 | side 300 Hz–4 kHz rises ≈+12 dB to −14 dBFS, peaks 0.22 s before the downbeat, **gone within 100 ms of the downbeat**, fully decorrelated (L/R corr 0.05–0.37), fixed partials 735/974/1074/1181/1315 Hz (a reused reversed sample, no pitch sweep) |
| Not present | — | no vinyl noise, no delays/echoes, no vocal hums in the instrumental, no filter sweeps inside sections, no crash cymbals, no gated silence before any drop, no sidechain pump (≤3–4 dB) |

### 1.5 Section map and transitions (bar 1 = 0.290 s)
Loudness is K-weighted LUFS per section mean; integrated −10.2 LUFS; sample peak 0 dBFS (brick-wall limited); crest ~9 dB in drops.

| Bars | Time | Section | LUFS | What is there / what changes at its start |
|---|---|---|---|---|
| 1–8 | 0:00.3 | Intro | −13.8 (bar 1 −13.2, i.e. 5.3 dB under the loudest section) | Opens on the downbeat kick from digital silence. Sample pad (+ intro top voice) + sample bass, clap 2&4, hat loop, knock, kick on beat 1 of odd bars only. Even bars have no sub at all. |
| 9–16 | 0:17.0 | A | −12.6 | Additive, no fill: kick on 1 and 2& every bar; SAMPLE-SUB (octave-down bass, −30 dB). Hats unchanged. |
| 17–23 | 0:33.7 | B (build) | −11.8 | SUB layer enters (whole-bar roots, −21 dB); even-bar kicks 1, 2&, 3&, 4e; first wide high element (side above 2 kHz −20 → −17 dB); even bars 1–1.4 dB louder. 7 bars because 24 is the drop-out bar. |
| 24 | 0:48.3 | PRE-DROP | −14.6 | Kick, hats, SUB all OUT; sample keeps playing at normal level; wide tonal reversed swell rises +14 dB over beats 2–4 (centroid does NOT rise — not a bright riser); 808 pickup F#1 on the last 16th at −27 dBFS. No silence gap. |
| 25–39 | 0:50.4 | DROP 1 | −10.2 | **The biggest moment: RMS −17.4 → −10.0 dBFS (+7.4 dB), sub band +40 dB from the last 16th of 24 to the downbeat, the swell is cut dead and width collapses (side/mid −5.2 → −19.8 dB, the mix snaps to near-mono).** 808 continuous (dotted-8th pulse), kick dense, hats unchanged, lead riff exposed, pad ducked except on C bars and bars 29/37. Bar 33: hats add 16ths 8 and 10 on even bars. Bars 35–36, 39: wide layer on. |
| 40 | 1:21.7 | transition | −9.5 | Hats OUT, replaced by a fully decorrelated wash (2–6 kHz side/mid ≈ 0 dB); 808 on every beat + slots 7, 10 (bass.md: q@1 q@5 X@7 X@10 F#1@13); kick roll `XXXX|XXXx|XxXx|XXXX` (blueprint says kick 0/4/8/12 only); no clap; no sweep; no level dip. |
| 41–55 | 1:23.8 | VERSE | −10.4 | Wide layer LEAVES (narrowest point, side above 2 kHz −20…−22 dB); 808 quiet (−16 dB) and replaced by the melodic glide-bass riff an octave up; busiest hats (16th runs into both backbeats); a wide low-mid layer (120–250 Hz +2.8 dB); bar 48: the only mid-section fill (2–6 kHz +7 dB on beat 4, hats `XXX.`). |
| 56 | 1:55.1 | PRE-DROP 2 | −10.4 | Sub pulled ~10 dB (808 notes at −17 dBFS), kick thinned (blueprint: removed), a 120–400 Hz hit on beat 2 (low-passed clap), clap build on 16ths 10–15, **the only true bright riser: centroid 1.1 → 3.0 kHz within the bar, 2k+ and 6k+ bands +14 dB mostly on beats 3–4**; >6 kHz part centred, 2–6 kHz part wide. No level dip. |
| 57–71 | 1:57.2 | DROP 2 | −9.3 | Sub +9.4 dB, RMS +3.4 dB, width −7 dB; 808 plays the full pulse on EVERY bar (the even-bar kick pulse is handed to the 808), kicks only 1 and 2&; **PAD-2 enters (A440)** → 250–500 Hz and 1–2 kHz +2.5 dB; hats `XXxx|X.xx|.xxx|X...`; wide layer toggles every 2 bars (ON 57, 59–60, 63–64, 67–68, 71); knock gone (blueprint). |
| 72 | 2:28.5 | transition | −9.0 | Hats OUT, wash fully wide, 808 dotted-8th roll (16ths 1,5,8,11,14 ≈ q@1 X@4 X@7 X@10 F#1@13), kick roll `XXXX|XXXX|XXXX|Xx..` (blueprint: soft kicks only); no sweep, no dip. Loudest bass bar. |
| 73–87 | 2:30.6 | DROP 3 / PEAK | −8.0 (bar 84 −7.5) | Mids +2 dB everywhere 250 Hz–4 kHz, mid-range layers continuous, wide layer on throughout (side/mid 500 Hz–4 kHz −4…−5 dB, L/R corr 0.88), PERC-2 added, hats add 16th 15 on odd bars, lead riff busiest, 808/kick as drop 1. Entry from 72 is additive (RMS +0.8 dB only, hats back +10 dB). |
| 88 | 3:01.9 | transition | −7.9 | Same recipe as 72. |
| 89–96 | 3:03.9 | POST-DROP | −9.5 | 808 reduced to beats 1–2 (quiet roots, long decay, no floor) with loud E1@3& and F#1@4e on the E bars; kick on 1 and 2 only; every 4th bar (92, 96) restores the full bar; hats, sample, wide layer continue; the empty second half of each bar exposes the wide pad. |
| 97–103 | 3:20.6 | OUTRO | −15.9 | **HARD CUT at the bar line, no riser, no fill, no crash:** 808/kick/hats removed in one step (RMS −7.8 dB). Sample continues at normal level but low-passed ~2 kHz (3 kHz −22 dB, 6 kHz −42 dB rel 1 kHz; ≈24 dB/oct); PAD-2 at −5 dB; bar 103 steps the low-pass down again (centroid 423 Hz). What remains above 2 kHz is mostly side (reverb/width). Ends with a hard digital cut at 215.238 s, no fade. |

Phrase logic: every boundary sits on bar 8n+1 (9, 17, 25, 41, 57, 73, 89, 97); each drop is preceded by a one-bar transition (24, 56) and each big section is separated by a one-bar 808-roll bar (40, 72, 88). Intro = 8 bars before the first pattern change, 24 bars (50 s) before the first full drop.

### 1.6 Note data
**Lead riff** (16th slots, 0 = beat 1; lengths in 16ths; MIDI numbers):
- Bm variant a (bars 25, 33, 73, 81; thinned in 57, 65): slot 6 F#4(66) ×1.6 · slot 9 G4(67) ×1.4 · slot 11 F#4 ×1.6 (73/81 only) · slot 14 E4(64) ×1.5 · tail F#4 ×3 on beat 1 of the next (F#m) bar.
- Bm variant b (bars 29, 37, 77, 85; 61, 69; 93): slot 6 D4(62) ×2.7 · slot 9 C#4(61) ×1.3 · slot 11 D4 ×2.5 · slot 14 A4(69) ×1.7 · tail C#4 ×2.3 on the next bar.
- F#m bar: only the tail note, then rest (the breath in the phrase).
- C bar (27, 31, 35, 39, 75, 79, 83, 87): slot 6 E4 ×2.4 · slot 8 E4 ×1.4 (75/83/87) · slot 9 D4 ×1.3 (27/31/83/87, else E4) · slot 11 E4 ×2.6 (39/75/79/83/87) · slot 14 F#4 ×1.7 · tail G4 on the next (Em) bar.
- Em bar (28, 32, 76, 84, 88): slot 0 G4(67) ×2.2 · slot 5 F#4 ×1.5 (28/32/88) · slot 8 E4 ×3 · slot 12–13 D4 ×2.3.
- Drop 2 (57–72) is sparser (C bar E4 long at slots 5–8 and 11–12; Em bar E4 long slots 0–10). 89–96: variant-b shape in Bm bars, long E4 over C, Em bar straight G4 F#4 E4 D4 on the beats.

**Kid Cudi's hook (from full − instrumental; NOT in the instrumental):** the same riff one octave down, C#3–A3. Bm var a: slot 6 F#3(54) ×2, slot 8 A3(57) ×1, slot 9 G3(55) ×1.8, slot 11 F#3 ×2.2, slot 14 E3(52) ×1.4, held F#3 ×3.5 into the next bar. Bm var b: D3(50) at slots 3 and 5, slot 9 C#3(49), slot 11 D3, slot 14 A3, held C#3 ×4.5. C bar: E3 ×2.5 from slot 0 (some bars), slot 6 E3 ×2.2, slot 9 D3 (27/59/99) else E3, slot 11 E3 ×2.3, slot 14 F#3 ×1.4, G3 into the Em bar. **Em bar (the most consistent line): G3 F#3 E3 D3 on the four beats, each ~3 16ths.** Excess vocal energy: +12…+15 dB in bars 25–40, +5…+12 in 57–72, +10…+15 in 89–97; ≈0 in 1–24 and 73–88. Press describes vocoder/talkbox passages and "choral vocals".

**808 patterns** (slots: 0=1, 4=2, 7=2a, 10=3&, 13=4e):
- Hook 1 (25–40) and bridge (73–88): ODD (Bm/C) bars: quiet root at slot 0 (−11 dBFS) + loud hits at 4, 7, 10, 13 (dotted-8th pulse); kick only on 1 and 2& (slots 0, 6). EVEN (F#m/Em) bars: quiet root at slot 1, loud at 4 and 7, the 7 note held to the bar end at the −16 dB floor; kick takes the pulse (0, 6, 10, 13); on Em bars an F#1 pickup at slot 13 (−8…−13 dBFS). 808 sits BETWEEN the kicks — that alternation is the groove.
- Hook 2 (57–72): loud 4, 7, 10, 13 on EVERY bar; kicks 0, 6 only.
- Verse 2 (41–56) riff, repeating every 4 bars (bar.beat positions; 1e=0.25 etc.): 41 (Bm): B0@1e(0.4 beat) C#2@2(0.5) D2@2a(0.5) C#2@3a(0.3) B0@4e(0.15) B1@4&(0.4) · 42: A1@1e(0.4) F#1@2(0.5) A1@2a(0.5) A1@3a(0.3) E1@4&(0.4) · 43: A1@1e(0.4) E1@1a(short) E2@2(0.4) A1@2a(0.4) E1@3e(0.6) A1@4&(0.4) · 44: E2@1e(0.4) E1@1a(short) rest 2e–2a E2@2a/3(0.4) E1@3e → D1@3& (−200 c step) E1@4 A1@4&.
- Bars 40/72/88: 808 alone-ish: q@1, X@4, X@7, X@10, F#1@13. Bar 24: F#1 pickup at slot 15 (−27 dB). Bar 56: notes at −17 dBFS. Hook 3 (89–96): B bars: B0 from beat 2 (−13); F# bars: F#1 at slots 0 and 4; C bars: C1 at 0; E bars: E1@10 (−5) and F#1@13 (−5).

**Drum grids** (16ths, from sounds.md, bar numbers shifted +1 to this document's numbering): KICK intro `K...|....|....|....` odd bars only; 9–16 `K...|..K.|....|....`; 17–96 `K...|..K.|..k.|.k..` (k on even/alternate bars). CLAP `....|C...|....|C...`. HAT 1–40 `h.hh|(c)..|..hh|(c)..` + downbeat variant; 41–56 `..hh|hhh.|..hh|hhh.`; 57–72 `h.hh|..hh|.hhh|....`; 73–96 `h.hh|.ppp|pphh|.ppp` (p = PERC-2). KNOCK `..x.|....|....|....`. Timing: kick on grid, hat +16 ms, clap onset +12 ms (peak +56 ms because of the 44 ms flam attack), knock +16 ms, sample +25 ms.

### 1.7 Mix/master targets (whole file)
RMS −10.7 dBFS, crest 10.7 dB (drops ~9), centroid 1826 Hz, L/R corr 0.92, side −13.6 dB vs mid; band shares <60 Hz 55.8 % | 60–120 13.4 | 120–400 18.1 | 400–2k 10.8 | 2–6k 1.2 | >6k 0.7. Sub <120 Hz mono everywhere. Width per section (side/mid in 500 Hz–4 kHz): intro −15, A −14, B −14.6, bar 24 −0.2, drop 1 −9, bar 40 −2.5, verse −13.7, bar 56 −3.1, drop 2 −6.2, bar 72 −2.4, drop 3 −4.8, bar 88 −4.5, post −4.1, outro −6.0.

---

## 2. HOW v1 WAS BUILT (every recipe, with numbers)

Everything is in `code/eig/build_eig.py` (sequencing + synthesis + processing), `code/tools/synth.py` (Faust presets, drum synths, sample loader), `code/tools/seq.py` (sequencer), `code/eig/fit_gains.py` + `remix.py` (balance), `code/tools/master.py` (master). Engines: **DawDreamer + Faust** for every synth voice (polyphonic, 44.1 kHz), **Pedalboard** for reverb/chorus/filters, numpy for the 808, kick, clap, hats, knock, perc, swells, riser and wash. No General MIDI anywhere.

### 2.1 Grid and conventions
`Song(115, 104)`; bar index b0(n) = n−1; slot(n, s) = 16th s of bar n; DET = 1.00812 (+14 cents) applied to the sample layers; NUDGE = +25 ms on pad, sample bass, sample sub, lead. Chord of bar n = ['Bm','F#m','C','Em'][(n−1) % 4].

### 2.2 Sample pad (Faust preset `rpad`)
Voice: saw·0.5 + pulse(0.5)·0.5 at freq·DET·vibrato; vibrato = 2^((vibc/1200)·sin(2π·7.667 t)) with vibc = 9.0 (measured result ±11–15 c); 2-pole lowpass at 2600 Hz; ASR envelope attack 15 ms / release 15 ms. Sequenced per BEAT (each beat re-triggers the chord, length 0.985 beat) so the layer "pumps" on every beat like the record. Voicing = VOICE[chord] (triad oct3-4 at velocity 100, triad oct4-5 at velocity 38 ≈ −8 dB). Intro top voice added as in §1.4. Drop-1 duck: velocity 40 (≈ −10 dB) except on C bars and bars 29, 37. Processing: peak-normalised to −14 dBFS, outro mask: 2 kHz 6-pole lowpass (bars 97–102) and 800 Hz 4-pole (bar 103); Pedalboard Chorus rate 0.3 Hz depth 0.12 mix 0.05; stereo width 0.2 (near mono); +4.6 dB on bars 40, 56, 72, 88. Final fitted gain **+8.5 dB**.

### 2.3 Sample bass, sample sub, SUB
numpy `tone_track`: continuous-phase sine + 0.4·octave at root oct 2 (MIDI 47/42/48/40) × DET, −17 dBFS, bars 1–103, width 0.3. Sample sub: sine at root oct 1 × DET, −30 dBFS, bars 9–16. SUB: root oct 1 at A440, −21 dBFS, 0.28 octave mix, 20 ms gate ramps, bars 17–23. Fitted gains: sample bass **−8.5 dB**, sub layers −1.0 dB.

### 2.4 Lead riff (Faust `rlead`)
Same voice as the pad, monophonic, ASR 35 ms / 40 ms, 4-pole lowpass 1600 Hz, DET; notes from §1.6 via `lead_notes(n)` (variants a/b, thin mode 57–72, busy mode 73–88, post mode 89–96). Processing: −15 dBFS peak, +4 dB on bars 25–39, Chorus 0.4 Hz depth 0.1 mix 0.15, width 0.7. Fitted gain **+5.5 dB** (+13 override in an earlier pass; final gains.json says +5.5).

### 2.5 Hum (Cudi line, synthesised — NOT in the instrumental, David wants vocal textures)
Faust `hum`: sine + harmonics (0.45·2f, 0.22·3f, 0.1·4f, 0.05·5f), nasal resonance 250 Hz Q3 blend 0.55, pink-noise breath 0.06 through a 1.2 kHz bandpass, 1-pole lowpass 2.6 kHz, vibrato 5.3 Hz ±0.7 % fading in over 0.35 s, ASR 90 ms / 300 ms, tanh. Notes from §1.6 (`hum_notes(n)`) in bars 25–40, 57–72, 89–103, +12 ms late. Processing: −12 dBFS peak, HPF 200 Hz, LPF 5 kHz, Chorus 0.25 Hz depth 0.15 mix 0.25, Reverb room 0.8 damp 0.6 wet 0.28 dry 0.8, width 1.1; level −15 dB (+2.3 dB in 89–103); fixed fit gain **−6 dB** (deliberately kept — the fit would push it to −24 because the reference has no hum). Outro adds `choirhi` (Faust `choir`, vowel 2 "ooh", attack 0.2 s, release 0.8 s) one octave up at −18 dBFS peak, HPF 300, big reverb, width 1.6, −14 dB.

### 2.6 PAD-2 and the wide layer
Faust `pad2`: per note, left = saw(f/d)·0.7 + saw(f)·0.3, right = saw(f·d)·0.7 + saw(f)·0.3 with d = 2^(3.5/1200); 2-pole LPF 3500 Hz; ASR 30/50 ms; voicing PAD2V (root oct2 + triads + 7th/9th in oct 5–6 at velocity 60). Bars 57–103. Processing: −12 dBFS peak, −9 dB, +41 % in 73–87, +60 % outro, +100 % on bars 40/72/88, outro 2-pole LPF 1500 Hz, width 1.2. Fitted gain **+16 dB**. Wide layer: Faust `choir` (formant "ooh", 3 detuned saws through 3 resonant bandpasses at the vowel formants) on VOICE[chord][1:5] in the WIDE bars (§1.4); HPF 500 / LPF 4500, right channel delayed 13 ms, Reverb room 0.85 wet 0.5 dry 0.6, width 1.7; −16 dB then fixed fit gain −12 dB.

### 2.7 Glide bass (Faust `glide`, 1 voice, bars 41–56)
freq smoothed with τ = 150 ms (portamento); unison saws at ±7 c (L: f/d, R: f·d) through moog_vcf (res 0.2, cutoff 520 Hz), HPF 90 Hz on the wide part + mono sine sub at 0.5, tanh drive 1.6; ASR 20/150 ms. Notes = the verse-2 riff (§1.6, `GL` table); bar 56 only beats 1–2. −8 dBFS peak, fitted +0.5 dB.

### 2.8 808 (numpy `render_808`)
For each note (bar, slot, MIDI, level dB, floor dB): sine f + 2f at −5 dB (+0.3 rad) + 3f at −17 + 4f at −22 + 6f at −24; envelope = 10^(−29·t/20) for t < 0.3 s then continues at −15 dB/s; if a floor is given, env = max(env, floor) until the bar end; 20 ms attack, 10 ms release; the next note cuts the previous (mono). 1-pole LPF 2 kHz, 2-pole HPF 25 Hz. Note list = `E808` built from §1.6 patterns (hook 1/bridge odd/even cells, hook 2 all-bar pulse, transition rolls, bar 24 pickup at −27, bar 56 at −24 with floor −34 and F#1 pickup at −22, hook 3 roots at −8/−9 with floors −12/−13 and E-bar hits at −5). Peak-normalised to **−2.5 dBFS**; fitted gain +1.0 dB. Saved per note in `out/e808.json`.

### 2.9 Drums
- Kick (`kick_e1`): f(t) = 40.6 + 90·e^(−t/0.015) Hz; env hold 1.0 for 80 ms then e^(−(t−0.08)/0.05), 3 ms attack; tanh(1.4); click = 1–8 kHz bandpassed noise τ 6 ms at −13 dB; thump = 120–400 Hz noise τ 8 ms at −5 dB; 0 dBFS; fixed gain 0 (the loudest element, into the clipper).
- Clap: `clap(spread=(0, 10, 20, 32 ms), tone 1900 Hz, bw 1.4, dec 40 ms, rev 0)`; body −9 dBFS; reverb send: right channel delayed 27 ms, HPF 400, LPF 8 k, Pedalboard Reverb room 0.88 damp 0.4 wet 1.0, width 1.8, at −36 dBFS peak. Fitted gain **+4.5 dB**. Beats 2 & 4, +12 ms late, bars 1–96 except 24/40/56/72/88.
- Hat (`hat_eig`): white noise → 2-pole HPF 3 kHz → peaks +6 dB @ 3.7 kHz (Q 2) and +4 dB @ 12.4 kHz (Q 3) → LPF 16 k; τ 16 ms; right channel 3 samples late ×0.97. Downbeat variant: τ 25 ms, peaks 7.5 kHz/9 kHz, on odd-bar slot 0. Base −19.5 dBFS, fitted gain **+17.5 dB** (the base level was far too low). Patterns per section as in §1.6, +16 ms late, velocity 100 (118 on the bar-48 fill and bar 56).
- Knock: 300–600 Hz noise ×0.7 + 350 Hz sine ×0.6, τ 15 ms, 10 ms attack, + 3 kHz+ click at −12 dB; −16 dBFS, fitted **+18.5 dB**; slot 2 every bar except 24, +6 ms late.
- PERC-2: decorrelated L/R 2–8 kHz noise, τ 25 ms, −27 dBFS, fitted +13.5 dB; bars 73–96 (not 88) slots 5,6,7,8,9,13,14,15.
- Tom on bar 56 beat 2: TR-808 BD7575 sample low-passed 500 Hz, −12 dBFS, fixed gain 0.
- Sample packs (not used in the final except the tom; available via `synth.KIT`): archive.org items `drum-machines-collection` (files "Roland TR808.zip", "Roland TR808 hifi set.zip", "EMU SP1200.zip", "EMU SP-12.zip", "Linn Linndrum.zip", "Linn LM-2.zip", "Oberheim DMX.zip", "Roland TR-909.zip"; license not stated), `tempest-808-kick-03` (Tempest 808 Kick 02.wav), public-domain `SC8850DrumSamples`, CC-BY `beckstrom-volca-modular-drum-samples-1`. Download: `curl -L -o X.zip "https://archive.org/download/drum-machines-collection/<url-encoded name>"`, unzip into `samples/<name with underscores>/`.

### 2.10 FX
- Reverse swells into bars 25, 57 (−16), 97 (−16): take 2.5 s of the pad from the target bar, HPF 300 + big reverb (room 0.95, wet 1.0), reverse, keep 2 s, fade-in curve x^2.2, right channel 300–4000 Hz bandpassed and delayed 21 ms (decorrelation), add 15 % of ringing peaks at 735/974/1074/1181/1315 Hz (Q 8), normalise to −14 dBFS, end 12 ms before the downbeat. Fitted gain **+14 dB**.
- Bright riser in bar 56: noise through a bandpass sweeping 1.5 kHz → 9 kHz with curve (t/bar)^2.5, level × p at −17 dBFS; fitted +5.5 dB.
- Wash in bars 40, 72, 88: the wide layer (or pad) HPF 800 / LPF 5000 → reverb wet 1.0 → right channel inverted and delayed 17 ms; −16 dBFS; gain override **+8 dB**.
- Hard cut: everything zeroed from (bar 104 start − 9 ms).

### 2.11 Balance (fit_gains.py → out/gains.json)
Per-stem band energies (6 bands) per section were fitted by coordinate descent so each section's band shares match the reference's (weights: drops ×2, verse/post ×1.5, transition bars ×0.7). Kick fixed at 0; hum −6, choir high 0, wide −12, tom 0 fixed. Result: Kick 0 · 808 +1.0 · Sub layers −1.0 · Glide +0.5 · Clap +4.5 · Hats +17.5 · Knock +18.5 · Perc2 +13.5 · Tom 0 · Sample Bass −8.5 · Sample Pad +8.5 · Lead +5.5 · Pad2 +16.0 · Wide −12 · Hum −6 · Choir High 0 · Swells +14.0 · Riser +5.5 · Wash +0.5 (then overridden to +8). Then section automation on the whole mix (dB): 1–8 −2.5 · 9–16 −1.5 · 17–23 −0.5 · 24 −4.0 · 40 −1.0 · 56 −2.5 · 72 −1.0 · 88 −1.0 · 89–96 −0.5 · 97–103 −6.0. Mix peak-normalised to −1 dBFS, 22 Hz HPF.

### 2.12 Mastering
Matchering (`master.py`, with the resampy shim) target = `out/mix.wav`, reference = `eig_inst.wav` → then tanh soft clip with drive 1.3, peak −0.8 dBFS. Result: RMS −10.0 dBFS, crest 9.2 (record 9–10.7), 0 clipped samples, centroid 1695 Hz (record 1826). Per-section RMS (record / mine): intro −15.8/−14.9 · A −13.2/−12.1 · B −11.9/−10.5 · 24 −18.6/−16.6 · drop 1 −9.6/−9.1 · 40 −8.9/−7.0 · verse −10.6/−9.2 · 56 −13.3/−11.0 · drop 2 −9.5/−8.9 · 72 −10.1/−7.3 · drop 3 −8.8/−8.7 · 88 −9.4/−7.2 · post −10.9/−9.8 · outro −18.6/−17.2. Band shares (whole file, mine vs ref): <60 37.7/55.8 · 60–120 17.5/13.4 · 120–400 33.6/18.1 · 400–2k 9.5/10.8 · 2–6k 1.2/1.2 · >6k 0.5/0.7 — i.e. v1 is still a few points light in the sub and heavy in 120–400 Hz. 8-bar change metric (measure.py): mine [6.6, 1.9, 2.9, 0.9, 3.5, 1.6, 3.4, 0.8, 1.2, 0.7, 2.7, 51.2], record [5.5, 1.4, 3.6, 2.0, 3.4, 1.1, 2.8, 0.6, 3.3, 0.9, 4.2, 30.8] — the record changes by layer swaps, not energy jumps, and v1 matches that profile.

### 2.13 How to rebuild on a Mac
```
brew install fluidsynth sox ffmpeg lame
pip3 install numpy scipy librosa soundfile matchering basic-pitch dawdreamer pedalboard pretty_midi mido
```
Put David's instrumental mp3 somewhere and convert: `ffmpeg -i <mp3> -ar 44100 -ac 2 refs/eig_inst.wav`. Folder expectations: `tools/` (synth.py, seq.py, master.py, measure.py, midiw.py), `eig/` (build_eig.py …), `refs/eig_inst.wav`, `samples/` (only needed for the bar-56 tom; `kit('808_long')` → edit the TOM line to a synthesised tom if the packs are absent). Then from `eig/`: `python3 build_eig.py` (~90 s) → `python3 fit_gains.py '{"15 Hum":-6,"16 Choir High":0,"14 Wide Choir":-12,"09 Tom":0}'` → `python3 remix.py out/stems.npz out/gains.json '{"19 Wash":8}'` → the section-automation + master snippet (in the handoff code section, `master_v1.py`) → `python3 compare.py out/master.wav`. matchering needs the resampy shim that master.py installs. DawDreamer prints "undefined symbol : effect" and "Steal release voice" warnings — harmless.

---


---

## 3. ALL SOURCE CODE, VERBATIM

Every file below is byte-identical to the repo copy. Paths are relative to `music/eig-remake/`. On the original machine the layout was `scratchpad/tools/*.py`, `scratchpad/eig/*.py`, `scratchpad/refs/analyse.py`; `build_eig.py` does `sys.path.insert(0,'../tools')` and expects `../refs/eig_inst.wav` from the `eig/` folder.

### `code/tools/synth.py` — Faust/DawDreamer synth presets, numpy drum synths, sample loader

```python
"""Faust/DawDreamer polyphonic renderer + Pedalboard FX helpers. All audio = float32 (N,2) at 44100."""
import numpy as np, dawdreamer as dd, soundfile as sf
SR=44100
HEAD='import("stdfaust.lib");\nfreq=hslider("freq",220,20,8000,0.01); gain=hslider("gain",0.5,0,1,0.001); gate=button("gate");\neffect=_,_;\n'

def render_faust(dsp, notes, seconds, bpm=None, voices=24, params=None):
    """notes: list of (start_sec_or_beats, dur, midi_pitch, vel 0-127). If bpm given, start/dur are in beats."""
    eng=dd.RenderEngine(SR,256); f=eng.make_faust_processor('v'); f.num_voices=voices
    f.set_dsp_string(HEAD+dsp); f.compile()
    if params:
        names=[d['name'] for d in f.get_parameters_description()]
        for k,v in params.items():
            m=[n for n in names if n.endswith('/'+k)]
            if not m: raise KeyError(f'param {k} not in {names}')
            f.set_parameter(m[0],v)
    sc=(60/bpm) if bpm else 1.0
    for st,du,p,v in notes: f.add_midi_note(int(p),int(max(1,min(127,v))),float(st*sc),float(max(0.01,du*sc)))
    eng.load_graph([(f,[])]); eng.render(float(seconds)); a=eng.get_audio().T.astype(np.float32)
    return a

def render_faust_mono_fx(dsp, seconds, params=None):
    """non-polyphonic generator (noise risers, drones): dsp must define process with no gate."""
    eng=dd.RenderEngine(SR,256); f=eng.make_faust_processor('g'); f.set_dsp_string('import("stdfaust.lib");\n'+dsp); f.compile()
    if params:
        names=[d['name'] for d in f.get_parameters_description()]
        for k,v in params.items(): f.set_parameter([n for n in names if n.endswith('/'+k)][0],v)
    eng.load_graph([(f,[])]); eng.render(float(seconds)); return eng.get_audio().T.astype(np.float32)

# ---------- presets (Faust bodies; HEAD provides freq/gain/gate) ----------
P={}
P['supersaw']='''det=hslider("det",0.12,0,1,0.001); cut=hslider("cut",2200,100,16000,1); res=hslider("res",0.3,0,0.95,0.01);
a=hslider("a",0.02,0.001,4,0.001); d=hslider("d",0.4,0.001,8,0.001); s=hslider("s",0.7,0,1,0.01); r=hslider("r",0.8,0.001,10,0.001);
env=en.adsr(a,d,s,r,gate); fenv=en.adsr(0.005,0.6,0.3,0.5,gate);
sawL=par(i,4,os.sawtooth(freq*(1+det*0.01*(i-1.5)))):>_/4; sawR=par(i,4,os.sawtooth(freq*(1+det*0.011*(i-1.5))*1.0007)):>_/4;
flt(x)=x:ve.moog_vcf_2b(res,min(16000,cut*(0.4+0.6*fenv)+freq*2));
process=(sawL:flt)*env*gain*0.6,(sawR:flt)*env*gain*0.6;'''
P['pad']='''det=hslider("det",0.25,0,1,0.001); cut=hslider("cut",1400,100,16000,1); lfo=0.5+0.5*os.osc(0.11);
a=hslider("a",1.2,0.001,8,0.001); r=hslider("r",2.5,0.001,12,0.001); env=en.asr(a,1,r,gate);
v(k)=os.sawtooth(freq*(1+det*0.01*(k-2)))+0.5*os.triangle(freq*0.5*(1+det*0.005*(k-2)));
L=par(i,5,v(i)):>_/5; R=par(i,5,v(i+0.37)):>_/5;
process=(L:fi.lowpass(2,cut*(0.6+0.5*lfo)))*env*gain*0.5,(R:fi.lowpass(2,cut*(0.6+0.5*(1-lfo))))*env*gain*0.5;'''
P['808']='''punch=hslider("punch",0.5,0,2,0.01); pdec=hslider("pdec",0.012,0.001,0.2,0.001); dec=hslider("dec",2.5,0.1,10,0.01);
drive=hslider("drive",3,1,12,0.1); gl=hslider("glide",0.08,0,1,0.001);
f=freq:si.smooth(ba.tau2pole(gl)); pe=en.ar(0.001,pdec,gate); env=en.asr(0.002,1,dec,gate):min(1);
osc=os.osc(f*(1+punch*pe)); body=osc*env; sat=ma.tanh(body*drive)/ma.tanh(drive);
process=(sat*0.75+body*0.35)*gain<:_,_;'''
P['pluck']='''cut=hslider("cut",3000,100,16000,1); d=hslider("d",0.35,0.01,4,0.001);
env=en.ar(0.002,d,gate); fenv=en.ar(0.001,d*0.6,gate);
x=os.sawtooth(freq)*0.6+os.square(freq*0.5)*0.3; y=x:ve.moog_vcf_2b(0.4,cut*fenv+200);
process=y*env*gain*0.8<:_,_*0.9;'''
P['fm_bell']='''ratio=hslider("ratio",3.5,0.5,12,0.01); idx=hslider("idx",2.5,0,12,0.01); d=hslider("d",1.8,0.05,10,0.01);
env=en.ar(0.002,d,gate); ienv=en.ar(0.001,d*0.4,gate);
mod=os.osc(freq*ratio)*idx*ienv*freq; car=os.osc(freq+mod);
process=car*env*gain*0.7<:_,_;'''
P['choir']='''vow=hslider("vowel",2,0,4,1); a=hslider("a",0.25,0.001,4,0.001); r=hslider("r",1.2,0.001,10,0.001);
env=en.asr(a,1,r,gate); vib=1+0.004*os.osc(5.2+0.3*no.lfnoise(0.5));
src=par(i,3,os.sawtooth(freq*vib*(1+0.003*(i-1)))):>_/3 + 0.08*no.noise:fi.lowpass(1,4000);
f1=ba.selectn(5,vow,730,530,300,400,350); f2=ba.selectn(5,vow,1090,1840,2200,800,600); f3=ba.selectn(5,vow,2440,2480,2900,2600,2700);
form=src<:(fi.resonbp(f1,8,1)+0.5*fi.resonbp(f2,10,1)+0.25*fi.resonbp(f3,12,1)):>_;
process=form*env*gain*0.9<:_,_;'''
P['sine_lead']='''a=hslider("a",0.01,0.001,2,0.001); r=hslider("r",0.3,0.001,5,0.001); env=en.asr(a,1,r,gate);
vib=1+0.006*os.osc(5.5)*en.asr(0.6,1,0.1,gate);
x=os.osc(freq*vib)+0.25*os.osc(freq*2*vib)+0.08*os.osc(freq*3*vib);
process=ma.tanh(x*1.4)*env*gain*0.7<:_,_;'''
P['hum']='''a=hslider("a",0.12,0.001,4,0.001); r=hslider("r",0.35,0.001,10,0.001); breath=hslider("breath",0.05,0,0.5,0.001); nasal=hslider("nasal",0.5,0,1,0.01);
env=en.asr(a,1,r,gate); vibd=en.asr(0.35,1,0.1,gate); vib=1+0.007*vibd*os.osc(5.3+0.4*no.lfnoise(0.7));
f=freq*vib; src=os.osc(f)+0.45*os.osc(2*f)+0.22*os.osc(3*f)+0.1*os.osc(4*f)+0.05*os.osc(5*f);
nas=src:fi.resonbp(250,3,1)*nasal+src*(1-nasal)*0.5; br=no.pink_noise*breath:fi.resonbp(1200,2,1);
out=(nas+br*env):fi.lowpass(1,2600);
process=ma.tanh(out*1.3)*env*gain*0.8<:_,_;'''
# ---- EVERYWHERE I GO voices (from the measured fingerprint) ----
P['rpad']='''det=hslider("det",1.00812,0.9,1.1,0.00001); vibr=hslider("vibr",7.667,0.1,20,0.001); vibc=hslider("vibc",11.5,0,50,0.1);
cut=hslider("cut",1400,100,16000,1); a=hslider("a",0.015,0.001,2,0.001); r=hslider("r",0.015,0.001,5,0.001); top=hslider("top",1,0,1,0.01);
env=en.asr(a,1,r,gate); vib=pow(2,(vibc/1200)*os.osc(vibr));
f=freq*det*vib; v=os.sawtooth(f)*0.5+os.pulsetrain(f,0.5)*0.5;
hi=(freq>1000)*(1-top)+top;   /* top-octave attenuation handled by velocity instead */
y=v:fi.lowpass(2,cut);
process=y*env*gain*0.9<:_,_*0.97;'''
P['rlead']='''det=hslider("det",1.00812,0.9,1.1,0.00001); cut=hslider("cut",1600,100,16000,1);
env=en.asr(0.035,1,0.04,gate); vib=pow(2,(11.5/1200)*os.osc(7.667));
f=freq*det*vib; v=os.sawtooth(f)*0.5+os.pulsetrain(f,0.5)*0.5; y=v:fi.lowpass(4,cut);
process=y*env*gain*0.9<:_,_;'''
P['pad2']='''cut=hslider("cut",3500,100,16000,1); a=hslider("a",0.03,0.001,2,0.001); r=hslider("r",0.05,0.001,5,0.001); spread=hslider("spread",3.5,0,30,0.1);
env=en.asr(a,1,r,gate); d=pow(2,spread/1200);
L=os.sawtooth(freq/d)*0.7+os.sawtooth(freq)*0.3; R=os.sawtooth(freq*d)*0.7+os.sawtooth(freq)*0.3;
process=(L:fi.lowpass(2,cut))*env*gain*0.6,(R:fi.lowpass(2,cut))*env*gain*0.6;'''
P['glide']='''gl=hslider("glide",0.15,0.001,2,0.001); cut=hslider("cut",500,50,8000,1); drive=hslider("drive",1.4,1,6,0.01);
f=freq:si.smooth(ba.tau2pole(gl)); env=en.asr(0.02,1,0.15,gate); d=pow(2,7/1200);
sub=os.osc(f)*0.5; L=(os.sawtooth(f/d)*0.6+os.sawtooth(f)*0.4):ve.moog_vcf_2b(0.2,cut); R=(os.sawtooth(f*d)*0.6+os.sawtooth(f)*0.4):ve.moog_vcf_2b(0.2,cut);
wl=(L:fi.highpass(2,90))*0.8+sub; wr=(R:fi.highpass(2,90))*0.8+sub;
process=ma.tanh(wl*drive)*env*gain*0.8,ma.tanh(wr*drive)*env*gain*0.8;'''
P['noise_riser']='''len=hslider("len",4,0.5,32,0.01); t=ba.time/ma.SR; p=min(1,t/len);
n=no.pink_noise:fi.resonlp(200+p*p*9000,2+p*4,1); process=n*p*p*0.8<:_,_*(1-0.3*os.osc(6));'''

# ---------- Pedalboard FX ----------
from pedalboard import Pedalboard, Reverb, Chorus, Delay, LadderFilter, Distortion, Compressor, HighpassFilter, LowpassFilter, Phaser, Gain, Limiter, PitchShift
def fx(x, *plugins): return Pedalboard(list(plugins))(x.T.astype(np.float32), SR).T
def db(g): return 10**(g/20)
def write(path,x): sf.write(path, x/max(1e-9,np.max(np.abs(x)))*0.9 if np.max(np.abs(x))>1 else x, SR)

# ---------- designed drums (numpy) ----------
def _env(n,a,d,curve=1.0):
    t=np.arange(n)/SR; e=np.exp(-t/d)**curve; e[:int(a*SR)]*=np.linspace(0,1,int(a*SR)) if a>0 else 1; return e
def kick(f0=52,f1=180,pdec=0.035,dec=0.45,click=0.3,drive=2.0,sec=0.9):
    n=int(sec*SR); t=np.arange(n)/SR; f=f0+(f1-f0)*np.exp(-t/pdec); ph=2*np.pi*np.cumsum(f)/SR
    x=np.sin(ph)*np.exp(-t/dec); c=np.random.default_rng(1).normal(0,1,n)*np.exp(-t/0.004)*click
    x=np.tanh((x+c)*drive)/np.tanh(drive); return np.stack([x,x],1).astype(np.float32)
def clap(sec=0.6,tone=1800,bw=1.2,dec=0.11,spread=(0,0.011,0.022,0.031),rev=0.25):
    rng=np.random.default_rng(2); n=int(sec*SR); t=np.arange(n)/SR; out=np.zeros(n)
    import scipy.signal as ss; sos=ss.butter(2,[tone/bw,tone*bw],'band',fs=SR,output='sos')
    for i,s in enumerate(spread):
        nz=ss.sosfilt(sos,rng.normal(0,1,n)); e=np.exp(-(t-s).clip(0)/(dec if i==len(spread)-1 else 0.012))*(t>=s); out+=nz*e
    tail=ss.sosfilt(sos,rng.normal(0,1,n))*np.exp(-t/0.35)*rev; out+=tail
    out/=np.abs(out).max(); L=out; R=np.roll(out,int(0.0004*SR)); return np.stack([L,R],1).astype(np.float32)
def snare(sec=0.5,f0=190,dec=0.12,ndec=0.18,mix=0.5):
    rng=np.random.default_rng(3); n=int(sec*SR); t=np.arange(n)/SR
    body=np.sin(2*np.pi*(f0+60*np.exp(-t/0.02))*t)*np.exp(-t/dec)
    import scipy.signal as ss; nz=ss.sosfilt(ss.butter(2,[1500,9000],'band',fs=SR,output='sos'),rng.normal(0,1,n))*np.exp(-t/ndec)
    x=body*(1-mix)+nz*mix; x=np.tanh(x*2.2)/np.tanh(2.2); return np.stack([x,x],1).astype(np.float32)
def hat(sec=0.25,dec=0.045,open_=False,bright=9000):
    rng=np.random.default_rng(4); n=int(sec*SR); t=np.arange(n)/SR
    # 6 square oscillators at inharmonic ratios (808-style metallic) + noise
    ratios=[1,1.4471,1.6170,1.9265,2.5028,2.6637]; x=sum(np.sign(np.sin(2*np.pi*bright*0.06*r*t+r)) for r in ratios)/6
    import scipy.signal as ss; x=ss.sosfilt(ss.butter(4,bright*0.8,'high',fs=SR,output='sos'),x+0.6*rng.normal(0,1,n))
    x=x*np.exp(-t/(0.28 if open_ else dec)); x/=np.abs(x).max(); return np.stack([x,x*0.95],1).astype(np.float32)
def perc_rim(sec=0.2,f=900,dec=0.03):
    n=int(sec*SR); t=np.arange(n)/SR; x=(np.sin(2*np.pi*f*t)+0.5*np.sin(2*np.pi*f*2.7*t))*np.exp(-t/dec); x/=np.abs(x).max(); return np.stack([x,x],1).astype(np.float32)
def place(canvas,sample,t_sec,gain=1.0,pan=0.0):
    i=max(0,int(t_sec*SR)); j=min(len(canvas),i+len(sample))
    if j<=i: return canvas
    seg=sample[:j-i]*gain
    if pan: a=(pan+1)*np.pi/4; seg=np.stack([seg[:,0]*np.cos(a)*1.414,seg[:,1]*np.sin(a)*1.414],1)
    canvas[i:j]+=seg; return canvas

# ---------- sample loading ----------
SAMPLES='/tmp/claude-0/-home-user-bimi-logo/5f15f32e-d96a-5fe0-b454-eb7800ecdd39/scratchpad/samples'
import librosa as _lr, os as _os
_cache={}
def load_sample(rel,trim_db=60,fade_ms=3,norm=True):
    """rel: path relative to SAMPLES. returns float32 (n,2) at 44100, trimmed, peak-normalised."""
    if rel in _cache: return _cache[rel]
    y,sr=sf.read(_os.path.join(SAMPLES,rel),always_2d=True); y=y.astype(np.float32)
    if sr!=SR: y=_lr.resample(y.T,orig_sr=sr,target_sr=SR).T
    if y.shape[1]==1: y=np.repeat(y,2,1)
    m=np.abs(y).max(1); thr=m.max()*10**(-trim_db/20); idx=np.where(m>thr)[0]
    if len(idx): y=y[max(0,idx[0]-8):idx[-1]+int(0.01*SR)]
    f=int(fade_ms*SR/1000); y[-f:]*=np.linspace(1,0,f)[:,None]
    if norm: y=y/max(1e-9,np.abs(y).max())
    _cache[rel]=y; return y
KIT={ # curated one-shots
 '808_long':'Roland_TR808_hifi_set/Roland TR808 hifi set/BD7575.WAV','808_mid':'Roland_TR808_hifi_set/Roland TR808 hifi set/BD5050.WAV','808_short':'Roland_TR808_hifi_set/Roland TR808 hifi set/BD0075.WAV',
 '808_cp':'Roland_TR808_hifi_set/Roland TR808 hifi set/CP.WAV','808_ch':'Roland_TR808_hifi_set/Roland TR808 hifi set/CH.WAV','808_oh':'Roland_TR808_hifi_set/Roland TR808 hifi set/OH25.WAV','808_oh_long':'Roland_TR808_hifi_set/Roland TR808 hifi set/OH75.WAV',
 '808_rs':'Roland_TR808_hifi_set/Roland TR808 hifi set/RS.WAV','808_sd':'Roland_TR808_hifi_set/Roland TR808 hifi set/SD5050.WAV','808_ma':'Roland_TR808_hifi_set/Roland TR808 hifi set/MA.WAV','808_cb':'Roland_TR808_hifi_set/Roland TR808 hifi set/CB.WAV',
 'sp_snare1':'EMU_SP1200/EMU SP1200/Snare1.wav','sp_snare2':'EMU_SP1200/EMU SP1200/Snare2.wav','sp_kick1':'EMU_SP1200/EMU SP1200/Kick1.wav','sp_clhh':'EMU_SP1200/EMU SP1200/Clhh1.wav','sp_rim':'EMU_SP1200/EMU SP1200/Rim.wav','sp_tamb':'EMU_SP1200/EMU SP1200/Tamb.wav',
 'linn_clap':'Linn_Linndrum/Linn Linndrum/Clap.wav','linn_snare':'Linn_Linndrum/Linn Linndrum/SnareDrum.wav','linn_kick':'Linn_Linndrum/Linn Linndrum/Kick.wav','linn_chh':'Linn_Linndrum/Linn Linndrum/Chh.wav',
 'dmx_clap':'Oberheim_DMX/Oberheim DMX/Clap.wav','dmx_kick':'Oberheim_DMX/Oberheim DMX/Kick02.wav','dmx_snare':'Oberheim_DMX/Oberheim DMX/Snare01.wav',
 'tempest_808':'tempest/tempest_808_kick_02.wav'}
def kit(name): return load_sample(KIT[name])
```

### `code/tools/seq.py` — sequencer: bars/beats, drum grids, swing, ducking, stem export

```python
"""Sequencer helpers: bars/beats -> note lists, drum grids -> hits, swing, ducking, stem export."""
import numpy as np, soundfile as sf, scipy.signal as ss, json, os, random
from synth import SR, render_faust, P, fx, db, place, kick, clap, snare, hat, perc_rim

class Song:
    def __init__(self, bpm, bars, seed=7):
        self.bpm=bpm; self.beat=60/bpm; self.bar=4*self.beat; self.bars=bars
        self.N=int((bars*self.bar+6)*SR); self.layers={}; self.drums={}; self.rng=random.Random(seed)
    def B(self,bar,beat=0.0): return bar*4+beat                      # beats
    def t(self,bar,beat=0.0): return (bar*4+beat)*self.beat            # seconds
    def hum(self,beats,ms=6): return beats+self.rng.uniform(-ms,ms)/1000/self.beat
    def add(self,layer,start_beats,dur_beats,pitch,vel):
        self.layers.setdefault(layer,[]).append((max(0,start_beats),dur_beats,int(pitch),int(vel)))
    def chord(self,layer,bar,beat,dur,pitches,vel,strum=0.0):
        for i,p in enumerate(pitches): self.add(layer,self.B(bar,beat)+i*strum,dur,p,vel)
    def hit(self,drum,bar,beat,vel=100,ms_late=0.0,pan=0.0):
        self.drums.setdefault(drum,[]).append((self.t(bar,beat)+ms_late/1000,vel,pan))
    def grid(self,drum,bar,pattern,vel=100,accent=None,res=16,swing=0.0,ms_late=0.0):
        """pattern: string of 16 (or res) chars per bar, 'X' accent, 'x' normal, '.' rest, 'g' ghost. swing 0-1 on the off-steps."""
        pat=pattern.replace('|','').replace(' ',''); step=4/res
        for i,c in enumerate(pat):
            if c=='.': continue
            b=i*step
            if swing and (i%2==1): b+=swing*step*0.5
            v={'X':vel+ (accent or 20),'x':vel,'g':max(20,vel-45)}[c]
            self.hit(drum,bar,self.hum(b,4),v,ms_late)
    def ducker(self,drum='kick',depth_db=-6,rel=0.18,hold=0.02):
        g=np.ones(self.N); L=int((rel*3+hold)*SR); t=np.arange(L)/SR
        shape=np.where(t<hold,db(depth_db),1-(1-db(depth_db))*np.exp(-(t-hold)/rel*2.5))
        for tt,_,_ in self.drums.get(drum,[]):
            i=max(0,int(tt*SR)); j=min(self.N,i+L)
            if j>i: g[i:j]=np.minimum(g[i:j],shape[:j-i])
        return g[:,None]
    def render_layer(self,layer,preset,params=None,voices=24):
        notes=self.layers.get(layer,[])
        if not notes: return np.zeros((self.N,2),np.float32)
        secs=self.N/SR; a=render_faust(preset,notes,secs,bpm=self.bpm,voices=voices,params=params)
        out=np.zeros((self.N,2),np.float32); n=min(self.N,len(a)); out[:n]=a[:n]; return out
    def render_drum(self,drum,sample,gain=1.0):
        c=np.zeros((self.N,2),np.float32)
        for tt,vel,pan in self.drums.get(drum,[]): place(c,sample,tt,gain*(vel/127)**1.5,pan)
        return c
    def mask(self,ranges_bars,fade=0.03):
        m=np.zeros(self.N)
        for a,b in ranges_bars: m[int(a*self.bar*SR):int(b*self.bar*SR)]=1
        k=np.hanning(max(3,int(fade*SR))); k/=k.sum(); return np.convolve(m,k,'same')[:,None]
    def midi(self,path,prog_map,tempo=None):
        import sys; sys.path.insert(0,os.path.dirname(__file__)); from midiw import MIDI
        m=MIDI()
        for i,(layer,notes) in enumerate(self.layers.items()):
            m.track(layer,notes,prog_map.get(layer,(i%15 if i%15!=9 else 10,0))[0],prog=prog_map.get(layer,(0,0))[1],tempo=self.bpm if i==0 else None)
        dr=[]
        for drum,hits in self.drums.items():
            key={'kick':36,'808':35,'snare':38,'clap':39,'hat':42,'ohat':46,'rim':37,'perc':75}.get(drum,60)
            dr+=[(tt/self.beat,0.25,key,int(v)) for tt,v,_ in hits]
        if dr: m.track('drums',dr,9,tempo=None)
        m.save(path)

def filt(x,fc,kind='low',o=4): return ss.sosfilt(ss.butter(o,fc,kind,fs=SR,output='sos'),x,axis=0)
def sat(x,d): return np.tanh(x*d)/np.tanh(d)
def width(x,w):
    M=(x[:,0]+x[:,1])/2; S=(x[:,0]-x[:,1])/2
    if np.ndim(w): w=w[:,0]
    return np.stack([M+S*w,M-S*w],1)
def pan(x,p):
    a=(p+1)*np.pi/4; m=x.mean(1); return np.stack([m*np.cos(a),m*np.sin(a)],1)*1.414
def reverse_into(x,at_sec,length_sec,curve=1.6):
    """take x after at_sec for length, reverse it, fade in, place so it ends at at_sec"""
    L=int(length_sec*SR); i=int(at_sec*SR); seg=x[i:i+L][::-1]*(np.linspace(0,1,L)[:,None]**curve)
    out=np.zeros_like(x); a=max(0,i-L); out[a:i]+=seg[-(i-a):]; return out
def tapestop(x,start_s,dur_s,curve=1.6):
    i,j=int(start_s*SR),int((start_s+dur_s)*SR); n=j-i; speed=np.linspace(1,0,n)**curve; pos=i+np.cumsum(speed); y=x.copy()
    for c in range(x.shape[1]): y[i:j,c]=np.interp(pos,np.arange(len(x)),x[:,c])*np.linspace(1,0.2,n)
    return y
def export(stems,outdir,mixname='mix.wav',peak_db=-1):
    os.makedirs(outdir,exist_ok=True); tot=sum(stems.values()); sc=db(peak_db)/max(1e-9,np.abs(tot).max())
    sf.write(os.path.join(outdir,mixname),tot*sc,SR,subtype='PCM_24')
    np.savez_compressed(os.path.join(outdir,'stems.npz'),**{k:(v*sc).astype(np.float32) for k,v in stems.items()})
    return tot*sc
```

### `code/tools/master.py` — Matchering + soft clip

```python
"""master(mix_wav, ref_wav, out_wav): Matchering to the reference, then gentle glue + soft clip to a target crest."""
import sys, types, numpy as np, scipy.signal as ss, soundfile as sf, subprocess, os
rp=types.ModuleType('resampy')
def _rs(x,sr_orig,sr_new,axis=-1,**kw):
    if sr_orig==sr_new: return x
    g=np.gcd(int(sr_orig),int(sr_new)); return ss.resample_poly(x,int(sr_new)//g,int(sr_orig)//g,axis=axis)
rp.resample=_rs; sys.modules['resampy']=rp
import matchering as mg
def stats(x):
    m=x.mean(1); r=np.sqrt(np.mean(m**2)); return 20*np.log10(r+1e-9), 20*np.log10(np.max(np.abs(x))/(r+1e-9))
def master(mix_wav, ref_wav, out_wav, crest_target=None, thr=-22, drive=1.5, peak_db=-0.8):
    tmp=out_wav.replace('.wav','_mg.wav')
    mg.process(target=mix_wav, reference=ref_wav, results=[mg.pcm24(tmp)])
    x,sr=sf.read(tmp); rms,crest=stats(x)
    if crest_target and crest>crest_target+0.5:
        for th,dr in [(-20,1.4),(-24,1.8),(-28,2.4),(-32,3.0)]:
            subprocess.run(['sox',tmp,tmp.replace('_mg','_c'),'compand','0.01,0.22',f'6:-80,-80,{th},{th},0,{th/4:.1f}'],check=True)
            y,_=sf.read(tmp.replace('_mg','_c')); y=y/np.max(np.abs(y)); y=np.tanh(y*dr)/np.tanh(dr); y=y/np.max(np.abs(y))*10**(peak_db/20)
            if stats(y)[1]<=crest_target+0.4: x=y; break
            x=y
    else:
        x=x/np.max(np.abs(x))*10**(peak_db/20)
    sf.write(out_wav,x,sr,subtype='PCM_16'); return stats(x)
if __name__=='__main__':
    print(master(*sys.argv[1:4], crest_target=float(sys.argv[4]) if len(sys.argv)>4 else None))
```

### `code/tools/measure.py` — 8-bar change metric

```python
import sys, numpy as np, librosa
def measure(path, bpm=None, bars=8):
    y,sr=librosa.load(path,sr=44100,mono=True)
    rms=np.sqrt(np.mean(y**2)); pk=np.max(np.abs(y))
    S=np.abs(librosa.stft(y,n_fft=4096,hop_length=1024))**2; f=librosa.fft_frequencies(sr=sr,n_fft=4096)
    tot=S.sum()
    if bpm is None: bpm=float(np.atleast_1d(librosa.beat.beat_track(y=y,sr=sr)[0])[0])
    out=dict(len=f"{int(len(y)/sr//60)}:{int(len(y)/sr%60):02d}",bpm=round(bpm,1),
        rms=round(20*np.log10(rms),1),crest=round(20*np.log10(pk/rms),1),
        centroid=int(librosa.feature.spectral_centroid(y=y,sr=sr).mean()),
        sub120=round(100*S[f<120].sum()/tot,1),hi6k=round(100*S[f>6000].sum()/tot,1))
    # per-block features: 5 band energies (dB) + onset density
    blk=int(bars*4*60/bpm*sr/1024); bands=[0,120,400,2000,6000,22050]
    on=librosa.onset.onset_strength(S=librosa.power_to_db(S),sr=sr)
    feats=[]
    for i in range(0,S.shape[1]-blk//2,blk):
        B=S[:,i:i+blk]
        feats.append([10*np.log10(B[(f>=a)&(f<b)].sum()/B.shape[1]+1e-9) for a,b in zip(bands,bands[1:])]+[on[i:i+blk].mean()*3])
    F=np.array(feats); d=np.linalg.norm(np.diff(F,axis=0),axis=1)
    out['boundary_change']=[round(x,1) for x in d]
    out['flat_boundaries']=int((d<2.0).sum())
    out['energy_curve_db']=[round(x,1) for x in F[:,:5].max(axis=1)-F[:,:5].max()]
    return out
if __name__=='__main__':
    for p in sys.argv[1:]: print(p, measure(p))
```

### `code/tools/midiw.py` — MIDI writer (David's, validated)

```python
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
```

### `code/tools/flpw.py` — FL Studio .flp writer (David's, validated; makes empty samplers)

```python
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
```

### `code/eig/build_eig.py` — THE TRACK: sequencing, synthesis, processing, stems

```python
"""EVERYWHERE I GO [REMIND ME] instrumental rebuild. Bar numbers = structure.md (bar 1 = first downbeat). 115 BPM, 104 bars."""
import sys, json, numpy as np, scipy.signal as ss, soundfile as sf
sys.path.insert(0,'../tools')
from seq import *; from synth import *
from pedalboard import Reverb, HighpassFilter, LowpassFilter, Compressor, Gain, Chorus
BPM=115; NB=104; S=Song(BPM,NB,seed=3); N=S.N; BEAT=S.beat; BAR=S.bar
DET=1.00812                      # sample layer +14 cents
NUDGE=0.025                      # sample layer sits ~25 ms behind the drum grid
CH=['Bm','F#m','C','Em']; chord=lambda n: CH[(n-1)%4]
ROOT2={'Bm':47,'F#m':42,'C':48,'Em':40}; ROOT1={'Bm':35,'F#m':30,'C':36,'Em':28}; ROOT0={'Bm':23,'F#m':30,'C':24,'Em':28}
VOICE={'Bm':[59,62,66,71,74,78],'F#m':[57,61,66,69,73,76],'C':[55,60,64,67,72,76],'Em':[55,59,64,67,71,76]}   # triad oct3-4 + triad oct4-5
PAD2V={'Bm':[47,59,62,66,71,74,78,81,85],'F#m':[42,57,61,66,69,73,76],'C':[48,55,60,64,67,72,76,79,86],'Em':[40,55,59,64,67,71,76,78,83]}
ODD=lambda n: n%2==1            # odd bars = Bm/C bars
def b0(n): return n-1           # structure bar -> 0-based bar index
def slot(n,s): return S.B(b0(n),s/4)   # 16th slot -> beats
hz=lambda p:440*2**((p-69)/12)
def sec_mask(ranges,fade=0.02): return S.mask([(b0(a),b0(b)+1) for a,b in ranges],fade)

# ============ SAMPLE LAYERS (+14 c, nudged) ============
def pad_level(n):
    if 25<=n<=40: return 100 if (chord(n)=='C' or n in (29,37)) else 40     # drop 1: pad ducked ~16 dB except C bars / alt Bm
    return 100
for n in range(1,104):
    c=chord(n); L=pad_level(n)
    for bt in range(4):
        for i,p in enumerate(VOICE[c]): S.add('pad',S.B(b0(n),bt)+NUDGE/BEAT,0.985,p,int(L*(1 if i<3 else 0.38)))
    if n<=8:   # intro top voice
        top={'Bm':[(15,69,5)],'F#m':[(7,73,2)],'C':[(5,72,6),(15,76,1)],'Em':[(0,71,9),(5,76,1),(14,76,2)]}[c]
        for s,p,l in top: S.add('pad',slot(n,s)+NUDGE/BEAT,l/4,p,62)
# ---- sample bass (sine + 0.4 octave, continuous), sample sub (9-16) : numpy ----
def tone_track(bars,pitch_of,level_db,oct_mix=0.4,det=DET,gate_bars=None):
    out=np.zeros(N); ph=0.0; ph2=0.0
    for n in bars:
        f=hz(pitch_of(n))*det; i=int((S.t(b0(n))+NUDGE)*SR); j=int((S.t(b0(n)+1)+NUDGE)*SR); t=np.arange(j-i)/SR
        seg=np.sin(ph+2*np.pi*f*t)+oct_mix*np.sin(ph2+2*np.pi*2*f*t); ph=(ph+2*np.pi*f*(j-i)/SR)%(2*np.pi); ph2=(ph2+2*np.pi*2*f*(j-i)/SR)%(2*np.pi)
        if gate_bars: seg*=np.minimum(1,t/0.02)*np.minimum(1,((j-i)-np.arange(j-i))/(0.02*SR))
        out[i:j]+=seg
    x=np.stack([out,out],1)*db(level_db); return x
sbass=tone_track(range(1,104),lambda n:ROOT2[chord(n)],-17)
ssub=tone_track(range(9,17),lambda n:ROOT1[chord(n)],-30,0.0)
subl=tone_track(range(17,24),lambda n:ROOT1[chord(n)],-21,0.28,det=1.0,gate_bars=True)      # SUB layer, A440, whole-bar gated
# ============ LEAD riff (chopped-vocal line) ============
def lead_notes(n):
    c=chord(n); k=n
    busy=73<=n<=88; thin=57<=n<=72; post=89<=n<=96
    if c=='Bm':
        va=(k in (25,33,57,65,73,81))
        if post: va=False
        if thin: return [(6,66,1.6),(14,64,1.5)] if va else [(6,62,2.7),(14,69,1.7)]
        if va: return [(6,66,1.6),(9,67,1.4)]+([(11,66,1.6)] if busy else [])+[(14,64,1.5)]
        return [(6,62,2.7),(9,61,1.3),(11,62,2.5),(14,69,1.7)]
    if c=='F#m':
        prev=chord(n-1); va=((n-1) in (25,33,57,65,73,81))
        return [(0,66 if va else 61,3.0 if va else 2.3)]
    if c=='C':
        if thin: return [(5,64,4),(11,64,2)]
        if post: return [(4,64,8)]
        out=[(6,64,2.4)]
        if n in (75,83,87): out.append((8,64,1.4))
        out.append((9,62,1.3) if n in (27,31,83,87) else (9,64,1.2))
        if n in (39,75,79,83,87): out.append((11,64,2.6))
        out.append((14,66,1.7)); return out
    if c=='Em':
        if thin: return [(0,64,10)]
        if post: return [(0,67,4),(4,66,4),(8,64,4),(12,62,4)]
        out=[(0,67,2.2)]
        if n in (28,32,88): out.append((5,66,1.5))
        out+= [(8,64,3.0),(12,62,2.3)]; return out
for n in list(range(25,41))+list(range(57,73))+list(range(73,89))+list(range(89,97)):
    for s,p,l in lead_notes(n): S.add('lead',slot(n,s)+NUDGE/BEAT,l/4*0.95,p,100)
# ============ HUM (Cudi hook line, C#3-A3) + choir shadow ============
def hum_notes(n):
    c=chord(n)
    if c=='Bm':
        va=n in (25,33,57,65,89,97)
        if va: return [(6,54,2),(8,57,1),(9,55,1.8),(11,54,2.2),(14,52,1.4)]
        return [(3,50,1.5),(5,50,1.2),(9,49,1.1),(11,50,1.5),(14,57,1.6)]
    if c=='F#m': return [(0,54 if (n-1) in (25,33,57,65,89,97) else 49,3.8)]
    if c=='C':
        out=[(0,52,2.5)] if n in (31,39,59,67,71,95,103) else []
        out+=[(6,52,2.2),(9,50,1.1) if n in (27,59,99) else (9,52,1.0),(11,52,2.3),(14,54,1.4)]; return out
    return [(0,55,3.4),(4,54,3),(8,52,3),(12,50,3)]
for n in list(range(25,41))+list(range(57,73))+list(range(89,104)):
    for s,p,l in hum_notes(n):
        S.add('hum',slot(n,s)+0.012/BEAT,l/4*0.95,p,100)
        if n>=97: S.add('choirhi',slot(n,s)+0.02/BEAT,l/4*0.95,p+12,80)
# ============ PAD-2 (A440 unison pad, 57-103) and WIDE choir layer ============
for n in range(57,104):
    for p in PAD2V[chord(n)]: S.add('pad2',S.B(b0(n)),3.98,p,88 if p<76 else 60)
WIDE=set([35,36,39])|{57,59,60,63,64,67,68,71}|set(range(73,88))|set(range(89,104))
for n in sorted(WIDE):
    for p in VOICE[chord(n)][1:5]: S.add('wide',S.B(b0(n)),3.95,p,80)
# ============ GLIDE BASS (41-56) ============
GL=[[(.25,23,.4),(1,37,.5),(1.75,38,.5),(2.75,37,.3),(3.25,23,.15),(3.5,35,.4)],
    [(.25,33,.4),(1,30,.5),(1.75,33,.5),(2.75,33,.3),(3.5,28,.4)],
    [(.25,33,.4),(.75,28,.2),(1,40,.4),(1.75,33,.4),(2.25,28,.6),(3.5,33,.4)],
    [(.25,40,.4),(.75,28,.2),(1.75,40,.4),(2.25,28,.25),(2.5,26,.5),(3,28,.5),(3.5,33,.4)]]
for n in range(41,57):
    for bt,p,l in GL[(n-41)%4]:
        if n==56 and bt>=2: continue
        S.add('glide',S.B(b0(n),bt),l,p,110)
# ============ 808 (numpy, two-stage envelope, H2 -5 dB) ============
E808=[]   # (bar, slot, pitch, level_db, floor_db)
def add808(n,s,p,lv,floor=None): E808.append((n,s,p,lv,floor))
for n in range(25,97):
    c=chord(n); r=ROOT0[c]
    if 41<=n<=55: continue
    if n==56:
        add808(n,1,r,-24); add808(n,4,r,-24); add808(n,7,r,-24,-34); add808(n,13,30,-22); continue
    if n in (40,72,88):
        add808(n,1,r,-13); add808(n,4,r,-4); add808(n,7,r,-4); add808(n,10,r,-4); add808(n,13,30,-5); continue
    if 89<=n<=96:
        if c=='Bm': add808(n,4,r,-8,-13)
        elif c=='F#m': add808(n,0,r,-8); add808(n,4,r,-7,-12)
        elif c=='C': add808(n,0,r,-8,-13)
        else: add808(n,10,r,-5); add808(n,13,30,-5)
        continue
    hook2=57<=n<=71
    if ODD(n) or hook2:
        add808(n,0,r,-11); add808(n,4,r,-4); add808(n,7,r,-4); add808(n,10,r,-4); add808(n,13,r,-4)
        if hook2 and c=='Em': E808[-1]=(n,13,30,-7,None)
    else:
        add808(n,1,r,-11); add808(n,4,r,-4); add808(n,7,r,-4,-16)
        if c=='Em': add808(n,13,30,-10)
add808(24,15,30,-27)
def render_808():
    out=np.zeros(N); ev=sorted(E808,key=lambda e:(e[0],e[1]))
    for k,(n,s,p,lv,floor) in enumerate(ev):
        t0=S.t(b0(n),s/4)
        if k+1<len(ev): t1=S.t(b0(ev[k+1][0]),ev[k+1][1]/4)
        else: t1=t0+2.5
        tend=S.t(b0(n)+1) if floor is not None else t1
        dur=max(0.05,min(tend,t1)-t0); i=int(t0*SR); j=min(N,i+int(dur*SR)); t=np.arange(j-i)/SR; f=hz(p)
        fast=10**(-29*np.minimum(t,0.3)/20); slow=10**(-29*0.3/20)*10**(-15*np.maximum(0,t-0.3)/20); env=np.where(t<0.3,fast,slow)
        if floor is not None: env=np.maximum(env,db(floor-lv))
        env*=np.minimum(1,t/0.02); env[-int(0.01*SR):]*=np.linspace(1,0,int(0.01*SR))
        x=(np.sin(2*np.pi*f*t)+db(-5)*np.sin(2*np.pi*2*f*t+0.3)+db(-17)*np.sin(2*np.pi*3*f*t)+db(-22)*np.sin(2*np.pi*4*f*t)+db(-24)*np.sin(2*np.pi*6*f*t))*env*db(lv)
        out[i:j]+=x
    out=ss.sosfilt(ss.butter(1,2000,'low',fs=SR,output='sos'),out); out=ss.sosfilt(ss.butter(2,25,'high',fs=SR,output='sos'),out)
    return np.stack([out,out],1).astype(np.float32)
# ============ DRUMS ============
def kick_e1(sec=0.32):
    n=int(sec*SR); t=np.arange(n)/SR; f=40.6+90*np.exp(-t/0.015); ph=2*np.pi*np.cumsum(f)/SR
    env=np.where(t<0.08,1.0,np.exp(-(t-0.08)/0.05)); env*=np.minimum(1,t/0.003)
    body=np.tanh(np.sin(ph)*1.4)/np.tanh(1.4)*env
    rng=np.random.default_rng(9); click=ss.sosfilt(ss.butter(2,[1000,8000],'band',fs=SR,output='sos'),rng.normal(0,1,n))*np.exp(-t/0.006)*db(-13)
    thump=ss.sosfilt(ss.butter(2,[120,400],'band',fs=SR,output='sos'),rng.normal(0,1,n))*np.exp(-t/0.008)*db(-5)
    x=body+click+thump; x/=np.abs(x).max(); return np.stack([x,x],1).astype(np.float32)
def hat_eig(tau=0.016,sec=0.12,peak1=3700,peak2=12400,seed=5):
    rng=np.random.default_rng(seed); n=int(sec*SR); t=np.arange(n)/SR; x=rng.normal(0,1,n)
    x=ss.sosfilt(ss.butter(2,3000,'high',fs=SR,output='sos'),x)
    for fc,g,q in ((peak1,6,2),(peak2,4,3)):
        b,a=ss.iirpeak(fc,q,fs=SR); x=x+ (db(g)-1)*ss.lfilter(b,a,x)
    x=ss.sosfilt(ss.butter(4,16000,'low',fs=SR,output='sos'),x)*np.exp(-t/tau)*np.minimum(1,t/0.001); x/=np.abs(x).max()
    return np.stack([x,np.roll(x,3)*0.97],1).astype(np.float32)
def knock(sec=0.12):
    rng=np.random.default_rng(11); n=int(sec*SR); t=np.arange(n)/SR
    nz=ss.sosfilt(ss.butter(2,[300,600],'band',fs=SR,output='sos'),rng.normal(0,1,n)); ping=np.sin(2*np.pi*350*t)
    x=(nz*0.7+ping*0.6)*np.exp(-t/0.015)*np.minimum(1,t/0.01)+ss.sosfilt(ss.butter(2,3000,'high',fs=SR,output='sos'),rng.normal(0,1,n))*np.exp(-t/0.004)*db(-12)
    x/=np.abs(x).max(); return np.stack([x,np.roll(x,int(0.0006*SR))],1).astype(np.float32)
def perc2(sec=0.12):
    rng=np.random.default_rng(13); n=int(sec*SR); t=np.arange(n)/SR; sos=ss.butter(2,[2000,8000],'band',fs=SR,output='sos')
    L=ss.sosfilt(sos,rng.normal(0,1,n))*np.exp(-t/0.025); R=ss.sosfilt(sos,rng.normal(0,1,n))*np.exp(-t/0.025)
    m=max(np.abs(L).max(),np.abs(R).max()); return np.stack([L/m,R/m],1).astype(np.float32)
KICK=kick_e1(); HAT=hat_eig(); HATDB=hat_eig(0.025,0.16,7500,9000,seed=6); CLAP=clap(spread=(0,0.010,0.020,0.032),tone=1900,bw=1.4,dec=0.04,rev=0.0); KNOCK=knock(); PERC2=perc2(); TOM=kit('808_long')
for n in range(1,97):
    c=chord(n); odd=ODD(n); b=b0(n)
    # kick
    if n<=8: ks=[0] if odd else []
    elif n<=16: ks=[0,6]
    elif n<=23: ks=[0,6] if odd else [0,6,10,13]
    elif n==24: ks=[]
    elif n<=39: ks=[0,6] if odd else [0,6,10,13]
    elif n==40: ks=[0,1,2,3,4,5,6,7,8,10,12,13,14,15]
    elif n<=55: ks=[0,6] if odd else [0,6,10,13]
    elif n==56: ks=[7,12]
    elif n<=71: ks=[0,6]
    elif n==72: ks=list(range(12))+[12,13]
    elif n<=87: ks=[0,6] if odd else [0,6,10,13]
    elif n==88: ks=[0,1,2,3,4,5,6,7,8,9,10,13,14,15]
    else: ks=[0,4]
    for s in ks:
        v=118 if s in (0,6,4) or n<25 else (100 if s%2==0 else 88)
        if n in (40,72,88) and s not in (0,4,8,12): v=92
        if n==56: v=84
        S.hit('kick',b,s/4,v)
    # clap
    if n not in (24,40,56,72,88):
        for s in (4,12): S.hit('clap',b,s/4,112,ms_late=12)
    # knock
    if n!=24: S.hit('knock',b,2/4,100,ms_late=6)
    # hats
    if n==24: hs=[]
    elif n<=40 and n!=40: hs=[0,2,3,10,11]+([8] if (n>=33 and not odd) else [])
    elif n==40: hs=[]
    elif n<=55: hs=[2,3,4,5,6,10,11,12,13,14]
    elif n==56: hs=[12,13,14,15]
    elif n<=71: hs=[0,2,3,6,7,9,10,11]
    elif n==72 or n==88: hs=[]
    elif n<=87: hs=[0,2,3,10,11]+([15] if odd else [])
    else: hs=[0,2,3,10,11]+([15] if odd else [])
    for s in hs:
        acc=(n==48 and s in (12,13,14)) or (n==56)
        S.hit('hatdb' if (s==0 and odd) else 'hat',b,s/4,100 if not acc else 118,ms_late=16)
    if 73<=n<=96 and n!=88:
        for s in (5,6,7,8,9,13,14,15): S.hit('perc2',b,s/4,96,ms_late=10)
S.hit('tom',b0(56),1.0,110)
# ============ RENDER ============
print('rendering synth layers...')
pad=S.render_layer('pad',P['rpad'],{'det':DET,'vibc':9.0,'cut':2600},voices=48)
lead=S.render_layer('lead',P['rlead'],{'det':DET,'cut':1600},voices=6)
hum=S.render_layer('hum',P['hum'],{'a':0.09,'r':0.3,'breath':0.06,'nasal':0.55},voices=6)
choirhi=S.render_layer('choirhi',P['choir'],{'vowel':2,'a':0.2,'r':0.8},voices=8)
pad2=S.render_layer('pad2',P['pad2'],{'cut':3500,'spread':3.5},voices=48)
wide=S.render_layer('wide',P['choir'],{'vowel':2,'a':0.35,'r':1.2},voices=24)
glide=S.render_layer('glide',P['glide'],{'glide':0.15,'cut':520,'drive':1.6},voices=1)
b808=render_808()
print('drums...')
K=S.render_drum('kick',KICK); H=S.render_drum('hat',HAT)+S.render_drum('hatdb',HATDB); C=S.render_drum('clap',CLAP); KN=S.render_drum('knock',KNOCK); P2=S.render_drum('perc2',PERC2); T=S.render_drum('tom',TOM)
# ---- processing ----
def norm_peak(x,peak_db): return x/max(1e-9,np.abs(x).max())*db(peak_db)
# pad: narrow, outro low-pass steps, legato
outro=sec_mask([(97,103)],0.05); last=sec_mask([(103,103)],0.05)
pad=norm_peak(pad,-14); pad_lp=filt(filt(pad,2000,'low',4),2000,'low',2); pad_lp2=filt(pad,800,'low',4)
pad=pad*(1-outro)+pad_lp*(outro-last)+pad_lp2*last
pad=width(fx(pad,Chorus(rate_hz=0.3,depth=0.12,mix=0.05)),0.2)*(1+0.58*sec_mask([(40,40),(72,72),(88,88),(56,56)],0.01))
lead=norm_peak(lead,-15)*(1+0.58*sec_mask([(25,39)],0.02)); lead=width(fx(lead,Chorus(rate_hz=0.4,depth=0.1,mix=0.15)),0.7)
sb=sbass; sb=width(sb,0.3)
# pad2: wide unison, level relative to pad; +3 dB in 73-87, -5 dB outro
p2g=db(-9)*(1+0.41*sec_mask([(73,87)])+0.6*outro)
pad2=norm_peak(pad2,-12)*p2g*(1+1.0*sec_mask([(40,40),(72,72),(88,88)],0.01)); pad2=pad2*(1-outro)+filt(pad2,1500,'low',2)*outro; pad2=width(pad2,1.2)
# wide choir layer: hard L/R split + long reverb, HPF 500, LPF 4k
wide=norm_peak(wide,-14); wide=filt(filt(wide,500,'high',2),4500,'low',2)
wide=np.stack([wide[:,0],np.roll(wide[:,1],int(0.013*SR))],1); wide=fx(wide,Reverb(room_size=0.85,damping=0.5,wet_level=0.5,dry_level=0.6,width=1.0)); wide=width(wide,1.7)
# hum: chest vowel, wide-ish, hall
hum=norm_peak(hum,-12); hum=fx(hum,HighpassFilter(200),LowpassFilter(5000),Chorus(rate_hz=0.25,depth=0.15,mix=0.25),Reverb(room_size=0.8,damping=0.6,wet_level=0.28,dry_level=0.8,width=1.0)); hum=width(hum,1.1)
choirhi=norm_peak(choirhi,-18); choirhi=fx(choirhi,HighpassFilter(300),Reverb(room_size=0.9,damping=0.5,wet_level=0.5,dry_level=0.5,width=1.0)); choirhi=width(choirhi,1.6)
glide=norm_peak(glide,-8)
# drums
K=norm_peak(K,0.0); b808=norm_peak(b808,-2.5)
H=norm_peak(H,-19.5); KN=norm_peak(KN,-16); P2=norm_peak(P2,-27); T=norm_peak(filt(T,500,'low',2),-12)
Cbody=norm_peak(C,-9); Cver=fx(np.stack([Cbody[:,0],np.roll(Cbody[:,1],int(0.027*SR))],1),HighpassFilter(400),LowpassFilter(8000),Reverb(room_size=0.88,damping=0.4,wet_level=1.0,dry_level=0.0,width=1.0))
Cver=width(norm_peak(Cver,-36),1.8); C=Cbody+Cver
# ---- FX: reverse swells into 25, 57, 97 ; bright riser in 56 ; washes in 40,72,88 ----
def swell_into(bar,length=2.0,gain_db=-14):
    src=wide if np.abs(wide).max()>0 else pad
    seg=fx(pad[int(S.t(b0(bar))*SR):int(S.t(b0(bar))*SR)+int(2.5*SR)],HighpassFilter(300),Reverb(room_size=0.95,damping=0.3,wet_level=1.0,dry_level=0.0,width=1.0))
    seg=seg[::-1][:int(length*SR)]; L=len(seg); env=(np.linspace(0,1,L)**2.2)[:,None]; seg=seg*env
    rng=np.random.default_rng(bar); seg=np.stack([seg[:,0],ss.sosfilt(ss.butter(2,[300,4000],'band',fs=SR,output='sos'),np.roll(seg[:,1],int(0.021*SR)))],1)   # decorrelate
    for fc in (735,974,1074,1181,1315):
        b,a=ss.iirpeak(fc,8,fs=SR); seg+=0.15*ss.lfilter(b,a,seg)
    out=np.zeros((N,2)); e=int(S.t(b0(bar))*SR)-int(0.012*SR); out[e-L:e]+=seg/max(1e-9,np.abs(seg).max())*db(gain_db); return out
SW=swell_into(25)+swell_into(57,2.0,-16)+swell_into(97,2.0,-16)
def riser(bar):
    L=int(BAR*SR); rng=np.random.default_rng(56); t=np.arange(L)/SR; p=(t/BAR)**2.5
    n=rng.normal(0,1,L); out=np.zeros(L)
    for k in range(0,L,2048):
        fc=1500*(9000/1500)**p[min(L-1,k)]; out[k:k+2048]=ss.sosfilt(ss.butter(2,[fc/1.6,min(16000,fc*1.6)],'band',fs=SR,output='sos'),n[max(0,k-4096):k+2048])[-(min(L,k+2048)-k):]
    out=out*p*db(-17); z=np.zeros((N,2)); i=int(S.t(b0(bar))*SR); z[i:i+L]=np.stack([out,out],1); return z
RS=riser(56)
def wash(bar):
    i=int(S.t(b0(bar))*SR); L=int(BAR*SR); seg=wide[i:i+L] if np.abs(wide[i:i+L]).max()>0 else pad[i:i+L]
    seg=fx(seg,HighpassFilter(800),LowpassFilter(5000),Reverb(room_size=0.9,damping=0.3,wet_level=1.0,dry_level=0.0,width=1.0))
    seg=np.stack([seg[:,0],-np.roll(seg[:,1],int(0.017*SR))],1); z=np.zeros((N,2)); z[i:i+L]=seg/max(1e-9,np.abs(seg).max())*db(-16); return z
WA=wash(40)+wash(72)+wash(88)
# ---- section gains ----
hum_g=db(-15)*(1+0.3*sec_mask([(89,103)]))
STEMS={'01 Kick':K,'02 808':b808,'03 Sub layers':ssub+subl,'04 Glide Bass':glide,'05 Clap':C,'06 Hats':H,'07 Knock':KN,'08 Perc2':P2,'09 Tom':T,
 '10 Sample Bass':sb,'11 Sample Pad':pad,'12 Lead Riff':lead,'13 Pad2':pad2,'14 Wide Choir':wide*db(-16),'15 Hum':hum*hum_g,'16 Choir High':choirhi*db(-14),
 '17 Swells':SW,'18 Riser':RS,'19 Wash':WA}
mix=sum(STEMS.values())
# hard cut 9 ms before bar 104 line
cut=int((S.t(b0(104))-0.009)*SR); mix[cut:]=0
for k in STEMS: STEMS[k][cut:]=0
mix=filt(mix,22,'high',2)
sc=db(-1)/np.abs(mix).max(); mix*=sc
os.makedirs('out',exist_ok=True); sf.write('out/mix.wav',mix,SR,subtype='PCM_24')
np.savez_compressed('out/stems.npz',**{k:(v*sc).astype(np.float32) for k,v in STEMS.items()})
S.midi('out/eig_remake.mid',{'pad':(0,89),'lead':(1,54),'hum':(2,53),'pad2':(3,90),'wide':(4,52),'glide':(5,38)})
json.dump({'E808':E808},open('out/e808.json','w'))
print('done', mix.shape, 'peak %.2f'%np.abs(mix).max())
```

### `code/eig/fit_gains.py` — fits per-stem gains to the reference band balance per section

```python
import numpy as np, soundfile as sf, librosa, json
SR=44100; BAR=4*60/115
SECS=[('intro',1,8),('A',9,16),('B',17,23),('pre24',24,24),('drop1',25,39),('t40',40,40),('verse',41,55),('pre56',56,56),('drop2',57,71),('t72',72,72),('drop3',73,87),('t88',88,88),('post',89,96),('outro',97,103)]
W={'intro':1,'A':1,'B':1,'pre24':0.7,'drop1':2,'t40':0.7,'verse':1.5,'pre56':0.7,'drop2':2,'t72':0.7,'drop3':2,'t88':0.7,'post':1.5,'outro':1}
bands=[(0,60),(60,120),(120,400),(400,2000),(2000,6000),(6000,22050)]
def bandE(x,t0,a,b):
    i=int((t0+(a-1)*BAR)*SR); j=int((t0+b*BAR)*SR); m=x[i:j].mean(1).astype(np.float32)
    S=np.abs(librosa.stft(m,n_fft=4096,hop_length=2048))**2; f=librosa.fft_frequencies(sr=SR,n_fft=4096)
    return np.array([S[(f>=lo)&(f<hi)].sum() for lo,hi in bands])
ref,_=sf.read('../refs/eig_inst.wav'); T={n:bandE(ref,0.290,a,b) for n,a,b in SECS}; T={n:v/v.sum() for n,v in T.items()}
st=np.load('out/stems.npz'); names=list(st.files)
E={n:{k:bandE(st[k],0.0,a,b) for k in names} for n,a,b in SECS}
import sys
FIX=json.loads(sys.argv[1]) if len(sys.argv)>1 else {}
g={k:0.0 for k in names}; g.update(FIX); fixed={'01 Kick'}|set(FIX)
def err(g):
    e=0
    for n,_,_ in SECS:
        tot=sum(E[n][k]*10**(g[k]/10) for k in names); sh=tot/max(tot.sum(),1e-12)
        e+=W[n]*np.sum((np.log(sh+0.002)-np.log(T[n]+0.002))**2)
    return e
print('start err %.2f'%err(g))
for it in range(8):
    for k in names:
        if k in fixed: continue
        best=None
        for d in np.arange(-24,24.5,0.5):
            gg=dict(g); gg[k]=d; e=err(gg)
            if best is None or e<best[0]: best=(e,d)
        g[k]=best[1]
    print('iter',it,'err %.2f'%err(g))
for k in names: print(f'  {k:16s} {g[k]:+5.1f} dB')
json.dump(g,open('out/gains.json','w'))
print('\nresulting shares vs target (sub/60-120/120-400/400-2k/2-6k/>6k):')
for n,_,_ in SECS:
    tot=sum(E[n][k]*10**(g[k]/10) for k in names); sh=100*tot/tot.sum(); print(f'  {n:6s} mine',np.round(sh,1),' ref',np.round(100*T[n],1))
```

### `code/eig/remix.py` — applies gains.json (+ overrides) to stems.npz

```python
import numpy as np, soundfile as sf, json, sys, scipy.signal as ss
SR=44100; db=lambda g:10**(g/20)
st=np.load(sys.argv[1]); g=json.load(open(sys.argv[2])); over=json.loads(sys.argv[3]) if len(sys.argv)>3 else {}
g.update(over)
stems={k:st[k]*db(g.get(k,0.0)) for k in st.files}
mix=sum(stems.values()); mix=ss.sosfilt(ss.butter(2,22,'high',fs=SR,output='sos'),mix,axis=0)
sc=db(-1)/np.abs(mix).max(); mix*=sc
sf.write('out/mix.wav',mix,SR,subtype='PCM_24'); np.savez_compressed('out/stems_mixed.npz',**{k:(v*sc).astype(np.float32) for k,v in stems.items()})
print('remixed; peak-normalised by %.1f dB'%(20*np.log10(sc)))
```

### `code/eig/master_v1.py` — section automation + matchering + clip (the exact v1 final stage)

```python
"""v1 final stage: section automation on the fitted stems, matchering vs the reference, soft clip. Run from eig/ after fit_gains.py."""
import numpy as np, soundfile as sf, json, scipy.signal as ss, sys
sys.path.insert(0,'../tools'); from master import master, stats
SR=44100; BAR=4*60/115; db=lambda g:10**(g/20)
st=np.load('out/stems.npz'); g=json.load(open('out/gains.json')); g.update({"19 Wash":8})
stems={k:st[k]*db(g.get(k,0.0)) for k in st.files}; N=len(next(iter(stems.values())))
def mask(ranges,fade=0.04):
    m=np.zeros(N)
    for a,b in ranges: m[int((a-1)*BAR*SR):int(b*BAR*SR)]=1
    k=np.hanning(int(fade*SR)); k/=k.sum(); return np.convolve(m,k,'same')[:,None]
auto=np.zeros((N,1))
for rng_,gdb in [((1,8),-2.5),((9,16),-1.5),((17,23),-0.5),((24,24),-4.0),((40,40),-1.0),((56,56),-2.5),((72,72),-1.0),((88,88),-1.0),((89,96),-0.5),((97,103),-6.0)]:
    auto+=mask([rng_])*gdb
gl=10**(auto/20)
mix=sum(stems.values())*gl; mix=ss.sosfilt(ss.butter(2,22,'high',fs=SR,output='sos'),mix,axis=0); sc=db(-1)/np.abs(mix).max(); mix*=sc
sf.write('out/mix.wav',mix,SR,subtype='PCM_24'); np.savez_compressed('out/stems_mixed.npz',**{k:(v*gl*sc).astype(np.float32) for k,v in stems.items()})
print('matchering only:',master('out/mix.wav','../refs/eig_inst.wav','out/master.wav',crest_target=None))
x,sr=sf.read('out/master.wav')
for drive in (1.3,1.6,2.0):
    y=np.tanh(x*drive)/np.tanh(drive); y=y/np.max(np.abs(y))*db(-0.8); r,c=stats(y); print(f'clip drive {drive}: rms {r:.1f} crest {c:.1f}')
    if c<=10.2: sf.write('out/master.wav',y,sr,subtype='PCM_16'); break
```

### `code/eig/compare.py` — per-section comparison vs the reference

```python
import numpy as np, soundfile as sf, scipy.signal as ss, librosa, sys
SR=44100; BAR=4*60/115
SECS=[('intro',1,8),('A',9,16),('B',17,23),('pre24',24,24),('drop1',25,39),('t40',40,40),('verse',41,55),('pre56',56,56),('drop2',57,71),('t72',72,72),('drop3',73,87),('t88',88,88),('post',89,96),('outro',97,103)]
def load(p,t0):
    x,sr=sf.read(p); return x, t0
def feats(x,t0,a,b):
    i=int((t0+(a-1)*BAR)*SR); j=int((t0+b*BAR)*SR); seg=x[i:j]; m=seg.mean(1); s=(seg[:,0]-seg[:,1])/2
    S=np.abs(librosa.stft(m.astype(np.float32),n_fft=4096,hop_length=1024))**2; f=librosa.fft_frequencies(sr=SR,n_fft=4096); tot=S.sum()
    bands=[(0,60),(60,120),(120,400),(400,2000),(2000,6000),(6000,22050)]
    bs=[100*S[(f>=lo)&(f<hi)].sum()/tot for lo,hi in bands]
    sm=ss.sosfilt(ss.butter(4,[500,4000],'band',fs=SR,output='sos'),s); mm=ss.sosfilt(ss.butter(4,[500,4000],'band',fs=SR,output='sos'),m)
    return dict(rms=20*np.log10(np.sqrt(np.mean(m**2))+1e-9), bands=bs, cent=librosa.feature.spectral_centroid(y=m.astype(np.float32),sr=SR).mean(), sm=20*np.log10(np.sqrt(np.mean(sm**2))/(np.sqrt(np.mean(mm**2))+1e-9)+1e-9), corr=np.corrcoef(seg[:,0],seg[:,1])[0,1])
ref,rt=load('../refs/eig_inst.wav',0.290); mine,mt=load(sys.argv[1] if len(sys.argv)>1 else 'out/mix.wav',0.0)
# global
for name,x,t0 in (('REF',ref,rt),('MINE',mine,mt)):
    F=feats(x,t0,1,103); print(f"{name:5s} rms {F['rms']:6.1f}  bands <60 {F['bands'][0]:4.1f} 60-120 {F['bands'][1]:4.1f} 120-400 {F['bands'][2]:4.1f} 400-2k {F['bands'][3]:4.1f} 2-6k {F['bands'][4]:4.1f} >6k {F['bands'][5]:4.1f}  cent {F['cent']:5.0f}  S/M(0.5-4k) {F['sm']:5.1f}  corr {F['corr']:.2f}")
print(f"\n{'sec':6s} {'rmsR':>6s} {'rmsM':>6s} | {'<60R':>5s} {'<60M':>5s} | {'midR':>5s} {'midM':>5s} | {'hiR':>5s} {'hiM':>5s} | {'centR':>5s} {'centM':>5s} | {'S/M R':>5s} {'S/M M':>5s}")
for n,a,b in SECS:
    R=feats(ref,rt,a,b); M=feats(mine,mt,a,b)
    print(f"{n:6s} {R['rms']:6.1f} {M['rms']:6.1f} | {R['bands'][0]:5.1f} {M['bands'][0]:5.1f} | {R['bands'][3]:5.1f} {M['bands'][3]:5.1f} | {R['bands'][4]+R['bands'][5]:5.1f} {M['bands'][4]+M['bands'][5]:5.1f} | {R['cent']:5.0f} {M['cent']:5.0f} | {R['sm']:5.1f} {M['sm']:5.1f}")
```

### `code/analyse.py` — reference-track analysis (tempo, key, bands, width, 8-bar map)

```python
import numpy as np, librosa, soundfile as sf, sys
KEYS=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
maj=np.array([6.35,2.23,3.48,2.33,4.38,4.09,2.52,5.19,2.39,3.66,2.29,2.88]); mnr=np.array([6.33,2.68,3.52,5.38,2.60,3.53,2.54,4.75,3.98,2.69,3.34,3.17])
for p in sys.argv[1:]:
    x,sr=sf.read(p); L,R=x[:,0],x[:,1]; m=(L+R)/2; s=(L-R)/2
    y=m.astype(np.float32)
    tempo=float(np.atleast_1d(librosa.beat.beat_track(y=y,sr=sr)[0])[0])
    H,P=librosa.effects.hpss(y)
    chroma=librosa.feature.chroma_cqt(y=H,sr=sr).mean(1)
    sc=[(np.corrcoef(np.roll(maj,k),chroma)[0,1],KEYS[k]+' maj') for k in range(12)]+[(np.corrcoef(np.roll(mnr,k),chroma)[0,1],KEYS[k]+' min') for k in range(12)]
    sc.sort(reverse=True)
    rms=np.sqrt(np.mean(m**2)); pk=np.max(np.abs(x))
    S=np.abs(librosa.stft(y,n_fft=4096,hop_length=1024))**2; f=librosa.fft_frequencies(sr=sr,n_fft=4096); tot=S.sum()
    band=lambda a,b: round(100*S[(f>=a)&(f<b)].sum()/tot,1)
    side_ratio=20*np.log10(np.sqrt(np.mean(s**2))/np.sqrt(np.mean(m**2)))
    corr=np.corrcoef(L,R)[0,1]
    # side-channel spectrum: where the wide stuff lives
    Ss=np.abs(librosa.stft(s.astype(np.float32),n_fft=4096,hop_length=1024))**2
    sband=lambda a,b: round(10*np.log10(Ss[(f>=a)&(f<b)].sum()/max(S[(f>=a)&(f<b)].sum(),1e-12)),1)
    print(f"\n== {p}  {int(len(m)/sr//60)}:{len(m)/sr%60:04.1f}")
    print(f" tempo {tempo:.1f} | key {sc[0][1]} ({sc[0][0]:.2f}) / {sc[1][1]} ({sc[1][0]:.2f})")
    print(f" RMS {20*np.log10(rms):.1f} dB | crest {20*np.log10(pk/rms):.1f} | centroid {librosa.feature.spectral_centroid(y=y,sr=sr).mean():.0f} Hz")
    print(f" bands %: <60 {band(0,60)} | 60-120 {band(60,120)} | 120-400 {band(120,400)} | 400-2k {band(400,2000)} | 2-6k {band(2000,6000)} | >6k {band(6000,22050)}")
    print(f" harmonic/percussive: {20*np.log10(np.sqrt(np.mean(H**2))):.1f} / {20*np.log10(np.sqrt(np.mean(P**2))):.1f} dB")
    print(f" stereo: L/R corr {corr:.3f} | side vs mid {side_ratio:.1f} dB | side-vs-mid by band: <120 {sband(0,120)} | 120-400 {sband(120,400)} | 400-2k {sband(400,2000)} | 2-6k {sband(2000,6000)} | >6k {sband(6000,22050)}")
    # 8-bar section map
    blk=8*4*60/tempo; n=int(len(m)/sr/blk)+1
    rows=[]
    for i in range(n):
        a,b=int(i*blk*sr),min(len(m),int((i+1)*blk*sr))
        if b-a<sr: break
        seg=m[a:b]; sseg=s[a:b]; Hs=H[a:b]; Ps=P[a:b]
        Sg=np.abs(librosa.stft(seg.astype(np.float32),n_fft=2048,hop_length=1024))**2; ff=librosa.fft_frequencies(sr=sr,n_fft=2048)
        rows.append((i*blk, 20*np.log10(np.sqrt(np.mean(seg**2))+1e-9), 20*np.log10(np.sqrt(np.mean(sseg**2))/(np.sqrt(np.mean(seg**2))+1e-9)+1e-9),
            20*np.log10(np.sqrt(np.mean(Hs**2))+1e-9),20*np.log10(np.sqrt(np.mean(Ps**2))+1e-9),
            100*Sg[ff<120].sum()/Sg.sum(), librosa.feature.spectral_centroid(y=seg.astype(np.float32),sr=sr).mean()))
    print("  t      rms   side  harm  perc  sub%  centroid")
    for t,r,sd,h,pp,sb,c in rows: print(f"  {int(t//60)}:{t%60:04.1f} {r:6.1f} {sd:5.1f} {h:6.1f} {pp:6.1f} {sb:5.1f} {c:6.0f}")
```

### `out/gains.json` — fitted stem gains (dB)

```json
{"01 Kick": 0.0, "02 808": 1.0, "03 Sub layers": -1.0, "04 Glide Bass": 0.5, "05 Clap": 4.5, "06 Hats": 17.5, "07 Knock": 18.5, "08 Perc2": 13.5, "09 Tom": 0, "10 Sample Bass": -8.5, "11 Sample Pad": 8.5, "12 Lead Riff": 5.5, "13 Pad2": 16.0, "14 Wide Choir": -12, "15 Hum": -6, "16 Choir High": 0, "17 Swells": 14.0, "18 Riser": 5.5, "19 Wash": 0.5}
```

### `code/research_workflow.js` — the 50-agent research/teardown/verify/blueprint workflow (Claude Code Workflow tool script)

```javascript
export const meta = {
  name: 'eig-remake-research',
  description: 'Full research + audio teardown of BNYX/Kid Cudi/Röyksopp EVERYWHERE I GO [REMIND ME] into a verified production blueprint',
  phases: [
    { title: 'Research', detail: 'web research + audio teardown, 10 agents in parallel' },
    { title: 'Consolidate', detail: 'pick the contested facts' },
    { title: 'Verify', detail: '3 lenses per fact, adversarial' },
    { title: 'Blueprint', detail: 'synthesis + completeness critic' },
  ],
}
const A = args
const CTX = `
CONTEXT: We are rebuilding, as an INSTRUMENTAL (no vocals, no singing), the track "EVERYWHERE I GO [REMIND ME]" by BNYX with Kid Cudi, which samples/interpolates Röyksopp "Remind Me". The user LOVES everything about this track. We cannot hear; every judgement must be a measurement or a cited source.
FILES (absolute paths, all 44.1 kHz stereo wav):
- Instrumental: ${A.inst}
- Full version with Kid Cudi vocals (visualizer rip): ${A.full}
- basic-pitch transcription of the instrumental (may still be rendering; wait/poll up to 10 min if missing): ${A.bpMidi}
- Existing analysis script (band energies, stereo, 8-bar map): python3 ${A.analyse} <wav>
MEASURED SO FAR: tempo 114.84 BPM (beat period 0.5224 s), first downbeat at 0.813 s, 1 bar = 2.0897 s, ~104 bars, length 3:37. Key reads E minor from chroma (E min 0.56 vs E maj 0.31) — treat as provisional. RMS -10.7 dB, crest 10.7 dB, centroid 1839 Hz, 56% of energy below 60 Hz.
TOOLS: python3 with numpy, scipy, librosa, soundfile, pretty_midi, mido; sox, ffmpeg, basic-pitch CLI. Write any files you create under ${A.outDir} (mkdir -p it). Do not touch anything else.
RULES: Never reproduce lyrics beyond a 3-word fragment. songbpm/tunebat/musicstax resell Spotify analysis and often report the relative major or double/half tempo — cross-check against human sources (Hooktheory, chord sheets, interviews, Song Exploder, WhoSampled, Genius annotations). Mark every claim with a confidence and a source URL or "measured".`

const FINDINGS = { type: 'object', properties: {
  summary: { type: 'string' },
  facts: { type: 'array', items: { type: 'object', properties: { claim: { type: 'string' }, confidence: { type: 'string' }, source: { type: 'string' } }, required: ['claim', 'confidence', 'source'] } },
  details: { type: 'string', description: 'Full report in markdown, as long as needed' },
}, required: ['summary', 'facts', 'details'] }

const RESEARCH = [
  { key: 'credits', prompt: `Research how "EVERYWHERE I GO [REMIND ME]" (BNYX, Kid Cudi, Röyksopp) was made: release date and project, producer/writer credits, how BNYX got and flipped the Röyksopp sample (pitch/tempo change, chopped vs interpolated vs re-sung), any interviews, tweets, Instagram/TikTok clips, beat-breakdown or "how it was made" videos, remake tutorials, Reddit/forum threads (r/trapproduction, r/makinghiphop), Genius annotations, WhoSampled entry. What does BNYX say about this beat? What plugins/sounds are named anywhere? Under 900 words, cite everything.` },
  { key: 'royksopp', prompt: `Research the ORIGINAL Röyksopp "Remind Me" (Melody A.M., 2001/2002; vocals by Erlend Øye) in production detail: tempo, key and mode (cross-check!), chord progression and the exact main riff/arpeggio notes if any transcription exists (Hooktheory, chord sheets, synth-cover tutorials), which synths/sounds made it (interviews with Svein Berge / Torbjørn Brundtland, Sound on Sound, gear lists), the vocal melody shape (describe in intervals/contour, no lyrics), the structure. Also note the "Someone Else's Radio Remix" since that version is the famous one — which version did BNYX sample? Under 900 words, cite everything.` },
  { key: 'bnyx', prompt: `Research producer BNYX (Ben Saidu): his production style and techniques in detail — drum programming habits (kick/808 relationship, hat patterns, clap/snare choices, swing), 808 design, how he treats samples and synths (his work with Yeat, Drake "IDGAF"/"Rich Baby Daddy", Kid Cudi INSANO era, Travis Scott), his DAW and named plugins/kits, his mixing tendencies (loudness, darkness, width), any interviews, masterclass/Beat Academy content, Twitter threads, YouTube "BNYX type beat" tutorial findings that name his specific sounds. Under 900 words, cite everything.` },
  { key: 'musicdata', prompt: `Collect hard musical data for "EVERYWHERE I GO [REMIND ME]" (BNYX / Kid Cudi): tempo, key and mode, chord progression, melody notes if transcribed anywhere, from as many independent sources as possible (Hooktheory, chord sites like Ultimate Guitar/Chordify, Musicstax/tunebat/songbpm WITH the caveat they are algorithmic, piano tutorials, remake videos, Reddit). Report each source's claim separately and then your resolved answer with reasoning. Our own measurement says 114.84 BPM and E minor-ish. Under 700 words, cite everything.` },
  { key: 'arrangement', prompt: `Reconstruct the ARRANGEMENT of "EVERYWHERE I GO [REMIND ME]" (BNYX / Kid Cudi): section map with timestamps (intro, hook, verses, post-hook, bridge, outro), where Cudi hums vs sings vs raps, what the beat does at each transition (drum drop-outs, filter sweeps, 808 switches, sample muted/unmuted, risers), and the "drop" moment(s). Use lyric sites with timestamps (LRCLIB API: https://lrclib.net/api/search?q=...), Genius structure annotations, reviews, YouTube comments pointing to timestamps, Reddit. ALSO describe Kid Cudi's signature hums (the "hmm hmm" melodic humming) in this song: where they appear, register, contour, how they interact with the sample — because we must imitate them with synth/vocal textures. Under 800 words, cite everything.` },
]

const AUDIO = { type: 'object', properties: {
  report: { type: 'string', description: 'markdown report, as long as needed' },
  facts: { type: 'array', items: { type: 'object', properties: { claim: { type: 'string' }, confidence: { type: 'string' }, source: { type: 'string' } }, required: ['claim', 'confidence', 'source'] } },
  files: { type: 'array', items: { type: 'string' } },
}, required: ['report', 'facts'] }

const AUDIOTASKS = [
  { key: 'drums', prompt: `AUDIO TASK — DRUMS. Using the instrumental wav and the measured grid (114.84 BPM, downbeat 0.813 s), extract the drum programming at 32nd-note resolution for EVERY distinct section (find sections by listening-by-measurement: 4-bar block energy changes). Separate: kick (<80 Hz transient onsets, distinguish from the sustained 808 by envelope), 808 (sustained sub, note onsets), snare/clap (1.5-5 kHz transients, on which beats; is it beat 3 halftime or 2&4?), hats (>8 kHz; 8ths/16ths/triplets/rolls, velocity accents, open hats), any percussion (rim, shaker, perc one-shots). Also measure swing/microtiming (how late are the hats/snares vs grid, in ms), hat velocity patterns, where rolls/fills occur relative to section boundaries, and whether the kick pattern changes between sections. Produce text grids like "K: X..x|....|X...|..x." per bar and a per-section summary. Write the grids to ${A.outDir}/drums.md.` },
  { key: 'bass', prompt: `AUDIO TASK — 808/BASS. From the instrumental wav (grid: 114.84 BPM, downbeat 0.813 s) and the basic-pitch MIDI, transcribe the 808/bass line: note names and octave, onset beat positions per bar, note lengths, glides/slides (detect pitch movement within a note via YIN/pyin on a <150 Hz band-passed signal), whether the 808 follows the kick or sits between kicks, how it changes per section, its tuning relative to the chords, and its timbre (fundamental vs 2nd/3rd harmonic ratio in dB, attack time, decay time, whether it is distorted — measure THD-ish via harmonic ratio). Also measure the kick's fundamental frequency and decay. Output a bar-by-bar table for the first 48 bars plus a section summary. Write to ${A.outDir}/bass.md.` },
  { key: 'harmony', prompt: `AUDIO TASK — HARMONY & MELODY. From the instrumental wav (grid: 114.84 BPM, downbeat 0.813 s): (1) compute chroma per bar and per 2-bar block (use harmonic component via HPSS, CQT chroma), fit chords (major/minor triads + 7ths) per bar and derive the chord loop and key/mode with evidence (Krumhansl profiles on the harmonic part, and the bass note from the 808 transcription). (2) From the basic-pitch MIDI (${A.bpMidi}) extract the lead/sample melody: pitch classes, register, the recurring riff with beat positions and lengths, rhythm of the riff (which 16ths), and whether it is one repeated loop or varies between sections. (3) Compare against the FULL version wav (${A.full}) to isolate Kid Cudi's vocal/hum melody: subtract or compare spectra (same tempo? align by cross-correlation of the first 10 s), and transcribe the hum contour (register, intervals, rhythm) where it is clearest. Write to ${A.outDir}/harmony.md with note tables.` },
  { key: 'structure', prompt: `AUDIO TASK — STRUCTURE & TRANSITIONS. From the instrumental wav (grid: 114.84 BPM, downbeat 0.813 s): build a 1-bar-resolution layer map. For each bar compute band RMS (sub <60, 60-120, 120-400, 400-2k, 2-6k, >6k), onset density in each band, stereo side/mid ratio, and spectral centroid. Detect every section boundary (bars where ≥2 features jump), and for each boundary describe WHAT changes: what enters (new band energy appears), what leaves, fills/risers in the preceding bar (rising centroid, reversed-envelope shapes), silences/gaps (sub-100 ms dropouts), filter sweeps (centroid ramps over several bars), and the biggest single "drop" moment. Also measure intro length, how loud bar 1 is relative to the loudest section (dB), and the loudness contour per section. Produce a table of sections with bar numbers, timestamps, and what changes, and write it to ${A.outDir}/structure.md.` },
  { key: 'sounds', prompt: `AUDIO TASK — SOUND DESIGN FINGERPRINT. From the instrumental wav (grid: 114.84 BPM, downbeat 0.813 s), identify each distinct sound layer (the Röyksopp-derived sample/pad/lead, any added synth, the 808, kick, snare/clap, hats, vocal textures/hums if present in the instrumental, FX like risers/reverses/vinyl noise) and for EACH give a reproducible synthesis recipe: spectral shape (where its energy sits, harmonic vs noisy, spectral flatness), amplitude envelope (attack/decay/sustain/release in ms, measured on isolated segments), pitch modulation (vibrato/wobble rate and depth in cents, measured via pyin on a filtered band), stereo width per layer (side/mid in its band), reverb tail length (decay time measured on a note ending or on the gap before a section), delay echoes (autocorrelation of the envelope for repeats at musical intervals), saturation (harmonic series growth), and any filter movement. Use HPSS, band isolation, and spectral peak tracking. Express recipes as: oscillator type(s) + detune + filter type/cutoff/resonance + envelope + effects chain with parameters, suitable for implementing in Faust or pedalboard. Write to ${A.outDir}/sounds.md.` },
]

phase('Research')
log('10 agents: 5 web research + 5 audio teardown')
const all = await parallel([
  ...RESEARCH.map(r => () => agent(CTX + '\n\n' + r.prompt, { label: `research:${r.key}`, phase: 'Research', schema: FINDINGS }).then(x => x && ({ key: r.key, ...x }))),
  ...AUDIOTASKS.map(t => () => agent(CTX + '\n\n' + t.prompt, { label: `audio:${t.key}`, phase: 'Research', schema: AUDIO }).then(x => x && ({ key: t.key, summary: x.report.slice(0, 400), facts: x.facts, details: x.report, files: x.files || [] }))),
])
const results = all.filter(Boolean)
log(`${results.length}/10 agents returned`)
const allFacts = results.flatMap(r => r.facts.map(f => ({ ...f, from: r.key })))

phase('Consolidate')
const CLAIMS = { type: 'object', properties: { claims: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, claim: { type: 'string' }, why: { type: 'string' } }, required: ['id', 'claim', 'why'] } } }, required: ['claims'] }
const picked = await agent(CTX + `\n\nBelow are ${allFacts.length} facts collected by 10 agents (web research and audio measurement). Pick the 8-12 claims that matter MOST for rebuilding the track and that are contested, surprising, or load-bearing (tempo, key/mode, chord loop, the sample's identity and how it was pitched/tempo-shifted, section boundaries, drum pattern essentials, 808 pattern, the main sound's synthesis, Cudi hum behaviour). Where two agents disagree, state the claim as one side so it can be refuted. Return them as short testable statements.\n\nFACTS:\n` + JSON.stringify(allFacts, null, 1), { label: 'pick-claims', phase: 'Consolidate', schema: CLAIMS })
const claims = (picked && picked.claims) || []
log(`${claims.length} claims to verify`)

phase('Verify')
const VERDICT = { type: 'object', properties: { refuted: { type: 'boolean' }, evidence: { type: 'string' }, corrected: { type: 'string' } }, required: ['refuted', 'evidence'] }
const LENSES = [
  'WEB lens: find independent sources (not the one already cited) that confirm or contradict it. Default refuted=true if you cannot find independent support.',
  'MEASUREMENT lens: test it directly on the wav files with python (librosa/scipy). Refute if the measurement disagrees. Show the numbers.',
  'MUSIC-THEORY lens: check internal consistency with the other established facts (key vs chords vs bass notes vs sample key; tempo vs section lengths in bars; structure vs timestamps). Refute if inconsistent.',
]
const verified = await pipeline(claims,
  c => parallel(LENSES.map((lens, i) => () => agent(CTX + `\n\nCLAIM TO TEST: "${c.claim}"\nWhy it matters: ${c.why}\nYour job is to try to REFUTE it. ${lens}\nIf refuted, give the corrected claim in 'corrected'.`, { label: `verify:${c.id}:${['web','measure','theory'][i]}`, phase: 'Verify', schema: VERDICT })))
    .then(vs => { const v = vs.filter(Boolean); return { ...c, votes: v, survives: v.filter(x => !x.refuted).length >= 2, corrections: v.filter(x => x.refuted && x.corrected).map(x => x.corrected) } }))
const vres = verified.filter(Boolean)
log(`verified: ${vres.filter(v => v.survives).length} survive, ${vres.filter(v => !v.survives).length} refuted`)

phase('Blueprint')
const BLUEPRINT = { type: 'object', properties: {
  path: { type: 'string' }, summary: { type: 'string' }, tempo: { type: 'number' }, key: { type: 'string' },
  sections: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, startBar: { type: 'integer' }, bars: { type: 'integer' }, time: { type: 'string' }, layers: { type: 'string' }, change: { type: 'string' } }, required: ['name', 'startBar', 'bars', 'layers', 'change'] } },
}, required: ['path', 'summary', 'sections'] }
const dossier = results.map(r => `\n\n# ${r.key}\n${r.details}`).join('') + `\n\n# VERIFICATION RESULTS\n` + JSON.stringify(vres.map(v => ({ claim: v.claim, survives: v.survives, corrections: v.corrections, evidence: v.votes.map(x => x.evidence.slice(0, 300)) })), null, 1)
const bp = await agent(CTX + `\n\nYou are the lead producer. Using the full dossier below (10 reports + verification verdicts; prefer verified facts, use corrections where a claim was refuted), write the PRODUCTION BLUEPRINT for rebuilding this track as an instrumental with synthesized sounds (Faust/DawDreamer synthesis, pedalboard effects, FluidSynth GM only as a last resort). It must be complete enough that a programmer who cannot hear can build it:
1. Tempo, key, chord loop with voicings (MIDI note numbers), bass/808 line bar by bar (note, beat position, length, glides).
2. Full arrangement bar by bar: every section with start bar, length, timestamp, which layers play, and exactly what changes at each boundary (the user's #1 rule: something must change at every 8-bar boundary; and the drop must be more than 'drums come in').
3. Every sound layer with a synthesis recipe: oscillators, detune, filter, envelope (ms), modulation, effects chain with parameters, level in dB relative to the 808, stereo width, register (MIDI note range).
4. The lead/sample riff as MIDI notes with beat positions and lengths; the Kid Cudi hum lines as a plan for synthesized vocal-like textures (formant/vowel synthesis, choir-like layering, pitch contour) — no words.
5. Drum programming per section as grids + velocities + microtiming.
6. Mix/master targets measured from the reference (band shares, crest, centroid, width per band, loudness contour per section).
7. A list of 'what makes this track feel the way it does' — the 5-8 decisive moves, ranked, each tied to evidence.
Write it to ${A.outDir}/BLUEPRINT.md and return the path, a summary, and the section table.\n\nDOSSIER:` + dossier, { label: 'blueprint', phase: 'Blueprint', schema: BLUEPRINT, effort: 'high' })

const GAPS = { type: 'object', properties: { gaps: { type: 'array', items: { type: 'string' } }, unsupported: { type: 'array', items: { type: 'string' } } }, required: ['gaps', 'unsupported'] }
const critic = bp && await agent(CTX + `\n\nRead ${bp.path}. You are a completeness critic. A programmer who cannot hear must rebuild the track from this file alone. List (a) GAPS: every concrete thing missing or too vague to implement (e.g. a sound with no envelope numbers, a section with no bar count, a riff with no note positions, a drum section with no grid, a transition with no mechanism), and (b) UNSUPPORTED: claims in the blueprint that contradict the dossier's verification results or have no evidence. Be exhaustive.\n\nDOSSIER for cross-checking:` + dossier, { label: 'critic', phase: 'Blueprint', schema: GAPS })
let fixed = null
if (critic && (critic.gaps.length || critic.unsupported.length)) {
  log(`critic found ${critic.gaps.length} gaps, ${critic.unsupported.length} unsupported claims — filling`)
  fixed = await agent(CTX + `\n\nRevise ${bp.path} IN PLACE to fix every item below. For gaps, measure on the wav files or derive from the dossier; where truly unknowable, state the best-guess value explicitly marked [ASSUMED]. For unsupported claims, correct or remove them. Keep everything else. Return the path, a summary of what you changed, and the final section table.\nGAPS:\n- ` + critic.gaps.join('\n- ') + `\nUNSUPPORTED:\n- ` + critic.unsupported.join('\n- ') + `\n\nDOSSIER:` + dossier, { label: 'fill-gaps', phase: 'Blueprint', schema: BLUEPRINT, effort: 'high' })
}
return { blueprint: fixed || bp, critic, verified: vres.map(v => ({ claim: v.claim, survives: v.survives, corrections: v.corrections })), reports: results.map(r => ({ key: r.key, summary: r.summary, files: r.files || [] })) }
```

---

## 4. FILES (all paths relative to `music/eig-remake/` in the repo)
- `deliver/EIG_remake_115bpm_Bmin.mp3` — v1 master, 3:43, 320 kbps (David has heard this one).
- `deliver/EIG_stems_part1_drums_bass.zip` — `00 Reference mix.mp3`, `01 Kick`, `02 808`, `03 Sub layers`, `04 Glide Bass`, `05 Clap`, `06 Hats`, `07 Knock`, `08 Perc2`, `09 Tom` (FLAC, 16-bit, all start at 0:00, tempo 115, bar 1 at 0:00).
- `deliver/EIG_stems_part2_music.zip` — `10 Sample Bass`, `11 Sample Pad`, `12 Lead Riff`, `13 Pad2`, `14 Wide Choir`, `15 Hum`, `16 Choir High`, `17 Swells`, `18 Riser`, `19 Wash`.
- `deliver/EIG_MIDI_parts.zip` and `midi/*.mid` — pad, lead, hum, choirhi, pad2, wide, glide, drums (GM drum keys: 36 kick, 38 snare, 39 clap, 42 hat, 46 open hat, 37 rim, 75 perc), 808 (velocity 110+level for loud, 70 for quiet).
- `out/gains.json`, `out/e808.json`, `out/eig_remake.mid`.
- `research/*.md` — the teardown reports (structure, harmony, sounds, bass, drums) and the verified `BLUEPRINT.md` (92 KB, the most complete spec; `BLUEPRINT_v1_backup.md` is the pre-revision version).
- `code/` — everything in §3.
- On the original cloud machine only (not pushed, regenerable): `out/mix.wav`, `out/master.wav`, `out/stems.npz`, `stems_flac/`, the `samples/` packs, `refs/*.wav`.

Earlier tracks from this project (not part of the EIG remake, all rejected or superseded): a Phantogram-style 96 BPM D minor sketch (David: intro and drop "fking amazing", rest "ordinary"), an "ethereal" v2 of it (rejected: "the same exact thing"), a Kept (AGTHA remix)-style 126 BPM D minor track (David: "love it not bad i guess you have a limit to simple sounds"), an OUT WEST-style 140 BPM G minor track (rejected: "genuinely not feeling it… generic"). Those used General MIDI sounds, which is why they sounded cheap; the EIG remake was the first with real synthesis.

---

## 5. v2 REFINEMENT LIST (from the verified BLUEPRINT.md; none applied yet)
1. Pad and lead voices → triangle-based (H3 −22, H5 −29) instead of saw/pulse; riff voice = triangle + octave sine through a 700 Hz LPF.
2. Add the HAT-32 ghost layer (32nd-note ghost hats, −35…−49 dBFS, bars 17–39 and 57–96, per-section widths) — "part of why the record feels alive while looping".
3. Bar 56: remove the kick entirely (not thin it), low-passed clap on beat 2 (400 Hz LPF, −6 dBFS), clap build `c@10 X@12 9@13 X@14 X@15`, riser routed through the wide chorus.
4. Bars 72 and 88: soft kicks only, no kick roll; the 808 roll (q@1 X@4 X@7 X@10 F#1@13) carries the bar. Bar 40: kick 0/4/8/12 + 808 q@1 q@5 X@7 X@10 F#1@13.
5. 808-HARM: a parallel saturation send producing the measured 0-cent H3–H10 series (fills the mids in the drops; v1 only partly does this) and an 808-HOLD sustain layer for the even-bar −16 dBFS floor.
6. Verse-2 bass = the 808 an octave up with a ±25 c side-channel double (V2-SIDE), grace-note retriggers, 160 Hz LPF variant — instead of the separate saw glide synth.
7. Hook-1 pad duck as a measured per-bar gain lane (−10…−19 dB), not a re-voicing; PAD-2 cutoff 2.5 kHz [assumed]; WIDE bus = PAD-2 oct-5/6 voices via ±15 c chorus with a per-bar send lane from bar 35; a CHORAL layer (riff +7/+9 dB + PAD-2 upper voices) with a half-bar amplitude lane in 73–97.
8. Hook-3 kick on slots 0/4; hook-2 clap on every bar (57: beat 4 only); knock ends at bar 54; clap plate T60 1.8 s (measurement conflict with 2.6 s noted).
9. Outro low-pass as three steps: bar 97 sweep 3.5 k → 2 k at 18 dB/oct, 98–102 static 2 kHz, bar 103 +12 dB/oct at 1 kHz.
10. Balance leftovers from v1: sub share still ~15 points under the record in the drops, 120–400 Hz ~10 points over; transition bars 40/72/88 ~2 dB hot.
Plus David's own "few issues" once he states them.

---

## 6. WHAT DAVID SAID (verbatim) AND HIS RULES

About this track:
- "lets try to remake this please its so so so fking peak bro i love eveyrhting about it" / "bro give yourself the prompt to do the full every isngle thingr esaearch and nmake this pls"
- After v1: "STILL HERE? CUS THIS WAS ABAISLULET THE BEST BRO UT WAS GOOD ONLY A FEW ISSUES I DOUBT YOU CAN DOO BUT THIS IS AN EXACT COPY BRO" — the issues were not specified. He also continued in a different Claude session during a usage limit; that session's work is unknown to me.

Rules he stated in this project (verbatim where possible):
- On earlier rejected tracks: "I'll be honest with you, bro. I'm genuinely not feeling it… it's just generic. Like, any man can just come up and make this." / "the main thing here is the sound should not be simple. You are used to simple sound. It should not be simple. And if you're trying to, don't confuse simple for noisy, for confusing. It should flow, it should transition, it shouldn't be the same from the beginning to the end. The hook should be crazy, the drop should be crazy, the drop shouldn't be the generic drum drop. It could be other instruments, could be ad libs, it could be backing vocals." / "I don't really care how long this takes, but just try to take as much time as possible and create peak." / "forget FL Studio for now. If it's limiting you from creating something… Create first, then we will talk." / "you're not even using voice. So that means like half of the work is done."
- "no vocals. No, no one should be singing. Yeah, just ad libs, like backing layers, backing vocals."
- "love it not bad i guess you have a limit to simple sounds" (on the Kept-style track).
- "Never touch ClickUp." (repeated; from his brief: "this is the tool were using do notttt do anythingon clikcup tahst my work")
- From his brief (standing): "all sound the same from the beginning to end" is his #1 complaint — something must change at every 8-bar boundary; "everything just full of piano" — always avoid piano and guitar; "too slow"; "too loud too fake" — crest 12 dB on his own tracks; "the intro was too long"; "some parts were just overdoing it" — fewer elements; "use only artist and producer names from now on"; "do not use artists i did not say".
- He wanted FL Studio import instructions earlier (stems at bar 1, tempo set first, MIDI per part); he cannot be given a working .flp with sounds (the writer makes empty samplers).

---

## 7. UNFINISHED / UNCERTAIN
- David's "few issues" with v1 are unknown. Ask him first, with timestamps.
- Whatever the other Claude session did during the usage limit is unknown; a handoff-extraction prompt was given to David for it.
- v2 refinements (§5) not built.
- Hum/choir layers are synthetic; the record's chopped vocal and Cudi's hum are real voices — the biggest remaining gap in realism. If David supplies any vocal take he likes, chop it into these layers.
- Uncertain measurements: tonic label (B minor vs E minor — notes identical); which Röyksopp version/section was sampled; lead-note lengths (±0.5 16th); exact hum rhythm (from a spectral-subtraction residual); clap reverb T60 (2.6 vs 1.8 s); whether bar 40/72/88 have a kick roll or soft kicks (structure.md vs blueprint); bar 104 content (assumed empty).
- Not done: a `.flp` with real sounds; Matchering was run against the instrumental only (never against the vocal version).
- Sample-pack licence: the archive.org "drum-machines-collection" has no stated licence; only the bar-56 tom uses it.
