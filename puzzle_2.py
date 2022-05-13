#!/usr/bin/env python3

import sys
import re

depth = 0
xpos = 0
aim = 0

for x in sys.stdin:
    m = re.search('(\S+) (\d+)', x)
    if m:
        direction, magnitude = m.group(1), int(m.group(2))
        if 'up' == direction:
            aim -= magnitude
        elif 'down' == direction:
            aim += magnitude
        elif 'forward' == direction:
            xpos += magnitude
            depth = max(0, depth + aim * magnitude)

print(aim, depth, xpos, depth*xpos)
