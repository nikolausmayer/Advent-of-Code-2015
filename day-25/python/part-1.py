import sys

with open(sys.argv[1]) as f:
    row = int(f.readline())
    col = int(f.readline())

code = 20151125
a = 252533
b = 33554393

c = r = 1

while True:
    code = (code*a)%b
    c += 1
    r -= 1
    if r == 0:
        r = c
        c = 1
    if r == row and c == col:
        print(code)
        break

