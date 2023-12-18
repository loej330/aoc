U, D, L, R = (-1, 0), (1, 0), (0, -1), (0, 1)
m = { '/': { U:R, D:L, L:D, R:U }, '\\': { U:L, D:R, L:U, R:D }}
s = { '|': { L:[U,D], R:[U,D] }, '-': { U:[L,R], D:[L,R] }}
g = [ list(l.strip()) for l in open("input.txt") ]
t = 0 

for start in (
    [ ((y,x),d) for y,d in [(len(g),U),(-1,D)] for x in range(len(g)) ]+
    [ ((y,x),d) for x,d in [(len(g),L),(-1,R)] for y in range(len(g)) ]): 
    e = [ [ [] for _ in range(len(g)) ] for _ in range(len(g)) ]
    b = [ start ]
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
    t = max(t, sum( sum( 1 if c else 0 for c in l ) for l in e))

print(t)