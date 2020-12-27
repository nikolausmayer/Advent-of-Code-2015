import sys

input = [l.strip().split() for l in open(sys.argv[1]).readlines()]

registers = {'a': 0, 'b': 0}

## Part 2 -->
registers['a'] = 1
## <-- Part 2

iptr = 0
while 0 <= iptr < len(input):
    line = input[iptr]
    instr = line[0]
    reg = line[1].strip(',')
    if instr == 'hlf':
        registers[reg] = registers[reg]//2
        iptr += 1
    elif instr ==  'tpl':
        registers[reg] *= 3
        iptr += 1
    elif instr == 'inc':
        registers[reg] += 1
        iptr += 1
    elif instr == 'jmp':
        iptr += int(line[1])
    elif instr == 'jie':
        if registers[reg] % 2 == 0:
            iptr += int(line[2])
        else:
            iptr += 1
    elif instr == 'jio':
        if registers[reg] == 1:
            iptr += int(line[2])
        else:
            iptr += 1
    else:
        print("err")
        break

print(registers['b'])
