strings = open('input.txt').readline().strip().split(',')
total = 0
boxes = [ {} for i in range(256 )]

for string in strings:
    if '=' in string:
        label, flen = string.split('=')
        box = 0
        for char in label: box = ((box + ord(char)) * 17) % 256
        boxes[box][label] = flen
    else:
        label = string[:-1]
        box = 0
        for char in label: box = ((box + ord(char)) * 17) % 256
        if label in boxes[box]: del boxes[box][label]

for i, box in enumerate(boxes): 
    if len(box) == 0: continue
    for j, flen in enumerate(box.values()):
        total += (i+1) * (j+1) * int(flen)

print(total)
