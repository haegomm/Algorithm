from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline

def bfs(comb):
    visited = [[-1] * n for _ in range(n)]
    deq = deque([])
    for x, y in comb:
        visited[x][y] = 0
        deq.append((x, y))
    
    while deq:
        x, y = deq.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and institute[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                deq.append((nx, ny))
    
    temp = 0
    for i in range(n):
            for j in range(n):
                if institute[i][j] == 0:
                    if visited[i][j] == -1:
                        return float('inf')
                    temp = max(temp, visited[i][j])
    return temp


n, m = map(int, input().split())
institute = [list(map(int, input().split())) for _ in range(n)]
virus = []
ans = float('inf')

for i in range(n):
    for j in range(n):
        if institute[i][j] == 2:
            virus.append((i, j))

for comb in combinations(virus, m):
    time = bfs(comb)
    ans = min(ans, time)

if ans == float('inf'):
    print(-1)
else:
    print(ans)