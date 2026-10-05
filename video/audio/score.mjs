// Generates the soundtrack from code. Every hit is placed from ../cues.js.
// Deep house, 120 BPM, F minor. Output: audio/score_raw.wav (float32, 48 kHz stereo).
import fs from 'node:fs';
import vm from 'node:vm';
const ctx = {}; vm.runInNewContext(fs.readFileSync(new URL('../cues.js', import.meta.url), 'utf8'), { globalThis: ctx });
const C = ctx.CUES;

const SR = 48000, DUR = C.duration, N = Math.round(DUR * SR);
const TAU = Math.PI * 2;
const bus = () => [new Float32Array(N), new Float32Array(N)];
const drums = bus(), bass = bus(), music = bus(), sfx = bus(), verbSend = bus(), lead = bus();

// seeded noise
let seed = 0x9e3779b9;
const rnd = () => { seed |= 0; seed = (seed + 0x6D2B79F5) | 0; let t = Math.imul(seed ^ (seed >>> 15), 1 | seed); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296 * 2 - 1; };

// RBJ biquad
class BQ {
  constructor(type, f, q = 0.707) { this.type = type; this.x1 = this.x2 = this.y1 = this.y2 = 0; this.set(f, q); }
  set(f, q = this.q) {
    this.q = q; f = Math.min(Math.max(f, 10), SR * 0.45);
    const w = TAU * f / SR, c = Math.cos(w), s = Math.sin(w), a = s / (2 * q);
    let b0, b1, b2; const a0 = 1 + a, a1 = -2 * c, a2 = 1 - a;
    if (this.type === 'lp') { b0 = (1 - c) / 2; b1 = 1 - c; b2 = b0; }
    else if (this.type === 'hp') { b0 = (1 + c) / 2; b1 = -(1 + c); b2 = b0; }
    else { b0 = a; b1 = 0; b2 = -a; } // bp
    this.b0 = b0 / a0; this.b1 = b1 / a0; this.b2 = b2 / a0; this.a1 = a1 / a0; this.a2 = a2 / a0;
  }
  p(x) { const y = this.b0 * x + this.b1 * this.x1 + this.b2 * this.x2 - this.a1 * this.y1 - this.a2 * this.y2; this.x2 = this.x1; this.x1 = x; this.y2 = this.y1; this.y1 = y; return y; }
}
const at = (t) => Math.round(t * SR);
const add = (b, i, v, pan = 0) => { if (i < 0 || i >= N) return; b[0][i] += v * Math.cos((pan + 1) * Math.PI / 4) * 1.414; b[1][i] += v * Math.sin((pan + 1) * Math.PI / 4) * 1.414; };
const mtof = (m) => 440 * Math.pow(2, (m - 69) / 12);

// ── arrangement helpers ──────────────────────────────────────────
const BEAT = C.beat, BAR = C.bar;
const S = C.sections;
const inS = (t, s) => t >= S[s][0] - 1e-6 && t < S[s][1] - 1e-6;
const grooveOn = (t) => (t >= C.drop1 && t < C.tapeStop) || (t >= C.drop2 && t < 36);
// chord progression, one bar each, 4-bar loop (F minor)
const CH = [
  { root: 29, v: [56, 60, 63, 67, 70] },  // Fm9   (F1 | Ab C Eb G Bb)
  { root: 37, v: [56, 60, 63, 65, 68] },  // Dbmaj9(Db2| Ab C Eb F Ab)
  { root: 32, v: [55, 60, 63, 67, 72] },  // Abmaj7(Ab1| G C Eb G C)
  { root: 39, v: [55, 58, 63, 65, 70] },  // Eb6/9 (Eb2| G Bb Eb F Bb)
];
const chordAt = (t) => CH[Math.floor(t / BAR + 1e-6) % 4];

