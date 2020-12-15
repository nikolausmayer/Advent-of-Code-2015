import re
import sys

RE_hex = re.compile(r'\\x..')

diff_sum = 0
for line in open(sys.argv[1]).readlines():
    line = line.strip()
    valuelen = len(line)
    line = line.replace('\\', '\\\\') \
               .replace('"', '\\"')           
    line = '"'+line+'"'
    codelen = len(line)
    diff_sum += (codelen - valuelen) 

print(diff_sum)

