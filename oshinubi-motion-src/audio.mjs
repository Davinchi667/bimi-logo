// Synthesizes a 20s soundtrack synced to the animation timeline. Writes track.wav (48k stereo).
import fs from 'fs';
const SR = 48000, DUR = 20.4, N = Math.floor(SR * DUR);
const L = new Float32Array(N), R = new Float32Array(N);
let seed = 1234567; const rnd = () => ((seed = (seed * 1664525 + 1013904223) >>> 0) / 4294967296) * 2 - 1;
const add = (i, v, pan = 0) => { if (i < 0 || i >= N) return; L[i] += v * Math.min(1, 1 - pan); R[i] += v * Math.min(1, 1 + pan); };
const mtof = m => 440 * Math.pow(2, (m - 69) / 12);

// --- instruments ---
function kick(t, g = 1) { const s = Math.floor(t * SR); let ph = 0;
  for (let i = 0; i < SR * .45; i++) { const x = i / SR; const f = 45 + 110 * Math.exp(-x * 28); ph += 2 * Math.PI * f / SR;
    const env = Math.exp(-x * 7.5); const click = i < 120 ? rnd() * (1 - i / 120) * .5 : 0;
    add(s + i, (Math.tanh(Math.sin(ph) * 1.6) * env + click) * .62 * g); } }
function clap(t, g = 1) { const s = Math.floor(t * SR); let bp = { lo: 0, bd: 0 };
  for (let i = 0; i < SR * .25; i++) { const x = i / SR;
    let env = Math.exp(-x * 22); for (const d of [0, .011, .022]) if (x > d && x < d + .008) env += .9 * Math.exp(-(x - d) * 200);
    const v = svf(bp, rnd(), 1500, .6).bp; add(s + i, v * env * .5 * g, (i % 2 ? .2 : -.2)); } }
function hat(t, g = 1, open = false) { const s = Math.floor(t * SR); let st = { lo: 0, bd: 0 };
  for (let i = 0; i < SR * (open ? .22 : .06); i++) { const x = i / SR; const env = Math.exp(-x * (open ? 18 : 70));
    const v = svf(st, rnd(), 9000, .3).hp; add(s + i, v * env * .16 * g, .35); } }
function svf(s, inp, fc, q) { const f = 2 * Math.sin(Math.PI * Math.min(fc, SR / 6) / SR);
  const lo = s.lo + f * s.bd; const hp = inp - lo - q * s.bd; const bd = f * hp + s.bd; s.lo = lo; s.bd = bd; return { lo, bp: bd, hp }; }
function bass(t, note, len, g = 1) { const s = Math.floor(t * SR), f = mtof(note); let st = { lo: 0, bd: 0 }, ph = 0;
  for (let i = 0; i < SR * len; i++) { const x = i / SR; ph += f / SR; const saw = 2 * (ph % 1) - 1; const sub = Math.sin(2 * Math.PI * ph);
    const env = Math.min(1, x * 200) * Math.exp(-x * 3.2) * (x > len - .02 ? (len - x) / .02 : 1);
    const v = svf(st, saw, 180 + 900 * Math.exp(-x * 14), .7).lo; add(s + i, (v * .5 + sub * .55) * env * .42 * g); } }
function pluck(t, note, g = 1, pan = 0, dec = 5) { const s = Math.floor(t * SR), f = mtof(note); let st = { lo: 0, bd: 0 }, ph = 0, ph2 = 0;
  for (let i = 0; i < SR * 1.2; i++) { const x = i / SR; ph += f / SR; ph2 += f * 1.006 / SR;
    const sq = (ph % 1 < .5 ? 1 : -1) * .5 + (2 * (ph2 % 1) - 1) * .5;
    const env = Math.min(1, x * 400) * Math.exp(-x * dec);
    const v = svf(st, sq, 400 + 3500 * Math.exp(-x * 9), .5).lo; add(s + i, v * env * .12 * g, pan); } }
