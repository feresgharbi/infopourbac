// Rend promo.html image par image (seek déterministe) puis encode en MP4 avec ffmpeg.
// Usage : node render.js [--fps 30] [--seconds 25]
// Prérequis : puppeteer-core (ou PUPPETEER_PATH), Chrome, ffmpeg dans le PATH.
const path = require('path');
const fs = require('fs');
const { execFileSync } = require('child_process');
const puppeteer = require(process.env.PUPPETEER_PATH || 'puppeteer-core');

const arg = (k, d) => { const i = process.argv.indexOf('--' + k); return i > -1 ? Number(process.argv[i + 1]) : d; };
const FPS = arg('fps', 30);
const SECONDS = arg('seconds', 25);
const W = 1080, H = 1920;
const FRAMES = path.join(__dirname, 'frames');
const OUT = path.join(__dirname, 'infopourbac-promo.mp4');

(async () => {
  fs.rmSync(FRAMES, { recursive: true, force: true });
  fs.mkdirSync(FRAMES);
  const b = await puppeteer.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: 'new' });
  const p = await b.newPage();
  await p.setViewport({ width: W, height: H, deviceScaleFactor: 1 });
  await p.goto(require('url').pathToFileURL(path.join(__dirname, 'promo.html')).href, { waitUntil: 'load' });
  // Polices : on attend qu'elles soient réellement chargées.
  await p.evaluate(() => Promise.race([Promise.all([
    document.fonts.load('700 40px "IBM Plex Sans Arabic"'), document.fonts.load('600 40px "IBM Plex Sans Arabic"'),
    document.fonts.load('300 40px "IBM Plex Sans Arabic"'), document.fonts.load('400 40px "IBM Plex Sans Arabic"'),
    document.fonts.load('700 40px Lexend'), document.fonts.load('600 40px Lexend'), document.fonts.load('500 40px Lexend'),
    document.fonts.load('600 40px "IBM Plex Mono"'), document.fonts.load('500 40px "IBM Plex Mono"'),
  ]).then(() => document.fonts.ready), new Promise(r => setTimeout(r, 10000))]));

  const total = FPS * SECONDS;
  const t0 = Date.now();
  for (let f = 0; f < total; f++) {
    await p.evaluate(ms => window.seek(ms), (f / FPS) * 1000);
    await p.screenshot({ path: path.join(FRAMES, String(f).padStart(5, '0') + '.png'), type: 'png' });
    if (f % 60 === 0) process.stdout.write(`frame ${f}/${total}\n`);
  }
  await b.close();
  console.log(`rendu ${total} images en ${((Date.now() - t0) / 1000).toFixed(0)} s`);

  execFileSync('ffmpeg', ['-y', '-framerate', String(FPS), '-i', path.join(FRAMES, '%05d.png'),
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'slow', '-movflags', '+faststart', OUT], { stdio: 'inherit' });
  fs.rmSync(FRAMES, { recursive: true, force: true });
  console.log('OK →', OUT);
})();
