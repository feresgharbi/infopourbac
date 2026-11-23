from h import P, A, DUO, T, TDO, NOTE, WARN, TIP, DEF, UL, OL, c

ALGOS = {
    'slug': 'algorithmes-classiques',
    'short': 'Algorithmes classiques',
    'h1': "Les algorithmes classiques du Bac informatique",
    'title': 'Algorithmes du Bac : premier, PGCD, palindrome',
    'desc': 'Les fonctions qui reviennent au Bac pratique : premier, diviseurs, parfait, PGCD, somme des chiffres, palindrome, binaire, factorielle. Algorithme + Python.',
    'lead': "Les sujets du Bac pratique changent chaque année, mais ils s'appuient presque toujours sur les mêmes briques : tester si un nombre est <strong>premier</strong>, calculer un <strong>PGCD</strong>, parcourir les <strong>chiffres</strong> d'un nombre, vérifier un <strong>palindrome</strong>, convertir en <strong>binaire</strong>. Voici ces algorithmes de référence, en notation officielle et en Python.",
    'bref': [
        "Premier : aucun diviseur entre 2 et n DIV 2.",
        "Chiffres d'un nombre : <code>n % 10</code> puis <code>n // 10</code>.",
        "PGCD : algorithme d'Euclide avec le reste <code>a % b</code>.",
        "Binaire : restes successifs de la division par 2, lus à l'envers.",
    ],
    'body': [
        ('premier', "Tester si un nombre est premier",
         "<p>Un entier n ≥ 2 est <strong>premier</strong> s'il n'est divisible que par 1 et par lui-même. On cherche un diviseur d entre 2 et n DIV 2 ; si on n'en trouve aucun, n est premier.</p>"
         + DUO('''
            Fonction Premier(n : Entier) : Booléen
            Début
                Si n < 2 Alors
                    Retourner Faux
                Fin Si
                d ← 2
                Tant que (d ≤ n DIV 2) ET (n MOD d ≠ 0) Faire
                    d ← d + 1
                Fin Tant que
                Retourner d > n DIV 2
            Fin''', '''
            def premier(n):
                if n < 2:
                    return False
                d = 2
                while d <= n // 2 and n % d != 0:
                    d = d + 1
                return d > n // 2''')),
        ('parfait', "Somme des diviseurs et nombre parfait",
         "<p>Un nombre est <strong>parfait</strong> s'il est égal à la somme de ses diviseurs autres que lui-même : 6 = 1 + 2 + 3 et 28 = 1 + 2 + 4 + 7 + 14.</p>"
         + DUO('''
            Fonction SommeDiv(n : Entier) : Entier
            Début
                s ← 0
                Pour d de 1 à n DIV 2 Faire
                    Si n MOD d = 0 Alors
                        s ← s + d
                    Fin Si
                Fin Pour
                Retourner s
            Fin

            Fonction Parfait(n : Entier) : Booléen
            Début
                Retourner SommeDiv(n) = n
            Fin''', '''
            def somme_div(n):
                s = 0
                for d in range(1, n // 2 + 1):
                    if n % d == 0:
                        s = s + d
                return s

            def parfait(n):
                return somme_div(n) == n''')),
        ('pgcd', "PGCD par l'algorithme d'Euclide",
         "<p>Le PGCD de a et b est le plus grand entier qui divise les deux. Euclide remplace (a, b) par (b, a MOD b) jusqu'à ce que b soit nul. Deux nombres sont <strong>premiers entre eux</strong> si leur PGCD vaut 1.</p>"
         + DUO('''
            Fonction PGCD(a, b : Entier) : Entier
            Début
                Tant que b ≠ 0 Faire
                    r ← a MOD b
                    a ← b
                    b ← r
                Fin Tant que
                Retourner a
            Fin''', '''
            def pgcd(a, b):
                while b != 0:
                    r = a % b
                    a = b
                    b = r
                return a''')
         + T(['a', 'b', 'r = a MOD b'], [['48', '18', '12'], ['18', '12', '6'], ['12', '6', '0'], ['6', '0', '— → PGCD = 6']], cap="Déroulement pour PGCD(48, 18)")),
        ('somme-chiffres', "Somme des chiffres d'un nombre",
         DUO('''
            Fonction SommeChiffres(n : Entier) : Entier
            Début
                s ← 0
                Tant que n ≠ 0 Faire
                    s ← s + n MOD 10
                    n ← n DIV 10
                Fin Tant que
                Retourner s
            Fin''', '''
            def somme_chiffres(n):
                s = 0
                while n != 0:
                    s = s + n % 10
                    n = n // 10
                return s''')),
        ('inverse', "Inverse d'un nombre et palindrome numérique",
         "<p>L'inverse de 1234 est 4321. Un nombre est palindrome s'il est égal à son inverse (121, 4554).</p>"
         + DUO('''
            Fonction Inverse(n : Entier) : Entier
            Début
                inv ← 0
                Tant que n ≠ 0 Faire
                    inv ← inv * 10 + n MOD 10
                    n ← n DIV 10
                Fin Tant que
                Retourner inv
            Fin''', '''
            def inverse(n):
                inv = 0
                while n != 0:
                    inv = inv * 10 + n % 10
                    n = n // 10
                return inv

            def palindrome_nombre(n):
                return inverse(n) == n''')),
        ('palindrome', "Palindrome sur une chaîne",
         "<p>On compare les caractères des deux extrémités en avançant vers le milieu. C'est l'algorithme donné dans le sujet du Bac pratique 2025.</p>"
         + DUO('''
            Fonction Palindrome(CH : Chaîne) : Booléen
            Début
                i ← 0
                j ← Long(CH) - 1
                Tant que (i < j) ET (CH[i] = CH[j]) Faire
                    i ← i + 1
                    j ← j - 1
                Fin Tant que
                Retourner i ≥ j
            Fin''', '''
            def palindrome(ch):
                i = 0
                j = len(ch) - 1
                while i < j and ch[i] == ch[j]:
                    i = i + 1
                    j = j - 1
                return i >= j''')
         + TIP("Pour tester un nombre, il suffit de le convertir : <code>palindrome(str(n))</code>.")),
        ('binaire', "Conversions décimal ↔ binaire",
         "<p>Pour écrire n en base 2, on divise n par 2 et on garde les restes, que l'on place à <strong>gauche</strong> du résultat. Exemple : 13 → 1101.</p>"
         + DUO('''
            Fonction Binaire(n : Entier) : Chaîne
            Début
                ch ← ""
                Répéter
                    ch ← Convch(n MOD 2) + ch
                    n ← n DIV 2
                Jusqu'à n = 0
                Retourner ch
            Fin''', '''
            def binaire(n):
                ch = ""
                while True:
                    ch = str(n % 2) + ch
                    n = n // 2
                    if n == 0:
                        break
                return ch''')
         + DUO('''
            Fonction Decimal(ch : Chaîne) : Entier
            Début
                d ← 0
                Pour i de 0 à Long(ch) - 1 Faire
                    d ← d * 2 + Valeur(ch[i])
                Fin Pour
                Retourner d
            Fin''', '''
            def decimal(ch):
                d = 0
                for i in range(len(ch)):
                    d = d * 2 + int(ch[i])
                return d''', cap_a='Binaire → décimal', cap_p='Binaire → décimal en Python')
         + NOTE("Avec la boucle Répéter, la conversion de 0 donne bien \"0\". Python propose aussi <code>bin(13)</code>, qui renvoie <code>'0b1101'</code>, mais au Bac on attend en général l'algorithme.")),
        ('factorielle', "Factorielle",
         "<p>n! = 1 × 2 × … × n, avec 0! = 1. C'est un accumulateur de produit : il commence à 1.</p>"
         + DUO('''
            Fonction Fact(n : Entier) : Entier
            Début
                f ← 1
                Pour i de 2 à n Faire
                    f ← f * i
                Fin Pour
                Retourner f
            Fin''', '''
            def fact(n):
                f = 1
                for i in range(2, n + 1):
                    f = f * i
                return f''')),
    ],
    'retenir': [
        "Ces fonctions se combinent : « premier palindrome » = <code>premier(n) and palindrome(str(n))</code>.",
        "Chiffres d'un nombre : <code>% 10</code> et <code>// 10</code> ; ou conversion en chaîne avec <code>str()</code>.",
        "Écris chaque brique dans sa propre fonction : c'est la solution modulaire attendue.",
    ],
    'faq': [
        ("Comment tester si un nombre est premier en Python ?",
         "On cherche un diviseur d entre 2 et n // 2. Si aucun d ne vérifie n % d == 0 (et si n ≥ 2), le nombre est premier."),
        ("Comment convertir un nombre en binaire sans bin() ?",
         "On divise successivement par 2 et on ajoute chaque reste à gauche d'une chaîne : <code>ch = str(n % 2) + ch</code>, puis <code>n = n // 2</code>, jusqu'à n = 0."),
        ("Comment calculer le PGCD de deux nombres en Python ?",
         "Avec l'algorithme d'Euclide : tant que b est non nul, on remplace (a, b) par (b, a % b) ; le PGCD est la dernière valeur de a."),
    ],
}

