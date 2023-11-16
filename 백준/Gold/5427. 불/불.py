from collections import deque

def bfs():
    global fire
    geun = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    time = 0

    while True:
        if not geun:
            break

        for _ in range(len(fire)):
            fx, fy = fire.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nfx = fx + dx
                nfy = fy + dy
                if 0 <= nfx < n and 0 <= nfy < m and building[nfx][nfy] == '.':
                    building[nfx][nfy] = '*'
                    fire.append((nfx, nfy))
        
        for _ in range(len(geun)):
            x, y = geun.popleft()
            if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                        return time + 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and building[nx][ny] == '.':
                    visited[nx][ny] = True
                    geun.append((nx, ny))
        
        time += 1
    
    return 'IMPOSSIBLE'


for _ in range(int(input())):
    m, n = map(int, input().split())
    building = [list(input()) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    start_x, start_y = 0, 0
    fire = deque([])

    for i in range(n):
        for j in range(m):
            if building[i][j] == '@':
                start_x = i
                start_y = j
            elif building[i][j] == '*':
                fire.append((i, j))
    
    print(bfs())