ca = lambda c0, c1: (c0[0]+c1[0],c0[1]+c1[1])
cs = lambda c0, c1: (c0[0]-c1[0],c0[1]-c1[1])
ci = lambda m, c: m[c[0]][c[1]]

n,e,s,w = [(-1,0),(0,1),(1,0),(0,-1)]
p = {'|':[n,s],'-':[e,w],'L':[n,e],'J':[n,w],'7':[s,w],'F':[s,e],'.':[],'S':[]}
m = (P:=[['.']*len((m:=[[*f".{l.strip()}."] for l in open('10/input.txt')])[0])])+m+P
S = [(i,l.index('S')) for i, l in enumerate(m) if 'S' in l ][0]
C0, C1 = [C for d in [n,e,s,w] if len(ds:=[*map(lambda x:ca(C,x), p[ci(m,C:=cs(S,d))])]) and S in ds]
C = [S, C0]

for char, fromto in p.items():
    if cs(C0, S) in fromto and cs(C1, S) in fromto: m[S[0]][S[1]] = char

l = [ [False] * len(m[0]) for _ in range(len(m)) ]
while C[1] != S:
    l[C[0][0]][C[0][1]] = True 
    n = list(p[ci(m,C[1])])
    n.remove(cs(C[0], C[1]))
    n = ca(n[0], C[1])
    C[0] = C[1]
    C[1] = n
l[C[0][0]][C[0][1]] = True 

total = 0 
for i in range(len(m)):
    inside = False; border = False; b0 = ' '
    for j in range(1,len(m[0])):
        n = m[i][j]; looppiece = l[i][j]
        if border: 
            if n == '7': 
                if b0 == 'L': inside = not inside
                border = False
            elif n == 'J': 
                if b0 == 'F': inside = not inside
                border = False
        elif looppiece:
            if n in ['F', 'L']: border = True; b0 = n
            elif n == '|': inside = not inside 
        elif inside: total += 1

print(total)