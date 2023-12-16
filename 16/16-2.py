lines = open("input.txt").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

def energize(init):
    # East, North, West, South
    energies = [[[0,0,0,0] for _ in range(len(lines[0]))] for _ in range(len(lines))]
    dirs = ((0,1),(-1,0),(0,-1),(1,0))
    beams = [init]

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
                tot += 1

    return tot

max_tot = -1

for i in range(len(lines)):
    max_tot = max(max_tot, energize((i, 0, 0)), energize((i, len(lines[0]) - 1, 2)))
for i in range(len(lines[0])):
    max_tot = max(max_tot, energize((0, i, 3)), energize((len(lines) - 1, i, 1)))
print(max_tot)