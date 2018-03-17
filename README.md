# Puzzle

This repository is for the French education system,
the rest of this note is in French.

# Résolution d'une énigme
Le but de ce programme est de montrer comment résoudre l'énigme ci-dessous
et d'introduire des techniques de programmation plus efficaces que les
algorithmes itératifs traditionnels.

L'exercice consiste à écrire une solution en Python, solution qui détaille les
étapes du raisonnement et explique celui-ci.

# L'énigme

Lors d'une promenade, un homme rencontre une amie de l'université.
Il discutent de la vie et de leurs études.
L'homme observe 3 garçons qui jouent dans le jardin de la maison de son amie.

__H__: Ils sont à toi ?<br/>
__F__: Oui.<br/>
__H__: Je n'ai pas une très bonne vue, ils vont déjà à l'école primaire ?<br/>
__F__: Ils ne sont pas assez âgés, il faut avoir plus de 6 ans pour cela.<br/>
__H__: Quel est donc leur âge (‡) ?<br/>
__F__: Je me souviens que tu aimes les énigmes, en voici une :

    la somme de leurs âges divise parfaitement le produit de leurs âges
    et le résultat de cette division est égal au plus grand de leurs âges.

__H__: Je ne peux pas savoir. Mais as-tu des filles ?<br/>
__F__: Oui, 3.<br/>
__H__: Quel est leur âge ?<br/>
__F__: Poursuivons l'énigme :

    le produit de l'âge de mes filles est le carré parfait
    qui suit le carré de l'âge de l'ainé des garçons.

__H__: Ah! Maintenant je connais l'âge de tes garçons,
    mais je ne peux pas savoir celui de tes filles.<br/>
__F__: Regarde le numéro de ma maison sur la boite aux lettres :

    La somme des âges de mes filles est égal à ce numéro.

__H__: Hélas, je ne peux toujours pas déterminer leur âge.<br/>
__F__: Pour t'aider je peux te dire que la plus jeune a des yeux verts.<br/>
__H__: Merci ! je connais maintenant l'âge de tes filles.

Quels sont les âges des garçons et des filles de l'amie de cet homme ?
Quel est âge de la fille aux yeux verts ?

(‡) l'âge est un élément de ℕ (ce serait difficile de faire autrement, au moment où l'on indiquerait l'âge, celui-ci serait déjà faux)

# Solution
Il y a bien sûr plusieurs façon de résoudre cette énigme. Le fichier
[enigme.py](https://github.com/jr-grenoble/puzzle/blob/master/enigme.py)
contient plusieurs solutions détaillées ainsi que de nombreux commentaires.

Il est recommandé de télécharger ce fichier et de l'exécuter sans lire le source
pour essayer de comprendre comment le programme est fait et s'en inspirer pour
résoudre l'exercice. Le mieux est d'interrompre l'execution du programme dès que
l'on a compris son fonctionnement (taper _q_ suivi de _return_ à l'invite ↩).

Une fois décidé à creuser la solution, il est recommandé de lire le code et les
commentaires dans leur intégralité.

Une solution peu commentée, mais en ligne avec la précédente est présente dans
[enigme-sans-texte.py](https://github.com/jr-grenoble/puzzle/blob/master/enigme-sans-texte.py).

Enfin une solution courte est donnée par
[enigme-solution-courte.py](https://github.com/jr-grenoble/puzzle/blob/master/enigme-ssolution-courte.py).
Le commentaire final de ce dernier fichier donne une solution en 6 lignes
mais il est tout à fait possible de faire plus laid.
