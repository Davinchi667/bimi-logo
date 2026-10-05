/* Single source of timing for the score AND the picture.
   120 BPM: 1 beat = 0.5 s, 1 bar = 2 s. Every time below is in seconds.
   Loaded by index.html (<script src="cues.js">) and by audio/score.mjs (vm). */
(function (g) {
  const BPM = 120, BEAT = 60 / BPM, BAR = BEAT * 4;
  const b = (bar, beat = 0) => +(bar * BAR + beat * BEAT).toFixed(4); // bar is 0-based

  const S = {
    intro:   [b(0),  b(2)],   // 0–4   notification storm
    order:   [b(2),  b(4)],   // 4–8   DROP 1 — checks, stack, dive
    name:    [b(4),  b(6)],   // 8–12  plum name card
    stats:   [b(6),  b(10)],  // 12–20 four proof bursts
    approach:[b(10), b(12)],  // 20–24 people / processes / systems / execution
    still:   [b(12), b(13)],  // 24–26 silence, one line
    cases:   [b(13), b(16)],  // 26–32 DROP 2 (peak) — case cards
    close:   [b(16), b(19)],  // 32–38 CTA + outro
  };

  const C = {
    bpm: BPM, beat: BEAT, bar: BAR, duration: b(19), sections: S,
    // ── picture + sound share these ───────────────────────────────
    toasts:    [0.5, 1.0, 1.5, 2.0, 2.5],      // tick each
    slamOps:   3.0,                            // "Operations," impact
    drop1:     4.0,
    checks:    [4.5, 5.0, 5.5, 6.0, 6.5],      // check-tick each
    repeatable:5.0,                            // italic line reveal
    merge:     7.0,                            // stack → pill
    dive:      7.5,                            // swish, camera dives into dot
    nameIn:    8.0,                            // impact, plum fills
    surname:   8.5,
    sticker:   9.5,
    clockRoll: 11.0,                           // 14:39 → 14:40
    whips:     [12.0, 14.0, 16.0, 18.0, 20.0], // camera whip lands on these
    stat:      [12.0, 14.0, 16.0, 18.0],
    toggle:    12.5,
    words:     [20.0, 21.0, 22.0, 23.0],       // slam each
    riser:     [22.0, 24.0],
    tapeStop:  23.75,
    still:     24.0,
    drop2:     26.0,
    cards:     [26.0, 27.5, 29.0, 30.5],       // thump each
    closeIn:   32.0,
    press:     34.0,                           // CTA press impact
    toast:     34.25,
    end:       b(19),
    // Odometer rolls: value(t) = from + (to-from)*ease(u). The score ticks every
    // time floor(value/step) changes; the picture shows the same value.
    rolls: {
      s40:   { t0: 12.25, t1: 13.4,  from: 0, to: 40,   step: 1   },
      s10:   { t0: 14.25, t1: 15.2,  from: 0, to: 10,   step: 1   },
      s20:   { t0: 16.25, t1: 17.3,  from: 0, to: 20,   step: 1   },
      s6000: { t0: 18.2,  t1: 19.3,  from: 0, to: 6000, step: 250 },
      fleet: { t0: 27.7,  t1: 28.8,  from: 0, to: 100,  step: 5   },
    },
  };
  C.ease = (u) => { u = Math.min(1, Math.max(0, u)); return 1 - Math.pow(1 - u, 3); };
  C.rollValue = (r, t) => r.from + (r.to - r.from) * C.ease((t - r.t0) / (r.t1 - r.t0));
  C.rollTicks = (r) => {
    const out = []; let last = Math.floor(r.from / r.step), prevT = -1;
    for (let t = r.t0; t <= r.t1 + 1e-6; t += 1 / 960) {
      const k = Math.floor(C.rollValue(r, t) / r.step + 1e-9);
      if (k !== last) { last = k; if (t - prevT > 0.022) { out.push(+t.toFixed(4)); prevT = t; } }
    }
    return out;
  };
  g.CUES = C;
  if (typeof module !== 'undefined') module.exports = C;
})(typeof window !== 'undefined' ? window : globalThis);
