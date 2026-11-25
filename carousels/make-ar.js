// Carrousels en dialecte tunisien (arabe, RTL) pour Instagram (1080×1350) et TikTok (1080×1920).
// Les termes français/anglais (cours, Python, Bac, InfoPourBac…) restent en latin.
// Usage : node make-ar.js   (puppeteer-core + Chrome installé ; PUPPETEER_PATH optionnel)
const path = require('path');
const fs = require('fs');
const puppeteer = require(process.env.PUPPETEER_PATH || 'puppeteer-core');

const SITE = 'infopourbac.com';
const OUT = __dirname;

// Mot latin inséré dans une phrase arabe : isolé en LTR pour que la ponctuation ne saute pas.
const L = s => `<span class="lt">${s}</span>`;

// ------------------------------------------------------------ contenu
const CAROUSELS = [
  {
    id: '0-intro-plateforme',
    slides: [
      { type: 'cover', kicker: `Bac scientifique · Informatique`,
        title: `موقع تتعلّم منّو ${L("l'informatique")}…<br><em>من الصفر حتى للتميّز</em>`,
        sub: `إذا أنت ${L('Bac scientifique')}، احنا عملنالك ${L('infopourbac.com')} : كل ${L("l'Info")} متاع الـ${L('Bac')}، مشروحة بالساهل، و بلاش.` },
      { title: `المشكلة اللي يعيشها كل تلميذ`, body: `<div class="cards3">
          <div><b>💸 ${L("l'étude")} غالية</b><span>مش كل واحد ينجم يخلّص ساعات ${L("étude")} كل جمعة.</span></div>
          <div><b>🌀 المواقع مخلّطة</b><span>برنامج ناقص، أمثلة مش متاع الـ${L('Bac')} التونسي، إشهار في كل بلاصة.</span></div>
          <div><b>⏳ و الـ${L('Bac')} ما يستنّاش</b><span>تلقى روحك تراجع في آخر لحظة من غير منهج واضح.</span></div></div>` },
      { title: `${L('InfoPourBac : Info Bac scientifique')}<br>مشروحة بالساهل… <em>و بلاش</em>`, body: `<p>موقع تونسي، معمول لتلامذة الـ<b>${L('Bac scientifique')}</b>، فيه <b>كل برنامج الـ${L('Info')}</b> مشروح بالساهل : الشرح بالدارجة متاعنا، و المصطلحات بالفرنسية كيما في القسم.</p>
          <div class="tipline"><b>${L('11 cours')}</b> · ${L('Algorithme')} و ${L('Python')} جنب بعضهم · الخوارزميات الكلاسيكية · قاموس المصطلحات</div>` },
      { title: `شنوّة تلقى فيه بالضبط ؟`, body: `<div class="list">
          <div><i>1</i><div><b>${L('Cours')} كاملين</b><span>من المتغيرات حتى لـ${L('PyQt5')}، بنفس ترتيب البرنامج الرسمي.</span></div></div>
          <div><i>2</i><div><b>${L('Algorithme → Python')}</b><span>كل مثال مكتوب بالزوز، باش تفهم الترجمة مرة وحدة.</span></div></div>
          <div><i>3</i><div><b>الخوارزميات الكلاسيكية</b><span>التري، البحث، الأعداد الأولية… اللي يطيحو في الـ${L('Bac')}.</span></div></div>
          <div><i>4</i><div><b>الغلطات اللي تنقّص نقاط</b><span>في كل ${L('cours')}، إطار « piège fréquent » و فيشة « à retenir ».</span></div></div></div>` },
      { type: 'cta', title: `بلاش ${L('100%')} و من غير تسجيل`,
        sub: `لا حساب، لا كارت، لا إشهار. تحلّ الموقع و تبدا تقرا توّا، على التليفون ولّا على الـ${L('PC')}.`,
        chips: [L('0 DT'), 'بلا تسجيل', L('11 cours'), L('Algorithme + Python')],
        save: `شارك الموقع مع صحابك اللي يقراو ${L('Bac scientifique')} 🎓` },
    ],
  },
  {
    id: '1-bellech',
    slides: [
      { type: 'free', kicker: `Bac scientifique · Informatique`,
        price: `0 DT`, label: `ثمن الموقع الكل`,
        title: `كل ${L("l'Info")} متاع الـ${L('Bac')}…<br><em>بلاش. ${L('100%')}.</em>`,
        sub: `لا ${L('abonnement')}، لا تسجيل، لا كارت. تحلّ ${L('infopourbac.com')} و تقرا.` },
      { title: `« بلاش » عندنا يعني <em>بلاش بالحق</em>`, body: `<div class="list check">
          <div><i>✓</i><div><b>${L('11 cours')} كاملين</b><span>كل برنامج الـ${L('Info')} متاع الـ${L('Bac scientifique')}، من أول ${L('cours')} حتى للآخر.</span></div></div>
          <div><i>✓</i><div><b>الخوارزميات و الأمثلة</b><span>${L('Algorithme')} و ${L('Python')} جنب بعضهم، مع الحلول.</span></div></div>
          <div><i>✓</i><div><b>قاموس المصطلحات</b><span>كل كلمة بالفرنسية مشروحة بالدارجة.</span></div></div>
          <div><i>✓</i><div><b>ما فيهاش ${L('version premium')}</b><span>ما تلقاش ${L('cours')} مسكّر ولّا « ادفع باش تكمّل ».</span></div></div></div>` },
      { title: `كيفاش تقرا على ${L('InfoPourBac')} ؟`, body: `<div class="cards3">
          <div><b>💰 الثمن : ${L('0 DT')}</b><span>ما تخلّص شي، لا توّا لا بعد. الموقع بلاش لكل الناس.</span></div>
          <div><b>🕐 الوقت : ${L('24h/24')}</b><span>تقرا وقت ما تحب، الليل ولّا النهار، بالسرعة اللي تريّحك.</span></div>
          <div><b>📱 البلاصة : تليفونك ولّا ${L('PC')}</b><span>تحلّ الموقع وين ما كنت، في الدار ولّا في الكار.</span></div>
          <div><b>📚 البرنامج : كل برنامج الـ${L('Bac')}</b><span>${L('11 cours')} بنفس ترتيب البرنامج الرسمي، من أول ${L('cours')} حتى للآخر.</span></div></div>` },
      { title: `علاش بلاش ؟`, body: `<p>خاطر الـ<b>${L('Info')}</b> ماهيش صعيبة، أما غالية باش تتعلّمها. تلميذ في تونس ما يلزمش <b>يطيح في الـ${L('Bac')}</b> خاطر ما عندوش فلوس باش يعمل ${L("étude")}.</p>
          <p>الموقع معمول من تونسي، لتلامذة تونس. <b>لا إشهار، لا بيع ${L('cours')}، لا جمع معلومات.</b></p>
          <div class="tipline"><b>الهدف :</b> أي تلميذ ${L('Bac scientifique')}، في أي ولاية، عندو نفس الـ${L('cours')} المشروحة بالساهل.</div>` },
      { type: 'cta', title: `بلاش. توّا. <em>لكل الناس.</em>`,
        sub: `حلّ الموقع من التليفون و ابدا من أوّل ${L('cours')}. ما تخلّص شي، ما تسجّل شي.`,
        chips: [L('0 DT'), 'بلا تسجيل', 'بلا إشهار', L('11 cours')],
        save: `عندك صاحبك يقرا ${L('Bac scientifique')} و يخمّم في الـ${L("étude")} ؟ ابعثلو الموقع 🎓` },
    ],
  },
];

