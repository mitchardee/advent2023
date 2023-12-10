lines = open("input.txt").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

pipes = { '|': [(-1, 0), (1, 0)], '-': [(0, -1), (0, 1)], 'L': [(-1, 0), (0, 1)], 'J': [(-1, 0), (0, -1)], '7': [(0, -1), (1, 0)], 'F': [(1, 0), (0, 1)], '.': [], 'S': [(-1, 0), (1, 0), (0, -1), (0, 1)] }
dists = [[-1] * len(lines[0]) for _ in range(len(lines))]
q = []
for i, line in enumerate(lines):
    if (x := line.find('S')) >= 0:
        q.append((i, x))
        dists[i][x] = 1

while q:
    p = q.pop(0)
    for dir in pipes[lines[p[0]][p[1]]]:
        # Bounds check
        if 0 <= p[0] + dir[0] < len(lines) and 0 <= p[1] + dir[1] < len(lines[0]):
            # Bi-directionality check
            if dists[p[0]+dir[0]][p[1]+dir[1]] < 0 and (-dir[0], -dir[1]) in pipes[lines[p[0]+dir[0]][p[1]+dir[1]]]:
                dists[p[0]+dir[0]][p[1]+dir[1]] = 1
                q.append((p[0]+dir[0], p[1]+dir[1]))

# 0 will be the insides, -1 will be the outsides, 1 will be the pipes
spacious = [[0] * 2*len(lines[0]) for _ in range(2*len(lines))]

for i, line in enumerate(dists):
    for j, val in enumerate(line):
        if val == 1:
            spacious[i*2][j*2] = 1
            for dir in pipes[lines[i][j]]:
                spacious[i*2 + dir[0]][j*2 + dir[1]] = 1
for i in range(len(spacious)):
    for p in ((i,0), (i,len(spacious[0])-1)):
        if spacious[p[0]][p[1]] == 0:
            spacious[p[0]][p[1]] = -1
            q.append(p)
for i in range(len(spacious[0])):
    for p in ((0,i), (len(spacious)-1,i)):
        if spacious[p[0]][p[1]] == 0:
            spacious[p[0]][p[1]] = -1
            q.append(p)

while q:
    p = q.pop()
    for dir in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        x = p[0]+dir[0]
        y = p[1]+dir[1]
        if 0 <= x < len(spacious) and 0 <= y < len(spacious[0]) and spacious[x][y] == 0:
            spacious[x][y] = -1
            q.append((x, y))
ret = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if spacious[i*2][j*2] == 0 and spacious[i*2+1][j*2] == 0 and spacious[i*2][j*2+1] == 0 and spacious[i*2+1][j*2+1] == 0:
            ret += 1
            dists[i][j] = 0

# for line in dists:
#     for x in line:
#         print(x, '\t', end='')
#     print()
# for line in spacious:
#     for x in line:
#         print(x, '\t', end='')
#     print()
print (ret)


    

