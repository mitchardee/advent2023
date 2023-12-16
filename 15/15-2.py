from functools import reduce

line = open("input.txt").readlines()
instructions = line[0].strip().split(',')

boxes = [[] for _ in range(256)]

def hash(ins):
    val = 0
    for c in ins:
        val += ord(c)
        val *= 17
        val %= 256
    return val


for ins in instructions:
    if '-' in ins:
        has = hash(ins[:-1])
        for i, val in enumerate(boxes[has]):
            if val[:-2] == ins[:-1]:
                boxes[has].pop(i)
                break
    else:
        has = hash(ins[:-2])
        placed = False
        for i, val in enumerate(boxes[has]):
            if val[:-2] == ins[:-2]:
                boxes[has][i] = ins
                placed = True
                break
        if not placed:
            boxes[has].append(ins)

tot = 0

for i, box in enumerate(boxes, 1):
    for j, val in enumerate(box, 1):
        tot += i * j * int(val[-1])

print(tot)