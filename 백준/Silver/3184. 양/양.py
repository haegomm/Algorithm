from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    visited[i][j] = True
    queue = deque([(i, j)])
    s, w = 0, 0

    if place[i][j] == 'o':
        s += 1
    elif place[i][j] == 'v':
        w += 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and place[nx][ny] != '#' and not visited[nx][ny]:
                if place[nx][ny] == 'o':
                    s += 1
                elif place[nx][ny] == 'v':
                    w += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    if s > w:
        w = 0
    else:
        s = 0

    return s, w
                

n, m = map(int, input().split())
place = [list(input().strip()) for _ in range(n)]
ans_sheep, ans_wolf = 0, 0
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if place[i][j] != '#' and not visited[i][j]:
            survival_sheep, survival_wolf = bfs(i, j)
            ans_sheep += survival_sheep
            ans_wolf += survival_wolf

print(ans_sheep, ans_wolf)