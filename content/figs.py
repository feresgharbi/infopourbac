"""Schémas et graphiques du cours, dessinés en SVG (aucune image externe).

Les couleurs viennent des variables CSS du site : les figures suivent donc le thème clair ou sombre.
FIGS associe (slug de la page, id de la section) à une liste de figures, insérées sous le titre de la section.
"""
import html
import math

esc = html.escape
_n = [0]


# ------------------------------------------------------------------ outils de dessin
def svg(w, h, inner, label):
    _n[0] += 1
    mid = 'ah%d' % _n[0]
    return ('<svg class="dg" viewBox="0 0 %d %d" style="max-width:%dpx;min-width:%dpx" role="img" aria-label="%s">'
            '<defs><marker id="%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path d="M0 0L10 5L0 10z" class="ah"/></marker></defs>%s</svg>') % (
        w, h, w, min(w, round(w * 0.74)), esc(label), mid, inner.replace('MARK', mid))


def fig(s, cap, wide=False):
    return '<figure class="diagram%s"><div class="dgwrap">%s</div><figcaption>%s</figcaption></figure>' % (
        ' wide' if wide else '', s, cap)


def rect(x, y, w, h, cls='b', rx=8):
    return '<rect class="%s" x="%g" y="%g" width="%g" height="%g" rx="%g"/>' % (cls, x, y, w, h, rx)


def txt(x, y, s, cls='', anchor='middle', size=None):
    lines = s.split('\n')
    st = ' style="font-size:%gpx"' % size if size else ''
    if len(lines) == 1:
        return '<text class="%s" x="%g" y="%g" text-anchor="%s" dominant-baseline="central"%s>%s</text>' % (
            cls, x, y, anchor, st, esc(s))
    lh = (size or 15) * 1.25
    y0 = y - lh * (len(lines) - 1) / 2
    sp = ''.join('<tspan x="%g" y="%g">%s</tspan>' % (x, y0 + i * lh, esc(l)) for i, l in enumerate(lines))
    return '<text class="%s" text-anchor="%s" dominant-baseline="central"%s>%s</text>' % (cls, anchor, st, sp)


def box(x, y, w, h, s, cls='b', tcls='', size=None, rx=8):
    return rect(x, y, w, h, cls, rx) + txt(x + w / 2, y + h / 2, s, tcls, size=size)


def dia(cx, cy, w, h, s, tcls='m', size=14):
    pts = '%g,%g %g,%g %g,%g %g,%g' % (cx, cy - h / 2, cx + w / 2, cy, cx, cy + h / 2, cx - w / 2, cy)
    return '<polygon class="a" points="%s"/>' % pts + txt(cx, cy, s, tcls, size=size)


def arr(*pts, cls='ar', head=True):
    d = ' '.join('%g,%g' % p for p in pts)
    m = ' marker-end="url(#MARK)"' if head else ''
    return '<polyline class="%s" points="%s"%s/>' % (cls, d, m)


def line(*pts, cls='ar'):
    return arr(*pts, cls=cls, head=False)


def pill(x, y, w, h, s):
    return box(x, y, w, h, s, 's', 'mut', 13, rx=h / 2)


# ------------------------------------------------------------------ schémas réutilisables
def pipeline(steps, verbs, label, w_box=128, gap=46, h=58, top=14, cls_last='a'):
    n = len(steps)
    W = 8 * 2 + n * w_box + (n - 1) * gap
    out = ''
    for i, s in enumerate(steps):
        x = 8 + i * (w_box + gap)
        out += box(x, top, w_box, h, s, cls_last if i in (0, n - 1) and cls_last else 'b', size=14)
        if i < n - 1:
            x2 = x + w_box + gap
            out += arr((x + w_box + 2, top + h / 2), (x2 - 3, top + h / 2))
            if verbs and verbs[i]:
                out += txt(x + w_box + gap / 2, top + h + 20, verbs[i], 'mut', size=12)
    return svg(W, top + h + 34, out, label)


def flow_si_simple():
    o = pill(95, 6, 130, 30, 'avant le Si')
    o += arr((160, 36), (160, 52))
    o += dia(160, 90, 190, 72, 'n < 0 ?')
    o += arr((160, 126), (160, 160)) + txt(168, 142, 'Vrai', 'ok', 'start', 13)
    o += box(80, 160, 160, 44, 'n ← -n', 'b', 'm')
    o += arr((160, 204), (160, 246))
    o += line((255, 90), (320, 90), (320, 230), (166, 230)) + arr((320, 230), (164, 230))
    o += txt(287, 80, 'Faux', 'no', size=13)
    o += pill(95, 248, 130, 30, 'suite')
    return svg(360, 286, o, 'Organigramme de la forme simple : si n < 0, n reçoit -n, sinon on passe directement à la suite')


def flow_si_complete():
    o = pill(170, 6, 120, 30, 'avant le Si')
    o += arr((230, 36), (230, 52))
    o += dia(230, 92, 230, 76, 'n MOD 2 = 0 ?')
    o += line((115, 92), (95, 92)) + arr((95, 92), (95, 150)) + txt(108, 80, 'Vrai', 'ok', size=13)
    o += line((345, 92), (375, 92)) + arr((375, 92), (375, 150)) + txt(352, 80, 'Faux', 'no', size=13)
    o += box(10, 150, 170, 46, 'Écrire("pair")', 'b', 'm', 13)
    o += box(290, 150, 170, 46, 'Écrire("impair")', 'b', 'm', 13)
    o += line((95, 196), (95, 226), (230, 226)) + line((375, 196), (375, 226), (230, 226))
    o += arr((230, 226), (230, 246))
    o += pill(170, 248, 120, 30, 'suite')
    return svg(470, 286, o, 'Organigramme de la forme complète : une seule des deux branches est exécutée')


