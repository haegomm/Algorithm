import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def melt_ice():
    melting_points = {}
    for x, y in ice_points:
        cnt = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and polar[nx][ny] == 0:
                cnt += 1
        melting_points[(x, y)] = cnt

    new_ice_points = set()
    for x, y in ice_points:
        polar[x][y] -= melting_points[(x, y)]
        if polar[x][y] < 0:
            polar[x][y] = 0
        elif polar[x][y] > 0:
            new_ice_points.add((x, y))

    return new_ice_points


def dfs(x, y):
    visited[x][y] = True
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if (nx, ny) in ice_points and not visited[nx][ny]:
            dfs(nx, ny)


n, m = map(int, input().split())
polar = [list(map(int, input().split())) for _ in range(n)]

ice_points = {(i, j) for i in range(n) for j in range(m) if polar[i][j] > 0}
time = 0

while True:
    visited = [[False] * m for _ in range(n)]
    components = 0
    for x, y in list(ice_points):
        if not visited[x][y]:
            dfs(x, y)
            components += 1
            if components >= 2:
                print(time)
                exit()
    if not ice_points:
        print(0)
        break

    ice_points = melt_ice()
    time += 1