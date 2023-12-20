from collections import deque

def bfs(i, j):
    visited[i][j] = True
    queue = deque([(i, j)])
    soldier = war[i][j]

    cnt = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and war[nx][ny] == soldier:
                visited[nx][ny] = True
                cnt += 1
                queue.append((nx, ny))
    
    return (cnt**2)
    
m, n = map(int, input().split())
war = [input() for _ in range(n)]
visited = [[False]*m for _ in range(n)]

w = 0
b = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if war[i][j] == 'W':
                w += bfs(i, j)
            else:
                b += bfs(i, j)

print(w, b)