def flow_si_gen():
    conds = [('moy ≥ 16 ?', '"Très bien"'), ('moy ≥ 14 ?', '"Bien"'), ('moy ≥ 12 ?', '"Assez bien"'), ('moy ≥ 10 ?', '"Passable"')]
    o = ''
    step = 84
    for i, (c, r) in enumerate(conds):
        y = 44 + i * step
        o += dia(130, y, 170, 60, c)
        o += arr((215, y), (282, y)) + txt(248, y - 11, 'Vrai', 'ok', size=12)
        o += box(282, y - 21, 150, 42, r, 'b', 'm', 12.5)
        o += line((432, y), (462, y))
        if i < len(conds) - 1:
            o += arr((130, y + 30), (130, y + step - 31)) + txt(138, y + 42, 'Faux', 'no', 'start', 12)
    ylast = 44 + 3 * step
    o += arr((130, ylast + 30), (130, ylast + 56)) + txt(138, ylast + 42, 'Faux', 'no', 'start', 12)
    o += box(55, ylast + 56, 150, 42, '"Sans mention"', 'b', 'm', 12.5)
    yj = ylast + 124
    o += line((462, 44), (462, yj), (130, yj)) + line((130, ylast + 98), (130, yj))
    o += arr((130, yj), (130, yj + 18))
    o += pill(70, yj + 20, 120, 30, 'suite')
    return svg(480, yj + 58, o, 'Organigramme Sinon Si : les conditions sont testées de haut en bas, la première vraie gagne')


def flow_pour():
    o = box(90, 8, 160, 40, 'i ← 0', 'b', 'm')
    o += arr((170, 48), (170, 80))
    o += dia(170, 114, 170, 64, 'i < n ?')
    o += arr((170, 146), (170, 176)) + txt(178, 160, 'Vrai', 'ok', 'start', 12)
    o += box(90, 176, 160, 40, 'traitement', 's')
    o += arr((170, 216), (170, 238))
    o += box(90, 238, 160, 40, 'i ← i + 1', 'b', 'm')
    o += line((90, 258), (40, 258), (40, 114)) + arr((40, 114), (84, 114))
    o += arr((255, 114), (322, 114)) + txt(288, 102, 'Faux', 'no', size=12)
    o += pill(322, 99, 110, 30, 'suite')
    o += txt(290, 258, 'Python fait ces deux cases', 'mut', 'start', 11.5) + txt(290, 274, 'pour toi : range(n)', 'mut', 'start', 11.5)
    return svg(460, 292, o, 'Organigramme de la boucle Pour : initialisation, test, traitement, incrémentation')


def flow_tantque():
    o = box(90, 8, 160, 40, 'initialisation', 'b')
    o += arr((170, 48), (170, 80))
    o += dia(170, 114, 190, 64, 'condition ?', '')
    o += arr((170, 146), (170, 178)) + txt(178, 162, 'Vrai', 'ok', 'start', 12)
    o += box(90, 178, 160, 52, 'traitement\n(modifie la condition)', 's', '', 13)
    o += line((90, 204), (34, 204), (34, 114)) + arr((34, 114), (74, 114))
    o += arr((265, 114), (322, 114)) + txt(292, 102, 'Faux', 'no', size=12)
    o += pill(322, 99, 110, 30, 'suite')
    o += txt(270, 160, 'le test est fait AVANT :', 'mut', 'start', 11.5) + txt(270, 176, '0 tour possible', 'mut', 'start', 11.5)
    return svg(450, 244, o, 'Organigramme de la boucle Tant que : la condition est testée avant le traitement')


def flow_repeter():
    o = arr((170, 4), (170, 24))
    o += box(90, 24, 160, 44, 'traitement', 's')
    o += arr((170, 68), (170, 96))
    o += dia(170, 132, 220, 68, "condition d'arrêt ?", '', 13)
    o += line((60, 132), (34, 132), (34, 46)) + arr((34, 46), (88, 46)) + txt(46, 120, 'Faux', 'no', 'start', 12)
    o += arr((170, 166), (170, 196)) + txt(178, 180, 'Vrai', 'ok', 'start', 12)
    o += pill(110, 198, 120, 30, 'suite')
    o += txt(290, 46, 'le test est fait APRÈS :', 'mut', 'start', 11.5) + txt(290, 62, 'au moins 1 tour', 'mut', 'start', 11.5)
    return svg(450, 236, o, "Organigramme de Répéter … Jusqu'à : le traitement est exécuté avant le test")


def choose_loop():
    o = dia(250, 40, 300, 62, 'Nombre de tours connu ?', '', 14)
    o += line((100, 40), (70, 40)) + arr((70, 40), (70, 92)) + txt(82, 28, 'Oui', 'ok', size=12)
    o += box(10, 92, 120, 44, 'Pour', 'a', 'm', 15)
    o += line((400, 40), (430, 40), (430, 74), (330, 74)) + arr((330, 74), (330, 106)) + txt(418, 28, 'Non', 'no', size=12)
    o += dia(330, 140, 280, 64, 'Au moins un tour ?', '', 14)
    o += line((190, 140), (180, 140)) + arr((180, 140), (180, 196)) + txt(197, 128, 'Non', 'no', size=12)
    o += line((470, 140), (480, 140)) + arr((480, 140), (480, 196)) + txt(462, 128, 'Oui', 'ok', size=12)
    o += box(110, 196, 140, 44, 'Tant que', 'a', 'm', 15)
    o += box(400, 196, 160, 44, "Répéter", 'a', 'm', 15)
    o += txt(70, 154, 'for i in range(…)', 'mut m', size=11.5)
    o += txt(180, 258, 'while condition:', 'mut m', size=11.5)
    o += txt(480, 258, 'while True: … break', 'mut m', size=11.5)
    return svg(570, 270, o, 'Arbre de décision pour choisir la bonne boucle')


