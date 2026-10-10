
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
