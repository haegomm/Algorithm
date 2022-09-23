t = int(input())

dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, 1, -1, -1, 1]

dol = [0, 2, 1]
dol_cnt = [0, 2, 2]
for tc in range(1, t+1):
    n, m = map(int, input().split())
    board = [[0] * (n + 1) for _ in range(n+1)]
    board[n // 2][n // 2 + 1], board[n // 2 + 1][n // 2] = 1, 1
    board[n//2][n//2], board[n//2+1][n//2+1] = 2, 2              
    find = False
    b = 2
    w = 2

    for _ in range(m):
        s_col, s_row, d = map(int, input().split())

        e_row = s_row
        e_col = s_col
        f_row = s_row
        f_col = s_col

        board[s_row][s_col] = d
        if d == 1:
            b += 1
        else:
            w += 1

        k = 0
        while k <= 7:
            n_row = e_row + dx[k]
            n_col = e_col + dy[k]
            if 1 <= n_row <= n and 1 <= n_col <= n and board[n_row][n_col] == dol[d]:
                e_row = n_row
                e_col = n_col
                find = True

            elif 1 <= n_row <= n and 1 <= n_col <= n and board[n_row][n_col] == d and find:

                while True:
                    f_row += dx[k]
                    f_col += dy[k]
                    board[f_row][f_col] = d
                    if d == 1:
                        b += 1
                        w -= 1
                    else:
                        b -= 1
                        w += 1
                    if f_row == e_row and f_col == e_col:
                        k += 1
                        e_row, e_col = s_row, s_col
                        find = False
                        f_row, f_col = s_row, s_col
                        break
            else:
                k += 1
                e_row, e_col = s_row, s_col
                find = False

    print(f'#{tc} {b} {w}')