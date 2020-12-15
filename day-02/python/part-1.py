import re
import sys

RE = re.compile(r'(\d+)x(\d+)x(\d+)')
paper = 0
for line in [l.strip() for l in open(sys.argv[1]).readlines()]:
    l, w, h = [int(s) for s in RE.match(line).groups()]
    paper += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
print(paper)
