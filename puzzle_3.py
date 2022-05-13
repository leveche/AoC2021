#!/usr/bin/env python3

import sys

n = 0
a = [ 0 for i in range(12) ]

for x in map(lambda x: str.rstrip(x), sys.stdin):
    y = list ( map (int, list(x)) )
    a = list ( map( sum, zip(a, y) ) )
    n += 1

gamma = [ 2*x//n for x in a ]
epsilon = [ 1-x for x in gamma ]

def toDec(v):
    a = 0
    for x in range(len(v)):
        if v[x]:
            a += 2**(11-x)
    return a

print(toDec(epsilon), epsilon, gamma, toDec(epsilon)*toDec(gamma))
