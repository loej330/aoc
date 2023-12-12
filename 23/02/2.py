import sys
import numpy as np

total = 0
for game, line in enumerate(sys.stdin.readlines()):
    maxes = { 'red': 0, 'green': 0, 'blue': 0 }
    sets = line[(line.find(':') + 1):].strip().split('; ')
    for set in sets:
        counts = set.split(', ')
        for count in counts:
            ammount, color = count.split(' ') 
            maxes[color] = max(int(ammount), maxes[color])
    total += np.prod(list(maxes.values()))
    
print(total)