// ── instruments ──────────────────────────────────────────────────
function kick(t, g = 1, muffled = false) {
  const i0 = at(t), len = at(0.42); let ph = 0; const lp = new BQ('lp', muffled ? 260 : 9000);
  for (let k = 0; k < len; k++) {
    const tt = k / SR, f = 46 + 110 * Math.exp(-tt * 28);
    ph += TAU * f / SR;
    let v = Math.sin(ph) * Math.exp(-tt * 7.5) + (k < 90 ? rnd() * 0.35 * (1 - k / 90) : 0);
    v = Math.tanh(v * 1.6) * g * 0.9;
    add(drums, i0 + k, lp.p(v));
  }
}
function clap(t, g = 1) {
  const i0 = at(t), len = at(0.35), bp = new BQ('bp', 1400, 1.1), hp = new BQ('hp', 600);
  for (let k = 0; k < len; k++) {
    const tt = k / SR; let e = 0;
    for (const o of [0, 0.011, 0.022]) if (tt >= o) e = Math.max(e, Math.exp(-(tt - o) * (o === 0.022 ? 18 : 140)));
    const v = hp.p(bp.p(rnd())) * e * g * 1.5;
    add(drums, i0 + k, v, -0.05); add(verbSend, i0 + k, v * 0.35);
  }
}
function hat(t, g = 1, open = false, pan = 0.2) {
  const i0 = at(t), len = at(open ? 0.22 : 0.05), hp = new BQ('hp', 8000), bp = new BQ('bp', 10500, 0.8);
  for (let k = 0; k < len; k++) { const tt = k / SR; const v = (hp.p(rnd()) * 0.6 + bp.p(rnd()) * 0.6) * Math.exp(-tt * (open ? 14 : 70)) * g * 0.5; add(drums, i0 + k, v, pan); }
}
function shaker(t, g = 1) {
  const i0 = at(t), len = at(0.06), bp = new BQ('bp', 6500, 1.5);
  for (let k = 0; k < len; k++) { const tt = k / SR; const e = Math.min(1, tt / 0.012) * Math.exp(-tt * 55); add(drums, i0 + k, bp.p(rnd()) * e * g * 0.45, -0.35); }
}
function crash(t, g = 1) {
  const i0 = at(t), len = at(2.2), hp = new BQ('hp', 5200);
  for (let k = 0; k < len; k++) { const tt = k / SR; const v = hp.p(rnd()) * Math.exp(-tt * 2.1) * g * 0.32; add(drums, i0 + k, v, 0.15 * Math.sin(tt * 3)); add(verbSend, i0 + k, v * 0.4); }
}
function bassNote(t, m, dur, g = 1) {
  const i0 = at(t), len = at(dur + 0.03), f = mtof(m); let ph = 0; const lp = new BQ('lp', 420, 0.9);
  for (let k = 0; k < len; k++) {
    const tt = k / SR; ph += TAU * f / SR;
    const e = Math.min(1, tt / 0.004) * (tt < dur ? 1 : Math.max(0, 1 - (tt - dur) / 0.03)) * Math.exp(-tt * 2.2);
    let v = Math.sin(ph) + 0.35 * Math.sin(2 * ph) + 0.12 * Math.sin(3 * ph);
    v = Math.tanh(v * 1.4) * e * g * 0.55;
    add(bass, i0 + k, lp.p(v));
  }
}
function saw(ph) { return 2 * (ph / TAU - Math.floor(ph / TAU + 0.5)); }
function stab(t, notes, dur, cutoff, g = 1, target = music) {
  const i0 = at(t), len = at(dur + 0.25);
  const voices = notes.flatMap((m, j) => [-9, 0, 9].map((d) => ({ f: mtof(m) * Math.pow(2, d / 1200), ph: (j * 1.7 + d) % TAU, pan: d / 14 })));
  const lpL = new BQ('lp', cutoff, 1.4), lpR = new BQ('lp', cutoff, 1.4);
  for (let k = 0; k < len; k++) {
    const tt = k / SR;
    if (k % 32 === 0) { const fc = cutoff * (0.45 + 1.6 * Math.exp(-tt * 9)); lpL.set(fc); lpR.set(fc); }
    const e = Math.min(1, tt / 0.003) * (tt < dur ? Math.exp(-tt * 3) : Math.exp(-dur * 3) * Math.exp(-(tt - dur) * 18));
    let l = 0, r = 0;
    for (const v of voices) { v.ph += TAU * v.f / SR; const s = saw(v.ph); l += s * (1 - v.pan); r += s * (1 + v.pan); }
    l = lpL.p(l) * e * g * 0.19; r = lpR.p(r) * e * g * 0.19;
    target[0][i0 + k] += l; target[1][i0 + k] += r; verbSend[0][i0 + k] += l * 0.5; verbSend[1][i0 + k] += r * 0.5;
  }
}
function pad(t0, t1, cutoff, g = 1) {
  // sustained soft chords following the progression
  for (let bt = t0; bt < t1 - 1e-6; bt += BAR) {
    const ch = chordAt(bt), len = Math.min(BAR, t1 - bt);
    const i0 = at(bt), n = at(len + 0.4);
    const voices = ch.v.flatMap((m) => [-6, 6].map((d) => ({ f: mtof(m - 12 * 0) * Math.pow(2, d / 1200), ph: m + d, pan: d / 8 })));
    const lp = [new BQ('lp', cutoff, 0.6), new BQ('lp', cutoff, 0.6)];
    for (let k = 0; k < n; k++) {
      const tt = k / SR, e = Math.min(1, tt / 0.25) * (tt < len ? 1 : Math.max(0, 1 - (tt - len) / 0.4));
      let l = 0, r = 0; for (const v of voices) { v.ph += TAU * v.f / SR; const s = Math.sin(v.ph) * 0.6 + saw(v.ph) * 0.4; l += s * (1 - v.pan); r += s * (1 + v.pan); }
      l = lp[0].p(l) * e * g * 0.03; r = lp[1].p(r) * e * g * 0.03;
      music[0][i0 + k] += l; music[1][i0 + k] += r; verbSend[0][i0 + k] += l * 0.6; verbSend[1][i0 + k] += r * 0.6;
    }
  }
}
function pluck(t, m, g = 1) {
  const i0 = at(t), len = at(0.5), f = mtof(m); let p1 = 0, p2 = 0; const lp = new BQ('lp', 3000, 2);
  for (let k = 0; k < len; k++) {
    const tt = k / SR; if (k % 32 === 0) lp.set(700 + 5200 * Math.exp(-tt * 14));
    p1 += TAU * f / SR; p2 += TAU * f * 1.006 / SR;
    const sq = (Math.sin(p1) > 0 ? 1 : -1) * 0.5 + saw(p2) * 0.5;
    const v = lp.p(sq) * Math.min(1, tt / 0.002) * Math.exp(-tt * 6.5) * g * 0.4;
    lead[0][i0 + k] += v; lead[1][i0 + k] += v;
  }
}
// ── sound design ─────────────────────────────────────────────────
function tick(t, g = 1, f = 3400, pan = 0) {
  const i0 = at(t), len = at(0.04); let ph = 0;
  for (let k = 0; k < len; k++) { const tt = k / SR; ph += TAU * f / SR; add(sfx, i0 + k, (Math.sin(ph) * Math.exp(-tt * 160) + (k < 24 ? rnd() * 0.6 : 0)) * g * 0.28, pan); }
}
function checkTone(t, g = 1) { // two-tone confirm blip
  for (const [o, f] of [[0, 1760], [0.06, 2637]]) {
    const i0 = at(t + o), len = at(0.16); let ph = 0;
    for (let k = 0; k < len; k++) { const tt = k / SR; ph += TAU * f / SR; const v = Math.sin(ph) * Math.min(1, tt / 0.002) * Math.exp(-tt * 26) * g * 0.13; add(sfx, i0 + k, v, 0.2); add(verbSend, i0 + k, v * 0.3); }
  }
}
function swish(tLand, g = 1, dir = 1, len = 0.42) {
  const t0 = tLand - len * 0.72, i0 = at(t0), n = at(len), bp = new BQ('bp', 500, 1.2);
  for (let k = 0; k < n; k++) {
    const u = k / n; if (k % 32 === 0) bp.set(350 + 5200 * Math.sin(Math.PI * Math.min(1, u * 1.1)) ** 2);
    const e = Math.sin(Math.PI * u) ** 2 * (u < 0.72 ? 1 : 1 - (u - 0.72) / 0.28 * 0.6);
    add(sfx, i0 + k, bp.p(rnd()) * e * g * 0.9, dir * (u * 2 - 1) * 0.8);
  }
}
function impact(t, g = 1, deep = true) {
  const i0 = at(t), n = at(1.4); let ph = 0; const lp = new BQ('lp', 2800);
  for (let k = 0; k < n; k++) {
    const tt = k / SR, f = (deep ? 38 : 55) + 90 * Math.exp(-tt * 16); ph += TAU * f / SR;
    const body = Math.tanh(Math.sin(ph) * 2.2) * Math.exp(-tt * (deep ? 3.2 : 6)) * 0.85;
    const hit = lp.p(rnd()) * Math.exp(-tt * 22) * 0.7;
    const v = (body + hit) * g; add(sfx, i0 + k, v); add(verbSend, i0 + k, hit * g * 0.8);
  }
}
function thump(t, g = 1) {
  const i0 = at(t), n = at(0.3); let ph = 0;
  for (let k = 0; k < n; k++) { const tt = k / SR; ph += TAU * (70 + 70 * Math.exp(-tt * 30)) / SR; add(sfx, i0 + k, (Math.sin(ph) * Math.exp(-tt * 14) + (k < 60 ? rnd() * 0.5 : 0)) * g * 0.6); }
}
function riser(t0, t1, g = 1) {
  const i0 = at(t0), n = at(t1 - t0), bp = new BQ('bp', 300, 2); let ph = 0;
  for (let k = 0; k < n; k++) {
    const u = k / n; if (k % 32 === 0) bp.set(300 * Math.pow(26, u));
    ph += TAU * (180 * Math.pow(5, u)) / SR;
    const e = Math.pow(u, 2.2);
    add(sfx, i0 + k, (bp.p(rnd()) * 1.4 + Math.sin(ph) * 0.08) * e * g * 0.55, Math.sin(u * 30) * 0.3 * u);
  }
}
function reverseSwell(t0, t1, g = 1) {
  const i0 = at(t0), n = at(t1 - t0), hp = new BQ('hp', 3500);
  for (let k = 0; k < n; k++) { const u = k / n; add(sfx, i0 + k, hp.p(rnd()) * Math.pow(u, 3.2) * g * 0.7, 0); }
}

