"""Petites illustrations (vignettes) des chapitres et des pages de référence.

Dessinées en SVG avec les couleurs du thème : elles servent sur les cartes de l'accueil et en tête de chaque page.
"""
_n = [0]


def _svg(inner):
    _n[0] += 1
    m = 'th%d' % _n[0]
    return ('<svg class="th" viewBox="0 0 160 100" aria-hidden="true" focusable="false">'
            '<defs><marker id="%s" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto">'
            '<path d="M0 0L10 5L0 10z" class="thh"/></marker></defs>%s</svg>') % (m, inner.replace('MK', 'url(#%s)' % m))


def R(x, y, w, h, c='l', rx=4):
    return '<rect class="%s" x="%g" y="%g" width="%g" height="%g" rx="%g"/>' % (c, x, y, w, h, rx)


def T(x, y, s, c='tx', size=11, anchor='middle'):
    return '<text class="%s" x="%g" y="%g" font-size="%g" text-anchor="%s" dominant-baseline="central">%s</text>' % (c, x, y, size, anchor, s)


def A(x1, y1, x2, y2):
    return '<line class="ln" x1="%g" y1="%g" x2="%g" y2="%g" marker-end="MK"/>' % (x1, y1, x2, y2)


def L(*p, c='ln'):
    return '<polyline class="%s" points="%s"/>' % (c, ' '.join('%g,%g' % q for q in p))


def t1():
    return _svg(R(8, 34, 38, 32) + T(27, 50, '?', 'tx', 18) + A(48, 50, 59, 50)
                + R(61, 34, 38, 32) + L((68, 43), (92, 43), c='ln2') + L((68, 50), (86, 50), c='ln2') + L((68, 57), (90, 57), c='ln2')
                + A(101, 50, 112, 50) + R(114, 34, 38, 32, 'a') + T(133, 50, '&lt;/&gt;', 'ta m', 11))


def t2():
    keys = ''.join(R(12 + (i % 4) * 9, 41 + (i // 4) * 9, 7, 7, 'k', 1.5) for i in range(8))
    return _svg(R(8, 36, 42, 26, 'l', 3) + keys + A(52, 49, 63, 49)
                + R(65, 33, 30, 32, 'a') + T(80, 49, 'x', 'ta m', 15) + A(97, 49, 108, 49)
                + R(110, 32, 42, 30, 'l', 3) + T(131, 47, '17', 'tx m', 11) + L((124, 70), (138, 70)) + L((131, 62), (131, 70)))


def t3():
    return _svg(R(14, 18, 60, 26, 'l') + T(44, 31, '17', 'tx m', 13) + R(86, 18, 60, 26, 'l') + T(116, 31, '3.5', 'tx m', 13)
                + R(14, 56, 60, 26, 'a') + T(44, 69, '"A"', 'ta m', 13) + R(86, 56, 60, 26, 'l') + T(116, 69, 'True', 'tx m', 11))


def t4():
    s = 'BONJO'
    o = ''
    for i, ch in enumerate(s):
        x = 15 + i * 26
        o += R(x, 30, 26, 30, 'a' if i == 2 else 'l', 0) + T(x + 13, 45, ch, 'ta m' if i == 2 else 'tx m', 13) + T(x + 13, 72, str(i), 'mu m', 9)
    return _svg(o)


def t5():
    return _svg('<polygon class="a" points="80,12 112,32 80,52 48,32"/>' + T(80, 32, '?', 'ta', 14)
                + L((48, 32), (30, 32), (30, 62)) + '<line class="ln" x1="30" y1="60" x2="30" y2="64" marker-end="MK"/>'
                + L((112, 32), (130, 32), (130, 62)) + '<line class="ln" x1="130" y1="60" x2="130" y2="64" marker-end="MK"/>'
                + R(10, 66, 40, 22, 'l') + T(30, 77, 'Vrai', 'ok', 9) + R(110, 66, 40, 22, 'l') + T(130, 77, 'Faux', 'mu', 9))


def t6():
    return _svg('<path class="ln" d="M80 18 A32 32 0 1 1 49 58" marker-end="MK"/>'
                + R(62, 38, 36, 24, 'a') + T(80, 50, 'i', 'ta m', 15) + T(124, 22, '+1', 'mu m', 11))


def t7():
    return _svg(A(10, 36, 50, 44) + A(10, 64, 50, 56) + T(10, 28, 'a', 'mu m', 10, 'start') + T(10, 74, 'b', 'mu m', 10, 'start')
                + R(54, 30, 52, 40, 'a', 6) + T(80, 50, 'f( )', 'ta m', 13) + A(108, 50, 132, 50)
                + '<circle class="l" cx="142" cy="50" r="10"/>')


def t8():
    v = [5, 2, 8, 3, 6, 4]
    o = ''
    for i, x in enumerate(v):
        X = 14 + i * 22
        o += R(X, 22, 22, 56, 'l', 0) + R(X + 5, 72 - x * 5.5, 12, x * 5.5, 'b2' if i != 2 else 'a2', 1)
        o += T(X + 11, 87, str(i), 'mu m', 8)
    return _svg(o)


def t9():
    v = [1, 2, 3, 4, 6, 5]
    o = ''
    for i, x in enumerate(v):
        o += R(16 + i * 22, 82 - x * 10, 16, x * 10, 'a2' if i >= 4 else 'b2', 2)
    o += '<path class="ln" d="M112 18 C116 8 130 8 134 18" marker-end="MK"/>'
    return _svg(o)


def t10():
    o = ''
    for i in range(6):
        o += R(14 + i * 22, 50, 22, 26, 'a' if i == 3 else 'l', 0)
    o += '<circle class="ln" cx="91" cy="34" r="13" fill="none" style="stroke-width:2.2"/>' + L((100, 43), (110, 53), c='ln thick')
    return _svg(o)


def t11():
    return _svg(R(14, 12, 132, 76, 'l', 5) + '<path class="b2" d="M14 17a5 5 0 0 1 5-5h122a5 5 0 0 1 5 5v8H14z"/>'
                + R(26, 38, 70, 16, 'k', 2) + R(102, 38, 32, 16, 'a2', 3) + L((26, 70), (90, 70), c='ln2'))


def t_algos():
    pr = {2, 3, 5, 7, 11, 13, 17, 19, 23}
    o = ''
    for k in range(1, 25):
        r, c = divmod(k - 1, 8)
        o += R(14 + c * 17, 20 + r * 21, 15, 18, 'a' if k in pr else 'l', 2)
    return _svg(o)


def t_bac():
    return _svg('<circle class="l" cx="62" cy="50" r="32"/>' + L((62, 50), (62, 28), c='ln thick') + L((62, 50), (78, 58), c='ln thick')
                + '<circle class="a2" cx="62" cy="50" r="3"/>' + T(124, 42, '1 h', 'ta', 18) + T(124, 62, 'Bac', 'mu', 11))


def t_gloss():
    return _svg(R(30, 18, 100, 64, 'l', 4) + L((80, 18), (80, 82), c='ln2') + T(55, 50, 'A', 'ta', 22) + T(105, 50, 'Z', 'tx', 22))


THUMBS = {1: t1, 2: t2, 3: t3, 4: t4, 5: t5, 6: t6, 7: t7, 8: t8, 9: t9, 10: t10, 11: t11,
          'algorithmes-classiques': t_algos, 'bac-pratique': t_bac, 'glossaire': t_gloss}


def thumb(key):
    return THUMBS[key]()
