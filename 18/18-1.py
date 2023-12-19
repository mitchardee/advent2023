lines = open("input.txt").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip().split()

dirs = [line[0] for line in lines]
nums = [int(line[1]) for line in lines]

compass = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}

min_x, min_y, max_x, max_y = 0,0,0,0
x,y = 0,0

for i, n in enumerate(nums):
    x += n * compass[dirs[i]][0]
    y += n * compass[dirs[i]][1] 
    min_x, min_y, max_x, max_y = min(min_x, x), min(min_y, y), max(max_x, x), max(max_y, y)

map = [[-1]*(max_y - min_y + 3) for _ in range(max_x - min_x + 3)]

x,y = -min_x+1,-min_y+1
map[x][y] = 1
for i, n in enumerate(nums):
    for j in range(n):
        x += compass[dirs[i]][0]
        y += compass[dirs[i]][1]
        map[x][y] = 1

q = [(0,0)]
while q:
    p = q.pop()
    for dir in compass.values():
        x = p[0] + dir[0]
        y = p[1] + dir[1]

        if not (0 <= x < len(map) and 0 <= y < len(map[0])) or map[x][y] != -1:
            continue
        map[x][y] = 0
        q.append((x,y))


excavated = 0
for i, line in enumerate(map):
    for j, v in enumerate(line):
        if v:
            excavated += 1

print(excavated)