import sys

for line in [l.strip() for l in open(sys.argv[1]).readlines()]:
    print(line.count('(')-line.count(')'))
