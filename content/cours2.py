from h import P, A, DUO, T, TDO, NOTE, WARN, TIP, DEF, UL, OL, c

CH7 = {
    'slug': 'cours/sous-programmes-fonctions-procedures',
    'short': 'Fonctions et procédures',
    'h1': "Les sous-programmes : fonctions et procédures",
    'title': 'Fonctions et procédures en Python | Bac Tunisie',
    'desc': 'Fonctions, procédures, paramètres, passage par référence (@), TDOL et solution modulaire : le chapitre clé du Bac pratique, traduit en Python.',
    'lead': "Un <strong>sous-programme</strong> est un bloc d'instructions nommé, que l'on écrit une fois et que l'on <strong>appelle</strong> autant de fois que nécessaire. Une <strong>fonction</strong> renvoie un résultat ; une <strong>procédure</strong> réalise une action sans rien renvoyer. Au Bac pratique, une <strong>solution modulaire</strong> (découpée en sous-programmes) est exigée.",
    'bref': [
        "Fonction : <code>Fonction Nom(paramètres) : Type</code> + <code>Retourner</code> → <code>def nom(paramètres):</code> + <code>return</code>.",
        "Procédure : <code>Procédure Nom(paramètres)</code> → <code>def nom(paramètres):</code> sans <code>return</code>.",
        "Un paramètre précédé de <code>@</code> est passé par référence : la procédure peut le modifier.",
        "Les objets locaux d'un sous-programme sont déclarés dans un <strong>TDOL</strong>.",
    ],
    'body': [
        ('pourquoi', "Pourquoi découper en sous-programmes ?",
         UL(["<strong>Lisibilité</strong> : chaque sous-programme a un nom qui dit ce qu'il fait ;",
             "<strong>Réutilisation</strong> : on écrit le code une fois, on l'appelle partout ;",
             "<strong>Tests</strong> : on vérifie chaque partie séparément ;",
             "<strong>Exigence du Bac</strong> : les sujets précisent qu'une solution modulaire est exigée et demandent des fonctions précises (par exemple <code>Premier(A)</code>, <code>Palindrome(CH)</code>, <code>Verif(N)</code>)."])),
        ('fonction', "La fonction : calculer et renvoyer un résultat",
         DEF('Fonction', "sous-programme qui reçoit des paramètres, effectue un traitement et <strong>renvoie un seul résultat</strong> avec <code>Retourner</code>.")
         + DUO('''
            Fonction Moyenne(a, b : Réel) : Réel
            Début
                m ← (a + b) / 2
                Retourner m
            Fin''', '''
            def moyenne(a, b):
                m = (a + b) / 2
                return m''')
         + TDO([('m', 'Réel')], 'Tableau de déclaration des objets locaux (TDOL)')
         + "<p>On <strong>appelle</strong> la fonction dans une expression, et on récupère son résultat :</p>"
         + DUO('''
            moy ← Moyenne(12, 15)
            Écrire(Moyenne(n1, n2))''', '''
            moy = moyenne(12, 15)     # moy vaut 13.5
            print(moyenne(n1, n2))''')
         + WARN("<code>return</code> termine la fonction immédiatement. Une fonction sans <code>return</code> renvoie <code>None</code>. Et <code>print</code> n'est pas <code>return</code> : <code>print</code> affiche, <code>return</code> renvoie une valeur utilisable.")),
        ('fonction-booleenne', "La fonction booléenne",
         "<p>Une fonction qui répond par vrai ou faux est très fréquente au Bac (« vérifier si N est premier », « tester si CH est palindrome »).</p>"
         + DUO('''
            Fonction EstPair(n : Entier) : Booléen
            Début
                Retourner n MOD 2 = 0
            Fin''', '''
            def est_pair(n):
                return n % 2 == 0''')
         + "<p>On l'utilise directement dans une condition : <code>if est_pair(x):</code>.</p>"),
        ('procedure', "La procédure : réaliser une action",
         DEF('Procédure', "sous-programme qui réalise une action (afficher, remplir, trier…) et ne renvoie pas de résultat.")
         + DUO('''
            Procédure Afficher(T : Tab, n : Entier)
            Début
                Pour i de 0 à n - 1 Faire
                    Écrire(T[i])
                Fin Pour
            Fin''', '''
            def afficher(T, n):
                for i in range(n):
                    print(T[i])''')
         + "<p>On appelle une procédure comme une instruction, sur sa propre ligne : <code>afficher(T, n)</code>.</p>"),
        ('parametres', "Paramètres formels, effectifs et mode de passage",
         DEF('Paramètres formels', "les noms écrits dans l'en-tête du sous-programme (<code>a</code>, <code>b</code>).")
         + DEF('Paramètres effectifs', "les valeurs ou variables données au moment de l'appel (<code>12</code>, <code>15</code>).")
         + T(['Mode', 'Notation', 'Effet', 'En Python'], [
             ['Par valeur', '<code>n : Entier</code>', 'Le sous-programme travaille sur une copie : la variable de l\'appelant ne change pas', 'Cas des nombres, chaînes et booléens'],
             ['Par référence', '<code>@T : Tab</code>', 'Le sous-programme peut modifier la variable de l\'appelant', 'Cas des tableaux numpy : une modification de <code>T[i]</code> est visible après l\'appel'],
         ], cap="Passage des paramètres")
         + DUO('''
            Procédure Remplir(@T : Tab, n : Entier)
            Début
                Pour i de 0 à n - 1 Faire
                    Lire(T[i])
                Fin Pour
            Fin''', '''
            def remplir(T, n):
                for i in range(n):
                    T[i] = int(input("T[" + str(i) + "] = "))
            # après remplir(T, n), T est rempli''')
         + NOTE("Une procédure Python ne peut pas modifier un <strong>entier</strong> reçu en paramètre. Pour « lire n » dans un sous-programme, on écrit une <strong>fonction</strong> qui renvoie la valeur : <code>n = saisir()</code>.")),
        ('saisie', "La fonction de saisie contrôlée",
         "<p>Presque tous les sujets demandent de s'assurer de la validité d'une donnée. On l'isole dans une fonction :</p>"
         + DUO('''
            Fonction Saisir() : Entier
            Début
                Répéter
                    Écrire("n = ")
                    Lire(n)
                Jusqu'à (n ≥ 2) ET (n ≤ 20)
                Retourner n
            Fin''', '''
            def saisir():
                n = int(input("n = "))
                while not (2 <= n <= 20):
                    n = int(input("n = "))
                return n''')),
        ('local-global', "Objets locaux et globaux",
         "<p>Un objet <strong>local</strong> est créé dans un sous-programme et n'existe que pendant son exécution. Un objet <strong>global</strong> est déclaré dans le programme principal. Pour éviter les erreurs, un sous-programme doit recevoir ce dont il a besoin par ses <strong>paramètres</strong> et renvoyer son résultat avec <code>return</code>.</p>"),
        ('programme-principal', "Organiser une solution modulaire",
         "<p>Une solution modulaire se compose de sous-programmes, puis d'un programme principal qui les appelle :</p>"
         + P('''
            from numpy import array

            def saisir():
                n = int(input("n = "))
                while not (2 <= n <= 20):
                    n = int(input("n = "))
                return n

            def remplir(T, n):
                for i in range(n):
                    T[i] = int(input("T[" + str(i) + "] = "))

            def somme(T, n):
                s = 0
                for i in range(n):
                    s = s + T[i]
                return s

            # programme principal
            n = saisir()
            T = array([int()] * n)
            remplir(T, n)
            print("Somme =", somme(T, n))''', 'Structure type d\'une solution modulaire')
         + TIP("Au Bac pratique, le programme principal est le <strong>module Play</strong> déclenché par le bouton de l'interface (voir le chapitre sur PyQt5).")),
    ],
    'retenir': [
        "Fonction = renvoie une valeur (<code>return</code>) ; procédure = réalise une action.",
        "Les deux s'écrivent avec <code>def</code> en Python ; on les définit <strong>avant</strong> de les appeler.",
        "<code>@</code> = passage par référence ; en Python, un tableau modifié dans une procédure reste modifié.",
    ],
    'faq': [
        ("Quelle est la différence entre une fonction et une procédure ?",
         "Une fonction renvoie un résultat avec <code>return</code> et s'utilise dans une expression. Une procédure réalise une action (afficher, remplir, trier) sans renvoyer de résultat et s'appelle comme une instruction."),
        ("Que signifie le symbole @ devant un paramètre ?",
         "Il indique un passage par référence : le sous-programme peut modifier la variable de l'appelant. C'est le cas d'un tableau à remplir ou à trier."),
        ("Que veut dire « solution modulaire » au Bac ?",
         "Que le programme doit être découpé en sous-programmes (fonctions et procédures), chacun responsable d'une tâche, au lieu d'un seul bloc de code."),
    ],
}

