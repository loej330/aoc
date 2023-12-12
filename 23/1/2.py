import sys
digits = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
total = 0
for line in sys.stdin.readlines():
    looking = True
    i = 0
    while looking:
        if line[i].isdigit():
            digit1 = int(line[i])
            break
        for d, digit in enumerate(digits):
            end = min(i+len(digit), len(line))
            if line[i:end] == digit:
                looking = False
                digit1 = d+1
                break
        i += 1

    line = line[::-1]
    looking = True
    i = 0
    while looking:
        if line[i].isdigit():
            digit2 = int(line[i])
            break
        for d, digit in enumerate(digits):
            digit = digit[::-1]
            end = min(i+len(digit), len(line))
            if line[i:end] == digit:
                looking = False
                digit2 = d+1
                break
        i += 1

    total += (digit1 * 10) + digit2
print(total)