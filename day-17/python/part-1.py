import sys

amount = 150

containers = [(i, int(l.strip())) for (i, l) in enumerate(list(open(sys.argv[1]).readlines()))]
combinations = {i:[] for i in range(1, amount+1)}

print(containers)

for i in range(1, amount+1):
    for (id, c) in containers:
        if c == i:
            newset = set()
            newset.add((id, c))
            combinations[i].append(newset)
        if i-c > 0:
            for sub in combinations[i-c]:
                if (id, c) in sub: continue
                newset = set(sub)
                newset.add((id, c))
                if newset in combinations[i]: continue
                combinations[i].append(newset)

print(len(combinations[amount]))

