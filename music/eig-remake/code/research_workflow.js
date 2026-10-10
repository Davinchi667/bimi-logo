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