lines = open("input.txt").readlines()

tot = 0
nums = []

for i, line in enumerate(lines):

    cur = 0
    curlen = 0

    for j, c in enumerate(line):
        if c.isdigit():
            cur *= 10
            cur += int(c)
            curlen += 1

        if cur and (not c.isdigit()):

            nums.append((i, j-curlen, cur, curlen))
            
            cur = 0
            curlen = 0

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '*':
            filtered = list(filter(lambda num: (i-1 <= num[0] <= i+1) and (num[1]-1 <= j <= num[1]+num[3]), nums))
            # print(i, j, filtered)
            if len(filtered) == 2:
                tot += filtered[0][2] * filtered[1][2]


    
print (tot)