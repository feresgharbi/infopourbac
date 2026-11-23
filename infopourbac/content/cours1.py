from h import P, A, DUO, T, TDO, NOTE, WARN, TIP, DEF, UL, OL, c

CH1 = {
    'slug': 'cours/introduction-algorithmique-python',
    'short': "Introduction à l'algorithmique",
    'h1': "Introduction à l'algorithmique et à Python",
    'title': "Introduction à l'algorithmique et Python | Bac Tunisie",
    'desc': "Algorithme, programme et Python : le point de départ du Bac informatique. Structure d'un algorithme, TDO, installation de Python, Thonny, numpy et PyQt5.",
    'lead': "Un <strong>algorithme</strong> est une suite finie et ordonnée d'instructions qui permet de résoudre un problème. Au Bac scientifique en Tunisie, on écrit d'abord la solution sous forme d'algorithme, puis on la <strong>traduit en Python</strong>, le langage officiel de l'épreuve pratique.",
    'bref': [
        "Algorithme = la solution écrite en langage structuré, indépendante de tout langage de programmation.",
        "Programme = la traduction de l'algorithme dans un langage (ici Python 3).",
        "Un algorithme commence par <code>Algorithme Nom</code>, contient les instructions entre <code>Début</code> et <code>Fin</code>, et ses objets sont déclarés dans un <strong>TDO</strong>.",
        "Outils à installer : Python 3, l'éditeur Thonny, les bibliothèques numpy et PyQt5 (avec Qt Designer).",
    ],
    'body': [
        ('definition', "Qu'est-ce qu'un algorithme ?",
         DEF('Algorithme', "suite finie et ordonnée d'instructions qui, exécutées dans l'ordre, permettent de résoudre un problème donné.")
         + "<p>Tu utilises des algorithmes tous les jours sans le savoir : une recette de cuisine, l'itinéraire pour aller au lycée ou la notice de montage d'un meuble. Chacun décrit des <strong>étapes précises</strong>, dans un <strong>ordre précis</strong>, qui mènent à un <strong>résultat</strong>.</p>"
         + "<p>Un bon algorithme a trois qualités :</p>"
         + UL(["<strong>il est fini</strong> : il s'arrête toujours après un nombre limité d'étapes ;",
               "<strong>il est précis</strong> : chaque instruction n'a qu'une seule interprétation possible ;",
               "<strong>il est général</strong> : il fonctionne pour toutes les données valides, pas seulement pour un exemple."])),
        ('algo-programme', "De l'algorithme au programme Python",
         "<p>Résoudre un problème en informatique se fait en deux temps : on <strong>réfléchit</strong> à la solution (l'algorithme), puis on la <strong>traduit</strong> pour que l'ordinateur puisse l'exécuter (le programme).</p>"
         + T(['', 'Algorithme', 'Programme'], [
             ['Rôle', 'Décrire la solution', "Faire exécuter la solution par l'ordinateur"],
             ['Langage', 'Langage algorithmique (notation officielle)', 'Langage de programmation : Python 3'],
             ['Exécutable ?', 'Non, il se lit et se vérifie à la main', 'Oui, avec un interpréteur Python'],
             ['Règles', 'Notation structurée (Début, Fin, Si, Pour…)', 'Syntaxe stricte : indentation, deux-points, parenthèses'],
         ], cap="Algorithme et programme : les différences")
         + "<p>Pourquoi Python ? Sa syntaxe est proche du langage naturel, il est gratuit, il fonctionne sur tous les ordinateurs, et c'est le langage retenu pour l'épreuve pratique d'informatique du baccalauréat tunisien.</p>"),
        ('structure', "La structure d'un algorithme",
         "<p>Tout algorithme suit la même structure : un <strong>nom</strong>, puis les instructions placées entre <code>Début</code> et <code>Fin</code>. Les objets utilisés (variables, constantes) sont décrits dans un tableau à part : le <strong>TDO</strong> (tableau de déclaration des objets).</p>"
         + DUO('''
            Algorithme Moyenne
            Début
                Écrire("Donner la première note : ")
                Lire(n1)
                Écrire("Donner la deuxième note : ")
                Lire(n2)
                moy ← (n1 + n2) / 2
                Écrire("La moyenne est ", moy)
            Fin''', '''
            n1 = float(input("Donner la première note : "))
            n2 = float(input("Donner la deuxième note : "))
            moy = (n1 + n2) / 2
            print("La moyenne est", moy)''')
         + TDO([('n1', 'Réel'), ('n2', 'Réel'), ('moy', 'Réel')])
         + "<p>Remarque que Python n'a ni <code>Début</code> ni <code>Fin</code> : un programme commence à la première ligne et se termine à la dernière. La déclaration des variables n'existe pas non plus : une variable est créée au moment où on lui donne une valeur.</p>"),
        ('installer', "Installer son environnement de travail",
         "<p>Pour suivre le programme du Bac, tu as besoin de quatre outils, tous gratuits :</p>"
         + T(['Outil', 'À quoi il sert', 'Comment l\'obtenir'], [
             ['Python 3', 'Exécuter les programmes', 'Télécharger sur python.org (cocher « Add Python to PATH » sous Windows)'],
             ['Thonny', 'Écrire et exécuter le code, avec un débogueur pas à pas', 'Télécharger sur thonny.org'],
             ['numpy', 'Créer des tableaux avec <code>array</code>', '<code>pip install numpy</code> ou, dans Thonny : Outils → Gérer les paquets'],
             ['PyQt5 + Qt Designer', "Créer des interfaces graphiques", '<code>pip install pyqt5 pyqt5-tools</code>'],
         ], cap="Les outils de l'informaticien au Bac")
         + P('''
            pip install numpy pyqt5 pyqt5-tools''', 'Terminal (invite de commandes)')
         + TIP("Entraîne-toi sur le même environnement que celui du lycée. Le jour de l'épreuve, tu n'auras pas le temps de découvrir un nouvel éditeur.")),
        ('bonnes-pratiques', "Les bonnes pratiques dès le départ",
         UL(["Donne des <strong>noms clairs</strong> à tes variables : <code>moyenne</code> plutôt que <code>m</code>.",
             "Respecte l'<strong>indentation</strong> (4 espaces) : en Python, elle fait partie de la syntaxe.",
             "Écris un <strong>commentaire</strong> avec <code>#</code> pour expliquer une ligne difficile.",
             "<strong>Teste</strong> ton programme avec plusieurs valeurs, y compris des cas limites (0, valeur négative, saisie vide).",
             "Enregistre ton travail <strong>souvent</strong>."])),
    ],
    'retenir': [
        "Algorithme = solution structurée ; programme = sa traduction en Python.",
        "Un algorithme : <code>Algorithme Nom</code>, <code>Début</code>, instructions, <code>Fin</code> + un TDO.",
        "Python ne déclare pas ses variables et n'a pas de Début/Fin : l'indentation structure le code.",
    ],
    'faq': [
        ("Quelle est la différence entre un algorithme et un programme ?",
         "L'algorithme décrit la solution dans un langage structuré, indépendant de tout langage informatique. Le programme est la traduction de cet algorithme dans un langage que l'ordinateur sait exécuter, comme Python."),
        ("Faut-il savoir lire un algorithme pour le Bac pratique ?",
         "Oui. Certains sujets donnent directement un algorithme (par exemple une fonction Palindrome en 2025) et demandent de l'implémenter en Python. Il faut donc savoir traduire chaque instruction algorithmique."),
        ("Quel éditeur utiliser pour programmer en Python au Bac ?",
         "Thonny est l'éditeur le plus utilisé dans les lycées tunisiens : il est simple, installe Python automatiquement et permet d'exécuter le code ligne par ligne."),
    ],
}

