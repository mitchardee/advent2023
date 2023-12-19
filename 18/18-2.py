lines = open("input.txt").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip().split()[-1]

dirs = [line[-2] for line in lines]
nums = [int(line[2:-2], 16) for line in lines]

compass = {'3': (-1,0), '1': (1,0), '2': (0,-1), '0': (0,1)}

x,y = 0,0
xs = set()
ys = set()

for i, n in enumerate(nums):
    x += n * compass[dirs[i]][0]
    y += n * compass[dirs[i]][1] 
    xs.add(x)
    xs.add(x-1)
    xs.add(x+1)
    ys.add(y)
    ys.add(y-1)
    ys.add(y+1)

xs = sorted(list(xs))
ys = sorted(list(ys))


map = [[-1]*(len(ys)) for _ in range(len(xs))]


x_ind, y_ind = xs.index(0), ys.index(0)
x_val, y_val = 0, 0
map[x_ind][y_ind] = 1

for i, n in enumerate(nums):
    d = compass[dirs[i]]
    x_val += n * d[0]
    y_val += n * d[1]
    x_next, y_next = x_ind, y_ind

    while (xs[x_next], ys[y_next]) != (x_val, y_val):
        x_next += d[0]
        y_next += d[1]
        map[x_next][y_next] = 1

    x_ind, y_ind = x_next, y_next
    

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
            excavated += (xs[i+1]-xs[i]) * (ys[j+1]-ys[j])

print(excavated)