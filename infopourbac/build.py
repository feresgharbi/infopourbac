"""Génère le site statique InfoPourBac dans le dossier public/.

Usage :  python build.py
Pour changer de domaine, modifie BASE ci-dessous puis relance.
"""
import json
import os
import re
import shutil
import sys
from html import escape, unescape

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, 'content'))

from h import DUO  # noqa: E402
from cours1 import CHAPTERS_A  # noqa: E402
from cours2 import CHAPTERS_B  # noqa: E402
from pages import ALGOS, GLOSSAIRE  # noqa: E402
from figs import build_figs  # noqa: E402
from thumbs import thumb  # noqa: E402

BASE = 'https://infopourbac.netlify.app'
SITE = 'InfoPourBac'
UPDATED = '2026-11-19'
UPDATED_FR = '19 novembre 2026'
OUT = os.path.join(ROOT, 'public')

CHAPTERS = CHAPTERS_A + CHAPTERS_B
for i, ch in enumerate(CHAPTERS, 1):
    ch['n'] = i
REFS = [ALGOS]
FIGS = build_figs()
NFIGS = sum(len(v) for v in FIGS.values())


def with_figs(slug, sid, x):
    """Place les schémas de la section après son premier paragraphe (ou en tête)."""
    f = ''.join(FIGS.pop((slug, sid), []))
    if not f:
        return x
    if x.startswith('<p') and '</p>' in x:
        k = x.index('</p>') + 4
        return x[:k] + f + x[k:]
    return f + x

ORG = {'@type': 'Organization', '@id': BASE + '/#org', 'name': SITE, 'url': BASE + '/',
       'logo': {'@type': 'ImageObject', 'url': BASE + '/assets/logo.png', 'width': 512, 'height': 512},
       'description': "Plateforme tunisienne de cours d'informatique pour le Bac scientifique : algorithmique et Python."}


def url(slug):
    return BASE + '/' + (slug.strip('/') + '/' if slug.strip('/') else '')


def href(slug):
    return '/' + (slug.strip('/') + '/' if slug.strip('/') else '')


def text_of(html):
    t = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', html, flags=re.S)
    t = re.sub(r'<br\s*/?>|</(p|li|h[1-6]|tr|pre|figure|div)>', '\n', t)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = unescape(t)
    t = re.sub(r'[ \t]+', ' ', t)
    return re.sub(r'\n\s*\n+', '\n\n', t).strip()


def minutes(html):
    return max(3, round(len(text_of(html).split()) / 180))


def ld(obj):
    return '<script type="application/ld+json">%s</script>' % json.dumps(obj, ensure_ascii=False, separators=(',', ':'))


LOGO_SVG = ('<svg class="logo" viewBox="0 0 40 40" aria-hidden="true"><rect width="40" height="40" rx="10" fill="#c8102e"/>'
            '<path d="M15 12l-6 8 6 8M25 12l6 8-6 8" stroke="#fff" stroke-width="3.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')

NAV = [('cours/', 'Cours'), ('algorithmes-classiques/', 'Algorithmes'), ('glossaire/', 'Glossaire')]


NB_RE = re.compile(r'(<(pre|script|style|code|textarea)\b.*?</\2>|<[^>]+>)', re.S)


def fr_typo(html):
    """Espaces insécables avant : ; ? ! et à l'intérieur des guillemets, hors code et balises."""
    out = []
    parts = NB_RE.split(html)
    i = 0
    while i < len(parts):
        t = parts[i]
        if i % 3 == 0:
            t = re.sub(r' ([:;?!»])', '\u00a0\\1', t)
            t = t.replace('« ', '«\u00a0')
            out.append(t)
            i += 1
        else:
            out.append(t)
            i += 2
    return ''.join(out)


