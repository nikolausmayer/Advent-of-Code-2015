import sys

for line in open(sys.argv[1]).readlines():
    line = line.strip()
    for iteration in range(50):
        output = []
        digit, rep = line[0], 0
        for char in line:
            if char == digit:
                rep += 1
            else:
                output.append(str(rep))
                output.append(digit)
                digit = char
                rep = 1
        output.append(str(rep))
        output.append(digit)
        output = "".join(output)
        print(len(output))
        line = output
