from cmath import inf

lines = open("sample.txt").readlines()
for i in range(len(lines)):
    lines[i] = [int(c) for c in lines[i].strip()]

r = len(lines)
c = len(lines[0])
dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
min_times_v = [[inf]*c for _ in range(r)]
min_times_h = [[inf]*c for _ in range(r)]

# walkers are (row, col, total_cooling, dir)
walkers = [(0,0,0,0), (0,0,0,1)]

while walkers:
    walker = walkers.pop(0)

    for d in (-1, 1):
        dir = (walker[3]+d)%4
        cooling = walker[2]
        for t in range(1, 11):
            x, y = walker[0]+t*dirs[dir][0], walker[1]+t*dirs[dir][1]

            if (not (0 <= x < r and 0 <= y < c)):
                break
            
            cooling += lines[x][y]

            if t > 3:
                if dir%2 == 0:
                    if cooling < min_times_v[x][y]:
                        min_times_v[x][y] = cooling
                        walkers.append((x,y,cooling,dir))

                else:
                    if cooling < min_times_h[x][y]:
                        min_times_h[x][y] = cooling
                        walkers.append((x,y,cooling,dir))


print(min(min_times_h[-1][-1], min_times_v[-1][-1]))