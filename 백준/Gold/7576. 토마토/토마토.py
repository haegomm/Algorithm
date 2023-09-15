import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    while tomato:
        x, y = tomato.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not box[nx][ny]:
                box[nx][ny] = box[x][y] + 1
                tomato.append([nx, ny])


m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
days = 0
tomato = deque([])


for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            tomato.append([i, j])

bfs()

for line in box:
    empty = line.count(0)
    if empty:
        print(-1)
        break
    else:
        days = max(days, max(line))
else:
    print(days - 1)