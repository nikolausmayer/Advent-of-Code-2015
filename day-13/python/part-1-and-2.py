import itertools
import re
import sys

RE = re.compile(r'(?P<getter>\w+) would (?P<sign>gain|lose) (?P<num>\d+) happiness units by sitting next to (?P<giver>\w+)\.')

persons = []
maps = {}

for line in open(sys.argv[1]).readlines():
    m = RE.match(line).groupdict()
    if m['getter'] not in persons:
        persons.append(m['getter'])
        maps[m['getter']] = {}
    maps[m['getter']][m['giver']] = int(m['num']) if m['sign'] == 'gain' else -1*int(m['num'])

## Part 2 -->
maps['me'] = {}
for p in persons:
    maps['me'][p] = 0
    maps[p]['me'] = 0
persons.append('me')
## <-- Part 2
    
maxgain = 0
for order in itertools.permutations(persons):
    gain = 0
    for i in range(len(persons)):
        gain += maps[order[i]][order[i-1]]
        gain += maps[order[i]][order[(i+1)%len(persons)]]
    maxgain = max(maxgain, gain)

print(maxgain)
