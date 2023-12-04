lines = open("sample.txt").readlines()

tot = 0

for line in lines:
    val = 0
    line = line[line.find(':') + 1:]
    ws, nums = line.split('|')
    wins = { int(w.strip()) for w in ws.split() }

    for n in nums.split():
        if n.isdigit() and int(n.strip()) in wins:
            val += 1
    if val:
        tot += 2 ** (val-1)
    

print (tot)