import re
import sys

RE_hex = re.compile(r'\\x..')

diff_sum = 0
for line in open(sys.argv[1]).readlines():
    line = line.strip()
    codelen = len(line)
    line = line[1:-1]
    line = line.replace(r'\"', "_") \
               .replace(r'\\', "_")
    line = re.sub(RE_hex, '_', line) 
    valuelen = len(line)
    diff_sum += (codelen - valuelen)

print(diff_sum)