def digits_chain(n=1234):
    vals = [n]
    while vals[-1] > 0:
        vals.append(vals[-1] // 10)
    o = ''
    step, w = 122, 72
    for i, v in enumerate(vals):
        x = 8 + i * step
        o += box(x, 18, w, 46, str(v), 'a' if v == 0 else 'b', 'm', 17)
        if i < len(vals) - 1:
            o += arr((x + w + 2, 41), (x + step - 3, 41))
            o += txt(x + w + (step - w) / 2, 8, 'DIV 10', 'mut m', size=11)
            cx = x + w + (step - w) / 2
            o += line((cx, 44), (cx, 82), cls='dash')
            o += '<circle class="a" cx="%g" cy="%g" r="17"/>' % (cx, 100) + txt(cx, 100, str(vals[i] % 10), 'acc m', size=15)
    o += txt(8, 136, 'MOD 10 donne les chiffres de droite à gauche : 4, 3, 2, 1. Arrêt quand n = 0.', 'mut', 'start', 12)
    return svg(8 + (len(vals) - 1) * step + w + 8, 150, o, 'Décomposition de 1234 en chiffres avec DIV 10 et MOD 10')


def var_box():
    o = ''
    for cx, code, val, note in [(130, 'x ← 5', '5', 'la case x reçoit 5'), (390, 'x ← x + 1', '6', "l'ancienne valeur 5 est remplacée")]:
        o += txt(cx, 22, code, 'acc m', size=17)
        o += arr((cx, 36), (cx, 62))
        o += rect(cx - 55, 64, 110, 70, 'b')
        o += txt(cx - 48, 76, 'x', 'mut m', 'start', 12)
        o += txt(cx, 102, val, 'm', size=30)
        o += txt(cx, 156, note, 'mut', size=12.5)
    o += line((260, 16), (260, 160), cls='dash')
    return svg(520, 172, o, "Une variable est une case nommée : l'affectation y range une valeur et remplace l'ancienne")


def swap_fig():
    o = box(40, 40, 110, 56, 'a', 'b', 'm', 20) + txt(95, 26, 'au départ : 3', 'mut', size=12)
    o += box(370, 40, 110, 56, 'b', 'b', 'm', 20) + txt(425, 26, 'au départ : 7', 'mut', size=12)
    o += box(205, 160, 110, 56, 'aux', 's', 'm', 20)
    o += arr((115, 98), (210, 160)) + txt(130, 146, '1. aux ← a', 'acc m', 'end', 14)
    o += arr((366, 68), (154, 68)) + txt(260, 56, '2. a ← b', 'acc m', size=14)
    o += arr((310, 160), (405, 98)) + txt(390, 146, '3. b ← aux', 'acc m', 'start', 14)
    return svg(520, 230, o, 'Permutation de deux variables avec une variable auxiliaire, en trois étapes')


def input_fig():
    o = box(8, 16, 128, 58, 'Tu tapes\n17', 's', '', 14)
    o += arr((138, 45), (229, 45)) + txt(183, 32, 'input()', 'acc m', size=13)
    o += box(232, 16, 128, 58, '"17"\ntype str', 'b', 'm', 14)
    o += arr((362, 45), (453, 45)) + txt(407, 32, 'int()', 'acc m', size=13)
    o += box(456, 16, 128, 58, '17\ntype int', 'a', 'm', 14)
    o += txt(296, 96, 'du texte : "17" + 1 → erreur', 'no', size=12)
    o += txt(520, 96, 'un nombre : 17 + 1 → 18', 'ok', size=12)
    return svg(592, 112, o, "input() renvoie toujours une chaîne : il faut la convertir avec int() ou float()")


def types_fig():
    data = [('Entier', 'int', '17'), ('Réel', 'float', '3.5'), ('Booléen', 'bool', 'True'), ('Caractère', 'str', '"A"'), ('Chaîne', 'str', '"Bac"')]
    o = ''
    for i, (a, p, e) in enumerate(data):
        x = 6 + i * 128
        o += rect(x, 8, 118, 116, 's')
        o += box(x, 8, 118, 36, a, 'a', '', 14)
        o += txt(x + 59, 62, 'Python : ' + p, 'mut', size=12)
        o += txt(x + 59, 96, e, 'm', size=19)
    return svg(648, 132, o, 'Les cinq types de base, leur nom en Python et un exemple de valeur')


def divmod_fig():
    o = ''
    for g in range(3):
        gx = 8 + g * 148
        o += rect(gx, 26, 138, 46, 's')
        for j in range(5):
            o += '<circle class="dot" cx="%g" cy="49" r="10"/>' % (gx + 17 + j * 26)
    for j in range(2):
        o += '<circle class="dot hi" cx="%g" cy="49" r="10"/>' % (470 + j * 28)
    o += txt(225, 12, '17 objets rangés par paquets de 5', 'mut', size=12)
    o += txt(225, 94, '3 paquets complets → 17 DIV 5 = 3', '', size=14)
    o += txt(484, 94, 'reste 2 → 17 MOD 5 = 2', 'acc', size=14)
    o += txt(300, 124, 'En Python : 17 // 5 vaut 3 et 17 % 5 vaut 2', 'mut m', size=12)
    return svg(600, 138, o, 'Illustration de la division entière : 17 DIV 5 = 3 et 17 MOD 5 = 2')


def prio_fig():
    def node(x, y, s, cls='b'):
        return '<circle class="%s" cx="%g" cy="%g" r="22"/>' % (cls, x, y) + txt(x, y, s, 'm', size=16)
    o = line((170, 40), (90, 112)) + line((170, 40), (250, 112)) + line((250, 112), (200, 180)) + line((250, 112), (300, 180))
    o += node(170, 40, '+') + node(90, 112, '2') + node(250, 112, '*', 'a') + node(200, 180, '3') + node(300, 180, '4')
    o += txt(380, 70, 'Expression : 2 + 3 * 4', 'm', 'start', 14)
    o += txt(380, 110, '1. 3 * 4 = 12', 'acc m', 'start', 14)
    o += txt(380, 140, '2. 2 + 12 = 14', 'm', 'start', 14)
    o += txt(380, 176, 'La multiplication est', 'mut', 'start', 12) + txt(380, 192, 'calculée en premier.', 'mut', 'start', 12)
    return svg(580, 212, o, "Arbre de calcul de 2 + 3 * 4 : la multiplication est prioritaire")


def string_fig():
    s = 'BONJOUR'
    o = txt(62, 30, 'indice', 'mut', 'end', 12) + txt(62, 128, 'négatif', 'mut', 'end', 12)
    for i, ch in enumerate(s):
        x = 72 + i * 56
        o += txt(x + 28, 30, str(i), 'mut m', size=13)
        o += box(x, 44, 56, 62, ch, 'a' if 3 <= i <= 6 else 'b', 'm', 22, rx=0)
        o += txt(x + 28, 128, str(i - len(s)), 'mut m', size=12)
    o += line((240, 146), (240, 154), (464, 154), (464, 146))
    o += txt(250, 176, 'ch[3:7] → "JOUR"  ·  Sous_chaine(ch, 3, 7)', 'acc m', size=13)
    return svg(500, 192, o, 'La chaîne BONJOUR avec ses indices positifs et négatifs, et la sous-chaîne ch[3:7]')


def modules_fig():
    o = box(200, 8, 220, 46, 'Programme principal', 'a', '', 15)
    kids = [('Saisir()', 'fonction'), ('Remplir(T, n)', 'procédure'), ('Afficher(T, n)', 'procédure'), ('Maximum(T, n)', 'fonction')]
    for i, (nm, k) in enumerate(kids):
        x = 8 + i * 152
        cx = x + 68
        o += line((310, 54), (310, 82), (cx, 82)) + arr((cx, 82), (cx, 110))
        o += rect(x, 110, 136, 56, 'b')
        o += txt(cx, 130, nm, 'm', size=13) + txt(cx, 151, k, 'mut', size=12)
    return svg(616, 176, o, 'Une solution modulaire : le programme principal appelle des fonctions et des procédures')


def blackbox_fig(kind='fonction'):
    if kind == 'fonction':
        ins, name, out, note = ['a = 12', 'b = 15'], 'Fonction\nMoyenne(a, b)', '13.5', 'Retourner'
    else:
        ins, name, out, note = ['T', 'n'], 'Procédure\nAfficher(T, n)', 'à l\'écran', 'action'
    o = ''
    for i, v in enumerate(ins):
        y = 22 + i * 58
        o += box(8, y, 100, 40, v, 's', 'm', 14)
        o += arr((110, y + 20), (192, 70))
    o += box(194, 34, 180, 72, name, 'a', 'm', 14)
    o += arr((376, 70), (450, 70)) + txt(413, 56, note, 'mut', size=12)
    o += box(452, 48, 110, 44, out, 'b' if kind == 'fonction' else 's', 'm', 15)
    o += txt(58, 136, 'paramètres', 'mut', size=12)
    o += txt(507, 112, 'une valeur renvoyée' if kind == 'fonction' else 'rien n\'est renvoyé', 'mut', size=12)
    lab = ('Une fonction reçoit des paramètres et renvoie une seule valeur' if kind == 'fonction'
           else 'Une procédure reçoit des paramètres et réalise une action sans renvoyer de valeur')
    return svg(570, 148, o, lab)


def params_fig():
    o = txt(270, 18, 'Appel dans le programme principal :  r ← Moyenne(x, y)', 'm', size=13)
    o += box(150, 36, 90, 44, 'x = 12', 'b', 'm', 14) + box(300, 36, 90, 44, 'y = 15', 'b', 'm', 14)
    o += txt(470, 58, 'paramètres effectifs', 'acc', 'start', 12)
    o += arr((195, 80), (195, 136)) + arr((345, 80), (345, 136))
    o += txt(205, 108, 'copie', 'mut', 'start', 12) + txt(355, 108, 'copie', 'mut', 'start', 12)
    o += box(150, 138, 90, 44, 'a', 'a', 'm', 16) + box(300, 138, 90, 44, 'b', 'a', 'm', 16)
    o += txt(470, 160, 'paramètres formels', 'acc', 'start', 12)
    o += txt(270, 204, 'Définition :  Fonction Moyenne(a, b : Réel) : Réel', 'm', size=13)
    return svg(620, 218, o, 'Les paramètres effectifs de l\'appel sont copiés dans les paramètres formels, dans le même ordre')


T6 = [12, 5, 18, 7, 14, 9]


def array_fig():
    o = txt(52, 82, 'T', 'm', 'end', 20)
    for i, v in enumerate(T6):
        x = 62 + i * 62
        o += txt(x + 31, 30, str(i), 'mut m', size=13)
        o += box(x, 48, 62, 62, str(v), 'a' if i == 2 else 'b', 'm', 20, rx=0)
    o += txt(62, 30, 'indice', 'mut', 'end', 11)
    o += arr((217, 140), (217, 114)) + txt(217, 154, 'T[2] vaut 18', 'acc m', size=13)
    o += txt(62 + 3 * 62, 182, '6 éléments : indices de 0 à n - 1 = 5', 'mut', size=12)
    return svg(450, 196, o, 'Un tableau de 6 entiers et ses indices de 0 à 5')


def bars_fig():
    W, H, base, x0 = 610, 230, 190, 50
    mx = max(T6)
    avg = sum(T6) / len(T6)
    sc = 150 / 20
    o = ''
    for k in range(0, 21, 5):
        y = base - k * sc
        o += line((x0, y), (W - 96, y), cls='grid') + txt(x0 - 8, y, str(k), 'mut', 'end', 11)
    for i, v in enumerate(T6):
        x = x0 + 14 + i * 76
        o += '<rect class="bar%s" x="%g" y="%g" width="46" height="%g" rx="3"/>' % (' hi' if v == mx else '', x, base - v * sc, v * sc)
        o += txt(x + 23, base - v * sc - 11, str(v), 'acc m' if v == mx else 'm', size=13)
        o += txt(x + 23, base + 16, 'T[%d]' % i, 'mut m', size=11.5)
    ya = base - avg * sc
    o += line((x0, ya), (W - 96, ya), cls='dash acc')
    o += txt(W - 90, ya - 8, 'moyenne', 'acc', 'start', 12) + txt(W - 90, ya + 9, '≈ %.2f' % avg, 'acc m', 'start', 12)
    o += txt(x0 + 14 + 2 * 76 + 23, 14, 'maximum', 'acc', size=12)
    return svg(W, H, o, 'Graphique des valeurs du tableau : le maximum 18 et la moyenne 10,83')


# ------------------------------------------------------------------ tris : déroulement en barres
def trace_selection(t):
    t = t[:]
    rows = [('Départ', t[:], set(), set(), '')]
    for i in range(len(t) - 1):
        m = min(range(i, len(t)), key=lambda k: t[k])
        moved = {i, m} if m != i else set()
        note = 'min = %d → échange T[%d] et T[%d]' % (t[m], i, m) if m != i else 'min = %d déjà en place' % t[m]
        t[i], t[m] = t[m], t[i]
        rows.append(('i = %d' % i, t[:], set(range(i + 1)) | ({len(t) - 1} if i == len(t) - 2 else set()), moved, note))
    return rows


def trace_bulles(t):
    t = t[:]
    rows = [('Départ', t[:], set(), set(), '')]
    p, ok = 0, set()
    while True:
        p += 1
        sw, moved = 0, set()
        for i in range(len(t) - 1):
            if t[i] > t[i + 1]:
                t[i], t[i + 1] = t[i + 1], t[i]
                sw += 1
                moved |= {i, i + 1}
        ok |= {len(t) - p}
        done = set(range(len(t))) if sw == 0 or t == sorted(t) and p >= 3 else ok
        rows.append(('passage %d' % p, t[:], done, moved, '%d échange%s' % (sw, 's' if sw > 1 else '') if sw else 'aucun échange → arrêt'))
        if sw == 0:
            return rows


def trace_insertion(t):
    t = t[:]
    rows = [('Départ', t[:], {0}, set(), '')]
    for i in range(1, len(t)):
        v, j = t[i], i
        while j > 0 and t[j - 1] > v:
            t[j] = t[j - 1]
            j -= 1
        t[j] = v
        rows.append(('i = %d' % i, t[:], set(range(i + 1)), {j}, '%d inséré à l\'indice %d' % (v, j)))
    return rows


def sort_fig(rows, label):
    rh, x0, bw, step = 74, 96, 40, 52
    o = ''
    for r, (lab, arr_, done, moved, note) in enumerate(rows):
        yb = 14 + r * rh + 50
        o += txt(8, yb - 18, lab, 'm' if r else 'mut', 'start', 13)
        for j, v in enumerate(arr_):
            x = x0 + j * step
            cls = 'bar hi' if j in moved else ('bar ok' if j in done else 'bar')
            h = v * 5.4
            o += '<rect class="%s" x="%g" y="%g" width="%g" height="%g" rx="3"/>' % (cls, x, yb - h, bw, h)
            o += txt(x + bw / 2, yb - h - 9, str(v), 'm', size=12)
        o += txt(x0 + 5 * step + 14, yb - 18, note, 'acc' if moved else 'mut', 'start', 12.5)
        if r < len(rows) - 1:
            o += line((8, yb + 7), (600, yb + 7), cls='grid')
    yl = 14 + len(rows) * rh + 8
    o += '<rect class="bar hi" x="8" y="%g" width="14" height="14" rx="2"/>' % (yl - 7) + txt(28, yl, 'élément déplacé', 'mut', 'start', 12)
    o += '<rect class="bar ok" x="160" y="%g" width="14" height="14" rx="2"/>' % (yl - 7) + txt(180, yl, 'partie déjà triée', 'mut', 'start', 12)
    o += '<rect class="bar" x="320" y="%g" width="14" height="14" rx="2"/>' % (yl - 7) + txt(340, yl, 'pas encore traité', 'mut', 'start', 12)
    return svg(600, yl + 14, o, label)


def complexity_fig():
    ns = [10, 20, 50, 100]
    vals = [n * (n - 1) // 2 for n in ns]
    W, x0, top, bh, gap = 560, 70, 16, 30, 16
    mx = max(vals)
    o = ''
    for i, (n, v) in enumerate(zip(ns, vals)):
        y = top + i * (bh + gap)
        wv = max(4, v / mx * (W - x0 - 90))
        o += txt(x0 - 10, y + bh / 2, 'n = %d' % n, 'm', 'end', 13)
        o += '<rect class="bar%s" x="%g" y="%g" width="%g" height="%g" rx="3"/>' % (' hi' if i == 3 else '', x0, y, wv, bh)
        o += txt(x0 + wv + 8, y + bh / 2, '{:,}'.format(v).replace(',', ' '), 'acc m' if i == 3 else 'm', 'start', 13)
    yb = top + len(ns) * (bh + gap) + 4
    o += txt(x0, yb, 'Comparaisons du tri par sélection : n × (n − 1) / 2. Le tableau 10 fois plus grand demande ~100 fois plus de travail.', 'mut', 'start', 11.5)
    return svg(W + 140, yb + 14, o, 'Nombre de comparaisons du tri par sélection selon la taille du tableau')


# ------------------------------------------------------------------ recherches
def seq_fig():
    x_ = 7
    o = txt(8, 20, 'On cherche x = 7 : on compare chaque case, de gauche à droite.', 'mut', 'start', 12.5)
    found = T6.index(x_)
    for i, v in enumerate(T6):
        x = 8 + i * 70
        cls = 'a' if i == found else ('s' if i < found else 'b')
        o += box(x, 44, 62, 56, str(v), cls, 'm', 19, rx=0)
        o += txt(x + 31, 116, str(i), 'mut m', size=12)
        if i <= found:
            o += txt(x + 31, 140, '= 7 ✓' if i == found else '≠ 7', 'ok' if i == found else 'no', size=12.5)
    o += txt(8, 168, 'Trouvé à l\'indice 3 après 4 comparaisons. Les cases suivantes ne sont pas regardées.', 'mut', 'start', 12.5)
    return svg(560, 182, o, 'Recherche séquentielle de 7 dans le tableau [12, 5, 18, 7, 14, 9]')


def dicho_fig():
    T = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    x_ = 23
    deb, fin, rows = 0, len(T) - 1, []
    while deb <= fin:
        mil = (deb + fin) // 2
        rows.append((deb, fin, mil))
        if T[mil] == x_:
            break
        if x_ < T[mil]:
            fin = mil - 1
        else:
            deb = mil + 1
    cw, rh, x0 = 50, 76, 80
    o = txt(8, 14, 'On cherche x = 23 dans un tableau trié.', 'mut', 'start', 12.5)
    for r, (d, f, m) in enumerate(rows):
        y = 36 + r * rh
        o += txt(8, y + 22, 'Étape %d' % (r + 1), 'm', 'start', 13)
        for i, v in enumerate(T):
            x = x0 + i * cw
            cls = 'a' if i == m else ('b' if d <= i <= f else 'off')
            o += box(x, y, cw, 44, str(v), cls, 'm off' if cls == 'off' else 'm', 15, rx=0)
        labs = {}
        for nm, k in (('deb', d), ('mil', m), ('fin', f)):
            labs.setdefault(k, []).append(nm)
        for k, nms in labs.items():
            o += txt(x0 + k * cw + cw / 2, y + 57, ' = '.join(nms), 'acc m' if 'mil' in nms else 'mut m', size=11)
        v = T[m]
        dec = 'trouvé !' if v == x_ else ('23 > %d → à droite' % v if x_ > v else '23 < %d → à gauche' % v)
        o += txt(x0 + len(T) * cw + 14, y + 22, dec, 'ok' if v == x_ else 'acc', 'start', 12.5)
    return svg(x0 + len(T) * cw + 170, 36 + len(rows) * rh, o, 'Recherche dichotomique de 23 : l\'intervalle est coupé en deux à chaque étape')


def search_compare_fig():
    ns = [16, 128, 1024, 8192]
    W, x0 = 600, 90
    o = ''
    y = 14
    for n in ns:
        seq, dic = n, int(math.log2(n)) + 1
        o += txt(x0 - 12, y + 22, 'n = %s' % '{:,}'.format(n).replace(',', ' '), 'm', 'end', 13)
        for k, (v, cls, nm) in enumerate([(seq, 'bar', 'séquentielle'), (dic, 'bar hi', 'dichotomique')]):
            wv = max(3, v / n * (W - x0 - 150))
            yy = y + k * 22
            o += '<rect class="%s" x="%g" y="%g" width="%g" height="18" rx="3"/>' % (cls, x0, yy, wv)
            o += txt(x0 + wv + 8, yy + 9, '%s  (%s)' % ('{:,}'.format(v).replace(',', ' '), nm), 'acc m' if k else 'm', 'start', 12)
        y += 62
    o += txt(x0, y + 2, "Nombre maximal de comparaisons. Quand n double, la dichotomie n'en ajoute qu'une.", 'mut', 'start', 11.5)
    return svg(W + 120, y + 16, o, 'Comparaison du nombre maximal de comparaisons : recherche séquentielle et dichotomique')


# ------------------------------------------------------------------ PyQt5
def window_fig():
    o = rect(10, 10, 380, 240, 'b', 6)
    o += '<path class="tbar" d="M10 16a6 6 0 0 1 6-6h368a6 6 0 0 1 6 6v20H10z"/>'
    o += txt(24, 23, 'Nombre premier', '', 'start', 12.5)
    for i, c in enumerate(['', '', '']):
        o += '<circle class="s" cx="%g" cy="23" r="5"/>' % (346 + i * 14)
    o += txt(36, 70, 'Donner un entier N :', '', 'start', 14)
    o += rect(36, 86, 200, 34, 'field', 4) + txt(46, 103, '17', 'm', 'start', 14)
    o += box(252, 86, 112, 34, 'Vérifier', 'btn', 'btnt', 14, rx=5)
    o += txt(36, 170, '17 est premier', 'acc', 'start', 15)
    o += line((36, 186), (300, 186), cls='dash')
    callouts = [(70, 'QLabel', 'texte fixe'), (103, 'QLineEdit', 'objectName : N'), (130, 'QPushButton', 'objectName : Verifier'), (170, 'QLabel', 'objectName : Resultat')]
    pts = {70: (190, 70), 103: (236, 103), 130: (308, 120), 170: (160, 170)}
    for y, k, nm in callouts:
        px, py = pts[y]
        ty = {70: 60, 103: 104, 130: 148, 170: 192}[y]
        o += line((px + 4, py), (420, ty), cls='dash') + '<circle class="pt" cx="%g" cy="%g" r="3.5"/>' % (px + 2, py)
        o += txt(426, ty - 8, k, 'm', 'start', 13) + txt(426, ty + 9, nm, 'mut m', 'start', 11.5)
    o += txt(300, 270, 'windows.N.text() lit « 17 » · windows.Resultat.setText(…) affiche le résultat', 'mut m', size=11.5)
    return svg(600, 284, o, "Fenêtre PyQt5 type du Bac pratique et le nom de chaque composant")


# ------------------------------------------------------------------ algorithmes classiques
def primes_fig():
    def pr(n):
        return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))
    o = ''
    for k in range(1, 61):
        r, c = divmod(k - 1, 10)
        x, y = 8 + c * 50, 8 + r * 44
        o += box(x, y, 46, 40, str(k), 'a' if pr(k) else 's', 'acc m' if pr(k) else 'mut m', 14, rx=4)
    return svg(508, 8 + 6 * 44 + 4, o, 'Les nombres premiers de 1 à 60 sont mis en évidence')


