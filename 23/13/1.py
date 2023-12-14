file = open('13/input.txt').readlines() + ['\n']
total = 0
while '\n' in file:
    k = file.index('\n')
    group = [*map(str.strip, file[:k])]

    n = 0
    for i in range(1, len(group[0])):
        c = min(i, len(group[0])-i)
        if all([ row[i-c:i] == row[i:i+c][::-1] for row in group ]): n = i
    if n == 0:
        for i in range(1, len(group)):
            c = min(i, len(group)-i)
            if group[i-c:i] == group[i:i+c][::-1]: n = i * 100
    
    total += n
    file = file[(k+1):]
print(total)
