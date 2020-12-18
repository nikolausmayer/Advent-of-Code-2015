import re
import sys

RE = re.compile(r'(?P<name>\w+) can fly (?P<speed>\d+) km/s for (?P<fly>\d+) seconds, but then must rest for (?P<rest>\d+) seconds.')

reindeers = {}

for line in open(sys.argv[1]).readlines():
    m = RE.match(line).groupdict()
    reindeers[m['name']] = (int(m['speed']), int(m['fly']), int(m['rest']))

time = 2503
maxdist = 0
for r in reindeers:
    data = reindeers[r]
    dist = data[0] * data[1] * (time // (data[1]+data[2])) +\
           data[0] * min(data[1], (time % (data[1]+data[2])))
    maxdist = max(maxdist, dist)

print(maxdist)