CH8 = {
    'slug': 'cours/tableaux',
    'short': 'Les tableaux',
    'h1': "Les tableaux à une dimension (vecteurs) avec numpy",
    'title': 'Tableaux en Python avec numpy (array) | Bac Tunisie',
    'desc': "Déclarer un tableau (TDNT), le créer avec numpy array, le remplir, l'afficher, calculer somme, moyenne, maximum. Cours du Bac Sciences en Tunisie.",
    'lead': "Un <strong>tableau</strong> (ou vecteur) est une structure qui regroupe, sous un seul nom, un nombre fixe d'éléments <strong>de même type</strong>. Chaque élément est repéré par son <strong>indice</strong>, de 0 à n − 1. Au Bac, on crée les tableaux avec la fonction <code>array</code> de la bibliothèque <strong>numpy</strong>.",
    'bref': [
        "Déclaration : un nouveau type dans le <strong>TDNT</strong>, puis la variable dans le TDO.",
        "Python : <code>from numpy import array</code> puis <code>T = array([int()] * n)</code>.",
        "<code>T[i]</code> est l'élément d'indice i ; les indices vont de 0 à n − 1.",
        "Tous les éléments ont le même type.",
    ],
    'body': [
        ('declaration', "Déclarer un tableau",
         "<p>En algorithmique, on définit d'abord un <strong>nouveau type</strong> dans le tableau de déclaration des nouveaux types (TDNT), puis on déclare la variable dans le TDO.</p>"
         + T(['Type'], [['<code>Tab = Tableau de 20 Entiers</code>']], cap="Tableau de déclaration des nouveaux types (TDNT)")
         + TDO([('T', 'Tab'), ('n', 'Entier')])
         + "<p>En Python, on crée le tableau avec <code>array</code>. L'expression <code>[int()] * n</code> fabrique une liste de n zéros, que <code>array</code> transforme en tableau :</p>"
         + T(['Tableau de…', 'Création en Python', 'Contenu initial'], [
             ['n entiers', '<code>T = array([int()] * n)</code>', 'n fois 0'],
             ['n réels', '<code>T = array([float()] * n)</code>', 'n fois 0.0'],
             ['n chaînes', '<code>T = array([str()] * n, dtype="U20")</code>', 'n chaînes vides (20 caractères max)'],
             ['n booléens', '<code>T = array([bool()] * n)</code>', 'n fois False'],
         ], cap="Créer un tableau avec numpy")
         + WARN("Sans <code>dtype</code>, <code>array([str()] * n)</code> crée des cases qui ne gardent qu'<strong>un seul caractère</strong> : la chaîne \"Tunis\" deviendrait \"T\". Précise toujours une taille, par exemple <code>dtype=\"U20\"</code>.")),
        ('acces', "Accéder aux éléments",
         T(['Indice', '0', '1', '2', '3', '4'], [['T[i]', '12', '7', '15', '9', '20']], cap="Un tableau T de 5 entiers")
         + DUO('''
            T[0] ← 12
            x ← T[2] + T[4]
            Écrire(T[n - 1])''', '''
            T[0] = 12
            x = T[2] + T[4]      # 15 + 20 = 35
            print(T[n - 1])      # dernier élément''')
         + WARN("Le dernier élément est <code>T[n - 1]</code>. Accéder à <code>T[n]</code> provoque une erreur <code>IndexError</code>.")),
        ('remplir', "Remplir un tableau",
         DUO('''
            Procédure Remplir(@T : Tab, n : Entier)
            Début
                Pour i de 0 à n - 1 Faire
                    Répéter
                        Écrire("T[", i, "] = ")
                        Lire(T[i])
                    Jusqu'à T[i] > 0
                Fin Pour
            Fin''', '''
            def remplir(T, n):
                for i in range(n):
                    T[i] = int(input("T[" + str(i) + "] = "))
                    while not (T[i] > 0):
                        T[i] = int(input("T[" + str(i) + "] = "))''', cap_p='Remplissage avec des entiers strictement positifs')),
        ('afficher', "Afficher un tableau",
         DUO('''
            Procédure Afficher(T : Tab, n : Entier)
            Début
                Pour i de 0 à n - 1 Faire
                    Écrire(T[i], " ")
                Fin Pour
            Fin''', '''
            def afficher(T, n):
                for i in range(n):
                    print(T[i], end=" ")
                print()''')
         + NOTE("<code>print(T)</code> affiche tout le tableau numpy d'un coup, au format <code>[12  7 15  9 20]</code>.")),
        ('calculs', "Les traitements classiques",
         "<p>Ces fonctions reposent toutes sur un parcours du tableau avec une boucle Pour.</p>"
         + DUO('''
            Fonction Maximum(T : Tab, n : Entier) : Entier
            Début
                max ← T[0]
                Pour i de 1 à n - 1 Faire
                    Si T[i] > max Alors
                        max ← T[i]
                    Fin Si
                Fin Pour
                Retourner max
            Fin''', '''
            def maximum(T, n):
                mx = T[0]
                for i in range(1, n):
                    if T[i] > mx:
                        mx = T[i]
                return mx''')
         + WARN("Initialise le maximum avec <code>T[0]</code>, jamais avec 0 : si toutes les valeurs sont négatives, le résultat serait faux. En Python, évite aussi de nommer une variable <code>max</code>, qui est le nom d'une fonction prédéfinie.")
         + DUO('''
            Fonction Moyenne(T : Tab, n : Entier) : Réel
            Début
                s ← 0
                Pour i de 0 à n - 1 Faire
                    s ← s + T[i]
                Fin Pour
                Retourner s / n
            Fin''', '''
            def moyenne(T, n):
                s = 0
                for i in range(n):
                    s = s + T[i]
                return s / n''')
         + DUO('''
            Fonction Occurrences(T : Tab, n, x : Entier) : Entier
            Début
                nb ← 0
                Pour i de 0 à n - 1 Faire
                    Si T[i] = x Alors
                        nb ← nb + 1
                    Fin Si
                Fin Pour
                Retourner nb
            Fin''', '''
            def occurrences(T, n, x):
                nb = 0
                for i in range(n):
                    if T[i] == x:
                        nb = nb + 1
                return nb''')),
    ],
    'retenir': [
        "Un tableau regroupe n éléments de même type, d'indices 0 à n − 1.",
        "Création : <code>from numpy import array</code> et <code>T = array([int()] * n)</code>.",
        "Maximum et minimum : initialiser avec <code>T[0]</code>.",
    ],
    'faq': [
        ("Comment créer un tableau de n entiers en Python pour le Bac ?",
         "Avec numpy : <code>from numpy import array</code>, puis <code>T = array([int()] * n)</code>. Le tableau contient n zéros."),
        ("Pourquoi utiliser numpy et non une liste Python ?",
         "Le programme tunisien utilise des tableaux de taille fixe et d'un seul type, ce qui correspond aux tableaux numpy créés avec array. Les listes Python peuvent changer de taille et mélanger les types."),
        ("Quel est l'indice du dernier élément d'un tableau de n éléments ?",
         "n − 1, car les indices commencent à 0."),
    ],
}

