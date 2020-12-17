import sys

def increment(w):
    w[-1] += 1
    i = -1
    while w[i] > ord('z'):
        w[i] = ord('a')
        w[i-1] += 1
        i -= 1
    return w

def criterion1(w):
    for i in range(len(w)-2):
        if w[i]+1 == w[i+1] and w[i+1]+1 == w[i+2]:
            return True
    return False
    
def criterion2(w):
    return (ord('i') not in w) and \
           (ord('o') not in w) and \
           (ord('l') not in w)

def criterion3(w):
    doubles = 0
    first_double_letter = None
    i = 0
    while i < len(w)-1:
        if w[i] == w[i+1] and w[i] != first_double_letter:
            doubles += 1
            i += 1
            first_double_letter = w[i]
        i += 1
    return doubles >= 2

def is_valid(w):
    return criterion1(w) and criterion2(w) and criterion3(w)

for line in [l.strip() for l in open(sys.argv[1]).readlines()]:
    current = [ord(c) for c in line]
    current = increment(current)
    while not is_valid(current):
        current = increment(current)
    current = increment(current)
    while not is_valid(current):
        current = increment(current)
    print("Next valid password is",
          "".join([chr(c) for c in current]))

