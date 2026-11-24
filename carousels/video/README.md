# Vidéo promo (1080×1920, 25 s, 30 fps, sans son)

- `promo.html` : l'animation (HTML/CSS, dialecte tunisien, termes FR/EN en latin). `window.seek(ms)` fige toutes les animations à un instant donné.
- `render.js` : capture une image par frame via Chrome headless puis encode `infopourbac-promo.mp4` avec ffmpeg.

```
node render.js            # 25 s à 30 fps
node render.js --fps 24   # autre cadence
```

Prérequis : Chrome, ffmpeg dans le PATH, `puppeteer-core` (ou `PUPPETEER_PATH`).
Ajouter la musique dans l'éditeur Reels/TikTok au moment de publier.

Scènes : 0–4 s accroche · 4–8 s logo · 8–14 s Algorithme → Python · 14–20 s contenu · 20–25 s CTA infopourbac.com
