def check(x, y):
    cnt = 0
    for dx, dy in [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1),
    ]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and mine[nx][ny] == '*':
            cnt += 1
    return cnt


def boom(x, y):
    global flag
    player[x][y] = '*'
    for i in range(n):
        for j in range(n):
            if mine[i][j] == '*':
                player[i][j] = '*'


n = int(input())
mine = [list(input()) for _ in range(n)]
player = [list(input()) for _ in range(n)]
flag = False

for i in range(n):
    for j in range(n):
        if player[i][j] == 'x':
            if mine[i][j] != '*':
                player[i][j] = check(i, j)
            else:
                if not flag:
                    boom(i, j)
                    flag = True

for line in player:
    print(''.join(map(str, line)))