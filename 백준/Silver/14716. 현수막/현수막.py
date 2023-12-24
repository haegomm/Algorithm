from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    placard[i][j] = 0
    queue = deque([(i, j)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and placard[nx][ny] == 1:
                placard[nx][ny] = 0
                queue.append((nx, ny))


n, m = map(int, input().split())
placard = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if placard[i][j] == 1:
            bfs(i, j)
            ans += 1

print(ans)