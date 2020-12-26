import sys

presents = int(open(sys.argv[1]).readline())

housemap = {i:11 for i in range(presents//11)}

for i in range(2, presents//11):
    for m in range(1, min(51, presents//11//i)):
        housemap[i*m] += i*11

for i in range(presents):
    if housemap[i] >= presents:
        print(i)
        break