function pad(t, notes, len, g = 1) { const s = Math.floor(t * SR);
  notes.forEach((n, k) => { let st = { lo: 0, bd: 0 }; const phs = [0, 0, 0]; const f = mtof(n);
    for (let i = 0; i < SR * len; i++) { const x = i / SR; let v = 0;
      [-.008, 0, .007].forEach((d, j) => { phs[j] += f * (1 + d) / SR; v += 2 * (phs[j] % 1) - 1; });
      const env = Math.min(1, x / .25) * Math.min(1, (len - x) / .4);
      add(s + i, svf(st, v / 3, 900, .8).lo * env * .05 * g, k % 2 ? .4 : -.4); } }); }
function whoosh(t, len = .45, g = 1, up = true) { const s = Math.floor(t * SR); let st = { lo: 0, bd: 0 };
  for (let i = 0; i < SR * len; i++) { const x = i / len / SR; const fc = up ? 300 + 6000 * x * x : 6000 - 5600 * Math.sqrt(x);
    const env = Math.sin(Math.PI * Math.min(1, x)) ** 2; add(s + i, svf(st, rnd(), fc, .5).bp * env * .55 * g, (x - .5) * 1.2); } }
function riser(t0, t1, g = 1) { const s = Math.floor(t0 * SR), n = Math.floor((t1 - t0) * SR); let st = { lo: 0, bd: 0 };
  for (let i = 0; i < n; i++) { const x = i / n; add(s + i, svf(st, rnd(), 400 + 7000 * x ** 2, .4).bp * x ** 2 * .35 * g); } }
function blip(t, f0, f1, len = .08, g = 1, pan = 0) { const s = Math.floor(t * SR); let ph = 0;
  for (let i = 0; i < SR * len; i++) { const x = i / SR; const f = f0 + (f1 - f0) * Math.min(1, x / len * 2); ph += f / SR;
    add(s + i, Math.sin(2 * Math.PI * ph) * Math.exp(-x * 40) * .22 * g, pan); } }
function tick(t, g = 1) { const s = Math.floor(t * SR); for (let i = 0; i < 240; i++) add(s + i, (i % 24 < 12 ? 1 : -1) * Math.exp(-i / 50) * .06 * g, -.3); }
function thud(t, g = 1) { kick(t, 1.3 * g); const s = Math.floor(t * SR); let st = { lo: 0, bd: 0 };
  for (let i = 0; i < SR * .35; i++) { const x = i / SR; add(s + i, svf(st, rnd(), 700, .7).lo * Math.exp(-x * 12) * .9 * g); } }
function crash(t, g = 1) { const s = Math.floor(t * SR); let st = { lo: 0, bd: 0 };
  for (let i = 0; i < SR * 1.8; i++) { const x = i / SR; add(s + i, svf(st, rnd(), 7000, .2).hp * Math.exp(-x * 2.6) * .18 * g, rnd() * .3); } }

// --- arrangement (120 BPM, beat = .5s) ---
const B = .5;
// Intro: tension under the inbox flood
riser(0, 1.38, .8);
pad(0, [45, 52], 1.4, .9);
[0.08, 0.36, 0.6, 0.8, 0.96, 1.08, 1.18, 1.26, 1.32, 1.37].forEach((a, i) => blip(a, 700 + i * 90, 1100 + i * 140, .07, .9, (i % 2 ? .3 : -.3)));
whoosh(1.2, .3, .9); thud(1.4, .9); crash(1.4, .5);
riser(1.6, 2.32, .6); whoosh(2.08, .3, .8);

