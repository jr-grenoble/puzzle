#!/usr/bin/python
# -*- coding:UTF-8 -*-
#
# Copyright (c) Jean-René Bouvier
#

# Tout ceci est du vieux python de base…
# Après la définition de quelques fonctions utilitaires,
# le programme cherche la solution d'une énigme en réduisant les possibilités de réponses.
# Pour cela, il utilise des listes de réponses "candidates",
# et il filtre ces listes en fonction des indices de l'énigme.

# Pour transformer ce programme en executable, le sauver dans un dossier,
# par exemple sous le nom "enigme.py".
# Puis, dans le terminal, aller dans le dossier en question et faire:
# » chmod +x enigme.py # » est le prompt Unix/Mac/Linux
# On peut alors lancer le programme sous la forme:
# » ./enigme.py
# Pour Windows, tourner dans l'interpréteur Pyton.
# Dans Atom, utiliser l'environement fantastique Hydrogen:
# https://atom.io/packages/hydrogen
# Atom et Hydrogen fonctionnent sous Linux,Unix (donc Mac) et Windows.


# ==| Fonctions utilitaires |==
def printl ( list ) :
    # Affiche une liste de façon propre
    items_per_line = 6 # on peut changer cette valeur en fonction de la taille de l'écran
    index = 0
    for item in list :
        if index % items_per_line == 0 :
            print "\n",
        index = index + 1
        print "\t", item,
    print "\n"

def assess ( list ) :
    # Détermine si on a trouvé la solution en fonction de la taille de la liste
    # Retourne True si on trouvé (liste réduite à un seul candidat)
    # Retourne False si la liste contient plusieurs candidats
    # Avorte le programme si la liste est vide: il n'y a donc pas de solution
    printl ( list )
    l = len ( list )
    if l > 1 :
        print """
        ...pour l'instant, la liste des candidats contient trop de candidats,
        il faut donc continuer à chercher.
        """
        return False
    elif l == 0 :
        print """
        ...la liste des candidats est vide,
        il n'y a donc pas de solution, l'enigme est insoluble sans alcool.
        """
        quit ()
    else :
        print """
        ...la liste des candidats ne contient plus qu'un élément, c'est donc la solution.
        """
        return True

def prod ( list ) :
    # Equivalent de la fonction sum, mais calcule le produit des éléments d'une liste
    p = 1
    for item in list :
        p = p * item
    return p

def prompt () :
    # Attend que l'utilisateur presse return
    answer = raw_input ( "\n↩ " )
    if answer in [ "q", "quit", "Q", "Quit", "QUIT", "s", "stop", "S", "Stop", "STOP" ] : quit ()

# ==| Enigme |==
enigme = """
    Lors d'une promenade, un homme rencontre une amie de l'université.
    Il discutent de la vie et de leurs études.
    L'homme observe 3 garçons qui jouent dans le jardin de la maison de son amie.
    H: Ils sont à toi ?
    F: Oui
    H: Je n'ai pas une très bonne vue, ils vont déjà à l'école primaire ?
    F: Non, ils ne sont pas assez âgés, il faut avoir plus de 6 ans pour cela.
    H: Quel est leur âge (*)?
    F: Je me souviens que tu aimes les énigmes, en voici une:
       la somme de leurs âges divise parfaitement le produit de leurs âges
       et le résultat de cette division est égal au plus grand de leurs âges.
    H: Je ne peux pas savoir. Mais as-tu des filles ?
    F: Oui, 3.
    H: Quel est leur âge?
    F: Le produit de l'âge de mes filles est le carré parfait qui suit le carré de l'âge de l'ainé des garçons.
    H: Ah! Maintenant je connais l'âge de tes garçons, mais je ne peux pas savoir celui de tes filles.
    F: Regarde le numéro de ma maison sur la boite aux lettres.
       La somme des âges de mes filles est égal à ce numéro.
    H: Hélas, je ne peux toujours pas déterminer leur âge.
    F: C'est normal, mais je peux te dire que la plus jeune a des yeux verts.
    H: Facile, je connais maintenant l'âge de tes filles.

    Quels sont les âges des garçons et des filles de l'amie de cet homme ?
    Quel est âge de la fille aux yeux verts ?

    (*) l'âge est un élément de ℕ
    (ce serait difficile de faire autrement, au moment où l'on indiquerait l'âge, ce serait déjà faux)
    """

