import re
import sys

re_pair   = re.compile(r'(..).*\1')
re_repeat = re.compile(r'(.).\1')

nice = 0
for line in [l.strip() for l in open(sys.argv[1]).readlines()]:
    if re_pair.search(line) and re_repeat.search(line):
        nice += 1
print(nice)