GLOSSAIRE = [
    ("Accumulateur", "Variable qui cumule des valeurs au fil d'une boucle (somme, produit). Une somme commence à 0, un produit à 1."),
    ("Affectation", "Action qui range une valeur dans une variable : x ← 5 en algorithme, x = 5 en Python."),
    ("Algorithme", "Suite finie et ordonnée d'instructions permettant de résoudre un problème."),
    ("array", "Fonction de la bibliothèque numpy qui crée un tableau : T = array([int()] * n)."),
    ("Booléen", "Type qui ne prend que deux valeurs : Vrai/Faux (True/False en Python)."),
    ("Boucle infinie", "Boucle dont la condition ne devient jamais fausse : le programme ne s'arrête pas."),
    ("Chaîne de caractères", "Suite de caractères entre guillemets, de type str en Python."),
    ("Compteur", "Variable qui compte le nombre de fois qu'un événement se produit : nb ← nb + 1."),
    ("Concaténation", "Mise bout à bout de deux chaînes avec l'opérateur +."),
    ("Constante", "Objet dont la valeur ne change pas pendant l'exécution."),
    ("DIV", "Opérateur du quotient de la division entière ; // en Python."),
    ("Dichotomie", "Méthode de recherche dans un tableau trié qui divise l'intervalle de recherche par deux à chaque étape."),
    ("Fonction", "Sous-programme qui renvoie un résultat avec Retourner (return)."),
    ("Indentation", "Décalage du code vers la droite (4 espaces) qui délimite les blocs en Python."),
    ("Indice", "Position d'un élément dans un tableau ou une chaîne ; il commence à 0."),
    ("loadUi", "Fonction de PyQt5 qui charge une interface dessinée dans Qt Designer (fichier .ui)."),
    ("MOD", "Opérateur du reste de la division entière ; % en Python."),
    ("Module Play", "Au Bac pratique, la fonction exécutée au clic sur le bouton de l'interface."),
    ("numpy", "Bibliothèque Python utilisée au Bac pour créer des tableaux avec array."),
    ("objectName", "Nom donné à un composant dans Qt Designer ; c'est le nom utilisé dans le code Python."),
    ("Paramètre effectif", "Valeur ou variable transmise à un sous-programme au moment de l'appel."),
    ("Paramètre formel", "Nom utilisé dans l'en-tête d'un sous-programme pour désigner une donnée reçue."),
    ("Passage par référence", "Mode de passage (noté @) qui permet au sous-programme de modifier la variable de l'appelant."),
    ("Passage par valeur", "Mode de passage où le sous-programme travaille sur une copie de la donnée."),
    ("Permutation", "Échange du contenu de deux variables, à l'aide d'une variable auxiliaire."),
    ("Procédure", "Sous-programme qui réalise une action sans renvoyer de résultat."),
    ("PyQt5", "Bibliothèque Python qui permet de créer et de piloter des interfaces graphiques Qt."),
    ("Qt Designer", "Logiciel qui permet de dessiner une interface graphique à la souris et de l'enregistrer en fichier .ui."),
    ("range", "Fonction Python qui génère une suite d'entiers pour une boucle for ; la borne de fin est exclue."),
    ("Solution modulaire", "Programme découpé en sous-programmes, chacun chargé d'une tâche précise. Exigée au Bac pratique."),
    ("Sous-programme", "Bloc d'instructions nommé que l'on peut appeler plusieurs fois : fonction ou procédure."),
    ("Structure conditionnelle", "Structure qui exécute des instructions selon qu'une condition est vraie ou fausse (Si, Selon)."),
    ("Structure itérative", "Structure qui répète des instructions (Pour, Tant que, Répéter)."),
    ("Tableau", "Structure qui regroupe un nombre fixe d'éléments de même type, repérés par un indice."),
    ("TDNT", "Tableau de déclaration des nouveaux types, où l'on définit par exemple un type tableau."),
    ("TDO", "Tableau de déclaration des objets : la liste des variables et constantes d'un algorithme avec leur type."),
    ("TDOL", "Tableau de déclaration des objets locaux d'un sous-programme."),
    ("Tri", "Opération qui range les éléments d'un tableau dans un ordre croissant ou décroissant."),
    ("Variable", "Nom désignant une case mémoire dont la valeur peut changer pendant l'exécution."),
]
