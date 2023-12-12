from collections import Counter
s = {**{str(n):n-2 for n in range(2,10)}, **{'T':8,'J':9,'Q':10,'K':11,'A':12}}
t = {(1,1,1,1,1):0,(1,1,1,2):1,(1,2,2):2,(1,1,3):3,(2,3):4,(1,4):5,(5,):6,}

print(sum([o[-1] * (i+1) for i, o in enumerate(sorted([
    [t[tuple(sorted(Counter(h).values()))]] + [*(map(s.get,h))] + [int(b)] 
    for h,b in [l.split() for l in open('7/input.txt')]]))]))