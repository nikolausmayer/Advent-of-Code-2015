import re
import sys

RE = re.compile(r'(\d+)x(\d+)x(\d+)')
ribbon = 0
for line in [l.strip() for l in open(sys.argv[1]).readlines()]:
    l, w, h = [int(s) for s in RE.match(line).groups()]
    ribbon += min(l+l+w+w, w+w+h+h, h+h+l+l) + l*w*h
print(ribbon)
