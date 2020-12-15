from collections import defaultdict
import re
import sys

parse = re.compile(r'''
    (?P<action>[a-zA-Z]+)\s
    (?P<x0>\d+),(?P<y0>\d+)\s
    through\s
    (?P<x1>\d+),(?P<y1>\d+)''',
    re.VERBOSE)

def d():
    return 0
map = defaultdict(d)

for line in open(sys.argv[1]).readlines():
    cmd = parse.search(line).groupdict()
    if cmd['action'] == 'on':
        for y in range(int(cmd['y0']), int(cmd['y1'])+1):
            for x in range(int(cmd['x0']), int(cmd['x1'])+1):
                map[(x, y)] += 1
    elif cmd['action'] == 'off':
        for y in range(int(cmd['y0']), int(cmd['y1'])+1):
            for x in range(int(cmd['x0']), int(cmd['x1'])+1):
                map[(x, y)] = max(0, map[(x, y)]-1)
    else:
        for y in range(int(cmd['y0']), int(cmd['y1'])+1):
            for x in range(int(cmd['x0']), int(cmd['x1'])+1):
                map[(x, y)] += 2

print(sum([v for k,v in map.items()]))
