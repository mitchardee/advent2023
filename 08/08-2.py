from collections import defaultdict

lines = open("input.txt").readlines()

l_path = len(lines[0].strip())

nodes = [line.strip().split() for line in lines[2:]]
maps = { n[0]: (n[2][1:-1], n[3][:-1]) for n in nodes }

nodes = list(filter(lambda s: s[-1] == 'A', maps.keys()))
visited = [defaultdict(list) for _ in range(len(nodes))]
cycles = [None] * len(nodes)
print(nodes)
i = 0

while None in cycles:
    for j, node in enumerate(nodes):
        if cycles[j] is None and node[-1] == 'Z':
            if node in visited[j]:
                cycles[j] = i - visited[j][node][0]
            visited[j][node].append(i)
        if lines[0][i % l_path] == 'L':
            nodes[j] = maps[node][0]
        else:
            nodes[j] = maps[node][1]
    i += 1
    # print(nodes, i)

# depends on the fact in this data set that the cycles are 
# all lambda = 0 and are prime multiples of the input directions string
ret = l_path
for c in cycles:
    ret *= (c // l_path)
print (ret)
# for j, v in enumerate(visited):
#     print(j)
#     print(v.items())