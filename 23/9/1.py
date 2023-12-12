total = 0
for l in open('9/input.txt'):
    fs = [[ *map(int, l.split()) ]]
    while any(f := fs[-1]): fs += [[ f[i+1] - f[i] for i in range(len(f)-1) ]]
    for i in range(len(fs)-1, 0, -1): 
        fs[i-1] += [fs[i-1][-1]+fs[i][-1]]
    total += fs[0][-1]
print(total)