CH2 = {
    'slug': 'cours/entrees-sorties-affectation',
    'short': 'Entrées, sorties, affectation',
    'h1': "Les actions élémentaires : affectation, entrées et sorties",
    'title': 'Affectation, Lire, Écrire : input et print | Bac',
    'desc': 'Affectation (←), lecture (Lire / input) et écriture (Écrire / print) : les actions de base, avec leur traduction Python pour le Bac Sciences en Tunisie.',
    'lead': "Tout algorithme est construit avec trois actions élémentaires : l'<strong>affectation</strong> (<code>←</code>, en Python <code>=</code>), la <strong>lecture</strong> d'une donnée (<code>Lire</code>, en Python <code>input()</code>) et l'<strong>écriture</strong> d'un résultat (<code>Écrire</code>, en Python <code>print()</code>).",
    'bref': [
        "<code>x ← 5</code> s'écrit <code>x = 5</code> en Python : on range la valeur 5 dans la variable x.",
        "<code>Lire(x)</code> devient <code>x = input()</code>, mais <code>input()</code> renvoie <strong>toujours une chaîne</strong>.",
        "Pour lire un nombre : <code>int(input())</code> (entier) ou <code>float(input())</code> (réel).",
        "<code>Écrire(\"msg\", x)</code> devient <code>print(\"msg\", x)</code>.",
    ],
    'body': [
        ('affectation', "L'affectation : ranger une valeur",
         DEF('Affectation', "action qui range une valeur dans une variable. L'ancienne valeur de la variable est remplacée.")
         + DUO('''
            x ← 5
            y ← x + 2
            x ← x * 10''', '''
            x = 5
            y = x + 2      # y vaut 7
            x = x * 10     # x vaut 50''')
         + "<p>L'affectation se lit <strong>de droite à gauche</strong> : on calcule d'abord l'expression à droite, puis on range le résultat dans la variable à gauche. C'est pour cela que <code>x ← x * 10</code> a un sens : on prend l'ancienne valeur de x, on la multiplie par 10, et on range le résultat dans x.</p>"
         + WARN("En Python, le signe <code>=</code> ne veut pas dire « égal » comme en mathématiques : il veut dire « reçoit ». Pour <strong>comparer</strong> deux valeurs, on utilise <code>==</code>.")),
        ('permutation', "Permuter deux variables",
         "<p>Échanger le contenu de deux variables est une opération classique (on la retrouve dans tous les algorithmes de tri). Il faut une <strong>variable auxiliaire</strong>, sinon une des deux valeurs est perdue.</p>"
         + DUO('''
            aux ← a
            a ← b
            b ← aux''', '''
            aux = a
            a = b
            b = aux''')
         + NOTE("Python permet aussi d'écrire <code>a, b = b, a</code>. Au Bac, les deux écritures sont acceptées, mais la version avec <code>aux</code> montre que tu as compris le mécanisme.")),
        ('sortie', "La sortie : Écrire / print",
         "<p>L'instruction de sortie affiche un message ou une valeur à l'écran.</p>"
         + DUO('''
            Écrire("Bonjour")
            Écrire("La somme est ", s)''', '''
            print("Bonjour")
            print("La somme est", s)''')
         + "<p><code>print</code> sépare automatiquement ses arguments par un espace et passe à la ligne à la fin. Deux paramètres permettent de changer ce comportement :</p>"
         + P('''
            print("a", "b", "c", sep="-")    # affiche a-b-c
            print("Sans retour", end=" ")
            print("à la ligne")              # affiche Sans retour à la ligne''')),
        ('entree', "L'entrée : Lire / input",
         "<p>L'instruction d'entrée demande une valeur à l'utilisateur. En algorithmique on écrit souvent un message avec <code>Écrire</code>, puis <code>Lire</code>. En Python, <code>input</code> fait les deux à la fois.</p>"
         + DUO('''
            Écrire("Donner votre âge : ")
            Lire(age)''', '''
            age = int(input("Donner votre âge : "))''')
         + WARN("<code>input()</code> renvoie <strong>toujours du texte</strong> (type <code>str</code>). Si l'utilisateur tape 17, la variable contient la chaîne <code>\"17\"</code>, et <code>\"17\" + 1</code> provoque une erreur. Il faut convertir : <code>int(input())</code> pour un entier, <code>float(input())</code> pour un réel.")),
        ('exemple-complet', "Exemple complet : périmètre et surface d'un cercle",
         DUO('''
            Algorithme Cercle
            Début
                Écrire("Donner le rayon : ")
                Lire(r)
                p ← 2 * PI * r
                s ← PI * r * r
                Écrire("Périmètre = ", p)
                Écrire("Surface = ", s)
            Fin''', '''
            from math import pi

            r = float(input("Donner le rayon : "))
            p = 2 * pi * r
            s = pi * r * r
            print("Périmètre =", p)
            print("Surface =", s)''')
         + TDO([('PI', 'Constante = 3.14'), ('r', 'Réel'), ('p', 'Réel'), ('s', 'Réel')])),
        ('correspondances', "Tableau des correspondances",
         T(['Action', 'Algorithme', 'Python'], [
             ['Affectation', '<code>x ← 5</code>', '<code>x = 5</code>'],
             ['Lire une chaîne', '<code>Lire(ch)</code>', '<code>ch = input()</code>'],
             ['Lire un entier', '<code>Lire(n)</code>', '<code>n = int(input())</code>'],
             ['Lire un réel', '<code>Lire(x)</code>', '<code>x = float(input())</code>'],
             ['Afficher', '<code>Écrire("x = ", x)</code>', '<code>print("x =", x)</code>'],
         ], cap="Actions élémentaires : algorithme ↔ Python")),
    ],
    'retenir': [
        "L'affectation se lit de droite à gauche et remplace l'ancienne valeur.",
        "<code>input()</code> renvoie toujours une chaîne : convertir avec <code>int()</code> ou <code>float()</code>.",
        "Pour permuter deux variables, passer par une variable auxiliaire.",
    ],
    'faq': [
        ("Comment lire un nombre entier en Python ?",
         "On convertit la saisie avec int : <code>n = int(input(\"n = \"))</code>. Sans int, la variable contient du texte."),
        ("Que signifie la flèche ← en algorithmique ?",
         "C'est l'affectation : la valeur à droite est rangée dans la variable à gauche. En Python, elle s'écrit avec un seul signe égal."),
        ("Pourquoi \"5\" + \"3\" donne \"53\" en Python ?",
         "Parce que ce sont deux chaînes de caractères : l'opérateur + les met bout à bout (concaténation). Avec des nombres, 5 + 3 donne 8."),
    ],
}

