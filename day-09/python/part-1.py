import itertools
import re
import sys

RE = re.compile(r'(?P<from>\w+) to (?P<to>\w+) = (?P<dist>\d+)')

distances = {}

for line in open(sys.argv[1]).readlines():
    m = RE.match(line).groupdict()
    FROM, TO, DIST = m['from'], m['to'], int(m['dist'])
    if FROM not in distances:
        distances[FROM] = {}
    distances[FROM][TO] = DIST
    if TO not in distances:
        distances[TO] = {}
    distances[TO][FROM] = DIST

minroute = -1
for route in itertools.permutations(distances.keys()):
    routelen = 0
    for i in range(len(route)-1):
        routelen += distances[route[i]][route[i+1]]
    if minroute < 0 or routelen < minroute:
        minroute = routelen

print(minroute)

