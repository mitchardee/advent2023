lines = open("input.txt").readlines()

n = 0
tot = 0

for line in lines:
    possible = True
    n+=1

    line = line[line.index(':') + 1:]
    games = line.split(';')

    for game in games:
        show = game.split(',')
        for g in show:
            lim = 0
            if "blue" in g:
                lim = 14
            if "green" in g:
                lim = 13
            if "red" in g:
                lim = 12

            if int(g.split(' ')[1]) > lim:
                possible = False
    
    if possible:
        tot += n

print(tot)


