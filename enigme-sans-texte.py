#!/usr/bin/python
# -*- coding:UTF-8 -*-
#
def printl ( list ) :
    items_per_line = 6
    index = 0
    for item in list :
        if index % items_per_line == 0 :
            print "\n",
        index = index + 1
        print "\t", item,
    print "\n"

def assess ( list ) :
    printl ( list )
    l = len ( list )
    if l > 1 :
        return False
    elif l == 0 :
        print "Ouch!"
        quit ()
    else :
        return True

def prod ( list ) :
    p = 1
    for item in list :
        p = p * item
    return p

def prompt () :
    answer = raw_input ( "\n↩ " )
    if answer in [ "q", "quit", "Q", "Quit", "QUIT", "s", "stop", "S", "Stop", "STOP" ] : quit ()

print "OK, essayons de trouver!\n"
prompt ()

def boys () :
    mini = 1
    maxi = 7

    boys = [
        [ i, j, k ]
        for i in range ( mini, maxi )
        for j in range ( i, maxi )
        for k in range ( j, maxi )
        ]
    if assess ( boys ) : return boys [ 0 ]

    prompt ()
    boys = [
        ages
        for ages in boys
        if prod ( ages ) % sum ( ages ) == 0 \
        and prod ( ages ) / sum ( ages ) == max ( ages )
        ]
    if assess ( boys ) : return boys [ 0 ]

    prompt ()
    boys = [ ages for ages in boys if ages.count ( max ( ages ) ) == 1 ]
    if assess ( boys ) : return boys [ 0 ]

    print "Ouch!"
    quit ()

def girls ( oldest ) :
    product = ( oldest + 1 ) ** 2
    mini = 1
    maxi = product + 1

    girls = [
        [ i, j, k ]
        for i in range ( mini, maxi )
        for j in range ( i, maxi )
        for k in range ( j, maxi )
        if i * j * k == product
        ]
    if assess ( girls ) : return girls [ 0 ]

    prompt ()
    sums = [ sum ( ages ) for ages in girls ]
    printl ( sums )

    prompt ()
    duplicates = [ d for d in sums if sums.count ( d ) > 1 ]
    printl ( duplicates )

    if len ( duplicates ) == 0 :
        print "Ouch!"
        quit ();

    prompt ()
    girls = [ ages for ages in girls if sum ( ages ) in duplicates ]
    if assess ( girls ) : return girls [ 0 ]

    prompt ()
    girls = [ ages for ages in girls if ages.count ( min ( ages ) ) == 1 ]
    if assess ( girls ) : return girls [ 0 ]

    print "Ouch!"
    quit ()

boys = boys ()
print "âges des garcons:", boys
oldest = max ( boys )
print "âge de l'ainé:", oldest

prompt ()
girls = girls ( oldest )
print "âges des filles:", girls
youngest = min ( girls )
print "âge de la plus jeune fille (aux yeux verts):", youngest
print
