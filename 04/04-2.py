lines = open("input.txt").readlines()

copies = [1] * len(lines)

for i, line in enumerate(lines):
    val = 0
    line = line[line.find(':') + 1:]
    ws, nums = line.split('|')
    wins = { int(w.strip()) for w in ws.split() }

    for n in nums.split():
        if n.isdigit() and int(n.strip()) in wins:
            val += 1
    
    for j in range(val):
        copies[i + j + 1] += copies[i]
    

print (sum(copies))