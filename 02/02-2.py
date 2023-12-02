lines = open("input.txt").readlines()

tot = 0

for line in lines:
    green = 0
    blue = 0
    red = 0

    line = line[line.index(':') + 1:]
    games = line.split(';')

    for game in games:
        show = game.split(',')
        for g in show:
            if "blue" in g:
                blue = max(int(g.split(' ')[1]), blue)
            if "green" in g:
                green = max(int(g.split(' ')[1]), green)
            if "red" in g:
                red = max(int(g.split(' ')[1]), red)

    
    tot += blue * green * red

print(tot)