// ── arrangement ──────────────────────────────────────────────────
// Intro: muffled kick + filtered pad, ticks per toast, slam, riser.
pad(0, C.drop1, 520, 1.1);
for (let t = 0; t < C.drop1 - 0.6; t += BEAT) kick(t, 0.42, true);
C.toasts.forEach((t, i) => tick(t, 1, 3000 + i * 180, -0.4 + i * 0.2));
impact(C.slamOps, 0.9); riser(C.slamOps, C.drop1, 0.9);

// Grooves
for (let t = 0; t < C.duration - 1e-6; t += BEAT) {
  const beatInBar = Math.round((t % BAR) / BEAT);
  if (grooveOn(t)) {
    const peak = t >= C.drop2;
    const building = t >= S.approach[0] + BAR; // last bar before tape stop
    kick(t, building ? 1.0 : 0.95);
    if (beatInBar === 1 || beatInBar === 3) clap(t, peak ? 1.1 : 0.85);
    hat(t + BEAT / 2, peak ? 1 : 0.8, peak || t >= S.stats[0], 0.25);
    if (t >= S.name[0]) { shaker(t + BEAT / 4, 0.8); shaker(t + 3 * BEAT / 4, 0.6); }
    // bass: off-beat 8ths on the chord root, octave pop on the last
    const ch = chordAt(t);
    if (!building || beatInBar < 2) bassNote(t + BEAT / 2, ch.root + (beatInBar === 3 ? 12 : 0), 0.2, 1);
    // stabs in a 3-3-2 pattern
    if (beatInBar === 0 || (beatInBar === 1 && false)) {
      const cut = peak ? 3600 : (t >= S.stats[0] ? 2600 : 1600);
      for (const o of [0, 1.5, 3.0]) stab(t + o * BEAT, ch.v, 0.16, cut, peak ? 1.15 : 1);
    }
  }
}
// pad under the peak for width
pad(C.drop2, 36, 1500, 0.7);

