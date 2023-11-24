from collections import deque

def bfs(x, y):
    visited[x][y] = True
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grassland[nx][ny] == '#':
                visited[nx][ny] = True
                queue.append((nx, ny))
    

for _ in range(int(input())):
    n, m = map(int, input().split())
    grassland = [input() for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(m):
            if grassland[i][j] == '#' and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    
    print(cnt)