CH3 = {
    'slug': 'cours/variables-types-operateurs',
    'short': 'Variables, types et opérateurs',
    'h1': "Variables, types, constantes et opérateurs",
    'title': 'Variables, types et opérateurs Python | Bac Tunisie',
    'desc': 'Types Entier, Réel, Booléen, Chaîne, conversions, constantes et opérateurs DIV, MOD, ET, OU, NON, avec leur traduction Python. Cours du Bac Sciences.',
    'lead': "Une <strong>variable</strong> est un nom qui désigne une case de la mémoire contenant une valeur. Chaque valeur a un <strong>type</strong> (entier, réel, booléen, caractère, chaîne) qui détermine les opérations possibles. Au Bac, il faut connaître chaque type, chaque opérateur et leur traduction en Python.",
    'bref': [
        "5 types simples : Entier (<code>int</code>), Réel (<code>float</code>), Booléen (<code>bool</code>), Caractère et Chaîne (<code>str</code>).",
        "<code>DIV</code> s'écrit <code>//</code> (quotient entier) et <code>MOD</code> s'écrit <code>%</code> (reste).",
        "<code>ET</code>, <code>OU</code>, <code>NON</code> s'écrivent <code>and</code>, <code>or</code>, <code>not</code>.",
        "Conversions : <code>int()</code>, <code>float()</code>, <code>str()</code>.",
    ],
    'body': [
        ('variable', "Variable et constante",
         DEF('Variable', "objet dont la valeur peut changer pendant l'exécution. Elle est identifiée par un nom.")
         + DEF('Constante', "objet dont la valeur est fixée une fois pour toutes et ne change jamais.")
         + "<p>Règles pour nommer une variable en Python : commencer par une lettre ou <code>_</code>, ne contenir que des lettres, des chiffres et <code>_</code>, pas d'espace, et éviter les mots réservés (<code>if</code>, <code>for</code>, <code>def</code>…). Python distingue majuscules et minuscules : <code>Note</code> et <code>note</code> sont deux variables différentes.</p>"
         + "<p>Python n'a pas de vraies constantes. Par convention, on écrit leur nom en majuscules :</p>"
         + DUO('''
            Algorithme Remise
            Début
                Lire(prix)
                net ← prix * (1 - TAUX)
                Écrire("Prix net : ", net)
            Fin''', '''
            TAUX = 0.2          # constante (convention : majuscules)
            prix = float(input("Prix : "))
            net = prix * (1 - TAUX)
            print("Prix net :", net)''')
         + TDO([('TAUX', 'Constante = 0.2'), ('prix', 'Réel'), ('net', 'Réel')])),
        ('types', "Les types de données",
         T(['Type (algorithme)', 'Python', 'Exemples', 'Remarque'], [
             ['Entier', '<code>int</code>', '<code>17</code>, <code>-4</code>, <code>0</code>', 'Pas de limite de taille en Python'],
             ['Réel', '<code>float</code>', '<code>3.14</code>, <code>-0.5</code>, <code>2.0</code>', 'Le séparateur décimal est le point'],
             ['Booléen', '<code>bool</code>', '<code>True</code>, <code>False</code>', 'Vrai / Faux en algorithmique'],
             ['Caractère', '<code>str</code>', '<code>"a"</code>, <code>"7"</code>', 'Une chaîne de longueur 1 en Python'],
             ['Chaîne', '<code>str</code>', '<code>"Bac 2027"</code>', 'Entre guillemets'],
         ], cap="Les types simples")
         + "<p>La fonction <code>type()</code> donne le type d'une valeur : <code>type(3.0)</code> renvoie <code>&lt;class 'float'&gt;</code>.</p>"),
        ('conversions', "Les conversions de type",
         T(['Conversion', 'Algorithme', 'Python', 'Exemple'], [
             ['Chaîne → entier', '<code>Valeur(ch)</code>', '<code>int(ch)</code>', '<code>int("42")</code> → 42'],
             ['Chaîne → réel', '<code>Valeur(ch)</code>', '<code>float(ch)</code>', '<code>float("2.5")</code> → 2.5'],
             ['Nombre → chaîne', '<code>Convch(x)</code>', '<code>str(x)</code>', '<code>str(42)</code> → "42"'],
             ['Réel → entier (partie entière)', '<code>Ent(x)</code>', '<code>int(x)</code>', '<code>int(7.9)</code> → 7'],
         ], cap="Conversions : algorithme ↔ Python")
         + WARN("<code>int(\"abc\")</code> ou <code>int(\"\")</code> provoque une erreur <code>ValueError</code>. Avant de convertir une saisie, vérifie qu'elle contient bien des chiffres (voir le chapitre sur les chaînes : <code>isdigit()</code>).")),
        ('arithmetiques', "Les opérateurs arithmétiques",
         T(['Opération', 'Algorithme', 'Python', 'Exemple', 'Résultat'], [
             ['Addition', '<code>+</code>', '<code>+</code>', '<code>7 + 2</code>', '9'],
             ['Soustraction', '<code>-</code>', '<code>-</code>', '<code>7 - 2</code>', '5'],
             ['Multiplication', '<code>*</code>', '<code>*</code>', '<code>7 * 2</code>', '14'],
             ['Division réelle', '<code>/</code>', '<code>/</code>', '<code>7 / 2</code>', '3.5'],
             ['Quotient entier', '<code>DIV</code>', '<code>//</code>', '<code>7 // 2</code>', '3'],
             ['Reste de la division', '<code>MOD</code>', '<code>%</code>', '<code>7 % 2</code>', '1'],
             ['Puissance', '—', '<code>**</code>', '<code>2 ** 3</code>', '8'],
         ], cap="Opérateurs arithmétiques")
         + TIP("<code>MOD</code> est l'opérateur le plus utilisé au Bac : <code>n % 2 == 0</code> teste si n est pair, <code>n % d == 0</code> teste si d divise n, <code>n % 10</code> donne le dernier chiffre de n et <code>n // 10</code> le supprime.")),
        ('comparaison-logique', "Opérateurs de comparaison et opérateurs logiques",
         T(['Sens', 'Algorithme', 'Python'], [
             ['égal à', '<code>=</code>', '<code>==</code>'],
             ['différent de', '<code>≠</code>', '<code>!=</code>'],
             ['inférieur / inférieur ou égal', '<code>&lt;</code> / <code>≤</code>', '<code>&lt;</code> / <code>&lt;=</code>'],
             ['supérieur / supérieur ou égal', '<code>&gt;</code> / <code>≥</code>', '<code>&gt;</code> / <code>&gt;=</code>'],
             ['et logique', '<code>ET</code>', '<code>and</code>'],
             ['ou logique', '<code>OU</code>', '<code>or</code>'],
             ['négation', '<code>NON</code>', '<code>not</code>'],
         ], cap="Comparaisons et logique")
         + T(['a', 'b', 'a ET b', 'a OU b', 'NON a'], [
             ['Vrai', 'Vrai', 'Vrai', 'Vrai', 'Faux'],
             ['Vrai', 'Faux', 'Faux', 'Vrai', 'Faux'],
             ['Faux', 'Vrai', 'Faux', 'Vrai', 'Vrai'],
             ['Faux', 'Faux', 'Faux', 'Faux', 'Vrai'],
         ], cap="Table de vérité")
         + NOTE("Python accepte les comparaisons enchaînées : <code>10 &lt;= n &lt;= 99</code> est équivalent à <code>(n &gt;= 10) ET (n &lt;= 99)</code>.")),
        ('fonctions-numeriques', "Les fonctions numériques prédéfinies",
         T(['Rôle', 'Algorithme', 'Python', 'Exemple'], [
             ['Valeur absolue', '<code>Abs(x)</code>', '<code>abs(x)</code>', '<code>abs(-4)</code> → 4'],
             ['Partie entière', '<code>Ent(x)</code>', '<code>int(x)</code>', '<code>int(5.8)</code> → 5'],
             ['Arrondi', '<code>Arrondi(x)</code>', '<code>round(x)</code>', '<code>round(5.8)</code> → 6'],
             ['Racine carrée', '<code>RacineCarré(x)</code>', '<code>sqrt(x)</code> (<code>from math import sqrt</code>)', '<code>sqrt(16)</code> → 4.0'],
             ['Entier aléatoire entre a et b', '<code>Aléa(a, b)</code>', '<code>randint(a, b)</code> (<code>from random import randint</code>)', '<code>randint(1, 6)</code> → 1 à 6'],
         ], cap="Fonctions numériques")
         + WARN("<code>round</code> arrondit les cas « .5 » vers l'entier <strong>pair</strong> le plus proche : <code>round(2.5)</code> donne 2 et <code>round(3.5)</code> donne 4.", "Bon à savoir")),
        ('priorites', "La priorité des opérateurs",
         OL(["les parenthèses <code>( )</code> ;",
             "la puissance <code>**</code> ;",
             "<code>*</code>, <code>/</code>, <code>//</code>, <code>%</code> ;",
             "<code>+</code>, <code>-</code> ;",
             "les comparaisons <code>==</code>, <code>!=</code>, <code>&lt;</code>… ;",
             "<code>not</code>, puis <code>and</code>, puis <code>or</code>."])
         + "<p>En cas de doute, ajoute des parenthèses : <code>(a + b) / 2</code> n'est pas <code>a + b / 2</code>.</p>"),
    ],
    'retenir': [
        "Entier → <code>int</code>, Réel → <code>float</code>, Booléen → <code>bool</code>, Caractère et Chaîne → <code>str</code>.",
        "<code>DIV</code> → <code>//</code>, <code>MOD</code> → <code>%</code>, <code>≠</code> → <code>!=</code>, <code>ET/OU/NON</code> → <code>and/or/not</code>.",
        "<code>=</code> affecte, <code>==</code> compare.",
    ],
    'faq': [
        ("Comment écrire DIV et MOD en Python ?",
         "DIV (quotient de la division entière) s'écrit <code>//</code> et MOD (reste) s'écrit <code>%</code>. Par exemple 17 // 5 vaut 3 et 17 % 5 vaut 2."),
        ("Comment savoir si un nombre est pair en Python ?",
         "Un nombre n est pair si le reste de sa division par 2 est nul : <code>n % 2 == 0</code>."),
        ("Quelle est la différence entre / et // en Python ?",
         "<code>/</code> fait une division réelle (7 / 2 = 3.5) ; <code>//</code> donne le quotient entier (7 // 2 = 3)."),
    ],
}

