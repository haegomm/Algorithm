import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    queue = deque([(x, y)])
    distance[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if (
                0 <= nx < n
                and 0 <= ny < m
                and board[nx][ny] == 1
                and distance[nx][ny] == -1
            ):
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
distance = []

for row in board:
    new_row = []
    for cell in row:
        if cell != 0:
            new_row.append(-1)
        else:
            new_row.append(0)
    distance.append(new_row)

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            gx, gy = i, j
            break

bfs(gx, gy)

for line in distance:
    print(*line)