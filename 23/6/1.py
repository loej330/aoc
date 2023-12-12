p = 1
f = open('6/input.txt').readlines()
for t, d in zip(*map(lambda x: list(map(int, x.split()[1:])), f)):
    s = ((t ** 2) - (4 * d)) ** 0.5 
    d0 = (((-t + s) / -2) + 1).__floor__()
    d1 = (((-t - s) / -2) - 1).__ceil__()
    p *= (d1 - d0 + 1)
print(p)