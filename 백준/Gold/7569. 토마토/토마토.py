import sys
from collections import deque


def bfs(queue):
    while queue:
        x, y, z = queue.popleft()

        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and boxes[nx][ny][nz] == 0:
                boxes[nx][ny][nz] = boxes[x][y][z] + 1
                queue.append((nx, ny, nz))


input = sys.stdin.readline

m, n, h = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
queue = deque()

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 1:
                queue.append((i, j, k))

bfs(queue)

ans = -2
unripe = False

for box in boxes:
    for line in box:
        for tomato in line:
            if tomato == 0:
                unripe = True
                break
            ans = max(ans, tomato)

if unripe:
    print(-1)
elif ans == 1:
    print(0)
else:
    print(ans - 1)