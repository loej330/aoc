seeds, _, *lines = open('5/input.txt', 'r').readlines() + ['\n']
# seeds, _, *lines = open('5/small-input.txt', 'r').readlines() + ['\n']
seeds = [ *map(int, seeds.strip().split()[1:]) ]
sranges = [ (seeds[i], seeds[i]+seeds[i+1]-1) for i in range(0, len(seeds), 2) ]

while '\n' in lines:
    n = lines.index('\n')
    mapping = []
    for line in lines[1:n]:
        d, s, l = map(int, line.strip().split())
        mapping.append((s, s+l-1, d-s))
    nsranges = []
    for s0, s1 in sranges:
        nsrange = (s0, s1)
        for m0, m1, o in mapping:
            if m0 <= s0 <= m1:
                if m0 <= s1 <= m1: 
                    nsrange = (s0+o, s1+o)
                    break
                else: 
                    nsrange = (s0+o, m1+o)
                    sranges += [(m1+1, s1)]
                    break
            if s0 < m1:
                if m0 <= s1 <= m1:
                    nsrange = (m0+o, s1+o)
                    sranges += [(s0, m0-1)]
                    break
                elif s1 > m1:
                    nsrange = (m0+o, m1+o)
                    sranges += [(s0, m0-1), (m1+1, s1)]
                    break
        nsranges += [nsrange]
    sranges = nsranges

    lines = lines[n+1:]
print(min(sranges)[0])

