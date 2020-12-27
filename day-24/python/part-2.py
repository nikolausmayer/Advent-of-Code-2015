from functools import reduce
import sys

packages = sorted([int(l) for l in open(sys.argv[1]).readlines()])[::-1]

fourth = sum(packages)//4

first = []

def sub_select(selection, rest, configs, skip=False):
    if not rest:
        return
    if sum(selection) + rest[0] == fourth:
        configs.append(selection + [rest[0]])
        if skip:
            return
    elif sum(selection) + rest[0] < fourth:
        sub_select(selection + [rest[0]], rest[1:], configs, skip)
        if skip and configs:
            return
    sub_select(selection, rest[1:], configs, skip)
    
sub_select([], packages, first, False)

def mul(a, b):
    return a * b

minsize = 9999
minqe = -1

for c in first:
    if len(c) > minsize:
        continue
    second = []
    leftovers = [p for p in packages if p not in c]
    sub_select([], leftovers, second, True)
    if not second:
        continue
    third = []
    for s in second:
        leftovers = [p for p in packages if p not in c and p not in s]
        sub_select([], leftovers, third, True)
    if not third:
        continue
    if len(c) < minsize:
        minsize = len(c)
        minqe = -1
    if len(c) <= minsize:
        qe = reduce(mul, c)
        if minqe == -1 or qe < minqe:
            minqe = qe

print(minqe)