// hook (peak only): two-bar phrase, repeats
const HOOK = [[[0, 72], [0.75, 75], [1.5, 77], [2.5, 75]], [[0, 72], [0.75, 68], [1.5, 70], [3.0, 72]]];
for (let bar = C.drop2; bar < 36 - 1e-6; bar += BAR) {
  const ph = HOOK[Math.round((bar - C.drop2) / BAR) % 2];
  for (const [o, m] of ph) pluck(bar + o * BEAT, m, 1);
}
// teaser of the hook in the last stats bar (low, filtered)
for (const [o, m] of HOOK[0]) pluck(18 + o * BEAT, m - 12, 0.6);

// Order: checks
C.checks.forEach((t) => checkTone(t, 1));
crash(C.drop1, 0.8); impact(C.drop1, 0.55);
swish(C.dive + 0.25, 1.0, 1, 0.55); impact(C.nameIn, 0.8);
tick(C.sticker, 0.9, 2200); thump(C.sticker, 0.6);
tick(C.clockRoll, 0.7, 2600);

// Stats: whips + odometers + toggle click
C.whips.forEach((t, i) => swish(t, 0.95, i % 2 ? -1 : 1));
tick(C.toggle, 1.2, 1900); thump(C.toggle, 0.35);
for (const r of Object.values(C.rolls)) C.rollTicks(r).forEach((t, i) => tick(t, 0.55, 4200 - (i % 3) * 300, 0.3));

