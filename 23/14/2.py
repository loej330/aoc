import numpy as np
from collections import deque

t = np.transpose; f = np.flip
d = np.array([*map(lambda l: list(l.strip()), open('input.txt').readlines())])

def shift(d):
    d = np.copy(d)
    for i in range(d.shape[0]):
        rocks = deque([0]) 
        for char in d[i]:
            if char == "#": rocks.append(0)
            elif char == 'O': rocks[-1] += 1
        for j, char in enumerate(d[i]):
            if char == '#': rocks.popleft()
            elif rocks[0] > 0: d[i][j] = 'O'; rocks[0] -= 1
            else: d[i][j] = '.'
    return d

past = [ d ]; repeat = -1
while repeat == -1:
    E = f(shift(t(shift(f(t(shift(t(shift(t(past[-1]))))))))))
    for i in range(len(past)):
        if np.array_equal(past[i], E): repeat = i; break
    past.append(E)
    
last = (repeat + ((1000000000 - repeat) % (len(past)-repeat-1)) )
print(sum(sum(len(col) - np.where(col == 'O')[0]) for col in t(past[last])))