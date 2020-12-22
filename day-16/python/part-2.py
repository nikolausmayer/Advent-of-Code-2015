import re
import sys

RE = re.compile(r'(\w+): (\d+)')

all_aunts = []

for line in open(sys.argv[1]).readlines():
    all_aunts.append({})
    for [k, v] in RE.findall(line):
        all_aunts[-1][k] = int(v)

true_aunt = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

for [i, possible_aunt] in enumerate(all_aunts):
    for [k, v] in possible_aunt.items():
        if k in ['cats', 'trees']:
            if true_aunt[k] >= v:
                break
        elif k in ['pomeranians', 'goldfish']:
            if true_aunt[k] <= v:
                break
        elif true_aunt[k] != v:
            break
    else:
        print(i+1)


