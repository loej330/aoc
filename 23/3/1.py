from enum import Enum
import sys

class T(Enum):
    IGNORE = 1
    DIGIT = 2
    SYMBOL = 3

def get_type(char : str):
    if char == '.': return T.IGNORE
    if char.isdigit(): return T.DIGIT
    return T.SYMBOL

moves = [
    (-1, 1), (0, 1), (1, 1),
    (-1, 0),         (1, 0),
    (-1,-1), (0,-1), (1,-1)]

total = 0
number = ''
found_symbol = False

grid = list(map(str.rstrip, sys.stdin.readlines()))
slack = '.' * (len(grid[0]) + 2)
grid = [slack] + [ '.' + line + '.' for line in grid ] + [slack]

for i in range(1, len(grid)):
    for j in range(1, len(grid)):
        char = grid[i][j]
        if get_type(char) == T.DIGIT:
            number += char
            if not found_symbol:
                for x, y in moves:
                    if get_type(grid[i+y][j+x]) == T.SYMBOL:
                        found_symbol = True
                        break
        else:
            if number != '':
                if found_symbol: 
                    found_symbol = False
                    total += int(number)     
                number = ''

print(total)