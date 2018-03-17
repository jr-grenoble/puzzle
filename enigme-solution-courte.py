#!/usr/bin/python
# -*- coding:UTF-8 -*-
#
boys = [
    ( i, j, k )
    for i in range ( 1, 7 )     # (i,j,k) ∈ ⟦ 1 .. 6 ⟧
    for j in range ( i, 7 )     # i ≤ j
    for k in range ( j + 1, 7 ) # j < k
    if i * j * k % ( i + j + k ) == 0 \
    and i * j * k / ( i + j + k  ) == k
    ]
print "Les âges des garçons correspondent à { (i,j,k) ∈ ⟦ 1 .. 6 ⟧³, i ≤ j < k, i+j+k | ijk, ijk ÷ (i+j+k) = k }, soit:", boys

prod = ( boys [ 0 ][ 2 ] + 1 ) ** 2
print "L'aîné des garçons a donc", boys [ 0 ][ 2 ] + 1, "ans. Le produit de l'âge des filles est donc:", prod

girls = {
    ( i, j, k ): i + j + k
    for i in range ( 1, prod + 1 )
    for j in range ( i, prod + 1 )
    for k in range ( j, prod + 1 )
    if i * j * k == prod
    }
girls = [
    t
    for t in girls
    if girls.values().count ( girls [ t ] ) > 1 \
    and t [ 0 ] < t [ 1 ]
    ]
print "Posons G = { (i,j,k) ∈ ⟦ 1 .. 36 ⟧³, i ≤ j ≤ k, ijk = 36 }"
print "et si β est le sac (bag) β = {{ i+j+k | (i,j,k) ∈ G }} avec mᵦ: β ⟶ ℕ, s ⟼ la multiplicité de s dans β"
print "Les âges des filles correspondent à { (i,j,k) ∈ G | mᵦ(i+j+k) > 1, i < j }, soit:", girls
print "Et la plus jeune a", girls [ 0 ] [ 0 ], "an(s)."

# Sans commentaires ceci s'écrit de façon compacte et donc illisible, en 6 lignes :
#
# boys = [ ( i, j, k ) for i in range ( 1, 7 ) for j in range ( i, 7 ) for k in range ( j + 1, 7 ) if i * j * k % ( i + j + k ) == 0 and i * j * k / ( i + j + k  ) == k ]
# print "les âges des garçons sont: ", boys, "l'ainé"
# prod = ( boys [ 0 ][ 2 ] + 1 ) ** 2
# girls = { ( i, j, k ): i + j + k for i in range ( 1, prod + 1 ) for j in range ( i, prod + 1 ) for k in range ( j, prod + 1 ) if i * j * k == prod }
# girls = [ t for t in girls if girls.values().count ( girls [ t ] ) > 1 and t [ 0 ] < t [ 1 ] ]
# print "les âges des filles sont: ", girls
