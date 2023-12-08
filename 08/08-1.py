lines = open("input.txt").readlines()

nodes = [line.strip().split() for line in lines[2:]]
maps = { n[0]: (n[2][1:-1], n[3][:-1]) for n in nodes }

node = "AAA"
i = 0

while node != "ZZZ":
    if lines[0][i % len(lines[0].strip())] == 'L':
        node = maps[node][0]
    else:
        node = maps[node][1]
    i += 1

print(node, i)