lines = open("input.txt").readlines()

tot = 0

def sy(c):
    return (not c.isdigit()) and (c != '.') and (c != '\n')

for i, line in enumerate(lines):

    cur = 0
    curlen = 0

    for j, c in enumerate(line):
        if c.isdigit():
            cur *= 10
            cur += int(c)
            curlen += 1

        if cur and (not c.isdigit()):

            symbol = sy(c)
            
            for k in range(max(j - curlen - 1, 0), min(j+1, len(line))):
                if i > 0:
                    symbol |= sy(lines[i-1][k])
                if i < len(lines)-1:
                    symbol |= sy(lines[i+1][k])

            if j > curlen:
                symbol |= sy(lines[i][j-curlen-1])
            
            if symbol:
                tot += cur
            
            cur = 0
            curlen = 0

    
print (tot)