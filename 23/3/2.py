from enum import Enum
import sys

g = list(map(str.rstrip, sys.stdin.readlines()))
slack = '.' * (len(g[0]) + 2)
g = [slack] + [ '.' + line + '.' for line in g ] + [slack]

total = 0
for i in range(1, len(g)):
    for j in range(1, len(g[0])):
        if g[i][j] == '*':
            nums = []

            if g[i-1][j].isdigit(): nums += [(i-1, j)]
            else:
                if g[i-1][j-1].isdigit(): nums += [(i-1, j-1)]
                if g[i-1][j+1].isdigit(): nums += [(i-1, j+1)]

            if g[i][j-1].isdigit(): nums += [(i, j-1)]
            if g[i][j+1].isdigit(): nums += [(i, j+1)]

            if g[i+1][j].isdigit(): nums += [(i+1, j)]
            else:
                if g[i+1][j-1].isdigit(): nums += [(i+1, j-1)]
                if g[i+1][j+1].isdigit(): nums += [(i+1, j+1)]

            if len(nums) == 2:
                add = 1
                for ni, nj in nums:
                    num = ''
                    o = 0
                    while g[ni][nj + o].isdigit(): 
                        num = num + g[ni][nj + o] 
                        o += 1
                    o = 1
                    while g[ni][nj - o].isdigit(): 
                        num = g[ni][nj - o] + num
                        o += 1
                    add *= int(num)
                total += add

print(total)