import sys

grid = [[{'#': True, '.': False}[c] for c in line.strip()]
        for line in open(sys.argv[1]).readlines()]

W = len(grid)

## Part 2 -->
grid[0][0] = True
grid[0][W-1] = True
grid[W-1][0] = True
grid[W-1][W-1] = True
## <-- Part 2

#def printGrid():
#    for line in grid:
#        print("".join([{True: '#', False: '.'}[v] for v in line]))

for iter in range(100):
    newgrid = [line[:] for line in grid]
    for y in range(W):
        for x in range(W):
            neighbors = 0
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    if x+dx >= 0 and x+dx < W and \
                       y+dy >= 0 and y+dy < W and \
                       grid[y+dy][x+dx]:
                        neighbors += 1
            if grid[y][x]:
                if neighbors != 2 and neighbors != 3:
                    newgrid[y][x] = False
            else:
                if neighbors == 3:
                    newgrid[y][x] = True
    ## Part 2 -->
    newgrid[0][0] = True
    newgrid[0][W-1] = True
    newgrid[W-1][0] = True
    newgrid[W-1][W-1] = True
    ## <-- Part 2
    grid = newgrid

print(sum([sum([1 for c in line if c]) for line in grid]))

