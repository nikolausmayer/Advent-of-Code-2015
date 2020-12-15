import sys

nice = 0
for line in [l.strip() for l in open(sys.argv[1]).readlines()]:
    if sum([line.count(vowel) for vowel in 'aeiou']) >= 3 and \
       any([line[i]==line[i+1] for i in range(len(line)-1)]) and \
       all([p not in line for p in ['ab','cd','pq','xy']]):
        nice += 1
print(nice)
