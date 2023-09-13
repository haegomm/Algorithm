import sys

input = sys.stdin.readline


def boom(x, y):
    temp[x][y] = '.'

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < r and 0 <= ny < c and temp[nx][ny] != '.':
            temp[nx][ny] = '.'


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c, n = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
time = 0

if n % 2 == 0:
    for _ in range(r):
        print('O' * c)
else:
    time = 1
    while time < n:
        temp = [['O'] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    boom(i, j)
        else:
            board = temp
            time += 2
    for row in board:
        print(''.join(row))