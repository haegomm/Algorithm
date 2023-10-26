from collections import deque, defaultdict

def bfs(x, y):
    visited[x][y] = group
    deq = deque([(x, y)])
    cnt = 1

    while deq:
        x, y = deq.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny] == 1:
                visited[nx][ny] = group
                cnt += 1
                deq.append((nx, ny))
    
    return cnt


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
ones = defaultdict(int)

group = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            c = bfs(i, j)
            ones[group] = c
            group += 1

ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            adjacent = set()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni = i + di
                nj = j + dj
                if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and visited[ni][nj] not in adjacent:
                    adjacent.add(visited[ni][nj])
            res = 1
            for num in adjacent:
                res += ones[num]
            ans = max(res, ans)
print(ans)