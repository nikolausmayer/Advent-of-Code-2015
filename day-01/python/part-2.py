import sys

for line in [l.strip() for l in open(sys.argv[1]).readlines()]:
    floor = 0
    for i, c in enumerate(line):
        floor += 1 if c == '(' else -1
        if floor < 0:
            print("Entering basement at position", i+1)
            break
