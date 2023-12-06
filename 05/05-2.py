from math import inf


lines = open("input.txt").readlines()

seeds = [int(n) for n in lines[0].split(": ")[1].split()]
seed_intervals = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]

maps = []

for line in lines[2:]:
    if(line.strip() == ""):
        continue
    elif(line[0].isalpha()):
        maps.append([])
    else:
        a, b, c = line.split()
        maps[-1].append([int(a), int(b), int(c)])

def reverse_map_interval(interval):
    for map in maps[::-1]:
        f = list(filter(lambda m: m[0] <= interval[0] < m[0]+m[2], map))
        t = list(filter(lambda m: interval[0] < m[0] < interval[0] + interval[1], map))
        if f:
            # print("F", f)
            i1 = f[0][1] + interval[0] - f[0][0]
            interval = (i1, min(f[0][1] + f[0][2], i1 + interval[1]) - i1)
        elif t:
            # print("T", t)
            interval = (interval[0], t[0][0] - interval[0])
    return interval

def inter_overlap(i1, i2):
    return 0 < i2[0] - i1[0] < i1[1] or 0 < i1[0] - i2[0] < i2[1]

test_interval = (0, inf)
while(True):
    rm = reverse_map_interval(test_interval)
    l = list(filter(lambda interval: inter_overlap(rm, interval), seed_intervals))
    if l:
        print(test_interval, rm, l)
        print("Answer: ", test_interval[0])
        break
    else:
        # print(test_interval, rm)
        test_interval = (test_interval[0] + rm[1], inf)

# A version that doesn't use intervals runs in under a minute on the input
# def reverse_map_val(val):
#     for map in maps[::-1]:
#         f = list(filter(lambda m: m[0] <= val < m[0]+m[2], map))
#         if f:
#             val += f[0][1] - f[0][0]
#     return val

# def val_overlap(val, interval):
#     return 0 < val - interval[0] < interval[1]

# v = 0
# while(True):
#     rm = reverse_map_val(v)
#     l = list(filter(lambda interval: val_overlap_overlap(rm, interval), seed_intervals))
#     if l:
#         print(v, rm, l)
#         break
#     else:
#         v += 1