def layout(slug, title, desc, body, schema, og_type='article', crumbs=None):
    canonical = url(slug)
    nav = ''.join('<a href="/%s"%s>%s</a>' % (p, ' aria-current="page"' if slug.startswith(p.strip('/')) and p.strip('/') else '', t) for p, t in NAV)
    bc = ''
    if crumbs:
        items = ''.join('<li><a href="%s">%s</a></li>' % (h, escape(t)) for h, t in crumbs[:-1]) + '<li aria-current="page">%s</li>' % escape(crumbs[-1][1])
        bc = '<nav class="crumbs" aria-label="Fil d\'Ariane"><ol>%s</ol></nav>' % items
        schema = schema + [{'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'name': t, 'item': BASE + h} for i, (h, t) in enumerate(crumbs)]}]
    if bc and '<header class="chead">' in body:
        body = body.replace('<header class="chead">', '<header class="chead">' + bc, 1)
        bc = ''
    footer_ch = ''.join('<li><a href="%s">%d. %s</a></li>' % (href(c['slug']), c['n'], escape(c['short'])) for c in CHAPTERS)
    return f'''<!doctype html>
<html lang="fr-TN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="fr-TN" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="{canonical}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<meta name="author" content="{SITE}">
<meta name="theme-color" content="#c8102e">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{SITE}">
<meta property="og:locale" content="fr_TN">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE}/assets/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(title)}">
<meta name="twitter:description" content="{escape(desc)}">
<meta name="twitter:image" content="{BASE}/assets/og.png">
<meta name="geo.region" content="TN">
<meta name="geo.placename" content="Tunisie">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/assets/logo.png" type="image/png" sizes="512x512">
<link rel="apple-touch-icon" href="/assets/logo.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/assets/style.css">
{ld({'@context': 'https://schema.org', '@graph': schema})}
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="site-header">
  <div class="wrap hdr">
    <a class="brand" href="/" aria-label="{SITE}, accueil">{LOGO_SVG}<span>Info<b>Pour</b>Bac</span></a>
    <nav class="mainnav" aria-label="Navigation principale">{nav}</nav>
  </div>
</header>
<main id="contenu">
{bc}
{fr_typo(body)}
</main>
<footer class="site-footer">
  <div class="wrap fgrid">
    <div>
      <a class="brand" href="/">{LOGO_SVG}<span>Info<b>Pour</b>Bac</span></a>
      <p>Cours d'informatique pour le baccalauréat scientifique en Tunisie : algorithmique et Python, chapitre par chapitre.</p>
    </div>
    <div><h2>Le cours</h2><ol class="flist">{footer_ch}</ol></div>
    <div><h2>Ressources</h2><ul class="flist">
      <li><a href="/algorithmes-classiques/">Algorithmes classiques</a></li>
      <li><a href="/glossaire/">Glossaire</a></li>
      <li><a href="/a-propos/">À propos</a></li>
    </ul></div>
  </div>
  <div class="wrap fbottom">© 2026 {SITE} · Mis à jour le {UPDATED_FR}</div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
'''


def article_page(p, prev=None, nxt=None, kind='Cours'):
    """Page de chapitre ou de référence."""
    pre = ('%d.' % p['n']) if 'n' in p else ''
    body_html = ''.join('<section id="%s"><h2><span class="secn">%s%d</span>%s</h2>%s</section>' % (i, pre, k, escape(h), with_figs(p['slug'], i, x))
                        for k, (i, h, x) in enumerate(p['body'], 1))
    mins = minutes(p['lead'] + body_html)
    toc = ''.join('<li><a href="#%s"><span>%s%d</span>%s</a></li>' % (i, pre, k, escape(h)) for k, (i, h, _) in enumerate(p['body'], 1))
    toc += '<li><a href="#a-retenir"><span>★</span>À retenir</a></li><li><a href="#faq"><span>?</span>Questions fréquentes</a></li>'
    bref = ''.join('<li>%s</li>' % b for b in p['bref'])
    ret = ''.join('<li>%s</li>' % r for r in p['retenir'])
    faq = ''.join('<details><summary>%s</summary><div>%s</div></details>' % (escape(q), a) for q, a in p['faq'])
    kicker = ('Chapitre %d sur %d' % (p['n'], len(CHAPTERS))) if 'n' in p else 'Pour le Bac'
    pn = ''
    if prev or nxt:
        pn = '<nav class="prevnext" aria-label="Chapitres">%s%s</nav>' % (
            '<a class="pv" href="%s"><small>← Précédent</small><b>%s</b></a>' % (href(prev['slug']), escape(prev['h1'])) if prev else '<span></span>',
            '<a class="nx" href="%s"><small>Suivant →</small><b>%s</b></a>' % (href(nxt['slug']), escape(nxt['h1'])) if nxt else '<span></span>')
    side = ''.join('<li><a href="%s"%s><span>%d</span>%s</a></li>' % (href(c['slug']), ' aria-current="page"' if c is p else '', c['n'], escape(c['short'])) for c in CHAPTERS)
    side_ref = ''.join('<li><a href="%s"%s>%s</a></li>' % (href(r['slug']), ' aria-current="page"' if r is p else '', escape(r['short'])) for r in REFS)
    side_ref += '<li><a href="/glossaire/">Glossaire</a></li>'
    key = p['n'] if 'n' in p else p['slug']
    if 'n' in p:
        ticks = ''.join('<i%s></i>' % (' class="done"' if c['n'] < p['n'] else (' class="now"' if c is p else '')) for c in CHAPTERS)
        prog = '<div class="prog" aria-hidden="true">%s</div>' % ticks
        num = '%02d' % p['n']
    else:
        prog, num = '', ''
    body = f'''
<header class="chead">
  <div class="wrap cheadgrid">
    <div class="cheadtext">
      <p class="chapnum">{'<b class="bignum">' + num + '</b>' if num else ''}<span>{kicker}</span></p>
      {prog}
      <h1>{escape(p['h1'])}</h1>
      <p class="meta">{mins} min de lecture · {len(p['body'])} parties · mis à jour le <time datetime="{UPDATED}">{UPDATED_FR}</time></p>
    </div>
    <div class="cheadart">{thumb(key)}</div>
  </div>
</header>
<div class="wrap docgrid">
  <nav class="side" aria-label="Chapitres du cours">
    <p class="side-t">Le cours</p><ol class="side-list">{side}</ol>
    <p class="side-t">Pour le Bac</p><ul class="side-list ref">{side_ref}</ul>
  </nav>
  <article class="article">
    <p class="lead">{p['lead']}</p>
    <div class="bref"><h2>L'essentiel</h2><ul>{bref}</ul></div>
    <details class="onpage"><summary>Dans cette page</summary><ol>{toc}</ol></details>
    {body_html}
    <section id="a-retenir" class="retenir"><h2>À retenir</h2><ul>{ret}</ul></section>
    <section id="faq" class="faq"><h2>Questions fréquentes</h2>{faq}</section>
    {pn}
  </article>
  <nav class="toc" aria-label="Dans cette page"><p class="side-t">Dans cette page</p><ol>{toc}</ol></nav>
</div>'''
    crumbs = [('/', 'Accueil')]
    if 'n' in p:
        crumbs.append(('/cours/', 'Cours'))
    crumbs.append((href(p['slug']), p['short']))
    art = {'@type': ['Article', 'LearningResource'], '@id': url(p['slug']) + '#article', 'headline': p['h1'],
           'description': p['desc'], 'inLanguage': 'fr-TN', 'datePublished': UPDATED, 'dateModified': UPDATED,
           'author': {'@id': BASE + '/#org'}, 'publisher': {'@id': BASE + '/#org'},
           'mainEntityOfPage': url(p['slug']), 'image': BASE + '/assets/og.png',
           'learningResourceType': kind, 'educationalLevel': '4ème année secondaire – Baccalauréat (sections scientifiques)',
           'audience': {'@type': 'EducationalAudience', 'educationalRole': 'student'},
           'timeRequired': 'PT%dM' % mins, 'isAccessibleForFree': True,
           'about': [{'@type': 'Thing', 'name': x} for x in ('Algorithmique', 'Python', 'Baccalauréat tunisien')],
           'articleSection': [h for _, h, _ in p['body']]}
    if 'n' in p:
        art['isPartOf'] = {'@id': BASE + '/cours/#course'}
        art['position'] = p['n']
    faq_ld = {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': text_of(a)}} for q, a in p['faq']]}
    return layout(p['slug'], p['title'], p['desc'], body, [ORG, art, faq_ld], crumbs=crumbs), mins


def home_page():
    demo = DUO('''
        Pour i de 1 à n Faire
            Si i MOD 2 = 0 Alors
                Écrire(i, " est pair")
            Fin Si
        Fin Pour''', '''
        for i in range(1, n + 1):
            if i % 2 == 0:
                print(i, "est pair")''')
    faq = [
        ("Que contient le programme d'informatique du Bac scientifique en Tunisie ?",
         "Les bases de l'algorithmique et de la programmation en Python : variables et types, entrées-sorties, structures conditionnelles et itératives, chaînes de caractères, sous-programmes (fonctions et procédures), tableaux, algorithmes de tri et de recherche, et interfaces graphiques avec Qt Designer et PyQt5."),
        ("Quel langage de programmation est utilisé au Bac informatique en Tunisie ?",
         "Python 3. Les tableaux sont créés avec la bibliothèque numpy et les interfaces graphiques avec PyQt5 et Qt Designer."),
        ("Pourquoi apprendre l'algorithme et le Python en même temps ?",
         "Parce que le programme officiel décrit les solutions en notation algorithmique (Début, Fin, Si, Pour, Tant que…) et que l'épreuve pratique se fait en Python. Savoir passer de l'un à l'autre est indispensable ; chaque notion est donc présentée dans les deux langages, côte à côte."),
        ("Comment réviser l'informatique pour le Bac ?",
         "Suis les chapitres dans l'ordre, lis l'encadré « En bref » puis la partie « À retenir » de chaque page, apprends les algorithmes classiques (premier, PGCD, palindrome, binaire) et entraîne-toi à écrire une interface PyQt5 avec un module Play complet."),
        ("Ce site prépare-t-il à l'épreuve pratique ?",
         "Oui : un chapitre entier traite des interfaces graphiques PyQt5 et du module Play, et la page des algorithmes classiques réunit les fonctions qui reviennent dans les sujets (premier, PGCD, palindrome, binaire)."),
    ]
    faq_html = ''.join('<details><summary>%s</summary><div>%s</div></details>' % (escape(q), a) for q, a in faq)
    groups = [('Les bases', [1, 2, 3, 4]), ('Les structures', [5, 6]), ('La modularité', [7, 8]), ('Trier, chercher, afficher', [9, 10, 11])]
    by = {c['n']: c for c in CHAPTERS}

    def card(c):
        return (f'''<li><a class="card" href="{href(c['slug'])}"><span class="art">{thumb(c['n'])}</span>'''
                f'''<span class="cbody"><span class="ck">Chapitre {c['n']} · {c['mins']} min</span><span class="ct">{escape(c['short'])}</span></span></a></li>''')
    prog = ''.join(f'''<div class="pstep"><h3><b>{g}</b>{escape(t)}</h3><ol class="cards">{''.join(card(by[n]) for n in ns)}</ol></div>'''
                   for g, (t, ns) in enumerate(groups, 1))
    refs = [('/algorithmes-classiques/', 'algorithmes-classiques', 'Algorithmes classiques', 'Premier, PGCD, chiffres, palindrome, binaire : les fonctions qui reviennent dans les sujets.'),
            ('/glossaire/', 'glossaire', 'Glossaire', f'{len(GLOSSAIRE)} mots expliqués simplement : TDO, MOD, procédure, objectName…')]
    ref_cards = ''.join(f'''<li><a class="card wide" href="{h}"><span class="art">{thumb(k)}</span><span class="cbody"><span class="ct">{t}</span><span class="cd">{d}</span></span></a></li>''' for h, k, t, d in refs)
    body = f'''
<section class="hero">
  <div class="wrap herogrid">
    <div class="herotext">
      <p class="eyebrow"><span class="flag" aria-hidden="true"></span>Bac scientifique · Tunisie · 4ᵉ année</p>
      <h1>L'informatique du Bac, <em>expliquée simplement.</em></h1>
      <p class="lead">Tout le programme en {len(CHAPTERS)} chapitres courts, avec des schémas. Pour chaque notion, l'algorithme et le code Python sont côte à côte.</p>
      <p class="cta"><a class="btn primary" href="{href(CHAPTERS[0]['slug'])}">Commencer le cours <span aria-hidden="true">→</span></a><a class="btn" href="/algorithmes-classiques/">Algorithmes classiques</a></p>
    </div>
    <div class="herocode">
      {demo}
    </div>
  </div>
  <div class="wrap">
    <ul class="stats">
      <li><b>{len(CHAPTERS)}</b><span>chapitres</span></li>
      <li><b>{NFIGS}</b><span>schémas et graphiques</span></li>
      <li><b>8</b><span>algorithmes du Bac</span></li>
      <li><b>0 DT</b><span>gratuit, sans inscription</span></li>
    </ul>
  </div>
</section>
<section class="wrap block" id="programme" aria-labelledby="t-prog">
  <div class="bhead"><h2 id="t-prog">Le programme, en 4 étapes</h2><p>Suis les chapitres dans l'ordre : chacun s'appuie sur le précédent.</p></div>
  <div class="psteps">{prog}</div>
</section>
<section class="band">
  <div class="wrap block" aria-labelledby="t-how">
    <div class="bhead"><h2 id="t-how">Comment réviser avec ce site</h2></div>
    <ol class="how">
      <li><b>Lis « L'essentiel »</b>En haut de chaque chapitre : les idées importantes en quelques lignes.</li>
      <li><b>Regarde les schémas</b>Organigrammes, tableaux en barres, déroulements pas à pas : la notion en une image.</li>
      <li><b>Compare l'algorithme et le Python</b>Ils sont toujours côte à côte, ligne par ligne.</li>
      <li><b>Relis « À retenir »</b>La veille de l'épreuve. C'est fait pour ça.</li>
    </ol>
  </div>
</section>
<section class="wrap block" aria-labelledby="t-ref">
  <div class="bhead"><h2 id="t-ref">Pour le jour du Bac</h2></div>
  <ul class="cards refs">{ref_cards}</ul>
</section>
<section class="wrap block faq narrowfaq" aria-labelledby="t-faq">
  <h2 id="t-faq">Questions fréquentes</h2>
  {faq_html}
</section>'''
    course = course_ld()
    web = {'@type': 'WebSite', '@id': BASE + '/#website', 'url': BASE + '/', 'name': SITE, 'inLanguage': 'fr-TN',
           'publisher': {'@id': BASE + '/#org'},
           'description': "Cours d'informatique pour le Bac scientifique en Tunisie : algorithmique et Python."}
    faq_ld = {'@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq]}
    return layout('', "Informatique Bac Sciences Tunisie : algorithme et Python",
                  "Le cours complet d'informatique du Bac scientifique en Tunisie : algorithme et Python côte à côte, des bases aux tris, tableaux numpy et interfaces PyQt5.",
                  body, [ORG, web, course, faq_ld], og_type='website')


def course_ld():
    return {'@type': 'Course', '@id': BASE + '/cours/#course', 'name': "Informatique – Bac scientifique (Tunisie) : algorithmique et Python",
            'description': "Cours complet d'informatique pour la 4ème année secondaire des sections scientifiques en Tunisie : algorithmique, Python, tableaux numpy, tris, recherche et interfaces PyQt5.",
            'url': BASE + '/cours/', 'inLanguage': 'fr-TN', 'provider': {'@id': BASE + '/#org'},
            'educationalLevel': '4ème année secondaire', 'isAccessibleForFree': True,
            'teaches': [c['h1'] for c in CHAPTERS],
            'hasCourseInstance': {'@type': 'CourseInstance', 'courseMode': 'online', 'courseWorkload': 'PT%dM' % sum(c['mins'] for c in CHAPTERS)},
            'offers': {'@type': 'Offer', 'price': 0, 'priceCurrency': 'TND', 'category': 'Free'},
            'hasPart': [{'@type': 'LearningResource', 'name': c['h1'], 'url': url(c['slug'])} for c in CHAPTERS]}


def cours_index():
    rows = ''.join(f'''<li><a class="card row" href="{href(c['slug'])}"><span class="art">{thumb(c['n'])}</span><span class="cbody"><span class="ck">Chapitre {c['n']} · {c['mins']} min</span><span class="ct">{escape(c['h1'])}</span><span class="cd">{escape(c['desc'])}</span></span></a></li>''' for c in CHAPTERS)
    body = f'''
<header class="chead">
  <div class="wrap cheadgrid">
    <div class="cheadtext">
      <p class="chapnum"><span>Programme complet · {len(CHAPTERS)} chapitres</span></p>
      <h1>Cours d'informatique du Bac scientifique</h1>
      <p class="meta">4ᵉ année secondaire · sections Mathématiques, Sciences expérimentales et Sciences techniques</p>
    </div>
    <div class="cheadart">{thumb(1)}</div>
  </div>
</header>
<div class="wrap narrow">
  <p class="lead pagelead">Les {len(CHAPTERS)} chapitres du programme, dans l'ordre conseillé. Chaque notion est présentée en notation algorithmique officielle et en Python, avec des schémas.</p>
  <ol class="cards list">{rows}</ol>
</div>'''
    itemlist = {'@type': 'ItemList', 'itemListElement': [{'@type': 'ListItem', 'position': c['n'], 'url': url(c['slug']), 'name': c['h1']} for c in CHAPTERS]}
    return layout('cours', "Cours d'informatique Bac Sciences : les 11 chapitres",
                  "Le programme d'informatique du Bac scientifique en Tunisie en 11 chapitres : algorithmique, Python, boucles, fonctions, tableaux, tris, recherche, PyQt5.",
                  body, [ORG, course_ld(), itemlist], og_type='website', crumbs=[('/', 'Accueil'), ('/cours/', 'Cours')])


def glossaire_page():
    terms = sorted(GLOSSAIRE, key=lambda t: t[0].lower())
    letters = sorted({t[0][0].upper() for t in terms})
    items = ''.join('<div class="term" id="%s"><dt>%s</dt><dd>%s</dd></div>' % (re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-'), escape(t), escape(d)) for t, d in terms)
    body = f'''
<header class="chead">
  <div class="wrap cheadgrid">
    <div class="cheadtext">
      <p class="chapnum"><span>Pour le Bac · {len(terms)} mots</span></p>
      <h1>Glossaire de l'informatique au Bac</h1>
      <p class="meta">De « Accumulateur » à « Variable » : les mots du programme, expliqués simplement.</p>
    </div>
    <div class="cheadart">{thumb('glossaire')}</div>
  </div>
</header>
<div class="wrap narrow">
  <p class="lead pagelead">{len(terms)} définitions courtes des mots de l'algorithmique et de Python que l'on rencontre dans le programme et dans les sujets du baccalauréat tunisien.</p>
  <p class="letters">{' '.join(letters)}</p>
  <dl class="gloss">{items}</dl>
</div>'''
    dts = {'@type': 'DefinedTermSet', '@id': BASE + '/glossaire/#set', 'name': "Glossaire de l'informatique au Bac", 'inLanguage': 'fr-TN',
           'hasDefinedTerm': [{'@type': 'DefinedTerm', 'name': t, 'description': d, 'url': BASE + '/glossaire/#' + re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')} for t, d in terms]}
    return layout('glossaire', "Glossaire informatique du Bac : TDO, MOD, procédure…",
                  "Définitions simples des termes d'algorithmique et de Python du Bac scientifique en Tunisie : TDO, TDNT, MOD, DIV, procédure, objectName, dichotomie.",
                  body, [ORG, dts], crumbs=[('/', 'Accueil'), ('/glossaire/', 'Glossaire')])


def about_page():
    body = f'''
<div class="wrap narrow prose">
  <header class="ahead"><p class="chapnum">À propos</p><h1>À propos d'{SITE}</h1>
  <p class="lead">{SITE} est une plateforme tunisienne consacrée à l'informatique du baccalauréat scientifique. Son objectif : rendre l'algorithmique et Python compréhensibles par tous les élèves, y compris ceux qui pensent que « l'informatique, ce n'est pas pour eux ».</p></header>
  <h2>Notre approche</h2>
  <ul><li>Un cours structuré qui suit le programme officiel de 4ᵉ année secondaire des sections scientifiques.</li>
  <li>La notation algorithmique officielle et sa traduction Python présentées côte à côte.</li>
  <li>Des pages courtes, avec un résumé au début et l'essentiel à retenir à la fin.</li></ul>
  <h2>Nos sources</h2>
  <p>Le contenu s'appuie sur le guide « Python pour le Bac Scientifique : guide simplifié pour les bacheliers », sur le programme officiel et sur les sujets officiels de l'épreuve pratique d'informatique (sessions 2022 à 2025).</p>
  <h2>Mises à jour</h2>
  <p>Les pages sont revues régulièrement. Dernière mise à jour : <time datetime="{UPDATED}">{UPDATED_FR}</time>.</p>
</div>'''
    about = {'@type': 'AboutPage', 'url': url('a-propos'), 'name': "À propos d'" + SITE, 'about': {'@id': BASE + '/#org'}}
    return layout('a-propos', "À propos d'InfoPourBac | Informatique Bac Tunisie",
                  "InfoPourBac rend l'informatique du Bac scientifique accessible à tous les élèves tunisiens : algorithmique et Python expliqués simplement.",
                  body, [ORG, about], og_type='website', crumbs=[('/', 'Accueil'), ('/a-propos/', 'À propos')])


def notfound_page():
    body = '''<div class="wrap narrow"><header class="ahead"><p class="chapnum">Erreur 404</p><h1>Cette page n'existe pas</h1>
    <p class="lead">Le lien est peut-être ancien. Reprends depuis le <a href="/cours/">sommaire du cours</a> ou la <a href="/">page d'accueil</a>.</p></header></div>'''
    return layout('404.html', 'Page introuvable | ' + SITE, "La page demandée n'existe pas.", body, [ORG]).replace(
        '<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">', '<meta name="robots" content="noindex">')


def write(rel, content, binary=False):
    path = os.path.join(OUT, *rel.split('/'))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb' if binary else 'w', encoding=None if binary else 'utf-8', newline='\n') as f:
        f.write(content)


def main():
    if os.path.isdir(OUT):
        for name in os.listdir(OUT):
            if name == 'assets':
                continue
            p = os.path.join(OUT, name)
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    os.makedirs(os.path.join(OUT, 'assets'), exist_ok=True)
    shutil.copy(os.path.join(ROOT, 'static', 'style.css'), os.path.join(OUT, 'assets', 'style.css'))
    shutil.copy(os.path.join(ROOT, 'static', 'site.js'), os.path.join(OUT, 'assets', 'site.js'))
    shutil.copy(os.path.join(ROOT, 'static', 'favicon.svg'), os.path.join(OUT, 'favicon.svg'))

    pages = []
    for i, ch in enumerate(CHAPTERS):
        html, ch['mins'] = article_page(ch, CHAPTERS[i - 1] if i else None, CHAPTERS[i + 1] if i + 1 < len(CHAPTERS) else None)
        pages.append((ch['slug'], html, '0.9'))
    for r in REFS:
        html, r['mins'] = article_page(r, kind='Guide de référence')
        pages.append((r['slug'], html, '0.9'))
    if FIGS:
        raise SystemExit('Figures sans section correspondante : %s' % sorted(FIGS))
    pages = [('', home_page(), '1.0'), ('cours', cours_index(), '0.9')] + pages + [
        ('glossaire', glossaire_page(), '0.7'), ('a-propos', about_page(), '0.4')]
    for slug, html, _ in pages:
        write((slug + '/' if slug else '') + 'index.html', html)
    write('404.html', notfound_page())

    sm = ''.join('<url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>' % (url(s), UPDATED, pr) for s, _, pr in pages)
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">%s</urlset>\n' % sm)
    bots = ['Googlebot', 'Bingbot', 'GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User',
            'PerplexityBot', 'Perplexity-User', 'Google-Extended', 'Applebot-Extended', 'CCBot']
    write('robots.txt', '# Les moteurs de recherche et les assistants IA sont les bienvenus.\nUser-agent: *\nAllow: /\n\n'
          + ''.join('User-agent: %s\nAllow: /\n\n' % b for b in bots) + 'Sitemap: %s/sitemap.xml\n' % BASE)
    write('site.webmanifest', json.dumps({'name': SITE, 'short_name': SITE, 'lang': 'fr-TN', 'start_url': '/', 'display': 'standalone',
                                          'background_color': '#fbfaf7', 'theme_color': '#c8102e',
                                          'icons': [{'src': '/assets/logo.png', 'sizes': '512x512', 'type': 'image/png'}]}, ensure_ascii=False, indent=2))

    # llms.txt : un plan lisible par les assistants IA ; llms-full.txt : tout le texte du cours.
    L = ['# %s' % SITE, '',
         "> Cours d'informatique pour le baccalauréat scientifique en Tunisie (4ème année secondaire : sections Mathématiques, Sciences expérimentales, Sciences techniques). Chaque notion est présentée en notation algorithmique officielle tunisienne et en Python 3, côte à côte. Tableaux avec numpy, interfaces graphiques avec Qt Designer et PyQt5.",
         '', '## Cours (dans l\'ordre)', '']
    L += ['- [%s](%s): %s' % (c['h1'], url(c['slug']), c['desc']) for c in CHAPTERS]
    L += ['', '## Ressources', '']
    L += ['- [%s](%s): %s' % (r['h1'], url(r['slug']), r['desc']) for r in REFS]
    L += ['- [Glossaire](%s): définitions des termes d\'algorithmique et de Python du programme.' % url('glossaire'), '',
          '## Optional', '', '- [Texte intégral du cours](%s/llms-full.txt)' % BASE, '']
    write('llms.txt', '\n'.join(L))
    full = ['# %s : texte intégral du cours' % SITE, '', 'Source : %s — mis à jour le %s.' % (BASE, UPDATED_FR), '']
    for p in CHAPTERS + REFS:
        full += ['', '=' * 70, '# ' + p['h1'], 'URL : ' + url(p['slug']), '', text_of(p['lead']), '', 'En bref :']
        full += ['- ' + text_of(b) for b in p['bref']]
        for _, h, x in p['body']:
            full += ['', '## ' + h, '', text_of(x)]
        full += ['', '## À retenir'] + ['- ' + text_of(r) for r in p['retenir']]
        full += ['', '## Questions fréquentes'] + ['Q : %s\nR : %s' % (q, text_of(a)) for q, a in p['faq']]
    full += ['', '=' * 70, '# Glossaire', ''] + ['- %s : %s' % (t, d) for t, d in sorted(GLOSSAIRE)]
    write('llms-full.txt', '\n'.join(full) + '\n')
    print('%d pages générées dans %s' % (len(pages) + 1, OUT))


if __name__ == '__main__':
    main()
