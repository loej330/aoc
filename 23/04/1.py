import sys
from functools import reduce
print(sum([reduce(lambda s1, s2: int((2**(len([*s1.intersection(s2)])-1))//1), map(lambda x: set(map(int, x.split())), l[9:-1].split('|'))) for l in sys.stdin.readlines()]))