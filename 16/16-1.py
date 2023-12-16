lines = open("input.txt").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

# East, North, West, South
energies = [[[0,0,0,0] for _ in range(len(lines[0]))] for _ in range(len(lines))]
dirs = ((0,1),(-1,0),(0,-1),(1,0))
beams = [(0,0,0)]

while beams:
    beam = beams.pop()
    if not (0<=beam[0]<len(lines) and 0<=beam[1]<len(lines[0])) or energies[beam[0]][beam[1]][beam[2]]:
        continue

    energies[beam[0]][beam[1]][beam[2]] = 1

    match lines[beam[0]][beam[1]]:
        case '.':
            dir = dirs[beam[2]]
            beams.append((beam[0] + dir[0], beam[1] + dir[1], beam[2]))
        case '/':
            d = -1
            match beam[2]:
                case 0:
                    d = 1
                case 1:
                    d = 0
                case 2:
                    d = 3
                case 3: 
                    d = 2
            dir = dirs[d]
            beams.append((beam[0] + dir[0], beam[1] + dir[1], d))
        case '\\':
            d = -1
            match beam[2]:
                case 0:
                    d = 3
                case 1:
                    d = 2
                case 2:
                    d = 1
                case 3: 
                    d = 0
            dir = dirs[d]
            beams.append((beam[0] + dir[0], beam[1] + dir[1], d))
        case '|':
            match beam[2]:
                case 0 | 2:
                    beams.append((beam[0] - 1, beam[1], 1))
                    beams.append((beam[0] + 1, beam[1], 3))
                case 1 | 3:
                    dir = dirs[beam[2]]
                    beams.append((beam[0] + dir[0], beam[1] + dir[1], beam[2]))
        case '-':
            match beam[2]:
                case 0 | 2:
                    dir = dirs[beam[2]]
                    beams.append((beam[0] + dir[0], beam[1] + dir[1], beam[2]))
                case 1 | 3:
                    beams.append((beam[0], beam[1] + 1, 0))
                    beams.append((beam[0], beam[1] - 1, 2))

tot = 0
for line in energies:
    for place in line:
        if any(place):
            print('#', end='')
            tot += 1
        else:
            print('.', end = '')
    print()
print(tot)