import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    deq = deque([(sx, sy, 0)])

    while deq:
        x, y, dist = deq.popleft()
        if x == ex and y == ey:
            return dist
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx <= n - box_x
                and 0 <= ny <= m - box_y
                and not visited[nx][ny]
            ):
                x1, y1 = nx, ny
                x2, y2 = nx + box_x - 1, ny + box_y - 1

                if prefix_sum[x2][y2] - (prefix_sum[x2][y1-1] if y1 > 0 else 0) - (prefix_sum[x1-1][y2] if x1 > 0 else 0) + (prefix_sum[x1-1][y1-1] if x1 > 0 and y1 > 0 else 0) == 0:
                    visited[nx][ny] = True
                    deq.append((nx, ny, dist + 1))
    return -1

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
box_x, box_y, sx, sy, ex, ey = map(int, input().split())
sx -= 1
sy -= 1
ex -= 1
ey -= 1

prefix_sum = [[0] * m for _ in range(n)]
prefix_sum[0][0] = board[0][0]
for i in range(1, n):
    prefix_sum[i][0] = prefix_sum[i-1][0] + board[i][0]
for j in range(1, m):
    prefix_sum[0][j] = prefix_sum[0][j-1] + board[0][j]
for i in range(1, n):
    for j in range(1, m):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + board[i][j]

print(bfs())
