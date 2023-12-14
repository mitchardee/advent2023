board = open("input.txt").readlines()

for i in range(len(board)):
    board[i] = list(board[i].strip())

dir = (-1, 0) #North direction, I'm assuming we'll need to do others in part 2

def tilt(board, dir):
    if dir[0] > 0 or dir[1] > 0:
        print("This won't work right, iterate backwards you fool")
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'O':
                x, y = i, j
                while 0 <= x+dir[0] < len(board) and 0 <= y+dir[1] < len(board[0]) and board[x+dir[0]][y+dir[1]] == '.':
                    x += dir[0]
                    y += dir[1]
                board[i][j], board[x][y] = '.', 'O'

def weigh(board):
    tot = 0
    for i, line in enumerate(board[::-1], 1):
        tot += i * line.count('O')
    return tot

for line in board:
    print(''.join(line))

print('tilted')

tilt(board, dir)
for line in board:
    print(''.join(line))
print(weigh(board))