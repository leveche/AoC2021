#!/usr/bin/env python

import sys

firstline = True
count = 0
window = 3

for x in map(lambda x: int(str.rstrip(x)), sys.stdin):
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