// Groove 2.5 -> 17.25
const prog = [[57, [69, 72, 76]], [53, [65, 69, 72]], [48, [64, 67, 72]], [55, [67, 71, 74]]]; // Am F C G
for (let bar = 0; bar < 8; bar++) {
  const t0 = 2.5 + bar * 4 * B; if (t0 >= 17.25) break;
  const [root, chord] = prog[bar % 4];
  pad(t0, chord.map(n => n - 12), Math.min(4 * B, 17.25 - t0) + .1, .8);
  for (let b8 = 0; b8 < 8; b8++) { const t = t0 + b8 * B / 2; if (t >= 17.2) break;
    bass(t, root - 24 + (b8 === 6 ? 7 : b8 === 7 ? 12 : 0), B / 2 - .01, b8 % 2 ? .75 : 1); }
  for (let b = 0; b < 4; b++) { const t = t0 + b * B; if (t >= 17.2) break;
    kick(t, b === 0 ? 1.05 : .9);
    if (b % 2 === 1) clap(t);
    hat(t + B / 2, .9, b === 3);
    if (t > 8.7 && t < 14.2) { hat(t + B / 4, .5); hat(t + 3 * B / 4, .5); } // 16ths in results
    // arp plucks on the offbeat sixteenths
    const arpN = chord[(bar + b) % 3] + (b === 2 ? 12 : 0);
    pluck(t + B * .75, arpN, .9, (b % 2 ? .45 : -.45));
  }
}
// transitions
[5.2, 8.42, 10.7, 11.92, 12.92, 14.18, 16.82].forEach(a => whoosh(a, .42, .85));
blip(3.62, 400, 900, .12, .8); // highlight swipe
// stat odometers: decelerating ticks
for (let c = 0; c < 4; c++) { const a = 5.45 + c * .09; for (let k = 0; k < 14; k++) tick(a + 1.1 * (1 - Math.pow(1 - k / 14, .5)) * .9, .7); }
// D1 counter
for (let k = 0; k < 18; k++) tick(9.0 + 1.05 * (k / 18), .8);
// D2 ring
for (let k = 0; k < 10; k++) tick(10.95 + .85 * (k / 10), .6);
// D3 swap
whoosh(12.34, .25, .7);
// D4 envelopes pop + counter + stamp
for (let i = 0; i < 5; i++) blip(13.18 + i * .065, 600 + i * 120, 1400 + i * 160, .08, 1, -.4 + i * .2);
for (let k = 0; k < 12; k++) tick(13.4 + .5 * (k / 12), .7);
thud(13.98, 1.1); crash(13.98, .35);
// E nodes light up (rising notes) + check
[14.82, 15.32, 15.82, 16.32].forEach((a, i) => pluck(a, [76, 79, 81, 84][i], 1.6, -.3 + i * .2, 4));
blip(16.42, 900, 1800, .14, .9);
// Finale
crash(17.3, 1); kick(17.3, 1.2); bass(17.3, 33, 1.5, 1.1);
pad(17.3, [57, 64, 69, 72, 76], 3.1, 1.3);
for (let i = 0; i < 8; i++) blip(17.55 + i * .045, 500 + i * 60, 900 + i * 80, .05, .6, -.4 + i * .1);
[69, 72, 76, 81, 79, 76, 72, 76].forEach((n, i) => pluck(18.0 + i * .25, n, .8, (i % 2 ? .4 : -.4), 3.5));
blip(19.24, 1800, 1200, .05, 1.4); tick(19.24, 1.5); // click

// master: gentle bus comp-ish via tanh, fade in/out
let peak = 0;
for (let i = 0; i < N; i++) { const t = i / SR; const fade = Math.min(1, t / .03) * (t > 19.4 ? Math.max(0, 1 - (t - 19.4) / 0.95) : 1);
  L[i] = Math.tanh(L[i] * 1.1) * fade; R[i] = Math.tanh(R[i] * 1.1) * fade; peak = Math.max(peak, Math.abs(L[i]), Math.abs(R[i])); }
const norm = .89 / peak;
const buf = Buffer.alloc(44 + N * 4);
buf.write('RIFF', 0); buf.writeUInt32LE(36 + N * 4, 4); buf.write('WAVEfmt ', 8); buf.writeUInt32LE(16, 16);
buf.writeUInt16LE(1, 20); buf.writeUInt16LE(2, 22); buf.writeUInt32LE(SR, 24); buf.writeUInt32LE(SR * 4, 28);
buf.writeUInt16LE(4, 32); buf.writeUInt16LE(16, 34); buf.write('data', 36); buf.writeUInt32LE(N * 4, 40);
for (let i = 0; i < N; i++) { buf.writeInt16LE(Math.round(L[i] * norm * 32767), 44 + i * 4); buf.writeInt16LE(Math.round(R[i] * norm * 32767), 46 + i * 4); }
fs.writeFileSync('/tmp/claude-0/video/track.wav', buf);
console.log('peak', peak.toFixed(3));
