"""Petits outils pour écrire le contenu des cours : blocs de code colorés, tableaux, encadrés."""
import html
import re

esc = html.escape

# ---------------------------------------------------------------- Python
PY_RE = re.compile(
    r'(?P<c>#[^\n]*)'
    r'|(?P<s>"[^"\n]*"|\'[^\'\n]*\')'
    r'|(?P<k>\b(?:def|return|if|elif|else|for|in|while|break|and|or|not|True|False|None|from|import|as|match|case|global)\b)'
    r'|(?P<b>\b(?:print|input|int|float|str|bool|len|range|type|abs|round|array|sqrt|randint|ord|chr|loadUi|QApplication)\b)'
    r'|(?P<n>\b\d+(?:\.\d+)?\b)'
)


def hl_py(code):
    out, last = [], 0
    for m in PY_RE.finditer(code):
        out.append(esc(code[last:m.start()], quote=False))
        out.append('<span class="t-%s">%s</span>' % (m.lastgroup, esc(m.group(), quote=False)))
        last = m.end()
    out.append(esc(code[last:], quote=False))
    return ''.join(out)


# ---------------------------------------------------------------- Algorithme (notation tunisienne)
ALGO_KW = [
    "Fin Tant que", "Fin Pour", "Fin Si", "Fin Selon", "Sinon Si", "Tant que", "Jusqu'à",
    "Algorithme", "Début", "Fin", "Si", "Alors", "Sinon", "Selon", "Pour", "de", "à", "pas", "Faire",
    "Répéter", "Fonction", "Procédure", "Retourner", "Lire", "Écrire", "ET", "OU", "NON", "DIV", "MOD",
]
ALGO_T = ["Entier", "Réel", "Booléen", "Caractère", "Chaîne", "Tableau", "Vrai", "Faux"]
ALGO_RE = re.compile(
    r'(?P<s>"[^"\n]*")'
    r'|(?P<k>(?<![\wÀ-ÿ])(?:' + '|'.join(re.escape(k) for k in ALGO_KW) + r')(?![\wÀ-ÿ]))'
    r'|(?P<b>(?<![\wÀ-ÿ])(?:' + '|'.join(ALGO_T) + r')(?![\wÀ-ÿ]))'
    r'|(?P<a>←|≠|≤|≥)'
    r'|(?P<n>\b\d+(?:\.\d+)?\b)'
)


def hl_algo(code):
    out, last = [], 0
    for m in ALGO_RE.finditer(code):
        out.append(esc(code[last:m.start()], quote=False))
        out.append('<span class="t-%s">%s</span>' % (m.lastgroup, esc(m.group(), quote=False)))
        last = m.end()
    out.append(esc(code[last:], quote=False))
    return ''.join(out)


def _clean(code):
    lines = code.strip('\n').split('\n')
    ind = min((len(l) - len(l.lstrip()) for l in lines if l.strip()), default=0)
    return '\n'.join(l[ind:] for l in lines)


def P(code, cap='Python'):
    """Bloc de code Python."""
    code = _clean(code)
    return ('<figure class="code py"><figcaption><span>%s</span><button class="copy" type="button">Copier</button></figcaption>'
            '<pre><code class="language-python">%s</code></pre></figure>') % (esc(cap), hl_py(code))


def A(code, cap='Algorithme'):
    """Bloc d'algorithme en notation du programme tunisien."""
    code = _clean(code)
    return ('<figure class="code al"><figcaption><span>%s</span></figcaption>'
            '<pre><code class="language-algo">%s</code></pre></figure>') % (esc(cap), hl_algo(code))


def DUO(algo, py, cap_a='Algorithme', cap_p='Traduction en Python'):
    """Algorithme et Python côte à côte."""
    return '<div class="duo">%s%s</div>' % (A(algo, cap_a), P(py, cap_p))


def T(head, rows, cap=None, cls=''):
    """Tableau. Les cellules sont du HTML."""
    h = ''.join('<th scope="col">%s</th>' % c for c in head)
    b = ''.join('<tr>%s</tr>' % ''.join('<td>%s</td>' % c for c in r) for r in rows)
    c = '<caption>%s</caption>' % cap if cap else ''
    return '<div class="tablewrap"><table class="%s">%s<thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (cls, c, h, b)


def TDO(rows, title='Tableau de déclaration des objets (TDO)'):
    return T(['Objet', 'Type / Nature'], [['<code>%s</code>' % o, t] for o, t in rows], cap=title, cls='tdo')


def NOTE(x, t='À savoir'):
    return '<aside class="box note"><strong>%s</strong><div>%s</div></aside>' % (t, x)


def WARN(x, t='Attention, piège fréquent'):
    return '<aside class="box warn"><strong>%s</strong><div>%s</div></aside>' % (t, x)


def TIP(x, t='Astuce pour le Bac'):
    return '<aside class="box tip"><strong>%s</strong><div>%s</div></aside>' % (t, x)


def DEF(term, x):
    return '<p class="def"><dfn>%s</dfn> : %s</p>' % (term, x)


def UL(items):
    return '<ul>%s</ul>' % ''.join('<li>%s</li>' % i for i in items)


def OL(items):
    return '<ol>%s</ol>' % ''.join('<li>%s</li>' % i for i in items)


def c(x):
    """Code en ligne (échappé)."""
    return '<code>%s</code>' % esc(x, quote=False)