def euclide_fig(a=48, b=18):
    steps = []
    while b:
        steps.append((a, b, a % b))
        a, b = b, a % b
    o = ''
    for i, (x, y, r) in enumerate(steps):
        yy = 12 + i * 54
        o += box(8, yy, 150, 40, 'a = %d,  b = %d' % (x, y), 'b', 'm', 13.5)
        o += arr((160, yy + 20), (220, yy + 20))
        o += txt(232, yy + 20, '%d MOD %d = %d' % (x, y, r), 'acc m' if r == 0 else 'm', 'start', 14)
        if r:
            o += txt(400, yy + 20, '→ (a, b) devient (%d, %d)' % (y, r), 'mut', 'start', 12)
        if i < len(steps) - 1:
            o += arr((83, yy + 40), (83, yy + 54))
    yy = 12 + len(steps) * 54
    o += box(8, yy, 150, 40, 'PGCD = %d' % a, 'a', 'm', 15)
    o += txt(172, yy + 20, 'b vaut 0 : le PGCD est la dernière valeur de a', 'mut', 'start', 12)
    return svg(600, yy + 52, o, 'Algorithme d\'Euclide pas à pas pour PGCD(48, 18) = 6')


def binary_fig(n=13):
    rows = []
    while n:
        rows.append((n, n // 2, n % 2))
        n //= 2
    o = ''
    for i, (a, q, r) in enumerate(rows):
        y = 16 + i * 46
        o += txt(30, y + 14, '%d ÷ 2' % a, 'm', 'start', 15)
        o += txt(130, y + 14, '= %d' % q, 'm', 'start', 15)
        o += txt(200, y + 14, 'reste', 'mut', 'start', 12.5)
        o += '<circle class="a" cx="268" cy="%g" r="16"/>' % (y + 14) + txt(268, y + 14, str(r), 'acc m', size=16)
    yb = 16 + len(rows) * 46
    o += arr((310, yb - 30), (310, 22), cls='ar acc')
    o += txt(326, (yb + 10) / 2 - 12, 'on lit les restes', 'acc', 'start', 13) + txt(326, (yb + 10) / 2 + 8, 'de bas en haut', 'acc', 'start', 13)
    o += txt(30, yb + 12, '13 en binaire : 1101', 'm', 'start', 16)
    o += txt(30, yb + 36, 'Vérification : 1×8 + 1×4 + 0×2 + 1×1 = 13', 'mut', 'start', 12.5)
    return svg(520, yb + 52, o, 'Conversion de 13 en binaire par divisions successives par 2 : 1101')


def palin_fig(s='RADAR'):
    o = ''
    n = len(s)
    for i, ch in enumerate(s):
        x = 90 + i * 64
        o += box(x, 100, 56, 56, ch, 'a' if i == n // 2 else 'b', 'm', 22, rx=4)
        o += txt(x + 28, 174, str(i), 'mut m', size=12)
    for i in range(n // 2):
        x1, x2 = 90 + i * 64 + 28, 90 + (n - 1 - i) * 64 + 28
        h = 36 + (n // 2 - 1 - i) * 40
        o += '<path class="ar" d="M%g 96 C%g %g %g %g %g 96"/>' % (x1, x1, 96 - h, x2, 96 - h, x2)
        o += txt((x1 + x2) / 2, 96 - h * 0.75 - 8, 'ch[%d] = ch[%d]' % (i, n - 1 - i), 'ok m', size=12)
    o += txt(250, 202, 'On compare les caractères deux à deux, depuis les extrémités vers le milieu.', 'mut', size=12)
    return svg(500, 216, o, 'Test du palindrome RADAR : comparaison des caractères symétriques')


def bac_timeline():
    steps = [(5, 'Lire'), (2, 'Dossier'), (8, 'Interface'), (25, 'Fonctions'), (10, 'Play'), (3, 'Annexe'), (7, 'Tests')]
    W, x0, w = 640, 10, 620
    o = ''
    t = 0
    for i, (m, lab) in enumerate(steps):
        x = x0 + t / 60 * w
        ww = m / 60 * w
        o += '<rect class="%s" x="%g" y="30" width="%g" height="46"/>' % ('seg hi' if lab == 'Fonctions' else 'seg s%d' % (i % 2), x, ww)
        if ww > 50:
            o += txt(x + ww / 2, 46, lab, 'acc' if lab == 'Fonctions' else '', size=12.5) + txt(x + ww / 2, 64, '%d min' % m, 'mut', size=11.5)
        else:
            o += txt(x + ww / 2, 96 + (i % 2) * 16, '%s %d′' % (lab, m), 'mut', size=11)
            o += line((x + ww / 2, 77), (x + ww / 2, 86 + (i % 2) * 16), cls='grid')
        t += m
    for k in range(0, 61, 15):
        o += txt(x0 + k / 60 * w, 16, '%d min' % k if k else '0', 'mut m', 'middle' if 0 < k < 60 else ('start' if k == 0 else 'end'), 11)
    return svg(W, 132, o, 'Proposition de répartition du temps pendant l\'heure de l\'épreuve pratique')


def parcours_fig(chapters, href):
    """Le parcours du cours en 4 étapes (HTML, pour rester lisible sur téléphone)."""
    groups = [('Les bases', [1, 2, 3, 4]), ('Les structures', [5, 6]), ('La modularité', [7, 8]), ('Trier, chercher, afficher', [9, 10, 11])]
    by = {c['n']: c for c in chapters}
    cols = ''
    for g, (t, ns) in enumerate(groups, 1):
        items = ''.join('<li><a href="%s"><span>%d</span>%s</a></li>' % (href(by[n]['slug']), n, esc(by[n]['short'])) for n in ns)
        cols += '<li class="step"><p class="step-t"><b>%d</b>%s</p><ol>%s</ol></li>' % (g, esc(t), items)
    return '<ol class="parcours">%s</ol>' % cols


# ------------------------------------------------------------------ table des figures
S = 'cours/'
C1, C2, C3, C4, C5, C6 = (S + 'introduction-algorithmique-python', S + 'entrees-sorties-affectation', S + 'variables-types-operateurs',
                          S + 'chaines-de-caracteres', S + 'structures-conditionnelles', S + 'structures-iteratives')
C7, C8, C9, C10, C11 = (S + 'sous-programmes-fonctions-procedures', S + 'tableaux', S + 'algorithmes-de-tri',
                        S + 'algorithmes-de-recherche', S + 'interfaces-graphiques-pyqt5')
TRI = [5, 2, 8, 1, 4]


def build_figs():
    return {
        (C1, 'definition'): [fig(pipeline(['Problème', 'Algorithme\n(sur papier)', 'Programme\nPython', 'Résultat'], ['analyser', 'traduire', 'exécuter'],
                                          'Du problème au résultat : analyser, écrire l\'algorithme, le traduire en Python, l\'exécuter'),
                                 "Le chemin d'un problème jusqu'au résultat.")],
        (C1, 'structure'): [fig(pipeline(['Entrées\nLire(n1, n2)', 'Traitement\nmoy ← (n1+n2)/2', 'Sorties\nÉcrire(moy)'], ['', ''],
                                         'Tout algorithme suit le schéma entrées, traitement, sorties', w_box=170, h=64),
                                "Entrées → traitement → sorties, sur l'exemple de la moyenne.")],
        (C2, 'affectation'): [fig(var_box(), "Une variable est une case qui porte un nom. L'affectation y range une valeur.")],
        (C2, 'permutation'): [fig(swap_fig(), "Permuter a et b : trois affectations, dans cet ordre précis.")],
        (C2, 'entree'): [fig(input_fig(), "Ce que fait <code>int(input())</code> : lire du texte, puis le convertir en nombre.")],
        (C3, 'types'): [fig(types_fig(), "Les cinq types de base du programme, avec leur nom en Python.", True)],
        (C3, 'arithmetiques'): [fig(divmod_fig(), "DIV donne le nombre de paquets complets, MOD donne ce qui reste.")],
        (C3, 'priorites'): [fig(prio_fig(), "Python évalue d'abord les opérateurs prioritaires, comme en mathématiques.")],
        (C4, 'indices'): [fig(string_fig(), "Chaque caractère a un indice. Le premier est à l'indice 0.")],
        (C5, 'si-simple'): [fig(flow_si_simple(), "Organigramme de la forme simple.")],
        (C5, 'si-complete'): [fig(flow_si_complete(), "Organigramme de la forme complète : une branche ou l'autre, jamais les deux.")],
        (C5, 'si-generalisee'): [fig(flow_si_gen(), "Organigramme de la forme généralisée sur l'exemple des mentions.")],
        (C6, 'pour'): [fig(flow_pour(), "Organigramme de la boucle Pour.")],
        (C6, 'tant-que'): [fig(flow_tantque(), "Organigramme de la boucle Tant que.")],
        (C6, 'repeter'): [fig(flow_repeter(), "Organigramme de Répéter … Jusqu'à.")],
        (C6, 'choisir'): [fig(choose_loop(), "Deux questions suffisent pour choisir la bonne boucle.")],
        (C6, 'chiffres'): [fig(digits_chain(), "Parcourir les chiffres de 1234 : MOD 10 donne le dernier chiffre, DIV 10 le supprime.", True)],
        (C7, 'pourquoi'): [fig(modules_fig(), "Une solution modulaire : chaque sous-programme fait une seule tâche.")],
        (C7, 'fonction'): [fig(blackbox_fig('fonction'), "Une fonction : des paramètres en entrée, une seule valeur en sortie.")],
        (C7, 'procedure'): [fig(blackbox_fig('procedure'), "Une procédure : des paramètres en entrée, une action, pas de valeur renvoyée.")],
        (C7, 'parametres'): [fig(params_fig(), "À l'appel, chaque paramètre effectif est copié dans le paramètre formel de même position.")],
        (C8, 'declaration'): [fig(array_fig(), "Un tableau de 6 entiers : les indices vont de 0 à 5.")],
        (C8, 'calculs'): [fig(bars_fig(), "Les valeurs du tableau T en graphique : le maximum et la moyenne.")],
        (C9, 'selection'): [fig(sort_fig(trace_selection(TRI), 'Déroulement du tri par sélection sur [5, 2, 8, 1, 4]'),
                                "Tri par sélection sur [5, 2, 8, 1, 4] : à chaque étape, le plus petit restant vient se placer à gauche.", True)],
        (C9, 'bulles'): [fig(sort_fig(trace_bulles(TRI), 'Déroulement du tri à bulles sur [5, 2, 8, 1, 4]'),
                             "Tri à bulles sur [5, 2, 8, 1, 4] : à chaque passage, le plus grand restant remonte à droite.", True)],
        (C9, 'insertion'): [fig(sort_fig(trace_insertion(TRI), 'Déroulement du tri par insertion sur [5, 2, 8, 1, 4]'),
                                "Tri par insertion sur [5, 2, 8, 1, 4] : chaque élément est inséré à sa place dans la partie gauche déjà triée.", True)],
        (C9, 'comparaison'): [fig(complexity_fig(), "Le nombre de comparaisons grandit beaucoup plus vite que la taille du tableau.", True)],
        (C10, 'sequentielle'): [fig(seq_fig(), "Recherche séquentielle : on avance case par case jusqu'à trouver x.")],
        (C10, 'dichotomique'): [fig(dicho_fig(), "Recherche dichotomique de 23 : 3 étapes au lieu de 6.", True)],
        (C10, 'comparaison'): [fig(search_compare_fig(), "Sur un grand tableau trié, la dichotomie est incomparablement plus rapide.", True)],
        (C11, 'ihm'): [fig(window_fig(), "Une interface type du Bac pratique et le nom de chacun de ses composants.", True)],
        (C11, 'module-play'): [fig(pipeline(['Lire\ntext()', 'Vérifier\nla saisie', 'Traiter\n(fonctions)', 'Afficher\nsetText()'], ['', '', ''],
                                            'Les quatre étapes du module Play : lire, vérifier, traiter, afficher', w_box=128, gap=40),
                                   "Le module Play suit toujours ces quatre étapes.")],
        ('algorithmes-classiques', 'premier'): [fig(primes_fig(), "Les nombres premiers entre 1 et 60 (en couleur).")],
        ('algorithmes-classiques', 'pgcd'): [fig(euclide_fig(), "PGCD(48, 18) avec l'algorithme d'Euclide.")],
        ('algorithmes-classiques', 'somme-chiffres'): [fig(digits_chain(), "Les chiffres de 1234 : 4 + 3 + 2 + 1 = 10.", True)],
        ('algorithmes-classiques', 'palindrome'): [fig(palin_fig(), "RADAR est un palindrome : il se lit pareil dans les deux sens.")],
        ('algorithmes-classiques', 'binaire'): [fig(binary_fig(), "Convertir 13 en binaire : divisions successives par 2.")],
    }
