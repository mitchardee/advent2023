from cmath import inf
from collections import defaultdict
from operator import gt, lt

lines = open("input.txt").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

works = lines[:lines.index('')]
# Each list element will follow (<x,m,a, or s as an index>, <lt or gt>, compare_value, destination)
workflows = defaultdict(list)
letters = {'x':0, 'm':1, 'a':2, 's':3}

for w in works:
    name = w[:w.index('{')]
    criteria = w[w.index('{')+1:-1].split(',')

    for criterion in criteria[:-1]:
        c = criterion.split(':')
        val = int(c[0][2:])
        if c[0][1] == '>':
            workflows[name].append((letters[c[0][0]], gt, val, c[1]))
        else:
            workflows[name].append((letters[c[0][0]], lt, val, c[1]))

    # Remove unnecessary rules
    for wf in reversed(workflows[name]):
        if wf[3] == criteria[-1]:
            workflows[name].pop()
        else:
            break
    
    # Base case will always evaluate to true
    workflows[name].append((0, lt, inf, criteria[-1]))

tot = 0

intervals = [[(1,4000), (1,4000), (1,4000), (1,4000), 'in']]
while intervals:
    interval = intervals.pop()
    
    wf_name = interval[-1]

    while wf_name !='A' and wf_name != 'R':
        for p in workflows[wf_name]:
            if p[1](interval[p[0]][0], p[2]):
                # Crack the interval into two if necessary
                if p[1] == lt and interval[p[0]][1] >= p[2]:
                    split = [*interval]
                    split[-1] = wf_name
                    split[p[0]] = (p[2], split[p[0]][1])
                    # print(split)
                    intervals.append(split)
                    interval[p[0]] = (interval[p[0]][0], p[2]-1)
                wf_name = p[3]
                break
            else:
                if p[1] == gt and interval[p[0]][1] > p[2]:
                    split = [*interval]
                    split[-1] = wf_name
                    split[p[0]] = (p[2]+1, split[p[0]][1])
                    # print(split)
                    intervals.append(split)
                    interval[p[0]] = (interval[p[0]][0], p[2])

    
    if wf_name == 'A':
        a = 1
        for v in interval[:-1]:
            a *= v[1] - v[0] + 1
        tot += a


print(tot)