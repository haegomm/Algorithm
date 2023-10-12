import sys, copy
from collections import deque

input = sys.stdin.readline


def bfs():
    global ans
    temp = copy.deepcopy(institute)

    virus = deque([(x, y) for x in range(n) for y in range(m) if temp[x][y] == 2])

    while virus:
        x, y = virus.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus.append((nx, ny))

    safe = 0
    for line in temp:
        safe += line.count(0)
    ans = max(ans, safe)


def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if institute[i][j] == 0:
                institute[i][j] = 1
                makeWall(cnt + 1)
                institute[i][j] = 0


n, m = map(int, input().split())
institute = [list(map(int, input().split())) for _ in range(n)]
ans = 0
makeWall(0)
print(ans)