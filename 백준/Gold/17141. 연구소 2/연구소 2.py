from itertools import combinations
from collections import deque

def bfs(virus_comb):
    visited = [[-1]*n for _ in range(n)]
    queue = deque([])

    for vx, vy in virus_comb:
        visited[vx][vy] = 0
        queue.append((vx, vy))

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and institute[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    
    temp = 0
    for i in range(n):
        for j in range(n):
            if institute[i][j] != 1:
                if visited[i][j] == -1:
                    return float('inf')
                else:
                    temp = max(temp, visited[i][j])
    return temp


n, m = map(int, input().split())
institute = [list(map(int, input().split())) for _ in range(n)]
ans = float('inf')
virus = []

for i in range(n):
    for j in range(n):
        if institute[i][j] == 2:
            virus.append((i, j))

for comb in combinations(virus, m):
    ans = min(ans, bfs(comb))

if ans == float('inf'):
    print(-1)
else:
    print(ans)