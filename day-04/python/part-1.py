import sys
import hashlib

for line in [l.strip() for l in open(sys.argv[1]).readlines()]:
    num = 1
    while True:
        if hashlib.md5((line+str(num)).encode()) \
                  .hexdigest()                   \
                  .startswith('00000'):
            print(num)
            break
        num += 1
