// Génère les carrousels Instagram (1080×1350) et TikTok (1080×1920) d'InfoPourBac.
// Usage : node make.js   (puppeteer-core + Chrome installé)
const path = require('path');
const fs = require('fs');
const puppeteer = require(process.env.PUPPETEER_PATH || 'puppeteer-core');

const SITE = 'infopourbac.netlify.app';
const OUT = __dirname;

// ------------------------------------------------------------ coloration du code
const esc = s => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
function hl(code, kind) {
  const kw = kind === 'py'
    ? ['def', 'return', 'if', 'elif', 'else', 'for', 'in', 'while', 'break', 'and', 'or', 'not', 'True', 'False']
    : ['Fin Tant que', 'Fin Pour', 'Fin Si', 'Sinon Si', 'Tant que', "Jusqu'à", 'Début', 'Fin', 'Si', 'Alors', 'Sinon', 'Pour', 'de', 'à', 'Faire',
      'Répéter', 'Fonction', 'Procédure', 'Retourner', 'Lire', 'Écrire', 'ET', 'OU', 'NON', 'DIV', 'MOD'];
  const bi = kind === 'py' ? ['print', 'input', 'int', 'float', 'len', 'range', 'str'] : ['Entier', 'Réel', 'Chaîne', 'Booléen'];
  const W = '[\\wÀ-ÿ]';
  const re = new RegExp('("[^"\\n]*")|(#[^\\n]*)|(?<!' + W + ')(' + kw.map(k => k.replace(/'/g, "\\'")).join('|') + ')(?!' + W + ')|(?<!' + W + ')(' + bi.join('|') + ')(?!' + W + ')|(←|≠|≤|≥)|\\b(\\d+)\\b', 'g');
  let out = '', last = 0, m;
  while ((m = re.exec(code))) {
    out += esc(code.slice(last, m.index));
    const cls = m[1] ? 's' : m[2] ? 'c' : m[3] ? 'k' : m[4] ? 'b' : m[5] ? 'a' : 'n';
    out += `<span class="t-${cls}">${esc(m[0])}</span>`;
    last = re.lastIndex;
  }
  return out + esc(code.slice(last));
}
const ALGO = (c, cap = 'Algorithme') => `<figure class="code al"><figcaption><i></i>${cap}</figcaption><pre>${hl(c.trim(), 'al')}</pre></figure>`;
const PY = (c, cap = 'Python') => `<figure class="code py"><figcaption><i></i>${cap}</figcaption><pre>${hl(c.trim(), 'py')}</pre></figure>`;
const PAIR = (a, p) => `<div class="pair">${ALGO(a)}<div class="arrow">↓</div>${PY(p)}</div>`;
const ROWS = rows => `<div class="tr">${rows.map(([a, p]) => `<div class="trow${(a + p).length > 30 ? ' stack' : ''}"><code class="a">${hl(a, 'al')}</code><div class="tpy"><span class="to">${(a + p).length > 30 ? '↳' : '→'}</span><code class="p">${hl(p, 'py')}</code></div></div>`).join('')}</div>`;
const BAD = (bad, good, why) => `<div class="bad"><span class="lbl no">✗ Faux</span><pre>${hl(bad, 'py')}</pre></div>
  <div class="good"><span class="lbl ok">✓ Juste</span><pre>${hl(good, 'py')}</pre></div><p class="why">${why}</p>`;

// barres d'un tableau : [valeurs, indices déplacés, indices triés, étiquette]
function BARS(rows) {
  return `<div class="bars">${rows.map(([v, moved, done, lab]) => `<div class="brow"><span class="blab">${lab}</span><div class="bcells">${v.map((x, i) =>
    `<div class="bc"><b>${x}</b><i class="${moved.includes(i) ? 'hi' : done.includes(i) ? 'ok' : ''}" style="height:calc(${x}px * var(--bar))"></i></div>`).join('')}</div></div>`).join('')}
  <div class="legend"><span><i class="hi"></i>déplacé</span><span><i class="ok"></i>déjà trié</span></div></div>`;
}

// ------------------------------------------------------------ contenu des carrousels
const CAROUSELS = [
  {
    id: '1-les-3-tris',
    slides: [
      { type: 'cover', kicker: 'Bac Sciences · Informatique', title: 'Les <em>3 tris</em> du Bac, expliqués en 1 minute', sub: 'Sélection, bulles, insertion : le même tableau, trois méthodes.' },
      { title: 'L\'outil commun : permuter', body: `<p>Les trois tris échangent des cases. On passe par une variable <b>aux</b>, sinon on perd une valeur.</p>` +
          PAIR('aux ← T[i]\nT[i] ← T[j]\nT[j] ← aux', 'aux = T[i]\nT[i] = T[j]\nT[j] = aux') },
      { title: '1. Tri par sélection', body: `<p>On cherche le <b>plus petit</b> élément restant et on le met à sa place, à gauche.</p>` +
          BARS([[[5, 2, 8, 1, 4], [], [], 'départ'], [[1, 2, 8, 5, 4], [0, 3], [0], 'étape 1'], [[1, 2, 8, 5, 4], [], [0, 1], 'étape 2'], [[1, 2, 4, 5, 8], [2, 4], [0, 1, 2, 3, 4], 'étape 3']]) },
      { title: '2. Tri à bulles', body: `<p>On compare chaque case avec sa <b>voisine</b> et on échange si elles sont mal rangées. Le plus grand « remonte » à droite.</p>` +
          BARS([[[5, 2, 8, 1, 4], [], [], 'départ'], [[2, 5, 1, 4, 8], [0, 1, 2, 3, 4], [4], 'passage 1'], [[2, 1, 4, 5, 8], [1, 2, 3], [3, 4], 'passage 2'], [[1, 2, 4, 5, 8], [0, 1], [0, 1, 2, 3, 4], 'passage 3']]) },
      { title: '3. Tri par insertion', body: `<p>Comme des cartes en main : on prend chaque élément et on l'<b>insère</b> à sa place dans la partie déjà triée.</p>` +
          BARS([[[5, 2, 8, 1, 4], [], [0], 'départ'], [[2, 5, 8, 1, 4], [0], [0, 1], 'i = 1'], [[1, 2, 5, 8, 4], [0], [0, 1, 2, 3], 'i = 3'], [[1, 2, 4, 5, 8], [2], [0, 1, 2, 3, 4], 'i = 4']]) },
      { title: 'Lequel retenir ?', body: `<div class="cards3">
          <div><b>Sélection</b><span>Le plus simple à écrire. Toujours le même nombre de comparaisons.</span></div>
          <div><b>Bulles</b><span>S'arrête tout seul si un passage ne fait aucun échange.</span></div>
          <div><b>Insertion</b><span>Très rapide si le tableau est déjà presque trié.</span></div></div>
          <p class="tipline">Astuce : pour un ordre <b>décroissant</b>, il suffit d'inverser la comparaison.</p>` },
      { type: 'cta', title: 'Le cours complet, gratuit', sub: 'Les 3 tris avec l\'algorithme, le code Python et les schémas pas à pas.', chips: ['11 chapitres', '38 schémas', '0 DT'] },
    ],
  },
  {
    id: '2-algorithme-vers-python',
    slides: [
      { type: 'cover', kicker: 'Bac Sciences · Informatique', title: 'Traduis <em>n\'importe quel algorithme</em> en Python', sub: 'Le dictionnaire algorithme → Python, en 5 slides. Enregistre-le.' },
      { title: 'Affectation, lecture, écriture', body: ROWS([['x ← 5', 'x = 5'], ['Lire(n)', 'n = int(input())'], ['Lire(r)  (réel)', 'r = float(input())'], ['Écrire("S = ", s)', 'print("S =", s)']]) +
          `<p class="tipline"><b>input()</b> renvoie toujours du texte : convertis avec <b>int()</b> ou <b>float()</b>.</p>` },
      { title: 'Les opérateurs', body: ROWS([['a DIV b', 'a // b'], ['a MOD b', 'a % b'], ['a = b', 'a == b'], ['a ≠ b', 'a != b'], ['ET  OU  NON', 'and  or  not']]) +
          `<p class="tipline"><b>n % 2 == 0</b> : n est pair. <b>n % 10</b> : son dernier chiffre.</p>` },
      { title: 'Si … Sinon Si … Sinon', body: PAIR('Si moy ≥ 10 Alors\n    Écrire("Admis")\nSinon Si moy ≥ 9 Alors\n    Écrire("Contrôle")\nSinon\n    Écrire("Refusé")\nFin Si',
          'if moy >= 10:\n    print("Admis")\nelif moy >= 9:\n    print("Contrôle")\nelse:\n    print("Refusé")') },
      { title: 'Les trois boucles', body: ROWS([['Pour i de 0 à n - 1 Faire', 'for i in range(n):'], ['Tant que cond Faire', 'while cond:'], ['Répéter … Jusqu\'à cond', 'while True: … if cond: break']]) +
          `<p class="tipline"><b>range(n)</b> va de 0 à n − 1 : la borne de fin n'est jamais atteinte.</p>` },
      { title: 'Fonctions et procédures', body: PAIR('Fonction Carre(x : Entier) : Entier\nDébut\n    Retourner x * x\nFin', 'def carre(x):\n    return x * x') +
          `<p class="tipline">Une <b>procédure</b> s'écrit aussi avec <b>def</b>, mais sans <b>return</b>.</p>` },
      { type: 'cta', title: 'Tout le tableau de traduction', sub: 'Chaque notion du programme, algorithme et Python côte à côte.', chips: ['11 chapitres', 'Algorithme + Python', '0 DT'] },
    ],
  },
  {
    id: '3-erreurs-qui-coutent-des-points',
    slides: [
      { type: 'cover', kicker: 'Bac Sciences · Informatique', title: '<em>5 erreurs</em> qui coûtent des points au Bac info', sub: 'La n° 4 fait planter l\'interface à chaque fois.' },
      { title: '1. Oublier de convertir input()', body: BAD('n = input("N = ")\nprint(n + 1)', 'n = int(input("N = "))\nprint(n + 1)', 'input() renvoie toujours une <b>chaîne</b> : "17" + 1 provoque une erreur.') },
      { title: '2. Confondre = et ==', body: BAD('if n % 2 = 0:', 'if n % 2 == 0:', '<b>=</b> range une valeur, <b>==</b> compare deux valeurs.') },
      { title: '3. Sortir de la chaîne', body: BAD('dernier = ch[len(ch)]', 'dernier = ch[len(ch) - 1]', 'Les indices vont de <b>0</b> à <b>len(ch) − 1</b>. Sinon : IndexError.') },
      { title: '4. Des parenthèses en trop', body: BAD('windows.Verifier.clicked.connect(Play())', 'windows.Verifier.clicked.connect(Play)', 'On donne <b>le nom</b> du module Play, on ne l\'exécute pas.') },
      { title: '5. Un objectName différent', body: BAD('windows.resultat.setText("Bravo")', 'windows.Resultat.setText("Bravo")', 'Le nom doit être <b>exactement</b> celui de Qt Designer, majuscules comprises. Sinon : AttributeError.') },
      { type: 'cta', title: 'Évite-les toutes', sub: 'Chaque chapitre a ses encadrés « piège fréquent » et sa fiche « À retenir ».', chips: ['Pièges', 'À retenir', '0 DT'] },
    ],
  },
];

// ------------------------------------------------------------ gabarit
const FORMATS = {
  instagram: { w: 1080, h: 1350, pad: '84px 92px 80px 120px', scale: 1, code: 28, bar: 9 },
  tiktok: { w: 1080, h: 1920, pad: '190px 170px 400px 120px', scale: 1.05, code: 31, bar: 13 },
};
const LOGO = '<svg viewBox="0 0 40 40"><rect width="40" height="40" rx="10" fill="#c8102e"/><path d="M15 12l-6 8 6 8M25 12l6 8-6 8" stroke="#fff" stroke-width="3.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';

function page(slide, i, n, fmt) {
  const F = FORMATS[fmt];
  const last = i === n - 1;
  let main;
  if (slide.type === 'cover') {
    main = `<div class="cover"><p class="kicker"><span class="flag"></span>${slide.kicker}</p><h1>${slide.title}</h1><p class="sub">${slide.sub}</p></div>`;
  } else if (slide.type === 'cta') {
    main = `<div class="cta"><h2>${slide.title}</h2><p class="sub">${slide.sub}</p>
      <div class="url">${SITE}</div><div class="chips">${slide.chips.map(c => `<span>${c}</span>`).join('')}</div>
      <p class="save">Enregistre ce post pour tes révisions 🔖</p></div>`;
  } else {
    main = `<h2>${slide.title}</h2><div class="body">${slide.body}</div>`;
  }
  return `<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>
*{box-sizing:border-box}
html,body{margin:0}
body{width:${F.w}px;height:${F.h}px;overflow:hidden;font-family:Lexend,sans-serif;color:#171a1f;background:#fbfaf6;
 background-image:linear-gradient(rgba(31,95,168,.08) 2px,transparent 2px),linear-gradient(90deg,rgba(31,95,168,.08) 2px,transparent 2px);background-size:54px 54px;position:relative;--bar:${F.bar};font-size:${38 * F.scale}px;line-height:1.45}
body::before{content:"";position:absolute;left:72px;top:0;bottom:0;width:4px;background:#b8102a;opacity:.45}
.frame{position:absolute;inset:0;padding:${F.pad};display:flex;flex-direction:column}
.top{display:flex;justify-content:space-between;align-items:center;margin-bottom:${fmt === 'tiktok' ? 70 : 40}px}
.brand{display:flex;align-items:center;gap:18px;font-weight:600;font-size:38px}
.brand svg{width:56px;height:56px}.brand b{color:#b8102a;font-weight:600}
.count{font-family:"IBM Plex Mono";font-size:30px;color:#6a707a;background:#fff;border:2px solid #e4e2db;border-radius:999px;padding:6px 22px}
.main{flex:1;display:flex;flex-direction:column;justify-content:${slide.type || fmt === 'tiktok' ? 'center' : 'flex-start'};min-height:0}
h1{font-size:${108 * F.scale}px;line-height:1.04;letter-spacing:-.035em;margin:0 0 40px;font-weight:700}
h1 em,h2 em{font-style:normal;color:#b8102a}
h2{font-size:${72 * F.scale}px;line-height:1.1;letter-spacing:-.03em;margin:0 0 36px;font-weight:600}
.kicker{display:inline-flex;align-items:center;gap:16px;font-size:32px;font-weight:500;color:#3b414b;background:#fff;border:2px solid #e4e2db;border-radius:999px;padding:10px 28px 10px 14px;margin:0 0 44px;align-self:flex-start}
.flag{width:44px;height:30px;border-radius:6px;background:#b8102a;position:relative}.flag::after{content:"";position:absolute;left:13px;top:6px;width:18px;height:18px;border-radius:50%;background:#fff}
.sub{font-size:${42 * F.scale}px;color:#3b414b;font-weight:300;margin:0}
.body p{margin:0 0 30px;color:#2b3038;font-weight:300}
.body b,.sub b{font-weight:600;color:#171a1f}
.code{margin:0;border-radius:22px;overflow:hidden}
.code figcaption{font-size:26px;font-weight:500;padding:16px 28px;display:flex;align-items:center;gap:14px}
.code figcaption i{width:16px;height:16px;border-radius:50%}
.code pre,.bad pre,.good pre{margin:0;padding:22px 28px 26px;font:400 ${32 * F.scale}px/1.55 "IBM Plex Mono",monospace;white-space:pre}
.code pre,.bad pre,.good pre{font-size:${F.code}px;padding:18px 26px 20px}
.al{background:#fff;border:2px solid #e4e2db}.al figcaption{color:#6a707a;border-bottom:2px solid #e4e2db}.al figcaption i{background:#b8102a}
.py{background:#1d2128;color:#e6e8ec}.py figcaption{color:#a3abb8;border-bottom:2px solid #2c323c}.py figcaption i{background:#f4c542}
.al .t-k{color:#a3123a;font-weight:600}.al .t-b{color:#1f5fa8}.al .t-s{color:#2e7031}.al .t-n{color:#a34f06}.al .t-a{color:#b8102a;font-weight:600}
.py .t-k,.p .t-k,.bad .t-k,.good .t-k{color:#d6a2ff}.py .t-b,.p .t-b,.bad .t-b,.good .t-b{color:#8ab4ff}.py .t-s,.p .t-s,.bad .t-s,.good .t-s{color:#a8db8f}.py .t-n,.p .t-n,.bad .t-n,.good .t-n{color:#ffab70}
.pair{display:flex;flex-direction:column;gap:6px}
.arrow{text-align:center;font-size:44px;color:#b8102a;line-height:1}
.tr{display:flex;flex-direction:column;gap:${fmt === 'tiktok' ? 34 : 22}px;margin:0 0 30px}
.trow{display:flex;align-items:center;gap:8px}
.trow.stack{flex-direction:column;align-items:flex-start}
.trow:not(.stack) .tpy{padding-left:8px}
.trow:not(.stack) .to::before{content:'';}
.tpy{display:flex;align-items:center;gap:14px;padding-left:22px}
.tr code{display:inline-block;font:500 ${F.code}px/1.35 "IBM Plex Mono",monospace;padding:14px 20px;border-radius:14px;white-space:nowrap}
.tr .a{background:#fff;border:2px solid #e4e2db;color:#2c2a24}
.tr .a .t-k{color:#a3123a;font-weight:600}.tr .a .t-a{color:#b8102a}.tr .a .t-s{color:#2e7031}.tr .a .t-n{color:#a34f06}
.tr .p{background:#1d2128;color:#e6e8ec}
.tr .to{color:#b8102a;font-size:40px;line-height:1}
.tipline{background:#fff;border:2px solid #e4e2db;border-left:8px solid #b8102a;border-radius:16px;padding:22px 28px!important;font-size:${33 * F.scale}px;margin-top:${fmt === 'tiktok' ? 30 : 10}px!important}
.bars{display:flex;flex-direction:column;gap:${fmt === 'tiktok' ? 30 : 16}px}
.brow{display:flex;align-items:flex-end;gap:30px;border-bottom:2px dashed #d3d0c7;padding-bottom:12px}
.blab{width:190px;font:500 28px "IBM Plex Mono";color:#3b414b;padding-bottom:4px}
.bcells{display:flex;gap:22px;align-items:flex-end}
.bc{display:flex;flex-direction:column;align-items:center;gap:6px;width:92px}
.bc b{font:500 26px "IBM Plex Mono";color:#3b414b}
.bc i{display:block;width:100%;border-radius:8px;background:#a9adb3}
.bc i.hi{background:#b8102a}.bc i.ok{background:#2f7a49}
.legend{display:flex;gap:40px;font-size:26px;color:#6a707a;margin-top:4px}
.legend i{display:inline-block;width:26px;height:26px;border-radius:6px;margin-right:12px;vertical-align:-4px}
.legend i.hi{background:#b8102a}.legend i.ok{background:#2f7a49}
.cards3{display:flex;flex-direction:column;gap:22px;margin-bottom:30px}
.cards3 div{background:#fff;border:2px solid #e4e2db;border-radius:20px;padding:24px 30px}
.cards3 b{display:block;font-size:40px;color:#b8102a;margin-bottom:6px}
.cards3 span{font-size:${32 * F.scale}px;color:#3b414b;font-weight:300}
.bad,.good{border-radius:22px;overflow:hidden;margin-bottom:26px;position:relative;background:#1d2128;color:#e6e8ec}
.bad{outline:5px solid #d9485f}.good{outline:5px solid #3a9a5c}
.lbl{display:block;font:600 28px Lexend;padding:14px 28px 0}
.lbl.no{color:#ff8b9b}.lbl.ok{color:#8fd6a5}
.why{font-size:${36 * F.scale}px;margin-top:16px!important}
.cover h1{margin-bottom:44px}
.cta{display:flex;flex-direction:column;gap:34px}
.cta h2{font-size:${92 * F.scale}px;margin:0}
.url{align-self:flex-start;font:600 ${46 * F.scale}px "IBM Plex Mono";background:#b8102a;color:#fff;border-radius:20px;padding:24px 36px;box-shadow:0 14px 30px -14px #b8102a}
.chips{display:flex;flex-wrap:wrap;gap:16px}
.chips span{background:#fff;border:2px solid #e4e2db;border-radius:999px;padding:10px 26px;font-size:30px;font-weight:500;color:#3b414b}
.save{font-size:32px;color:#6a707a;margin:0}
.foot{display:flex;justify-content:space-between;align-items:center;margin-top:36px;font-size:30px;color:#6a707a}
.dots{display:flex;gap:12px}.dots i{width:16px;height:16px;border-radius:50%;background:#d3d0c7}.dots i.on{background:#b8102a;width:44px;border-radius:8px}
.swipe{font-weight:500;color:#b8102a}
</style></head><body><div class="frame">
<div class="top"><div class="brand">${LOGO}<span>Info<b>Pour</b>Bac</span></div><div class="count">${String(i + 1).padStart(2, '0')} / ${String(n).padStart(2, '0')}</div></div>
<div class="main">${main}</div>
<div class="foot"><div class="dots">${Array.from({ length: n }, (_, k) => `<i class="${k === i ? 'on' : ''}"></i>`).join('')}</div>
<span class="${last ? '' : 'swipe'}">${last ? SITE : 'Glisse →'}</span></div>
</div></body></html>`;
}

(async () => {
  const b = await puppeteer.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: 'new' });
  const p = await b.newPage();
  const problems = [];
  for (const fmt of Object.keys(FORMATS)) {
    const F = FORMATS[fmt];
    await p.setViewport({ width: F.w, height: F.h, deviceScaleFactor: 1 });
    for (const c of CAROUSELS) {
      const dir = path.join(OUT, fmt, c.id);
      fs.mkdirSync(dir, { recursive: true });
      for (let i = 0; i < c.slides.length; i++) {
        await p.setContent(page(c.slides[i], i, c.slides.length, fmt), { waitUntil: 'domcontentloaded' });
        await p.evaluate(() => Promise.race([document.fonts.ready, new Promise(r => setTimeout(r, 6000))]));
        // contrôle : rien ne doit dépasser du cadre de contenu
        const over = await p.evaluate(() => {
          const m = document.querySelector('.main'), f = document.querySelector('.foot');
          const wide = [...document.querySelectorAll('.main *')].some(e => e.getBoundingClientRect().right > innerWidth - 40);
          return m.scrollHeight > m.clientHeight + 2 || wide || f.getBoundingClientRect().bottom > innerHeight;
        });
        if (over) problems.push(`${fmt}/${c.id}/${i + 1}`);
        await p.screenshot({ path: path.join(dir, String(i + 1).padStart(2, '0') + '.png') });
      }
    }
  }
  console.log('débordements :', problems.length ? problems : 'aucun');
  await b.close();
})();
