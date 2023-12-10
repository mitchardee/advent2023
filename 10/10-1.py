lines = open("input.txt").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

pipes = { '|': [(-1, 0), (1, 0)], '-': [(0, -1), (0, 1)], 'L': [(-1, 0), (0, 1)], 'J': [(-1, 0), (0, -1)], '7': [(0, -1), (1, 0)], 'F': [(1, 0), (0, 1)], '.': [], 'S': [(-1, 0), (1, 0), (0, -1), (0, 1)] }
dists = [[-1] * len(lines[0]) for _ in range(len(lines))]
q = []
for i, line in enumerate(lines):
    if (x := line.find('S')) >= 0:
        q.append((i, x))
        dists[i][x] = 0

farthest = 0

while q:
    p = q.pop(0)
    for dir in pipes[lines[p[0]][p[1]]]:
        # Bounds check
        if 0 <= p[0] + dir[0] < len(lines) and 0 <= p[1] + dir[1] < len(lines[0]):
            # Bi-directionality check
            if dists[p[0]+dir[0]][p[1]+dir[1]] < 0 and (-dir[0], -dir[1]) in pipes[lines[p[0]+dir[0]][p[1]+dir[1]]]:
                dists[p[0]+dir[0]][p[1]+dir[1]] = dists[p[0]][p[1]] + 1
                farthest = max(farthest, dists[p[0]][p[1]] + 1)
                q.append((p[0]+dir[0], p[1]+dir[1]))

# for line in dists:
#     print(line)
print(farthest)