import sys
total = 0
limits = { 'red': 12, 'green': 13, 'blue': 14 }
for game, line in enumerate(sys.stdin.readlines()):
    possible = True
    sets = line[(line.find(':') + 1):].strip().split('; ')
    for set in sets:
        counts = set.split(', ')
        for count in counts:
            ammount, color = count.split(' ') 
            if int(ammount) > limits[color]: possible = False
    if possible: total += game + 1
    
print(total)