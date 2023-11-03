from collections import deque

def bfs(i,  j):
    global cheese
    visited[i][j] = True
    deq = deque([(i, j)])
    candidate = []

    while deq:
        x, y = deq.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if cheese[nx][ny] == 1:
                    candidate.append((nx, ny))
                    continue
                deq.append((nx, ny))
    
    melt = check(candidate)
    for mx, my in melt:
        cheese[mx][my] = 0

    return len(melt)

def check(candidate):
    ok = []
    
    for x, y in candidate:
        air = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] and cheese[nx][ny] == 0:
                air += 1
                if air >= 2:
                    ok.append((x, y))
                    break
    return ok


n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]
time = 0

while True:
    visited = [[False] * m for _ in range(n)]
    melted = bfs(0, 0)
    if melted == 0:
        print(time)
        break
    time += 1