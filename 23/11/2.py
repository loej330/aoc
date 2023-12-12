from itertools import combinations

g = 1000000 
f = [ [*ln.strip()] for ln in open('11/input.txt') ]

non_empty_cols = set() 
for i in range(len(f)):
    matches = [ j for j, char in enumerate(f[i]) if char == '#' ]
    if len(matches) == 0: f[i] = len(f[i]) * [g]
    else: 
        for j in range(len(f[i])): 
            if f[i][j] == '.': f[i][j] = 1
        non_empty_cols.update(matches)

empty_cols = set([*range(len(f[0]))]).difference(non_empty_cols)
for i in range(len(f)):
    for j in range(len(f[i])):
        if j in empty_cols: f[i][j] = f[i][j] * g 

galaxies = []; ic = [0] * len(f[0])
for i in range(len(f)):
    jc = 0
    for j in range(len(f[i])):
        if f[i][j] == '#': galaxies.append((ic[j], jc)); jc += 1; ic[j] += 1
        else: jc += f[i][j]; ic[j] += f[i][j]

print(sum([ abs(a[0]-b[0])+abs(a[1]-b[1]) for a,b in combinations(galaxies,2) ]))