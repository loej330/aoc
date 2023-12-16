strings = open('input.txt').readline().strip().split(',')
total = 0

for string in strings:
    current = 0
    for char in string: current = ((current + ord(char)) * 17) % 256
    total += current

print(total)