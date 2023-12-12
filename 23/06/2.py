t, d = map(lambda x: int("".join(x.split()[1:])), open('6/input.txt').readlines())
print(((-t-(t**2-4*d)**0.5)/-2-1).__ceil__() - ((-t+(t**2-4*d)**0.5)/-2+1).__floor__() + 1)