CH4 = {
    'slug': 'cours/chaines-de-caracteres',
    'short': 'Les chaînes de caractères',
    'h1': "Les chaînes de caractères en algorithme et en Python",
    'title': 'Chaînes de caractères en Python et algorithme | Bac',
    'desc': 'Indices, parcours, concaténation et fonctions Long, Pos, Convch, Valeur, Estnum, Sous_chaine, Effacer, Majus traduites en Python. Cours Bac Tunisie.',
    'lead': "Une <strong>chaîne de caractères</strong> est une suite de caractères entre guillemets. Chaque caractère a une position, son <strong>indice</strong>, qui commence à <strong>0</strong>. Les chaînes sont partout dans les sujets du Bac : on parcourt les chiffres d'un nombre, on teste un palindrome, on construit un message.",
    'bref': [
        "<code>ch[i]</code> est le caractère d'indice i ; les indices vont de 0 à <code>Long(ch) - 1</code>.",
        "<code>Long(ch)</code> → <code>len(ch)</code> ; <code>Sous_chaine(ch, d, f)</code> → <code>ch[d:f]</code>.",
        "<code>+</code> met deux chaînes bout à bout (concaténation).",
        "Une chaîne Python ne se modifie pas : on en construit une nouvelle.",
    ],
    'body': [
        ('indices', "Indices et accès aux caractères",
         "<p>Dans <code>ch = \"PYTHON\"</code>, le caractère <code>P</code> a l'indice 0 et <code>N</code> a l'indice 5. Python accepte aussi les indices négatifs, qui partent de la fin.</p>"
         + T(['Caractère', 'P', 'Y', 'T', 'H', 'O', 'N'], [
             ['Indice', '0', '1', '2', '3', '4', '5'],
             ['Indice négatif', '-6', '-5', '-4', '-3', '-2', '-1'],
         ], cap='Indices de la chaîne "PYTHON"')
         + DUO('''
            ch ← "PYTHON"
            Écrire(ch[0])
            Écrire(ch[Long(ch) - 1])''', '''
            ch = "PYTHON"
            print(ch[0])             # P
            print(ch[len(ch) - 1])   # N  (ou ch[-1])''')
         + WARN("Le dernier caractère est <code>ch[len(ch) - 1]</code>. Écrire <code>ch[len(ch)]</code> provoque une erreur <code>IndexError</code>.")),
        ('fonctions', "Les fonctions prédéfinies sur les chaînes",
         T(['Rôle', 'Algorithme', 'Python', 'Exemple (ch = "bonjour")'], [
             ['Longueur', '<code>Long(ch)</code>', '<code>len(ch)</code>', '<code>len(ch)</code> → 7'],
             ['Position de ch1 dans ch2 (-1 si absente)', '<code>Pos(ch1, ch2)</code>', '<code>ch2.find(ch1)</code>', '<code>ch.find("jour")</code> → 3'],
             ['Nombre → chaîne', '<code>Convch(x)</code>', '<code>str(x)</code>', '<code>str(25)</code> → "25"'],
             ['Chaîne → nombre', '<code>Valeur(ch)</code>', '<code>int(ch)</code> / <code>float(ch)</code>', '<code>int("25")</code> → 25'],
             ['La chaîne est-elle numérique ?', '<code>Estnum(ch)</code>', '<code>ch.isdigit()</code>', '<code>"2025".isdigit()</code> → True'],
             ['Sous-chaîne de d à f (f exclu)', '<code>Sous_chaine(ch, d, f)</code>', '<code>ch[d:f]</code>', '<code>ch[0:3]</code> → "bon"'],
             ['Effacer de d à f (f exclu)', '<code>Effacer(ch, d, f)</code>', '<code>ch[:d] + ch[f:]</code>', '<code>ch[:3] + ch[6:]</code> → "bonr"'],
             ['Majuscules', '<code>Majus(ch)</code>', '<code>ch.upper()</code>', '<code>ch.upper()</code> → "BONJOUR"'],
             ['Code d\'un caractère', '<code>Ord(c)</code>', '<code>ord(c)</code>', '<code>ord("A")</code> → 65'],
             ['Caractère d\'un code', '<code>Chr(n)</code>', '<code>chr(n)</code>', '<code>chr(66)</code> → "B"'],
         ], cap="Fonctions sur les chaînes : algorithme ↔ Python")
         + NOTE("<code>isdigit()</code> renvoie <code>True</code> seulement si la chaîne n'est pas vide et ne contient que des chiffres. <code>\"-5\".isdigit()</code> et <code>\"2.5\".isdigit()</code> renvoient <code>False</code>.")),
        ('concatenation', "Concaténation et construction d'une chaîne",
         "<p>L'opérateur <code>+</code> colle deux chaînes. On l'utilise souvent pour construire un résultat caractère par caractère, en partant d'une chaîne vide <code>\"\"</code>.</p>"
         + DUO('''
            inv ← ""
            Pour i de 0 à Long(ch) - 1 Faire
                inv ← ch[i] + inv
            Fin Pour''', '''
            inv = ""
            for i in range(len(ch)):
                inv = ch[i] + inv     # ajoute ch[i] devant
            # "bac" donne "cab"''', cap_p='Inverser une chaîne en Python')
         + WARN("Une chaîne Python est <strong>non modifiable</strong> : <code>ch[0] = \"B\"</code> provoque une erreur. Il faut construire une nouvelle chaîne : <code>ch = \"B\" + ch[1:]</code>.")),
        ('parcours', "Parcourir une chaîne",
         "<p>Le parcours caractère par caractère sert à compter, chercher ou vérifier. Voici le comptage des voyelles :</p>"
         + DUO('''
            Fonction NbVoyelles(ch : Chaîne) : Entier
            Début
                nb ← 0
                Pour i de 0 à Long(ch) - 1 Faire
                    Si Pos(ch[i], "aeiouy") ≠ -1 Alors
                        nb ← nb + 1
                    Fin Si
                Fin Pour
                Retourner nb
            Fin''', '''
            def nb_voyelles(ch):
                nb = 0
                for i in range(len(ch)):
                    if "aeiouy".find(ch[i]) != -1:
                        nb = nb + 1
                return nb''')),
        ('nombre-chaine', "Passer d'un nombre à une chaîne (et inversement)",
         "<p>Beaucoup de sujets du Bac portent sur les <strong>chiffres d'un nombre</strong> (palindrome, nombre ondulant, somme des chiffres…). Deux méthodes existent :</p>"
         + UL(["<strong>convertir en chaîne</strong> avec <code>str(n)</code>, puis parcourir les caractères ; chaque chiffre se reconvertit avec <code>int(ch[i])</code> ;",
               "<strong>rester en nombres</strong> avec <code>n % 10</code> (dernier chiffre) et <code>n // 10</code> (on le retire)."])
         + P('''
            n = 2025
            ch = str(n)
            s = 0
            for i in range(len(ch)):
                s = s + int(ch[i])
            print(s)      # 2 + 0 + 2 + 5 = 9''', 'Somme des chiffres par conversion en chaîne')),
    ],
    'retenir': [
        "Les indices vont de 0 à <code>len(ch) - 1</code>.",
        "<code>Long</code> → <code>len</code>, <code>Pos</code> → <code>find</code>, <code>Sous_chaine</code> → <code>ch[d:f]</code>, <code>Estnum</code> → <code>isdigit()</code>.",
        "On ne modifie pas une chaîne : on en construit une nouvelle avec <code>+</code>.",
    ],
    'faq': [
        ("Comment obtenir la longueur d'une chaîne en Python ?",
         "Avec la fonction <code>len</code> : <code>len(\"Tunis\")</code> renvoie 5. Elle correspond à <code>Long(ch)</code> en algorithmique."),
        ("Comment traduire Sous_chaine(ch, d, f) en Python ?",
         "Par une tranche : <code>ch[d:f]</code>. Le caractère d'indice f n'est pas inclus."),
        ("Comment vérifier qu'une saisie contient seulement des chiffres ?",
         "Avec <code>ch.isdigit()</code>, l'équivalent de <code>Estnum(ch)</code>. C'est la vérification la plus courante dans le module Play du Bac pratique."),
    ],
}