// ------------------------------------------------------------ gabarit
const FORMATS = {
  instagram: { w: 1080, h: 1350, pad: '84px 120px 80px 92px', scale: 1 },
  tiktok: { w: 1080, h: 1920, pad: '190px 120px 400px 170px', scale: 1.05 },
};
const LOGO = '<svg viewBox="0 0 40 40"><rect width="40" height="40" rx="10" fill="#c8102e"/><path d="M15 12l-6 8 6 8M25 12l6 8-6 8" stroke="#fff" stroke-width="3.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>';

function page(slide, i, n, fmt) {
  const F = FORMATS[fmt];
  const last = i === n - 1;
  let main;
  if (slide.type === 'cover') {
    main = `<div class="cover"><p class="kicker"><span class="flag"></span>${L(slide.kicker)}</p><h1>${slide.title}</h1><p class="sub">${slide.sub}</p></div>`;
  } else if (slide.type === 'free') {
    main = `<div class="cover"><p class="kicker"><span class="flag"></span>${L(slide.kicker)}</p>
      <div class="price"><b>${slide.price}</b><span>${slide.label}</span></div>
      <h1>${slide.title}</h1><p class="sub">${slide.sub}</p></div>`;
  } else if (slide.type === 'cta') {
    main = `<div class="cta"><h2>${slide.title}</h2><p class="sub">${slide.sub}</p>
      <div class="url">${SITE}</div><div class="chips">${slide.chips.map(c => `<span>${c}</span>`).join('')}</div>
      <p class="save">${slide.save}</p></div>`;
  } else {
    main = `<h2>${slide.title}</h2><div class="body">${slide.body}</div>`;
  }
  return `<!doctype html><html lang="ar-TN" dir="rtl"><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&family=Lexend:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600&display=swap">
<style>
*{box-sizing:border-box}
html,body{margin:0}
body{width:${F.w}px;height:${F.h}px;overflow:hidden;font-family:"IBM Plex Sans Arabic",Lexend,sans-serif;color:#171a1f;background:#fbfaf6;
 background-image:linear-gradient(rgba(31,95,168,.08) 2px,transparent 2px),linear-gradient(90deg,rgba(31,95,168,.08) 2px,transparent 2px);background-size:54px 54px;position:relative;font-size:${38 * F.scale}px;line-height:1.6}
body::before{content:"";position:absolute;right:72px;top:0;bottom:0;width:4px;background:#b8102a;opacity:.45}
.frame{position:absolute;inset:0;padding:${F.pad};display:flex;flex-direction:column}
.lt{direction:ltr;unicode-bidi:isolate;font-family:Lexend,sans-serif}
.top{display:flex;justify-content:space-between;align-items:center;margin-bottom:${fmt === 'tiktok' ? 70 : 40}px}
.brand{display:flex;align-items:center;gap:18px;font-weight:600;font-size:38px;direction:ltr;font-family:Lexend}
.brand svg{width:56px;height:56px}.brand b{color:#b8102a;font-weight:600}
.count{font-family:"IBM Plex Mono";font-size:30px;color:#6a707a;background:#fff;border:2px solid #e4e2db;border-radius:999px;padding:6px 22px;direction:ltr}
.main{flex:1;display:flex;flex-direction:column;justify-content:${slide.type || fmt === 'tiktok' ? 'center' : 'flex-start'};min-height:0}
h1{font-size:${fmt === 'tiktok' ? 86 : 96}px;line-height:1.25;margin:0 0 40px;font-weight:700}
h1 em,h2 em{font-style:normal;color:#b8102a}
h2{font-size:${64 * F.scale}px;line-height:1.3;margin:0 0 36px;font-weight:600}
.kicker{display:inline-flex;align-items:center;gap:16px;font-size:32px;font-weight:500;color:#3b414b;background:#fff;border:2px solid #e4e2db;border-radius:999px;padding:10px 14px 10px 28px;margin:0 0 44px;align-self:flex-start}
.flag{width:44px;height:30px;border-radius:6px;background:#b8102a;position:relative}.flag::after{content:"";position:absolute;left:13px;top:6px;width:18px;height:18px;border-radius:50%;background:#fff}
.sub{font-size:${42 * F.scale}px;color:#3b414b;font-weight:300;margin:0}
.body p{margin:0 0 30px;color:#2b3038;font-weight:300}
.body b,.sub b,.tipline b{font-weight:600;color:#171a1f}
.tipline{background:#fff;border:2px solid #e4e2db;border-right:8px solid #b8102a;border-radius:16px;padding:22px 28px;font-size:${34 * F.scale}px;margin-top:10px;color:#2b3038}
.cards3{display:flex;flex-direction:column;gap:22px;margin-bottom:30px}
.cards3 div{background:#fff;border:2px solid #e4e2db;border-radius:20px;padding:24px 30px}
.cards3 b{display:block;font-size:40px;color:#b8102a;margin-bottom:6px}
.cards3 span{font-size:${32 * F.scale}px;color:#3b414b;font-weight:300}
.list{display:flex;flex-direction:column;gap:${fmt === 'tiktok' ? 30 : 20}px}
.list>div{display:flex;gap:22px;align-items:flex-start;background:#fff;border:2px solid #e4e2db;border-radius:20px;padding:20px 24px}
.list i{flex:none;width:58px;height:58px;border-radius:50%;background:#b8102a;color:#fff;font:600 30px/58px Lexend;text-align:center;font-style:normal;direction:ltr}
.list b{display:block;font-size:36px;color:#171a1f;margin-bottom:2px}
.list span{font-size:${30 * F.scale}px;color:#3b414b;font-weight:300}
.cover h1{margin-bottom:44px}
.free h1,.price~h1{font-size:${fmt === 'tiktok' ? 78 : 84}px;margin-bottom:34px}
.price{display:flex;align-items:center;gap:30px;margin:0 0 40px;align-self:flex-start}
.price b{direction:ltr;font:700 ${fmt === 'tiktok' ? 150 : 140}px/1 Lexend;color:#fff;background:#b8102a;border-radius:28px;padding:22px 40px 30px;letter-spacing:-.02em;box-shadow:0 24px 50px -22px #b8102a;transform:rotate(-2deg)}
.price span{font-size:34px;font-weight:500;color:#3b414b;max-width:260px;line-height:1.4}
.list.check i{background:#1f8a4c;font-size:34px}
.cmp{display:grid;grid-template-columns:170px 1fr 1.25fr;gap:0;background:#fff;border:2px solid #e4e2db;border-radius:20px;overflow:hidden;font-size:${34 * F.scale}px;font-weight:300;color:#3b414b}
.cmp>div{padding:${fmt === 'tiktok' ? 30 : 26}px 24px;border-bottom:2px solid #e4e2db;display:flex;align-items:center;line-height:1.4}
.cmp>div:nth-last-child(-n+3){border-bottom:0}
.cmp .h{font-weight:600;color:#171a1f;font-size:${36 * F.scale}px;background:#f3f1ea;text-align:center}
.cmp .k{font-weight:600;color:#171a1f;background:#faf9f4}
.cmp .red{color:#b8102a;background:#fff5f6}
.cmp .red b{color:#b8102a;font-weight:700}
.cmp .h.red{background:#b8102a;color:#fff}
.note{font-size:${31 * F.scale}px;color:#6a707a;margin:30px 0 0;font-weight:300}
.note b{color:#171a1f;font-weight:600}
.cta{display:flex;flex-direction:column;gap:34px}
.cta h2{font-size:${80 * F.scale}px;margin:0}
.url{align-self:flex-start;direction:ltr;font:600 ${46 * F.scale}px "IBM Plex Mono";background:#b8102a;color:#fff;border-radius:20px;padding:24px 36px;box-shadow:0 14px 30px -14px #b8102a}
.chips{display:flex;flex-wrap:wrap;gap:16px}
.chips span{background:#fff;border:2px solid #e4e2db;border-radius:999px;padding:10px 26px;font-size:30px;font-weight:500;color:#3b414b}
.save{font-size:32px;color:#6a707a;margin:0}
.foot{display:flex;justify-content:space-between;align-items:center;margin-top:36px;font-size:30px;color:#6a707a}
.dots{display:flex;gap:12px}.dots i{width:16px;height:16px;border-radius:50%;background:#d3d0c7}.dots i.on{background:#b8102a;width:44px;border-radius:8px}
.swipe{font-weight:500;color:#b8102a}
.site{direction:ltr;font-family:Lexend}
</style></head><body><div class="frame">
<div class="top"><div class="brand">${LOGO}<span>Info<b>Pour</b>Bac</span></div><div class="count">${String(i + 1).padStart(2, '0')} / ${String(n).padStart(2, '0')}</div></div>
<div class="main">${main}</div>
<div class="foot"><div class="dots">${Array.from({ length: n }, (_, k) => `<i class="${k === i ? 'on' : ''}"></i>`).join('')}</div>
<span class="${last ? 'site' : 'swipe'}">${last ? SITE : '👈 اسحب'}</span></div>
</div></body></html>`;
}