print "ENIGME"
print enigme

# ==| Solution |==
print "OK, essayons de trouver!\n"
prompt ()

def boys () :
    # Cette fonction gère pas à pas la recherche de l'âge des garçons
    print "Comme la somme des âges divisé par leur produit est le plus grand des âges, aucun âge ne peut être nul."
    print "Sinon, le produit serait nul, et donc tous les âges seraient nuls. Mais  c'est impossible car 0 ne divise pas 0."
    print "On sait aussi que les garçons ont au plus 6 ans puisqu'ils ne vont pas à l'école primaire."
    mini = 1
    maxi = 7
    print "L'âge minimum est donc", mini, "et cet âge est strictement inférieur à", maxi
    print
    print "Commençons par chercher tous les triplets d'âges inférieurs à", maxi, "et au moins égaux à", mini, "."
    print "Voici la liste ordonnée correpondant à l'ensemble { (i,j,k) ∈ ⟦ 1 .. 6 ⟧³, i ≤ j ≤ k }:"

    # utilisation de la déclaration de liste en compréhension
    boys = [
        [ i, j, k ]
        for i in range ( mini, maxi )
        for j in range ( i, maxi )
        for k in range ( j, maxi )
        ]

    if assess ( boys ) : return boys [ 0 ]

    prompt ()
    print """
    Maintenant, on ne veut garder que les âges dont la somme divise le produit,
    et qui plus est, pour lesquels cette division est égale au(x) plus grand(s) des âges.
    L'ensemble devient ainsi { (i,j,k) ∈ ⟦ 1 .. 6 ⟧³, i ≤ j ≤ k, i+j+k | i.j.k, i.j.k ÷ (i+j+k) = k }
    Voici la liste:
    """
    boys = [
        ages
        for ages in boys
        if prod ( ages ) % sum ( ages ) == 0 \
        and prod ( ages ) / sum ( ages ) == max ( ages )
        ]

    if assess ( boys ) : return boys [ 0 ]

    prompt ()
    print """
    Mais on sait qu'il y a un aîné, il faut donc eliminer les âges candidats où il y a plusieurs ainés.
    L'ensemble devient ainsi { (i,j,k) ∈ ⟦ 1 .. 6 ⟧³, i ≤ j < k, i+j+k | ijk, ijk ÷ (i+j+k) = k }
    (la différence avec l'ensemble précédent est l'inégalité stricte entre j et k;
    on aurait pu utiliser ce critère dès le début, mais cela n'aurait pas respecté
    temporellement la logique appliquée par l'ami de la mère des enfants)
    Voici la liste:
    """

    # note: la méthode count retourne le nombre de fois qu'un élément apparaît dans une liste
    boys = [ ages for ages in boys if ages.count ( max ( ages ) ) == 1 ]

    if assess ( boys ) : return boys [ 0 ]

    # si on arrive ici, on n'a pas de solution possible
    print "Je ne sais pas comment trouver l'âge des garçons!"
    quit ()

