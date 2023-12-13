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
        # print(map[n-x:n], map[n+x-1:n-1:-1])
        if map[n-x:n] == map[n+x-1:n-1:-1]:
            return n
    return -1
        
def vert_symmetry(map):
    for n in range(1, len(map[0])):
        x = min(len(map[0])-n, n)
        # print(x, n)
        good = True
        for line in map:
            # print(line[n-x:n],'|',  line[n+x-1: n-1:-1])
            good &= line[n-x:n] == line[n+x-1:n-1:-1]
            if not good:
                break
        if good:
            return n
    return -1

ret = 0
for map in maps:
    if (v:=vert_symmetry(map)) > 0:
        ret += v
    else:
        ret += 100*hor_symmetry(map)
print(ret)