CH9 = {
    'slug': 'cours/algorithmes-de-tri',
    'short': 'Algorithmes de tri',
    'h1': "Les algorithmes de tri : sélection, bulles, insertion",
    'title': 'Tri par sélection, à bulles, par insertion | Bac',
    'desc': 'Les 3 tris du programme : principe, algorithme en notation officielle, code Python et déroulement pas à pas sur un exemple. Cours Bac Tunisie.',
    'lead': "<strong>Trier</strong> un tableau, c'est ranger ses éléments dans un ordre (croissant ou décroissant). Le programme étudie trois méthodes : le <strong>tri par sélection</strong> (on place le minimum au début), le <strong>tri à bulles</strong> (on échange les voisins mal rangés) et le <strong>tri par insertion</strong> (on insère chaque élément à sa place).",
    'bref': [
        "Sélection : chercher la position du minimum, puis le permuter avec le premier élément non trié.",
        "Bulles : parcourir et échanger deux voisins mal rangés, recommencer tant qu'il y a eu un échange.",
        "Insertion : prendre chaque élément et décaler les plus grands vers la droite pour l'insérer.",
        "Ordre décroissant : il suffit d'inverser la comparaison.",
    ],
    'body': [
        ('permuter', "L'outil commun : permuter deux éléments",
         DUO('''
            Procédure Permuter(@T : Tab, i, j : Entier)
            Début
                aux ← T[i]
                T[i] ← T[j]
                T[j] ← aux
            Fin''', '''
            def permuter(T, i, j):
                aux = T[i]
                T[i] = T[j]
                T[j] = aux''')),
        ('selection', "Le tri par sélection",
         "<p><strong>Principe :</strong> pour chaque position i, on cherche la position du plus petit élément de la partie non triée (de i à n − 1), puis on le permute avec <code>T[i]</code>.</p>"
         + DUO('''
            Fonction PosMin(T : Tab, d, n : Entier) : Entier
            Début
                pmin ← d
                Pour j de d + 1 à n - 1 Faire
                    Si T[j] < T[pmin] Alors
                        pmin ← j
                    Fin Si
                Fin Pour
                Retourner pmin
            Fin

            Procédure Tri_Selection(@T : Tab, n : Entier)
            Début
                Pour i de 0 à n - 2 Faire
                    p ← PosMin(T, i, n)
                    Si p ≠ i Alors
                        Permuter(T, i, p)
                    Fin Si
                Fin Pour
            Fin''', '''
            def pos_min(T, d, n):
                pmin = d
                for j in range(d + 1, n):
                    if T[j] < T[pmin]:
                        pmin = j
                return pmin

            def tri_selection(T, n):
                for i in range(n - 1):
                    p = pos_min(T, i, n)
                    if p != i:
                        permuter(T, i, p)''')
         + T(['Étape', 'Minimum trouvé', 'Tableau après l\'étape'], [
             ['Départ', '—', '[5, 2, 8, 1, 4]'],
             ['i = 0', '1 (indice 3)', '[<b>1</b>, 2, 8, 5, 4]'],
             ['i = 1', '2 (déjà en place)', '[<b>1, 2</b>, 8, 5, 4]'],
             ['i = 2', '4 (indice 4)', '[<b>1, 2, 4</b>, 5, 8]'],
             ['i = 3', '5 (déjà en place)', '[<b>1, 2, 4, 5, 8</b>]'],
         ], cap="Déroulement du tri par sélection sur [5, 2, 8, 1, 4]")),
        ('bulles', "Le tri à bulles",
         "<p><strong>Principe :</strong> on parcourt le tableau en comparant chaque élément avec son voisin de droite ; s'ils sont mal rangés, on les échange. On recommence tant qu'au moins un échange a eu lieu. À chaque passage, le plus grand élément restant « remonte » à sa place, comme une bulle.</p>"
         + DUO('''
            Procédure Tri_Bulles(@T : Tab, n : Entier)
            Début
                Répéter
                    echange ← Faux
                    Pour i de 0 à n - 2 Faire
                        Si T[i] > T[i + 1] Alors
                            Permuter(T, i, i + 1)
                            echange ← Vrai
                        Fin Si
                    Fin Pour
                Jusqu'à echange = Faux
            Fin''', '''
            def tri_bulles(T, n):
                echange = True
                while echange:
                    echange = False
                    for i in range(n - 1):
                        if T[i] > T[i + 1]:
                            permuter(T, i, i + 1)
                            echange = True''')
         + T(['Passage', 'Échanges réalisés', 'Tableau après le passage'], [
             ['Départ', '—', '[5, 2, 8, 1, 4]'],
             ['1', '5↔2, 8↔1, 8↔4', '[2, 5, 1, 4, <b>8</b>]'],
             ['2', '5↔1, 5↔4', '[2, 1, 4, <b>5, 8</b>]'],
             ['3', '2↔1', '[<b>1, 2, 4, 5, 8</b>]'],
             ['4', 'aucun → arrêt', '[1, 2, 4, 5, 8]'],
         ], cap="Déroulement du tri à bulles sur [5, 2, 8, 1, 4]")
         + NOTE("Le dernier passage, sans aucun échange, sert à constater que le tableau est trié.")),
        ('insertion', "Le tri par insertion",
         "<p><strong>Principe :</strong> comme lorsqu'on range des cartes dans sa main. Pour chaque élément à partir de l'indice 1, on le met de côté, on décale vers la droite les éléments déjà triés qui sont plus grands que lui, puis on l'insère dans la place libérée.</p>"
         + DUO('''
            Procédure Tri_Insertion(@T : Tab, n : Entier)
            Début
                Pour i de 1 à n - 1 Faire
                    v ← T[i]
                    j ← i
                    Tant que (j > 0) ET (T[j - 1] > v) Faire
                        T[j] ← T[j - 1]
                        j ← j - 1
                    Fin Tant que
                    T[j] ← v
                Fin Pour
            Fin''', '''
            def tri_insertion(T, n):
                for i in range(1, n):
                    v = T[i]
                    j = i
                    while j > 0 and T[j - 1] > v:
                        T[j] = T[j - 1]
                        j = j - 1
                    T[j] = v''')
         + T(['Étape', 'Élément inséré', 'Tableau après l\'étape'], [
             ['Départ', '—', '[5, 2, 8, 1, 4]'],
             ['i = 1', '2 (5 décalé)', '[<b>2, 5</b>, 8, 1, 4]'],
             ['i = 2', '8 (aucun décalage)', '[<b>2, 5, 8</b>, 1, 4]'],
             ['i = 3', '1 (8, 5, 2 décalés)', '[<b>1, 2, 5, 8</b>, 4]'],
             ['i = 4', '4 (8, 5 décalés)', '[<b>1, 2, 4, 5, 8</b>]'],
         ], cap="Déroulement du tri par insertion sur [5, 2, 8, 1, 4]")
         + WARN("L'ordre des conditions compte : <code>j &gt; 0</code> doit être testé <strong>avant</strong> <code>T[j - 1] &gt; v</code>. Python arrête l'évaluation de <code>and</code> dès que la première condition est fausse, ce qui évite de lire <code>T[-1]</code>.")),
        ('comparaison', "Comparer les trois méthodes",
         T(['', 'Sélection', 'Bulles', 'Insertion'], [
             ['Idée', 'Placer le minimum au début', 'Échanger les voisins mal rangés', 'Insérer chaque élément à sa place'],
             ['Outil principal', 'Recherche du minimum + permutation', 'Permutation + indicateur booléen', 'Décalage vers la droite'],
             ['Tableau déjà trié', 'Autant de comparaisons qu\'un tableau désordonné', 'Un seul passage suffit', 'Très rapide : aucun décalage'],
             ['Nombre de comparaisons (ordre de grandeur)', 'n² / 2', 'jusqu\'à n²', 'jusqu\'à n² / 2'],
         ], cap="Tri par sélection, à bulles et par insertion")
         + TIP("Pour un tri <strong>décroissant</strong>, inverse simplement la comparaison : <code>&gt;</code> au lieu de <code>&lt;</code> dans la sélection (recherche du maximum), <code>&lt;</code> au lieu de <code>&gt;</code> dans les bulles et l'insertion.")),
    ],
    'retenir': [
        "Sélection : minimum de la partie non triée → permutation avec T[i].",
        "Bulles : échange des voisins, répété jusqu'à un passage sans échange.",
        "Insertion : décalage des plus grands vers la droite, puis insertion.",
    ],
    'faq': [
        ("Quel est le principe du tri par sélection ?",
         "À chaque étape, on cherche le plus petit élément de la partie non triée du tableau et on le permute avec le premier élément de cette partie."),
        ("Pourquoi le tri à bulles s'appelle-t-il ainsi ?",
         "Parce qu'à chaque passage, le plus grand élément restant remonte jusqu'à la fin du tableau, comme une bulle qui monte à la surface."),
        ("Quel tri est le plus rapide sur un tableau presque trié ?",
         "Le tri par insertion : chaque élément n'a besoin que de très peu de décalages. Le tri à bulles avec indicateur s'arrête lui aussi rapidement."),
    ],
}