(async () => {
  const b = await puppeteer.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: 'new' });
  const p = await b.newPage();
  const problems = [];
  // Échauffement : charge les polices une première fois pour que la première vraie slide les ait déjà.
  await p.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 1 });
  await p.setContent(page(CAROUSELS[0].slides[0], 0, 5, 'instagram'), { waitUntil: 'domcontentloaded' });
  await p.evaluate(() => new Promise(r => setTimeout(r, 4000)));
  for (const fmt of Object.keys(FORMATS)) {
    const F = FORMATS[fmt];
    await p.setViewport({ width: F.w, height: F.h, deviceScaleFactor: 1 });
    for (const c of CAROUSELS) {
      const dir = path.join(OUT, fmt, c.id);
      fs.mkdirSync(dir, { recursive: true });
      for (let i = 0; i < c.slides.length; i++) {
        await p.setContent(page(c.slides[i], i, c.slides.length, fmt), { waitUntil: 'domcontentloaded' });
        await p.evaluate(() => Promise.race([Promise.all([
          document.fonts.load('700 40px "IBM Plex Sans Arabic"'), document.fonts.load('600 40px "IBM Plex Sans Arabic"'),
          document.fonts.load('300 40px "IBM Plex Sans Arabic"'), document.fonts.load('400 40px "IBM Plex Sans Arabic"'),
          document.fonts.load('600 40px Lexend'), document.fonts.load('500 40px Lexend'), document.fonts.load('400 40px Lexend'),
          document.fonts.load('600 40px "IBM Plex Mono"'), document.fonts.load('500 40px "IBM Plex Mono"'),
        ]).then(() => document.fonts.ready), new Promise(r => setTimeout(r, 8000))]));
        const over = await p.evaluate(() => {
          const m = document.querySelector('.main'), f = document.querySelector('.foot');
          const wide = [...document.querySelectorAll('.main *')].some(e => { const r = e.getBoundingClientRect(); return r.right > innerWidth - 40 || r.left < 40; });
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
