from collections import deque

def bfs():
    ans = 0
    while shark:
        x, y = shark.popleft()
        for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and sea[nx][ny] != 1:
                visited[nx][ny] = True
                sea[nx][ny] = sea[x][y] + 1
                shark.append((nx, ny))
                ans = max(ans, sea[nx][ny])

    return ans - 1


n, m = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)]
shark = deque([])
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if sea[i][j] == 1:
            visited[i][j] = True
            shark.append((i,j))

print(bfs())