CH5 = {
    'slug': 'cours/structures-conditionnelles',
    'short': 'Structures conditionnelles',
    'h1': "Les structures conditionnelles : Si, Sinon, Selon",
    'title': 'Si, Sinon, Selon en Python (if, elif, else) | Bac',
    'desc': 'Structures conditionnelles : Si simple, complète, généralisée et Selon, traduites en Python avec if, else, elif et match. Cours Bac Sciences Tunisie.',
    'lead': "Une <strong>structure conditionnelle</strong> permet d'exécuter des instructions seulement si une condition est vraie. Le programme officiel distingue quatre formes : <strong>Si simple</strong>, <strong>Si complète</strong> (Si…Sinon), <strong>Si généralisée</strong> (Sinon Si) et <strong>Selon</strong>. En Python, elles s'écrivent avec <code>if</code>, <code>else</code>, <code>elif</code> et <code>match</code>.",
    'bref': [
        "<code>Si … Alors … Fin Si</code> → <code>if condition:</code>",
        "<code>Sinon</code> → <code>else:</code> ; <code>Sinon Si</code> → <code>elif condition:</code>",
        "Python termine chaque condition par <strong>deux-points</strong> et indente le bloc de 4 espaces.",
        "Une seule branche est exécutée : la première dont la condition est vraie.",
    ],
    'body': [
        ('si-simple', "La forme simple",
         "<p>Les instructions ne sont exécutées que si la condition est vraie. Sinon, on passe directement à la suite.</p>"
         + DUO('''
            Si n < 0 Alors
                n ← -n
            Fin Si''', '''
            if n < 0:
                n = -n''')),
        ('si-complete', "La forme complète : Si … Sinon",
         DUO('''
            Si n MOD 2 = 0 Alors
                Écrire(n, " est pair")
            Sinon
                Écrire(n, " est impair")
            Fin Si''', '''
            if n % 2 == 0:
                print(n, "est pair")
            else:
                print(n, "est impair")''')
         + NOTE("Le <code>else</code> n'a jamais de condition : il traite <strong>tous les autres cas</strong>.")),
        ('si-generalisee', "La forme généralisée : Sinon Si",
         "<p>Quand il y a plus de deux cas, on enchaîne les conditions. Python les teste <strong>de haut en bas</strong> et s'arrête à la première qui est vraie.</p>"
         + DUO('''
            Si moy ≥ 16 Alors
                mention ← "Très bien"
            Sinon Si moy ≥ 14 Alors
                mention ← "Bien"
            Sinon Si moy ≥ 12 Alors
                mention ← "Assez bien"
            Sinon Si moy ≥ 10 Alors
                mention ← "Passable"
            Sinon
                mention ← "Sans mention"
            Fin Si''', '''
            if moy >= 16:
                mention = "Très bien"
            elif moy >= 14:
                mention = "Bien"
            elif moy >= 12:
                mention = "Assez bien"
            elif moy >= 10:
                mention = "Passable"
            else:
                mention = "Sans mention"''')
         + WARN("L'ordre compte. Si on teste <code>moy &gt;= 10</code> en premier, une moyenne de 17 recevrait « Passable », car Python s'arrête à la première condition vraie.")),
        ('selon', "La structure Selon",
         "<p><code>Selon</code> choisit un traitement d'après la <strong>valeur</strong> d'une variable. Depuis Python 3.10, on peut la traduire avec <code>match</code> ; avec une version plus ancienne, on utilise <code>if … elif</code>.</p>"
         + DUO('''
            Selon j Faire
                1 : nom ← "Lundi"
                2 : nom ← "Mardi"
                6, 7 : nom ← "Week-end"
            Sinon
                nom ← "Autre jour"
            Fin Selon''', '''
            match j:
                case 1:
                    nom = "Lundi"
                case 2:
                    nom = "Mardi"
                case 6 | 7:
                    nom = "Week-end"
                case _:
                    nom = "Autre jour"''', cap_p='Python 3.10 et plus')
         + P('''
            if j == 1:
                nom = "Lundi"
            elif j == 2:
                nom = "Mardi"
            elif j == 6 or j == 7:
                nom = "Week-end"
            else:
                nom = "Autre jour"''', 'Équivalent avec if / elif (toutes versions)')),
        ('conditions-composees', "Les conditions composées",
         "<p>On combine plusieurs conditions avec <code>and</code>, <code>or</code> et <code>not</code>.</p>"
         + T(['Condition', 'Algorithme', 'Python'], [
             ['n est un nombre de 3 chiffres', '<code>(n ≥ 100) ET (n ≤ 999)</code>', '<code>100 &lt;= n &lt;= 999</code>'],
             ['n est hors de [1, 20]', '<code>(n &lt; 1) OU (n &gt; 20)</code>', '<code>n &lt; 1 or n &gt; 20</code>'],
             ['c est une voyelle', '<code>Pos(c, "aeiouy") ≠ -1</code>', '<code>c in "aeiouy"</code>'],
             ['ch n\'est pas numérique', '<code>NON Estnum(ch)</code>', '<code>not ch.isdigit()</code>'],
         ], cap="Exemples de conditions composées")
         + WARN("<code>n &gt; 5 or n &lt; 10</code> est toujours vrai : tout nombre est soit plus grand que 5, soit plus petit que 10. Pour un intervalle, on utilise <code>and</code>.")),
        ('syntaxe', "Les règles de syntaxe en Python",
         UL(["chaque ligne <code>if</code>, <code>elif</code>, <code>else</code> se termine par <strong>deux-points</strong> <code>:</code> ;",
             "le bloc à exécuter est <strong>indenté</strong> (décalé de 4 espaces) ;",
             "on compare avec <code>==</code>, jamais avec <code>=</code> ;",
             "il n'y a pas de <code>Fin Si</code> : le bloc se termine quand l'indentation revient à gauche."])),
    ],
    'retenir': [
        "Si → <code>if</code>, Sinon Si → <code>elif</code>, Sinon → <code>else</code>, Selon → <code>match</code> ou <code>if/elif</code>.",
        "Deux-points et indentation obligatoires.",
        "Une seule branche est exécutée : la première condition vraie, de haut en bas.",
    ],
    'faq': [
        ("Comment traduire Sinon Si en Python ?",
         "Avec le mot-clé <code>elif</code>, contraction de « else if »."),
        ("Comment traduire la structure Selon en Python ?",
         "Avec <code>match … case</code> à partir de Python 3.10, ou avec une suite de <code>if … elif … else</code> qui fonctionne dans toutes les versions."),
        ("Pourquoi Python affiche-t-il IndentationError ?",
         "Parce que le bloc qui suit un <code>if</code>, <code>elif</code> ou <code>else</code> n'est pas correctement décalé. Toutes les lignes d'un même bloc doivent avoir exactement la même indentation."),
    ],
}

