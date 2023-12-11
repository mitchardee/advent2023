lines = open("input.txt").readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

stars = []
for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        if ch == '#':
            stars.append((i, j))

rows = [1000000 if ''.join(line) == ('.' * len(line)) else 1 for line in lines]

cols = []
for i in range(len(lines[0])):
    blank = True
    for line in lines:
        blank &= (line[i] == '.')
    cols.append(1000000 if blank else 1)

ret = 0
for i, star in enumerate(stars):
    for star2 in stars[i+1:]:
        ret += sum(rows[min(star[0],star2[0]): max(star[0],star2[0])]) + sum(cols[min(star[1], star2[1]): max(star[1], star2[1])])

print(ret)