// Approach: four slams + build + tape stop
C.words.forEach((t, i) => impact(t, 0.6 + i * 0.1, i === 3));
riser(C.riser[0], C.tapeStop, 1.1);
for (let t = 22, i = 0; t < C.tapeStop - 1e-6; i++) { clap(t, 0.25 + 0.5 * ((t - 22) / 1.75)); t += t < 23 ? BEAT / 2 : BEAT / 4; }

// Stillness → drop 2
reverseSwell(25.0, C.drop2, 1);
crash(C.drop2, 1.1); impact(C.drop2, 1.0);
C.cards.forEach((t, i) => { thump(t, 1); if (i) swish(t, 0.5, i % 2 ? 1 : -1, 0.3); });

// Close
swish(C.closeIn, 0.8, -1); impact(C.press, 1.0); crash(C.press, 0.7); checkTone(C.toast + 0.05, 1.1);
// Final chord rings out from 36 (drums stop) — Fm9, long
stab(36, CH[0].v, 1.6, 2200, 1.4); bassNote(36, 29, 1.4, 1); kick(36, 0.9);

// ── sidechain pump on bass + music, keyed by the groove kicks ────
const duck = new Float32Array(N).fill(1);
for (let t = 0; t < C.duration; t += BEAT) if (grooveOn(t)) {
  const i0 = at(t), n = at(BEAT);
  for (let k = 0; k < n && i0 + k < N; k++) { const u = k / n; duck[i0 + k] = Math.min(duck[i0 + k], 0.25 + 0.75 * Math.min(1, Math.pow(u / 0.55, 1.6))); }
}
for (const b of [bass, music]) for (let c = 0; c < 2; c++) for (let i = 0; i < N; i++) b[c][i] *= duck[i];

// ── lead delay (dotted 8th ping-pong) ────────────────────────────
{ const d = at(BEAT * 0.75), fb = 0.38; const L = lead[0], R = lead[1];
  for (let i = d; i < N; i++) { L[i] += R[i - d] * fb; R[i] += L[i - d] * fb; }
  for (let i = 0; i < N; i++) { music[0][i] += L[i]; music[1][i] += R[i]; verbSend[0][i] += L[i] * 0.3; verbSend[1][i] += R[i] * 0.3; } }

