import re
import sys

ASSIGN = re.compile(                  r' -> (\w+)')
INIT   = re.compile(             r'(\d+) -> (\w+)')
COPY   = re.compile(             r'(\w+) -> (\w+)')
OR     = re.compile(    r'(\w+) OR (\w+) -> (\w+)')
AND    = re.compile(   r'(\w+) AND (\w+) -> (\w+)')
NOT    = re.compile(         r'NOT (\w+) -> (\w+)')
LSHIFT = re.compile(r'(\w+) LSHIFT (\d+) -> (\w+)')
RSHIFT = re.compile(r'(\w+) RSHIFT (\d+) -> (\w+)')

lines = list(open(sys.argv[1]).readlines())

def memoize(fun):
    memory = {}
    def inner(arg):
        if arg == 'RESET':
            nonlocal memory
            memory = {}
            return
        if arg not in memory:
            memory[arg] = fun(arg)
        return memory[arg]
    return inner

@memoize
def f(wire):
    try:
        i = int(wire)
        return i
    except:
        pass

    try:
        wire_rule = [l for l in lines if ASSIGN.search(l).groups()[0] == wire][0]
    except:
        exit(1)
    mINIT   = INIT.match(wire_rule)
    mCOPY   = COPY.match(wire_rule)
    mOR     = OR.match(wire_rule)
    mAND    = AND.match(wire_rule)
    mNOT    = NOT.match(wire_rule)
    mLSHIFT = LSHIFT.match(wire_rule)
    mRSHIFT = RSHIFT.match(wire_rule)
    if mINIT: return int(mINIT.groups()[0])
    elif mCOPY: return f(mCOPY.groups()[0])
    elif mOR: return f(mOR.groups()[0]) | f(mOR.groups()[1])
    elif mAND: return f(mAND.groups()[0]) & f(mAND.groups()[1])
    elif mNOT: return ~(f(mNOT.groups()[0])) + 2**16
    elif mLSHIFT: return f(mLSHIFT.groups()[0]) << int(mLSHIFT.groups()[1])
    elif mRSHIFT: return f(mRSHIFT.groups()[0]) >> int(mRSHIFT.groups()[1])
    else: print(wire_rule)

b = f('a')
for i in range(len(lines)):
    if ASSIGN.search(lines[i]).groups()[0] == 'b':
        lines[i] = "%d -> b" % b
        break

f('RESET')
print(f('a'))

