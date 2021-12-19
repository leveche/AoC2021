#!/usr/bin/env python

import sys

firstline = True
count = 0

for x in map(str.rstrip, sys.stdin):
    if firstline:
        firstline = False
        y = x
        print(y,x,"first line",count)
    else:
        if x >= y:
            count += 1
            print (y,x,"increased",count)
        else:
            print (y,x,"not increased", count)
        y = x

print(count)