CH10 = {
    'slug': 'cours/algorithmes-de-recherche',
    'short': 'Algorithmes de recherche',
    'h1': "Les algorithmes de recherche : séquentielle et dichotomique",
    'title': 'Recherche séquentielle et dichotomique | Bac',
    'desc': 'Chercher une valeur dans un tableau : recherche séquentielle et dichotomique, avec algorithme, code Python et déroulement. Cours Bac Sciences.',
    'lead': "Rechercher, c'est déterminer si une valeur x se trouve dans un tableau. La <strong>recherche séquentielle</strong> examine les éléments un par un et fonctionne sur n'importe quel tableau. La <strong>recherche dichotomique</strong> divise l'intervalle de recherche par deux à chaque étape, mais exige un tableau <strong>trié</strong>.",
    'bref': [
        "Séquentielle : on avance tant que l'élément courant est différent de x.",
        "Dichotomique : on compare x à l'élément du milieu et on garde la bonne moitié.",
        "Sur 1 000 éléments : jusqu'à 1 000 comparaisons en séquentielle, une dizaine en dichotomique.",
        "La dichotomie ne marche que sur un tableau trié.",
    ],
    'body': [
        ('sequentielle', "La recherche séquentielle",
         DUO('''
            Fonction Recherche(T : Tab, n, x : Entier) : Booléen
            Début
                i ← 0
                Tant que (i < n) ET (T[i] ≠ x) Faire
                    i ← i + 1
                Fin Tant que
                Retourner i < n
            Fin''', '''
            def recherche(T, n, x):
                i = 0
                while i < n and T[i] != x:
                    i = i + 1
                return i < n''')
         + "<p>La boucle s'arrête soit parce que x a été trouvé (<code>T[i] = x</code>), soit parce qu'on a dépassé la fin du tableau (<code>i = n</code>). Le test final <code>i &lt; n</code> distingue les deux cas.</p>"
         + NOTE("Pour renvoyer la <strong>position</strong> de x au lieu d'un booléen, on retourne <code>i</code> si <code>i &lt; n</code>, et -1 sinon.")),
        ('dichotomique', "La recherche dichotomique",
         "<p><strong>Principe :</strong> dans un tableau trié, on compare x à l'élément du milieu. S'il est égal, c'est trouvé. Si x est plus petit, on continue dans la moitié gauche ; sinon dans la moitié droite. On s'arrête quand x est trouvé ou quand l'intervalle est vide.</p>"
         + DUO('''
            Fonction Dichotomie(T : Tab, n, x : Entier) : Booléen
            Début
                deb ← 0
                fin ← n - 1
                trouve ← Faux
                Tant que (deb ≤ fin) ET (trouve = Faux) Faire
                    mil ← (deb + fin) DIV 2
                    Si T[mil] = x Alors
                        trouve ← Vrai
                    Sinon Si x < T[mil] Alors
                        fin ← mil - 1
                    Sinon
                        deb ← mil + 1
                    Fin Si
                Fin Tant que
                Retourner trouve
            Fin''', '''
            def dichotomie(T, n, x):
                deb = 0
                fin = n - 1
                trouve = False
                while deb <= fin and not trouve:
                    mil = (deb + fin) // 2
                    if T[mil] == x:
                        trouve = True
                    elif x < T[mil]:
                        fin = mil - 1
                    else:
                        deb = mil + 1
                return trouve''')
         + T(['Étape', 'deb', 'fin', 'mil', 'T[mil]', 'Décision'], [
             ['1', '0', '9', '4', '16', '23 > 16 → moitié droite'],
             ['2', '5', '9', '7', '56', '23 < 56 → moitié gauche'],
             ['3', '5', '6', '5', '23', 'trouvé'],
         ], cap="Recherche de 23 dans [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]")),
        ('comparaison', "Comparer les deux méthodes",
         T(['', 'Séquentielle', 'Dichotomique'], [
             ['Condition', 'Aucune', 'Tableau trié'],
             ['Principe', 'Examiner les éléments un par un', 'Diviser l\'intervalle par deux'],
             ['Comparaisons au pire (n = 1 000)', '1 000', '10'],
             ['Comparaisons au pire (n = 1 000 000)', '1 000 000', '20'],
         ], cap="Recherche séquentielle et dichotomique")
         + TIP("Si un sujet te demande de chercher plusieurs fois dans un même grand tableau, trier une fois puis utiliser la dichotomie est bien plus efficace.")),
        ('chaine', "Rechercher dans une chaîne",
         "<p>Pour savoir si une chaîne en contient une autre, Python propose <code>ch2.find(ch1)</code> (l'équivalent de <code>Pos(ch1, ch2)</code>), qui renvoie la position ou -1, et l'opérateur <code>in</code> qui renvoie un booléen.</p>"
         + P('''
            ch = "baccalauréat"
            print(ch.find("lau"))   # 5
            print("bac" in ch)      # True''')),
    ],
    'retenir': [
        "Séquentielle : tant que <code>i &lt; n</code> et <code>T[i] != x</code>, avancer.",
        "Dichotomique : milieu <code>(deb + fin) // 2</code>, garder la bonne moitié ; tableau trié obligatoire.",
        "La dichotomie divise le nombre de comparaisons de façon spectaculaire.",
    ],
    'faq': [
        ("Quelle est la condition pour utiliser la recherche dichotomique ?",
         "Le tableau doit être trié. Sinon, comparer x à l'élément du milieu ne permet pas de savoir dans quelle moitié il se trouve."),
        ("Comment calculer le milieu en Python ?",
         "Avec la division entière : <code>mil = (deb + fin) // 2</code>, qui correspond à <code>(deb + fin) DIV 2</code>."),
        ("Que renvoie la recherche séquentielle si la valeur est absente ?",
         "Dans la version booléenne, elle renvoie False (la boucle s'arrête avec i = n). Dans la version qui renvoie une position, on renvoie conventionnellement -1."),
    ],
}

