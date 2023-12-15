from collections import deque
cols = zip(*map(str.strip, open('input.txt')))
total = 0
for col in cols:
    rocks = deque([0])
    for i, char in enumerate(col):
        if char == "#" and i < len(col)-1 and col[i+1] != '#': rocks.append(0)
        elif char == 'O': rocks[-1] += 1
    for i, char in enumerate(col):
        if char == "#" and i < len(col)-1 and col[i+1] != '#': rocks.popleft()
        elif rocks[0] > 0: total += len(col)-i; rocks[0] -= 1
print(total)