import { chromium } from 'playwright';
import { spawn } from 'child_process';
const FPS = 60, DUR = 20, OUT = '/tmp/claude-0/video/silent.mp4';
const b = await chromium.launch();
const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
p.on('pageerror', e => console.log('PAGEERR', e.message));
await p.goto('file:///tmp/claude-0/video/index.html');
await p.evaluate(() => window.ready);
const ff = spawn('ffmpeg', ['-loglevel', 'error', '-y', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
  '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', OUT], { stdio: ['pipe', 'inherit', 'inherit'] });
const total = FPS * DUR;
for (let f = 0; f < total; f++) {
  await p.evaluate(t => window.seek(t), f / FPS);
  const buf = await p.screenshot({ type: 'jpeg', quality: 95 });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  if (f % 120 === 0) console.log('frame', f, '/', total);
}
ff.stdin.end();
await new Promise(r => ff.on('close', r));
await b.close();
console.log('done');