def girls ( oldest ) :
    # Cette fonction gère pas à pas la recherche de l'âge des filles
    product = ( oldest + 1 ) ** 2
    print "L'âge de l'ainé des garçons est", oldest, \
        "donc le produit de l'âge des filles est le carré de", \
        oldest, "+ 1, soit", product, "\n"
    mini = 1
    print "Ce produit est non nul, donc l'âge des filles est au moins égal à", mini
    maxi = product + 1
    print "De ce fait, l'âge des filles ne peut excéder", maxi, "car sinon leur produit dépasserait", product
    print "Cherchons donc les triplets d'âges <", maxi, "et >=", mini, "et dont le produit est égal à", product
    print """
    Ceci équivaut à G = { (i,j,k) ∈ ⟦ 1 .. (a+1)² ⟧³, i ≤ j ≤ k, ijk = (a+1)² } si a est l'âge de l'ainé des garçons.
    Voici la liste des éléments de G:
    """

    girls = [
        [ i, j, k ]
        for i in range ( mini, maxi )
        for j in range ( i, maxi )
        for k in range ( j, maxi )
        if i * j * k == product
        ]

    if assess ( girls ) : return girls [ 0 ]

    prompt ()
    print """
    On a beaucoup de candidats, mais l'indication du numéro de la boite au lettre va nous servir;
    calculons les sommes des âges des triplets candidats, c'est un sac (multiensemble) qui correspond
    à S = {{ i+j+k | (i,j,k) ∈ G }} :
    """

    sums = [ sum ( ages ) for ages in girls ]
    printl ( sums )

    prompt ()
    print """
    Et comme le fait de connaître cette somme ne suffit pas à déterminer l'âge des filles,
    il faut que l'on cherche les doublons (ou plus) dans cette liste de sommes, soit le sac (multiensemble)
    D = {{ d ∈ S | m(d) > 1 }} si m dénote la multiplicité:
    """
    # on pourrait être plus efficace, en démontrant que sums est une liste ordonnée décroissante par construction
    duplicates = [ d for d in sums if sums.count ( d ) > 1 ]
    printl ( duplicates )

    if len ( duplicates ) == 0 :
        print "Il n'y a pas de doublon donc pas de solution avec les informations disponibles :("
        quit ();

    prompt ()
    print """
    Voici la liste des âges correspondant à ces doublons, soit { (i,j,k) ∈ G | i+j+k ∈ D }:
    """
    girls = [ ages for ages in girls if sum ( ages ) in duplicates ]
    if assess ( girls ) : return girls [ 0 ]

    prompt ()
    print """
    On sait qu'il y a une seule fille qui est la plus jeune.
    Dans la liste des candidats, ceux qui ont un seul benjamin
    correspondent à l'ensemble { (i,j,k) ∈ G | i+j+k ∈ D, i < j }
    (là aussi on aurait pu utiliser ce critère i < j dès le début,
    mais cela n'aurait pas non plus respecté temporellement la logique
    de l'ami de la mère des enfants):
    """
    girls = [ ages for ages in girls if ages.count ( min ( ages ) ) == 1 ]
    if assess ( girls ) : return girls [ 0 ]

    print "Je ne sais pas comment déterminer l'âge des filles!"
    quit ()

# ==| Main (programme principal) |==
boys = boys ()
print "Les âges des garcons sont donc:", boys
oldest = max ( boys )
print "\nEt l'âge de l'ainé des garçons est donc de", oldest, "an(s)"

prompt ()

girls = girls ( oldest )
print "Les âges des filles sont donc:", girls
youngest = min ( girls )
print "L'âge de la plus jeune fille (aux yeux verts) est donc de", youngest, "an(s)."
print "\nÉtudions maintenant la façon de résoudre cette énigme."
prompt ()
print """
L'enigme est résolue sans que ce programme n'ait eu à faire explicitement la moindre boucle.
La méthode utilisée n'est pas optimale car on aurait pu réduire le nombre de candidats plus
rapidement (en utilisant les informations sur les ainés ou les plus jeunes enfants) et on aurait
aussi pu éviter de filtrer trop de triplets dans G en notant que k = (a+1)² ÷ (i.j).
Mais le but de ce programme est de montrer la clarté apportée par la notion de définition en compréhension
par rapport à l'utilisation explicite de boucles (for).
"""

print "Une façon plus rapide de résoudre l'énigme est donc donnée ci-dessous."

# ==| Commentaires utiles |==
prompt ()

print "Les âges des garçons correspondent à { (i,j,k) ∈ ⟦ 1 .. 6 ⟧³, i ≤ j < k, i+j+k | ijk, ijk ÷ (i+j+k) = k }, soit:"
altboys = [
    ( i, j, k )
    for i in range ( 1, 7 )     # (i,j,k) ∈ ⟦ 1 .. 6 ⟧
    for j in range ( i, 7 )     # i ≤ j
    for k in range ( j + 1, 7 ) # j < k
    if i * j * k % ( i + j + k ) == 0 \
    and i * j * k / ( i + j + k  ) == k
    ]
printl ( altboys )

prod = ( altboys [ 0 ][ 2 ] + 1 ) ** 2
print "Le produit de l'âge des filles est donc", prod

