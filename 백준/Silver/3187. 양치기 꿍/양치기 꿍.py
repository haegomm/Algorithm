import sys
sys.setrecursionlimit(10**9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    global wolf, sheep
    if farm[x][y] == 'v':
        wolf += 1
    elif farm[x][y] == 'k':
        sheep += 1
    farm[x][y] = 0

    for d in range(4):
        ny = y + dy[d]
        nx = x + dx[d]
        if 0 <= nx < n and 0 <= ny < m and farm[nx][ny] and farm[nx][ny] != '#':
            dfs(nx, ny)


n, m = map(int, input().split())
farm = [list(input()) for _ in range(n)]
result = [0, 0]

for i in range(n):
    for j in range(m):
        wolf, sheep = 0, 0
        if farm[i][j] != '#' and farm[i][j] != 0:
            dfs(i, j)
            if wolf >= sheep:
                result[1] += wolf
            else:
                result[0] += sheep

print(*result)