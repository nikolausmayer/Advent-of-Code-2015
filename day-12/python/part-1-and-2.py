import json
import sys

for line in [l.strip() for l in open(sys.argv[1]).readlines()]:
    data = json.loads(line)

    def count(d):
        if type(d) == type([]):
            return sum([count(s) for s in d])
        elif type(d) == type({}):
            ## Part 2 -->
            if 'red' in d.values():
                return 0
            ## <-- Part 2
            else:
                return sum([count(s) for s in d.values()])
        else:
            try:
                return int(d)
            except:
                return 0

    print(count(data))

