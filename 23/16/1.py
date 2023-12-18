u, d, l, r = (-1, 0), (1, 0), (0, -1), (0, 1)
m = { '/': { u:r, d:l, l:d, r:u }, '\\': { u:l, d:r, l:u, r:d }}
s = { '|': { l:[u,d], r:[u,d] }, '-': { u:[l,r], d:[l,r] }}
g = [ list(l.strip()) for l in open("input.txt") ]
e = [ [ [] for _ in range(len(g)) ] for _ in range(len(g)) ]
b = [ ((0, -1), r) ]

while b:
    k = []
    for xy, d in b:
        x, y = xy[0] + d[0], xy[1] + d[1]
        if not 0 <= x < len(g) or not 0 <= y < len(g[0]): continue
        if (c:=g[x][y]) in m: 
            if (d:=m[c][d]) in e[x][y]: continue
            k.append(((x,y), d)); e[x][y].append(d) 
        elif c in s and d in s[c]: 
            if (d:=s[c][d])[0] in e[x][y] or d[1] in e[x][y]: continue
            k.extend([*zip([(x,y)]*2, d)]); e[x][y].extend(d)
        else: k.append(((x,y),d)); e[x][y].append(d)
    b = k

print(sum( sum( 1 if c else 0 for c in l ) for l in e))