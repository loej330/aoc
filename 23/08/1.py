moves, _, *lines = map(str.strip, open('8/input.txt'))
cardinality = { 'L': 0, 'R': 1 }
network = { line[0:3]: (line[7:10], line[12:15]) for line in lines }
current = 'AAA'
total = 0
i = 0
while current != 'ZZZ':
    if i == len(moves): i = 0
    current = network[current][cardinality[moves[i]]]
    total += 1
    i += 1
print(total)