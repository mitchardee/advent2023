from collections import defaultdict


board = open("sample.txt").readlines()

for i in range(len(board)):
    board[i] = list(board[i].strip())

def tilt(board, dir):
    for i in reversed(range(len(board))) if dir[0]>0 else range(len(board)):
        for j in reversed(range(len(board[0]))) if dir[1]>0 else range(len(board[0])):
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

states = dict()
loop_start = 0
period = 0
target = 1000000000

for i in range(1,target):
    for dir in ((-1, 0), (0,-1), (1,0), (0,1)):
        tilt(board, dir)

    str_board = ''.join([''.join(line) for line in board])

    if str_board in states.keys():
        ind = states[str_board][1]
        period = i-ind
        loop_start = ind
        break
    states[str_board] = (weigh(board), i)

first_target = target - ((target-loop_start)//period)*period

for val in states.values():
    if val[1] == first_target:
        print("Target weight is:\t", val[0], '\nand first occurrs at:\t', val[1], ' cycles')
