from math import lcm 
moves, _, *lines = map(str.strip, open('8/input.txt'))
cardinality = { 'L': 0, 'R': 1 }
network = { line[0:3]: (line[7:10], line[12:15]) for line in lines }
currents = [ node for node in network if node[2] == 'A' ]
totals = [0] * len(currents)

for j, current in enumerate(currents):
    times_reached_z = 0
    total = 0; i = 0
    while current[2] != 'Z':
        current = network[current][cardinality[moves[i]]]
        i += 1; total += 1
        if i == len(moves): i = 0
    totals[j] = total

print(lcm(*totals))