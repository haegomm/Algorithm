import sys
from collections import deque

input = sys.stdin.readline


def dfs(i, j):
    visited[i][j] = True
    deq = deque([(i, j)])
    melt = []

    while deq:
        x, y = deq.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if board[nx][ny] == 1:
                    melt.append((nx, ny))
                    continue
                deq.append((nx, ny))

    for x, y in melt:
        board[x][y] = 0

    return len(melt)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
time = 0
cheese = 0

while True:
    visited = [[False] * m for _ in range(n)]
    melted = dfs(0, 0)
    if melted == 0:
        break
    time += 1
    cheese = melted

print(time)
print(cheese)