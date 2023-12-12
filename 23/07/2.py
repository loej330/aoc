from collections import Counter
s = {**{'J':0},**{str(n):n-1 for n in range(2,10)},**{'T':9,'Q':10,'K':11,'A':12}}
t = {(1,1,1,1,1):0,(1,1,1,2):1,(1,2,2):2,(1,1,3):3,(2,3):4,(1,4):5,(5,):6,}

rs = []
for h, b in [l.split() for l in open('7/input.txt')]:
    if 'J' in (c:=Counter(h)) and len(c) > 1:
        j = c.pop('J')
        c[c.most_common()[0][0]] += j
    rs.append([t[tuple(sorted(c.values()))]] + [*(map(s.get, h))] + [int(b)])
print(sum([ r[-1] * (i+1) for i, r in enumerate(sorted(rs)) ]))