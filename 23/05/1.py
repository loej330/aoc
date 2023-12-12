seeds, _, *lines = open('5/input.txt', 'r').readlines() + ['\n']
seeds = [ *map(int, seeds.strip().split()[1:]) ]

while '\n' in lines:
    n = lines.index('\n')
    mapping = []
    for line in lines[1:n]:
        d, s, l = map(int, line.strip().split())
        mapping.append((s, s+l, d-s))

    for i, seed in enumerate(seeds):
        for r0, r1, o in mapping:
            if r0 <= seed < r1: 
                seeds[i] += o
                break

    lines = lines[n+1:]

print(min(seeds))