CH6 = {
    'slug': 'cours/structures-iteratives',
    'short': 'Structures itératives (boucles)',
    'h1': "Les structures itératives : Pour, Tant que, Répéter",
    'title': 'Boucles Pour, Tant que, Répéter en Python | Bac',
    'desc': "Boucles Pour (for, range), Tant que (while) et Répéter … Jusqu'à en Python, compteurs, accumulateurs et saisie contrôlée. Cours Bac Sciences Tunisie.",
    'lead': "Une <strong>structure itérative</strong> (ou boucle) répète un bloc d'instructions. On utilise la boucle <strong>Pour</strong> quand le nombre de répétitions est connu, et les boucles <strong>Tant que</strong> ou <strong>Répéter … Jusqu'à</strong> quand il dépend d'une condition.",
    'bref': [
        "<code>Pour i de d à f Faire</code> → <code>for i in range(d, f + 1):</code> (la borne f est incluse en algorithme, exclue dans range).",
        "<code>Tant que cond Faire</code> → <code>while cond:</code>",
        "<code>Répéter … Jusqu'à cond</code> n'existe pas en Python : on écrit <code>while True:</code> … <code>if cond: break</code>.",
        "Somme et compteur commencent à 0, produit à 1.",
    ],
    'body': [
        ('pour', "La boucle Pour (nombre de tours connu)",
         DUO('''
            Pour i de 1 à 5 Faire
                Écrire(i)
            Fin Pour''', '''
            for i in range(1, 6):
                print(i)          # 1 2 3 4 5''')
         + WARN("En algorithmique, <code>Pour i de 1 à 5</code> <strong>inclut</strong> 5. Dans <code>range(1, 6)</code>, la borne 6 est <strong>exclue</strong>. Règle de traduction : <code>Pour i de d à f</code> → <code>range(d, f + 1)</code>.")
         + T(['Algorithme', 'Python', 'Valeurs de i'], [
             ['<code>Pour i de 0 à n - 1 Faire</code>', '<code>for i in range(n):</code>', '0, 1, …, n − 1'],
             ['<code>Pour i de 1 à n Faire</code>', '<code>for i in range(1, n + 1):</code>', '1, 2, …, n'],
             ['<code>Pour i de 0 à 10 (pas = 2) Faire</code>', '<code>for i in range(0, 11, 2):</code>', '0, 2, 4, 6, 8, 10'],
             ['<code>Pour i de n à 1 (pas = -1) Faire</code>', '<code>for i in range(n, 0, -1):</code>', 'n, n − 1, …, 1'],
         ], cap="Traduire la boucle Pour avec range")),
        ('tant-que', "La boucle Tant que (condition testée avant)",
         "<p>La condition est testée <strong>avant</strong> chaque tour. Si elle est fausse dès le départ, la boucle ne s'exécute jamais.</p>"
         + DUO('''
            n ← 1
            Tant que n < 1000 Faire
                n ← n * 2
            Fin Tant que
            Écrire(n)''', '''
            n = 1
            while n < 1000:
                n = n * 2
            print(n)          # 1024''')
         + WARN("Il faut que la condition finisse par devenir fausse. Si rien ne change dans la boucle, le programme ne s'arrête jamais : c'est une <strong>boucle infinie</strong>.")),
        ('repeter', "La boucle Répéter … Jusqu'à (condition testée après)",
         "<p>Le bloc est exécuté <strong>au moins une fois</strong>, puis répété <strong>jusqu'à ce que</strong> la condition devienne vraie. Python n'a pas d'équivalent direct ; deux traductions sont possibles.</p>"
         + DUO('''
            Répéter
                Écrire("Donner une note entre 0 et 20 : ")
                Lire(note)
            Jusqu'à (note ≥ 0) ET (note ≤ 20)''', '''
            while True:
                note = float(input("Donner une note entre 0 et 20 : "))
                if 0 <= note <= 20:
                    break''', cap_p='Traduction 1 : while True et break')
         + P('''
            note = float(input("Donner une note entre 0 et 20 : "))
            while not (0 <= note <= 20):
                note = float(input("Donner une note entre 0 et 20 : "))''', 'Traduction 2 : lecture, puis while not')
         + NOTE("Attention au sens : <code>Répéter … Jusqu'à cond</code> s'arrête quand cond est <strong>vraie</strong>, alors que <code>while cond</code> continue tant que cond est vraie. D'où le <code>not</code> dans la deuxième traduction.")),
        ('choisir', "Quelle boucle choisir ?",
         T(['Situation', 'Boucle', 'Exemple'], [
             ['Nombre de tours connu à l\'avance', 'Pour', 'Parcourir un tableau, calculer une somme de 1 à n'],
             ['Condition à vérifier avant de commencer', 'Tant que', 'Diviser un nombre par 10 tant qu\'il est non nul'],
             ['Action à faire au moins une fois', 'Répéter … Jusqu\'à', 'Saisie contrôlée'],
         ], cap="Choisir la bonne structure itérative")),
        ('accumulateurs', "Compteurs et accumulateurs",
         "<p>Un <strong>compteur</strong> compte des événements (<code>nb ← nb + 1</code>). Un <strong>accumulateur</strong> cumule des valeurs (<code>s ← s + x</code>). Leur valeur de départ est essentielle.</p>"
         + DUO('''
            s ← 0
            p ← 1
            Pour i de 1 à n Faire
                s ← s + i
                p ← p * i
            Fin Pour''', '''
            s = 0      # somme : départ à 0
            p = 1      # produit : départ à 1
            for i in range(1, n + 1):
                s = s + i
                p = p * i''')
         + "<p>Avec n = 5, on obtient s = 15 (1 + 2 + 3 + 4 + 5) et p = 120 (5!). Un produit initialisé à 0 resterait toujours égal à 0.</p>"),
        ('chiffres', "Parcourir les chiffres d'un nombre",
         "<p>Le schéma « <code>n % 10</code> puis <code>n // 10</code> » revient dans presque tous les sujets sur les nombres.</p>"
         + DUO('''
            nb ← 0
            Tant que n ≠ 0 Faire
                chiffre ← n MOD 10
                nb ← nb + 1
                n ← n DIV 10
            Fin Tant que''', '''
            nb = 0
            while n != 0:
                chiffre = n % 10    # dernier chiffre
                nb = nb + 1
                n = n // 10         # on retire ce chiffre''', cap_p='Compter les chiffres de n (n > 0)')),
    ],
    'retenir': [
        "<code>Pour i de d à f</code> → <code>range(d, f + 1)</code>.",
        "Tant que teste avant, Répéter teste après (au moins un passage).",
        "Répéter … Jusqu'à cond → <code>while True:</code> … <code>if cond: break</code>.",
    ],
    'faq': [
        ("Comment traduire Pour i de 1 à n en Python ?",
         "<code>for i in range(1, n + 1):</code>. La fonction range exclut sa borne de fin, d'où le + 1."),
        ("Comment écrire la boucle Répéter Jusqu'à en Python ?",
         "Python n'a pas de boucle Répéter. On utilise <code>while True:</code> avec un <code>break</code> quand la condition d'arrêt est vraie, ou une première lecture suivie de <code>while not condition:</code>."),
        ("Quelle est la différence entre for et while ?",
         "<code>for</code> s'utilise quand on connaît le nombre de tours ; <code>while</code> quand on répète tant qu'une condition reste vraie, sans savoir à l'avance combien de fois."),
    ],
}

CHAPTERS_A = [CH1, CH2, CH3, CH4, CH5, CH6]
