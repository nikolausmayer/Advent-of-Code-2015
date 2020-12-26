import re
import sys

RE = re.compile(r'(\w+) => (\w+)')

recipes = {}

for line in open(sys.argv[1]).readlines():
    if line == "\n":
        continue
    m = RE.search(line.strip())
    if m:
        src = m.groups()[0]
        trg = m.groups()[1]
        if src not in recipes:
            recipes[src] = []
        recipes[src].append(trg)
    else:
        target = line.strip()

pool = set()
for r in recipes:
    RE = re.compile(r)
    for f in RE.finditer(target):
        for t in recipes[r]:
            pool.add(target[:f.start()] + t + target[f.end():])
print(len(pool))


