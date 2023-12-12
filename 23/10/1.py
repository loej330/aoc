
ca = lambda c0, c1: (c0[0]+c1[0],c0[1]+c1[1])
cs = lambda c0, c1: (c0[0]-c1[0],c0[1]-c1[1])
ci = lambda m, c: m[c[0]][c[1]]

n,e,s,w = [(-1,0),(0,1),(1,0),(0,-1)]
p = {'|':[n,s],'-':[e,w],'L':[n,e],'J':[n,w],'7':[s,w],'F':[s,e],'.':[],'S':[]}
m = (P:=[['.']*len((m:=[[*f".{l.strip()}."] for l in open('10/input.txt')])[0])])+m+P
S = [(i,l.index('S')) for i,l in enumerate(m) if 'S' in l ][0]
C0, C1 = [C for d in [n,e,s,w] if len(ds:=[*map(lambda x:ca(C,x), p[ci(m,C:=cs(S,d))])]) and S in ds]
C = [S, C0]
l = 1

while C[1] != S:
    l += 1
    n = list(p[ci(m,C[1])])
    n.remove(cs(C[0], C[1]))
    n = ca(n[0], C[1])
    C[0] = C[1]
    C[1] = n

print(l/2)