// ── reverb (Freeverb-style) ──────────────────────────────────────
function reverb(inp, room = 0.82, damp = 0.35) {
  const out = bus(); const combs = [1557, 1617, 1491, 1422, 1277, 1356], aps = [556, 441, 341];
  for (let c = 0; c < 2; c++) {
    const sp = c ? 23 : 0, x = inp[c], y = out[c];
    for (const L of combs) { const len = Math.round((L + sp) * SR / 44100), buf = new Float32Array(len); let idx = 0, lp = 0;
      for (let i = 0; i < N; i++) { const o = buf[idx]; lp = o * (1 - damp) + lp * damp; buf[idx] = x[i] * 0.015 + lp * room; idx = (idx + 1) % len; y[i] += o; } }
    for (const L of aps) { const len = Math.round((L + sp) * SR / 44100), buf = new Float32Array(len); let idx = 0;
      for (let i = 0; i < N; i++) { const b = buf[idx], v = y[i]; buf[idx] = v + b * 0.5; y[i] = b - v; idx = (idx + 1) % len; } }
  }
  return out;
}
const verb = reverb(verbSend);

// ── mix ──────────────────────────────────────────────────────────
const G = { drums: 0.85, bass: 0.95, music: 1.0, sfx: 0.9, verb: 2.5 };
const mus = bus();
for (let c = 0; c < 2; c++) for (let i = 0; i < N; i++)
  mus[c][i] = drums[c][i] * G.drums + bass[c][i] * G.bass + music[c][i] * G.music + verb[c][i] * G.verb;

// Tape stop on the music bus (sfx untouched): playback rate falls 1 → 0 over 0.25 s,
// then the music is silent until the reverse swell into drop 2.
{
  const i0 = at(C.tapeStop), i1 = at(C.still), n = i1 - i0, src = [mus[0].slice(), mus[1].slice()];
  let pos = i0;
  for (let k = 0; k < n; k++) {
    const u = k / n, rate = Math.pow(1 - u, 1.4); pos += rate;
    const p = Math.floor(pos), fr = pos - p, g = 1 - Math.pow(u, 4);
    for (let c = 0; c < 2; c++) mus[c][i0 + k] = (src[c][p] * (1 - fr) + src[c][p + 1] * fr) * g;
  }
  for (let c = 0; c < 2; c++) for (let i = i1; i < at(C.drop2); i++) mus[c][i] = 0;
}

if (process.env.STEMS) {
  const rms = (b, t0, t1) => { let s = 0; for (let i = at(t0); i < at(t1); i++) s += b[0][i] ** 2 + b[1][i] ** 2; return (10 * Math.log10(s / (2 * (at(t1) - at(t0))) + 1e-12)).toFixed(1); };
  for (const [n, b] of Object.entries({ drums, bass, music, lead, sfx, verb })) console.log(n.padEnd(6), 'intro', rms(b, 0, 4), ' drop1', rms(b, 4, 12), ' stats', rms(b, 12, 20), ' peak', rms(b, 26, 32));
}
const out = bus();
for (let c = 0; c < 2; c++) for (let i = 0; i < N; i++) {
  let v = mus[c][i] + sfx[c][i] * G.sfx;
  const tail = (N - i) / SR; if (tail < 0.35) v *= tail / 0.35;   // clean ending
  out[c][i] = Math.tanh(v * 0.5) / 0.5 * 0.5;                        // gentle glue
}

// write float32 WAV
const data = Buffer.alloc(N * 8);
for (let i = 0; i < N; i++) { data.writeFloatLE(out[0][i], i * 8); data.writeFloatLE(out[1][i], i * 8 + 4); }
const h = Buffer.alloc(44);
h.write('RIFF', 0); h.writeUInt32LE(36 + data.length, 4); h.write('WAVE', 8); h.write('fmt ', 12);
h.writeUInt32LE(16, 16); h.writeUInt16LE(3, 20); h.writeUInt16LE(2, 22); h.writeUInt32LE(SR, 24);
h.writeUInt32LE(SR * 8, 28); h.writeUInt16LE(8, 32); h.writeUInt16LE(32, 34); h.write('data', 36); h.writeUInt32LE(data.length, 40);
fs.writeFileSync(new URL('./score_raw.wav', import.meta.url), Buffer.concat([h, data]));
console.log('wrote score_raw.wav', DUR, 's');
