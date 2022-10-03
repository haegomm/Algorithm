dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, 1, -1, -1, 1]


def find_dol(r, c, d):

    for k in range(8):
        nr = r + dx[k]
        nc = c + dy[k]

        while 0 < nr <= n and 0 < nc <= n and board[nr][nc] and board[nr][nc] != d:
            nr += dx[k]
            nc += dy[k]

        if 0 < nr <= n and 0 < nc <= n and board[nr][nc] == d:
            sr = r + dx[k]
            sc = c + dy[k]
            while True:
                if sr == nr and sc == nc:
                    break
                board[sr][sc] = d
                dol_cnt[d] += 1
                dol_cnt[dol[d]] -= 1
                sr += dx[k]
                sc += dy[k]


for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    board = [[0] * (n + 1) for _ in range(n + 1)]
    board[n//2][n//2+1], board[n//2+1][n//2] = 1, 1
    board[n//2][n//2], board[n//2+1][n//2+1] = 2, 2
    dol = [0, 2, 1]
    dol_cnt = [0, 2, 2]

    for _ in range(m):
        col, row, d = map(int, input().split())

        board[row][col] = d
        dol_cnt[d] += 1

        find_dol(row, col, d)

    print(f'#{t}', *dol_cnt[1:])