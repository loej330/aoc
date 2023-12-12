import sys
from functools import reduce; 
l = sys.stdin.readlines()
o = [1] * len(l)
for i in range(len(l)):
    for j in range(i+1, i+1+reduce(lambda s1, s2: int(len([*s1.intersection(s2)])), map(lambda x: set(map(int, x.split())), l[i][9:-1].split('|')))): o[j] += o[i]
print(sum(o))