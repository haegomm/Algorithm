import copy
import sys
sys.setrecursionlimit(10**9)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y, c):
    arr[x][y] = 0

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == c:
            dfs(nx, ny, c)


def dfs_rg(x, y, c):
    arr2[x][y] = 0

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n:
            if c == 'R':
                if arr2[nx][ny] == c or arr2[nx][ny] == 'G':
                    dfs_rg(nx, ny, c)

            elif c == 'G':
                if arr2[nx][ny] == c or arr2[nx][ny] == 'R':
                    dfs_rg(nx, ny, c)

            else:
                if arr2[nx][ny] == c:
                    dfs_rg(nx, ny, c)


n = int(input())
arr = [list(map(str, input())) for _ in range(n)]
arr2 = copy.deepcopy(arr)
cnt = 0
cnt_rg = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 'R' or arr[i][j] == 'B' or arr[i][j] == 'G':
            dfs(i, j, arr[i][j])
            cnt += 1

        if arr2[i][j] == 'R' or arr2[i][j] == 'B' or arr2[i][j] == 'G':
            dfs_rg(i, j, arr2[i][j])
            cnt_rg += 1

print(cnt, cnt_rg)