prompt ()
print "Posons G = { (i,j,k) ∈ ⟦ 1 .. 36 ⟧³, i ≤ j ≤ k, ijk = 36 }"
print "et si β est le sac (bag) β = {{ i+j+k | (i,j,k) ∈ G }} avec mᵦ: β ⟶ ℕ, s ⟼ la multiplicité de s dans β"
print "les âges des filles correspondent à { (i,j,k) ∈ G | mᵦ(i+j+k) > 1, i < j }, soit:"
altgirls = {    # dictionaire de la forme { triplet: valeur } avec la valeur égale à la somme des âges du triplet, c'est une combinaison de G et β
    ( i, j, k ): i + j + k
    for i in range ( 1, prod + 1 )
    for j in range ( i, prod + 1 )
    for k in range ( j, prod + 1 )
    if i * j * k == prod
    }
altgirls = [ # t est un triplet d'âge, donc une clé du dictionnaire
    t
    for t in altgirls
    if altgirls.values().count ( altgirls [ t ] ) > 1
    and t [ 0 ] < t [ 1 ]
    ]
# ceci est équivalent à l'usage de la fonction de filtrage couplée à des expressions lambda
# altgirls = filter ( lambda item: altgirls.values().count ( altgirls [ item ] ) > 1 and item [ 0 ] < item [ 1 ], altgirls )
printl ( altgirls )

prompt ()
print "Quelques commentaires finaux suivent."

prompt ()
print """
La méthode des listes en compréhension est beaucoup plus claire que celle des boucles explicites.
Elle correspond par ailleurs à la notation ensembliste utilisée en mathématique.
Elle est aussi généralement plus efficace car le compilateur/interpréteur peut l'optimiser à sa guise.

Noter toutefois que cette optimisation n'est pas omnisciente et que si l'ensemble généré par l'expression
est inutilement grand, la performance s'en ressentira.

Cette notation s'étend aux dictionaires et aux ensembles (sets).
"""

prompt ()
print """
Elle peut aussi s'utiliser directement pour passer des paramètres aux itérateurs.
Par exemple, si l'on écrit:

	sum ( [ x * x for x in range ( 10 ) ] )
	# ceci est Σ⁹ᵢ₌₀ i² c.a.d. la somme des carrés des entiers de 0 à 9

en fait l'interpréteur crée une liste en mémoire contenant tous les carrés de 0 à 9,
puis il itère sur cette liste pour en calculer la somme. Si la liste était plus grande,
la consommation mémoire s'en ressentirait et donc la performance aussi, en particulier
si la liste générée excède la taille du cache.

Mais il y a moyen d'éviter ce problème et d'être encore plus efficace.
"""

prompt ()
print """
Cependant, la fonction sum permet d'opérer sur des expressions génératrices directement
(c'est le cas des fonctions max, min, et plus généralement des fonctions qui réduisent
une liste itérable à une seule valeur).
Il est ainsi plus efficace de calculer la somme ci-dessus sans générer la liste des carrés,
et ceci s'exprime:

	sum ( x * x for x in xrange ( 10 ) ) # noter l'absence de [] autour de l'expression génératrice
	# et noter l'utilisation de xrange qui ne génère ses éléments qu'au fur et à mesure des besoins.

Dans l'expression ci-dessus, la fonction sum itère sur une liste de carrés générés un à un,
au fur et à mesure de l'itération de la fonction sum. C'est l'équivalent d'une boucle,
sauf que cette boucle est gérée entièrement dans l'interpréteur, alors qu'une boucle
explicite passerait à chaque itération entre le source et l'interpréteur.
"""

prompt ()
print """
Un autre exemple d'expression génératrice utilisé avec une fonction de reduction est:

	with open ( 'input' ) as file : print max ( len ( line ) for line in file if line.strip () )

qui calcule la longueur de la ligne la plus longue d'un fichier en sautant les lignes blanches.
Ceci est strictement équivalent (mais bien plus rapide) que la boucle:

	with open ( 'input' ) as file :
		result = 0
		for line in file :
			if line.strip () :
				result = max ( result, len ( line ) )
		print ( result )

On peut facilement montrer (et mesurer) que les expressions en compréhension sont généralement
plus efficaces que les boucles explicites. La lecture en détail de
http://leadsift.com/loop-map-list-comprehension/ permet de comprendre les nuances de la généralisation.
"""
# Il faut noter que Guido Von Rossum (l'auteur de Python) indique que map est meilleur que
# les boucles pour des fonctions simples, car il n'y a pas de surcharge liée à l'interpréteur.
# Ceci est validé par les mesures du site http://leadsift.com/loop-map-list-comprehension/
# pour des fonctions sumples (en O(n)).

