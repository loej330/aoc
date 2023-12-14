def reflection(g):
    for i in range(1, len(g[0])):
        errors = 0
        c = min(i, len(g[0])-i)
        for row in g:
            errors += sum(1 for c0, c1 in zip(row[i-c:i], row[i:i+c][::-1]) if c0 != c1)
            if errors > 1: break
        if errors == 1: return(i) 
    for i in range(1, len(g)):
        c = min(i, len(g)-i)
        if sum(1 for c0, c1 in zip(''.join(g[i-c:i]), ''.join(g[i:i+c][::-1])) if c0 != c1) == 1:
            return(i * 100)

file = open('13/input.txt').readlines() + ['\n']
total = 0

while '\n' in file:
    k = file.index('\n')
    total += reflection([*map(str.strip, file[:k])]) 
    file = file[(k+1):]

print(total)
