lines = open("input.txt").readlines()

maps = [[]]
for line in lines:
    if line.strip() == "":
        maps.append([])
    else:
        maps[-1].append(line.strip())

def hor_symmetry(map):
    for n in range(1, len(map)):
        x = min(len(map)-n, n)
        diffs = 0

        for i in range(x):
            for j in range(len(map[0])):
                if map[n-i-1][j] != map[n+i][j]:
                    diffs += 1
                if diffs > 1:
                    break
                
        if diffs == 1:
            return n
        
    return -1
        
def vert_symmetry(map):
    for n in range(1, len(map[0])):
        x = min(len(map[0])-n, n)
        diffs = 0

        for j,line in enumerate(map):
            for i in range(x):
                if line[n-i-1] != line[n+i]:
                    diffs += 1
                if diffs > 1:
                    break

        if diffs == 1:
            return n
        
    return -1

ret = 0

for map in maps:
    if (v:=vert_symmetry(map)) > 0:
        ret += v
    else:
        ret += 100*(h:=hor_symmetry(map))

print(ret)