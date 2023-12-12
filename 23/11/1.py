from itertools import combinations

f = [ [*ln.strip()] for ln in open('11/input.txt') ]
non_empty_cols = set() 
for i in range(len(f)-1, -1, -1):
    matches = [ j for j, char in enumerate(f[i]) if char == '#' ]
    if len(matches) == 0: f.insert(i+1, ['.'] * len(f[i]))
    else: non_empty_cols.update(matches)

empty_cols = set([*range(len(f[0]))]).difference(non_empty_cols)
for i in range(len(f)):
    for j in range(len(f[i])-1, -1, -1):
        if j in empty_cols: f[i].insert(j, '.')
    
galaxies = []
for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j] == '#': galaxies.append((i, j))

print(sum([ abs(a[0]-b[0])+abs(a[1]-b[1]) for a,b in combinations(galaxies,2) ]))
