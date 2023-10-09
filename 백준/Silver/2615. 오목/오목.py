def gobang(x, y):
    global res
    dol = board[x][y]

    for dx, dy in [(0, 1), (1, 0), (1, 1), (-1, 1)]:
        cnt = 0
        nx, ny = x, y
        while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == dol:
            cnt += 1
            nx += dx
            ny += dy

        if cnt == 5:
            back_x, back_y = x - dx, y - dy
            if 0 <= back_x < 19 and 0 <= back_y < 19 and board[back_x][back_y] == dol:
                continue
            if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == dol:
                continue
            res = dol
            return


board = [list(map(int, input().split())) for _ in range(19)]
res = 0

for i in range(19):
    for j in range(19):
        if board[i][j] != 0:
            gobang(i, j)
            if res:
                print(res)
                print(i + 1, j + 1)
                exit()
else:
    print(res)
