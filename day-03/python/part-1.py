import sys

dx = {'<': -1, '>': 1, '^':  0, 'v': 0}
dy = {'<':  0, '>': 0, '^': -1, 'v': 1}
for line in [l.strip() for l in open(sys.argv[1]).readlines()]:
    visited = set([(0, 0)])
    x, y = 0, 0
    for c in line:
        x += dx[c]
        y += dy[c]
        visited.add((x, y))
    print(len(visited))
