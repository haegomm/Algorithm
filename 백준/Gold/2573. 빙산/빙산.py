import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def bfs():
    melt = {}
    for x, y in ice:
        cnt = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and polar[nx][ny] == 0:
                cnt += 1
        melt[(x, y)] = cnt

    new = []
    for x, y in ice:
        polar[x][y] -= melt[(x, y)]
        if polar[x][y] <= 0:
            polar[x][y] = 0
            continue
        new.append((x, y))

    return new


def dfs(x, y):
    visited[x][y] = True
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and polar[nx][ny] != 0:
            dfs(nx, ny)


n, m = map(int, input().split())
polar = [list(map(int, input().split())) for _ in range(n)]
time = 0
ice = []

for i in range(n):
    for j in range(m):
        if polar[i][j] != 0:
            ice.append((i, j))

while True:
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i, j in ice:
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1
            if cnt >= 2:
                print(time)
                exit()

    ice = bfs()
    if not ice:
        print(0)
        break

    time += 1