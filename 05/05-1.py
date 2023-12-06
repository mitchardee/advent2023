lines = open("input.txt").readlines()

seeds = [int(n) for n in lines[0].split(": ")[1].split()]

maps = []

for line in lines[2:]:
    if(line.strip() == ""):
        continue
    elif(line[0].isalpha()):
        maps.append([])
    else:
        a, b, c = line.split()
        maps[-1].append([int(b), int(a), int(c)])

for i in range(len(maps)):
    maps[i].sort()

for map in maps:
    nextSeeds = []
    for s in seeds:
        f = list(filter(lambda m: m[0] <= s < m[0]+m[2], map))
        nextSeeds.append(f[0][1] + s - f[0][0] if len(f) else s)
    seeds = nextSeeds

print(min(seeds))
        
