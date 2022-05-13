#!/usr/bin/env python3

import sys
import re

depth = 0
xpos = 0

for x in sys.stdin:
    m = re.search('(\S+) (\d+)', x)
    if m:
        direction, magnitude = m.group(1), int(m.group(2))
        if 'up' == direction:
            depth = max(0, depth - magnitude)
        elif 'down' == direction:
            depth += magnitude
        elif 'forward' == direction:
            xpos += magnitude

print(depth, xpos, depth*xpos)
