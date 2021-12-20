#!/usr/bin/env python

import sys

count = 0
wsize = 3
window = [ 0 for i in range(wsize) ]

class IncCounter:

    def __init__(self):
        self.firstline = True
        self.count = 0

    def push(self, x):
        if (self.firstline):
            self.firstline = False
            self.lastinput = x
        else:
            if (x >= self.lastinput):
                self.count += 1
                self.lastinput = x
                print (self.lastinput, x, "increasing")

    def getCount(self):
        return self.count

counter = IncCounter()

linenr = wsize - 1
for x in map(lambda x: int(str.rstrip(x)), sys.stdin):
    window[linenr % wsize] = x
    linenr += 1
    counter.push(sum(window))
    print (linenr, window, sum(window))

print(counter.getCount())