prompt ()
print """
Finalement, on peut observer l'équivalence des compréhensions avec l'utilisation des fonctions
de filtrage et de reduction.
Par exemple, dans l'enigme ci-dessus, après avoir calculé l'âge des garçon, on connaît le produit
des âges des filles (36). Donc on peut calculer l'âge des filles de la façon suivante:

prod = 36
girls = {   # dictionaire de la forme { triplet: valeur } avec la valeur égale à la somme des âges du triplet
	( i, j, k ): i + j + k
	for i in range ( 1, prod + 1 )
	for j in range ( i, prod + 1 )
	for k in range ( j, prod + 1 )
	if i * j * k == prod
	}
girls = [ t for t in girls if girls.values().count ( girls [ t ] ) > 1 and t [ 0 ] < t [ 1 ] ] # où t est un triplet
"""

prompt ()
print """
Cette dernière expression est équivalent à l'usage de la fonction de filtrage couplée à des expressions lambda:

girls = filter ( lambda item: girls.values().count ( girls [ item ] ) > 1 and item [ 0 ] < item [ 1 ], girls )

La fonction filter prend deux arguments: une fonction de test et une liste (plus précisément un itérable)
et elle retourne la liste réduite aux éléments pour lesquels la fonction de test retourne "true".
La spécification de python indique explicitement l'équivalence entre
'filter(function, iterable)' et l'expression génératrice '(item for item in iterable if function(item))'.

On remarque aussi l'utilisation d'expression lambda pour définir la fonction de filtrage.
L'expression:

lambda item: girls.values().count ( girls [ item ] ) > 1 and item [ 0 ] < item [ 1 ]

est équivalente à définir une fonction anonyme:

def <anonymous> ( item ) :      # en fait une expression lambda n'a pas de nom
    return girls.values().count ( girls [ item ] ) > 1 and item [ 0 ] < item [ 1 ]
"""

prompt ()
print """
Au delà des aspects de performance, les compréhensions donnent un code
systématiquement plus lisible que les boucles.

En conclusion, on voit donc que l'utilisation des listes en compréhension
(ou des ensembles ou dictionnaires) et des expressions génératrices correspondantes
est quasiment toujours supérieure à l'écriture de boucles ou l'utilisation
de fonctions de type map, filter, reduce, cette supériorité se mesurant sur
2 critères:

- celui de la performance
- celui de la lisibilité du code

Ce dernier critère est au moins aussi important que celui de la performance.

Il faut enfin noter que l'utilisation des notations de compréhension fait partie
des tests de recrutement pour les entreprises utilisant Python, et la non-maîtrise
de ces notions est rédhibitoire à l'embauche. Python est principalement utilisé
aujourd'hui dans l'analyse de donnée et l'intelligence artificielle. C'est le
langage majeur ayant la plus forte croissance d'utilisation en 2017.
Cf. https://insights.stackoverflow.com/survey/2017 pour plus de détails.
Les géants Google, Facebook, Netflix, Spotify, Industrial Light and Magic...
utilisent intensément Python.

Moi pas (j'utilise javascript).
"""

# Sans commentaires la résolution de notre problème s'écrit de façon compacte et donc illisible, en 6 lignes (b=boys, g=girls):
#
# b = [ ( i, j, k ) for i in range ( 1, 7 ) for j in range ( i, 7 ) for k in range ( j + 1, 7 ) if i * j * k % ( i + j + k ) == 0 and i * j * k / ( i + j + k  ) == k ]
# print "les âges des garçons sont: ", b, "l'ainé est agé de", b [ 0 ][ 2 ], "ans."
# prod = ( b [ 0 ][ 2 ] + 1 ) ** 2
# g = { ( i, j, k ): i + j + k for i in range ( 1, prod + 1 ) for j in range ( i, prod + 1 ) for k in range ( j, prod + 1 ) if i * j * k == prod }
# g = [ t for t in g if g.values().count ( g [ t ] ) > 1 and t [ 0 ] < t [ 1 ] ]
# print "les âges des filles sont: ", g
