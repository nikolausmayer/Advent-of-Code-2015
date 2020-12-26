import heapq
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

class Item:
    def __init__(self, molecule, steps):
        self.molecule = molecule
        self.steps = steps
    def __lt__(self, rhs):
        return len(self.molecule) < len(rhs.molecule)

heap = []
heapq.heapify(heap)
heapq.heappush(heap, Item(target, 0))

while heap:
    node = heapq.heappop(heap)
    steps = node.steps
    node = node.molecule
    for src in recipes:
        for trg in recipes[src]:
            RE = re.compile(trg)
            for f in RE.finditer(node):
                x = node[:f.start()] + src + node[f.end():]
                #print(node, "<-%d-"%(steps+1), x)
                if x == "e":
                    print(steps+1)
                    exit(0)
                heapq.heappush(heap, Item(x, steps+1))

