import sys

presents = int(open(sys.argv[1]).readline()) // 10

housemap = [1] * presents

for i in range(2, presents):
    for m in range(1, presents//i):
        housemap[i*m] += i

for i in range(presents):
    if housemap[i] >= presents:
        print(i)
        break

