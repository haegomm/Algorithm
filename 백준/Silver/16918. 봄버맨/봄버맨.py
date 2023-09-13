import sys

input = sys.stdin.readline


def boom(board):
    temp = [['O'] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if board[x][y] == 'O':
                temp[x][y] = '.'
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < r and 0 <= ny < c:
                        temp[nx][ny] = '.'
    return temp


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c, n = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
time = 1

if n == 1:
    for li in board:
        print(''.join(li))

elif n % 2 == 0:
    for _ in range(r):
        print('O' * c)

elif n % 4 == 3:
    result = boom(board)
    for li in result:
        print(''.join(li))

elif n % 4 == 1:
    result = boom(board)
    result = boom(result)
    for row in result:
        print(''.join(row))