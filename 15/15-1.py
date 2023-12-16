from functools import reduce

line = open("sample.txt").readlines()
instructions = line[0].strip().split(',')

def hash(ins):
    val = 0
    for c in ins:
        val += ord(c)
        val *= 17
        val %= 256
    return val

print(reduce(lambda x, y: x + hash(y), instructions, 0))