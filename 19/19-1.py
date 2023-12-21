from cmath import inf
from collections import defaultdict
from operator import gt, lt

lines = open("input.txt").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

works = lines[:lines.index('')]
# Each list element will follow (<x,m,a, or s>, <lt or gt>, compare_value, destination)
workflows = defaultdict(list)
xmas = lines[lines.index('')+1:]

for w in works:
    name = w[:w.index('{')]
    criteria = w[w.index('{')+1:-1].split(',')

    for criterion in criteria[:-1]:
        c = criterion.split(':')
        workflows[name].append((c[0][0], gt if c[0][1] == '>' else lt, int(c[0][2:]), c[1]))
    # Base case will always evaluate to true
    workflows[name].append(('a', lt, inf, criteria[-1]))

for i, line in enumerate(xmas):
    xmas[i] = {s[0]:int(s[s.index('=')+1:]) for s in line[1:-1].split(',')}

tot = 0
for xm in xmas:
    wf_name = 'in'
    while wf_name not in ('A', 'R'):
        for p in workflows[wf_name]:
            if p[1](xm[p[0]], p[2]):
                wf_name = p[3]
                break

    if wf_name == 'A':
        tot += sum(xm.values())

print(tot)