CH11 = {
    'slug': 'cours/interfaces-graphiques-pyqt5',
    'short': 'Interfaces graphiques PyQt5',
    'h1': "Les interfaces graphiques avec Qt Designer et PyQt5",
    'title': 'Interface graphique PyQt5 et Qt Designer | Bac',
    'desc': "Qt Designer, QLabel, QLineEdit, QPushButton, loadUi, text(), setText() et module Play : tout pour l'interface du Bac pratique en Tunisie.",
    'lead': "Au Bac pratique, le programme Python est piloté par une <strong>interface graphique</strong> : une fenêtre dessinée avec <strong>Qt Designer</strong>, enregistrée dans un fichier <code>.ui</code>, puis chargée en Python avec <strong>PyQt5</strong>. Un clic sur un bouton lance le <strong>module Play</strong>, qui lit les saisies, les vérifie, calcule et affiche le résultat.",
    'bref': [
        "3 composants essentiels : QLabel (texte), QLineEdit (saisie), QPushButton (bouton).",
        "Chaque composant a un <strong>objectName</strong> : c'est le nom utilisé dans le code.",
        "Lire : <code>windows.nom.text()</code> ; écrire : <code>windows.nom.setText(texte)</code>.",
        "Relier : <code>windows.bouton.clicked.connect(Play)</code>, sans parenthèses après Play.",
    ],
    'body': [
        ('ihm', "Qu'est-ce qu'une interface graphique ?",
         DEF('Interface graphique (IHM)', "fenêtre qui permet à l'utilisateur d'interagir avec le programme à l'aide de zones de saisie, de boutons et de zones d'affichage, au lieu de la console.")
         + T(['Composant (widget)', 'Rôle', 'Méthodes utiles'], [
             ['<code>QLabel</code>', 'Afficher un texte fixe ou un résultat', '<code>setText(ch)</code>, <code>text()</code>, <code>clear()</code>'],
             ['<code>QLineEdit</code>', 'Saisir une valeur sur une ligne', '<code>text()</code>, <code>setText(ch)</code>, <code>clear()</code>'],
             ['<code>QPushButton</code>', 'Déclencher un traitement par un clic', '<code>clicked.connect(module)</code>'],
         ], cap="Les composants utilisés au Bac")),
        ('qt-designer', "Créer l'interface dans Qt Designer",
         OL(["Ouvre Qt Designer et choisis un modèle de fenêtre (<em>Main Window</em> ou <em>Widget</em>).",
             "Glisse depuis la boîte de widgets les <strong>labels</strong>, la ou les <strong>zones de saisie</strong> et le <strong>bouton</strong> demandés.",
             "Modifie le texte affiché (double-clic) : par exemple « N = » ou « Vérifier ».",
             "Dans l'éditeur de propriétés, donne à chaque composant un <strong>objectName</strong> court et clair : <code>N</code>, <code>Verifier</code>, <code>Resultat</code>.",
             "Enregistre le fichier avec le nom demandé (par exemple <code>Interface.ui</code>) <strong>dans ton dossier de travail</strong>."])
         + WARN("Le nom utilisé dans le code (<code>windows.Resultat</code>) doit être <strong>exactement</strong> l'objectName choisi dans Qt Designer, majuscules comprises. Sinon Python affiche une erreur <code>AttributeError</code>.")),
        ('code-base', "Le code de base (l'annexe du sujet)",
         "<p>Chaque sujet de Bac pratique fournit ce squelette en annexe. Tu dois y ajouter tes sous-programmes et ton module Play, puis remplacer les noms génériques par les tiens.</p>"
         + P('''
            from PyQt5.uic import loadUi
            from PyQt5.QtWidgets import QApplication

            # ... tes fonctions et le module Play ...

            app = QApplication([])
            windows = loadUi("Interface.ui")
            windows.show()
            windows.Verifier.clicked.connect(Play)
            app.exec_()''', "Squelette d'une application PyQt5")
         + T(['Ligne', 'Rôle'], [
             ['<code>from PyQt5.uic import loadUi</code>', 'Importer l\'outil qui charge un fichier .ui'],
             ['<code>from PyQt5.QtWidgets import QApplication</code>', 'Importer la classe de l\'application'],
             ['<code>app = QApplication([])</code>', 'Créer l\'application'],
             ['<code>windows = loadUi("Interface.ui")</code>', 'Charger la fenêtre dessinée dans Qt Designer'],
             ['<code>windows.show()</code>', 'Afficher la fenêtre'],
             ['<code>windows.Verifier.clicked.connect(Play)</code>', 'Lancer Play à chaque clic sur le bouton Verifier'],
             ['<code>app.exec_()</code>', 'Démarrer la boucle d\'attente des événements'],
         ], cap="Que fait chaque ligne ?")
         + WARN("On écrit <code>connect(Play)</code> et <strong>pas</strong> <code>connect(Play())</code>. Avec les parenthèses, Play serait exécuté immédiatement au démarrage, avant tout clic.")),
        ('lire-ecrire', "Lire une saisie et afficher un résultat",
         T(['Action', 'Code', 'Remarque'], [
             ['Lire le texte saisi', '<code>ch = windows.N.text()</code>', 'Renvoie toujours une chaîne'],
             ['Lire un entier', '<code>n = int(windows.N.text())</code>', 'Erreur si la saisie est vide ou non numérique'],
             ['Afficher un texte', '<code>windows.Resultat.setText("Bravo")</code>', 'setText attend une chaîne'],
             ['Afficher un nombre', '<code>windows.Resultat.setText(str(n))</code>', 'Convertir avec str()'],
             ['Vider un composant', '<code>windows.N.clear()</code>', ''],
         ], cap="Lire et écrire dans l'interface")),
        ('module-play', "Le module Play : lire, vérifier, traiter, afficher",
         "<p>Le module Play suit toujours le même plan en quatre temps. La <strong>vérification</strong> se fait sur la chaîne, <strong>avant</strong> toute conversion avec <code>int()</code>.</p>"
         + P('''
            def premier(n):
                if n < 2:
                    return False
                d = 2
                while d <= n // 2 and n % d != 0:
                    d = d + 1
                return d > n // 2

            def Play():
                ch = windows.N.text()                          # 1. lire
                if not ch.isdigit() or not (2 <= int(ch) <= 1000):
                    windows.Resultat.setText("Veuillez saisir un entier entre 2 et 1000")   # 2. vérifier
                else:
                    n = int(ch)
                    if premier(n):                             # 3. traiter
                        windows.Resultat.setText(ch + " est premier")                       # 4. afficher
                    else:
                        windows.Resultat.setText(ch + " n'est pas premier")''', 'Exemple de module Play complet')
         + TIP("Recopie exactement le format des messages donnés dans les exemples du sujet (espaces, majuscules, ponctuation) : c'est ce que le correcteur compare.")),
        ('plusieurs', "Afficher plusieurs résultats",
         "<p>Quand il faut afficher une liste de valeurs dans un seul label (par exemple « Les nombres ronds sont : 35-37-38 »), on construit une chaîne au fur et à mesure :</p>"
         + P('''
            res = ""
            for x in range(a, b + 1):
                if condition(x):
                    res = res + str(x) + "-"
            if res == "":
                windows.Resultat.setText("Aucun nombre trouvé")
            else:
                windows.Resultat.setText("Les nombres sont : " + res[:-1])   # retire le dernier tiret''')),
        ('erreurs', "Les erreurs les plus fréquentes",
         T(['Message ou symptôme', 'Cause', 'Solution'], [
             ['<code>AttributeError: … has no attribute …</code>', 'objectName différent entre Qt Designer et le code', 'Vérifier l\'orthographe exacte dans l\'éditeur de propriétés'],
             ['<code>FileNotFoundError</code> sur le fichier .ui', 'Le .ui n\'est pas dans le même dossier que le .py', 'Enregistrer les deux fichiers dans le dossier de travail'],
             ['<code>ValueError: invalid literal for int()</code>', 'Saisie vide ou non numérique convertie avec int()', 'Vérifier avec <code>isdigit()</code> avant de convertir'],
             ['<code>TypeError</code> sur setText', 'Un nombre est passé à setText', 'Convertir avec <code>str()</code>'],
             ['Le programme réagit au démarrage, pas au clic', '<code>connect(Play())</code> avec parenthèses', 'Écrire <code>connect(Play)</code>'],
             ['Rien ne se passe au clic', 'Mauvais nom de bouton dans connect', 'Utiliser l\'objectName du bouton'],
         ], cap="Diagnostiquer une interface qui ne marche pas")),
    ],
    'retenir': [
        "Qt Designer → fichier .ui ; PyQt5 → <code>loadUi</code> le charge.",
        "<code>text()</code> lit (une chaîne), <code>setText()</code> écrit (une chaîne).",
        "Play : lire → vérifier → traiter → afficher ; <code>connect(Play)</code> sans parenthèses.",
    ],
    'faq': [
        ("Comment récupérer la valeur saisie dans un QLineEdit ?",
         "Avec la méthode <code>text()</code> : <code>ch = windows.N.text()</code>, où N est l'objectName de la zone de saisie. Le résultat est une chaîne."),
        ("Comment afficher un nombre dans un QLabel ?",
         "<code>setText</code> attend une chaîne : on convertit le nombre avec <code>str()</code>, par exemple <code>windows.Resultat.setText(str(s))</code>."),
        ("Où enregistrer le fichier .ui au Bac pratique ?",
         "Dans le dossier de travail portant ton numéro d'inscription, à côté du fichier .py. loadUi cherche le fichier dans le dossier courant, qui est celui du programme quand tu l'exécutes depuis Thonny."),
    ],
}

CHAPTERS_B = [CH7, CH8, CH9, CH10, CH11]
