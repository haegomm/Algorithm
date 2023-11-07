from collections import deque

def bfs():
    global water
    queue = deque([start])

    while queue:
        
        temp = []
        for wx, wy in water:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nwx = wx + dx
                nwy = wy + dy
                if 0 <= nwx < n and 0 <= nwy < m and forest[nwx][nwy] == '.':
                    forest[nwx][nwy] = '*'
                    temp.append((nwx, nwy))
        water = temp

        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and forest[nx][ny] != '*' and forest[nx][ny] != 'X':
                    if (nx, ny) == end:
                        return visited[x][y] + 1
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    
    return 'KAKTUS'


n, m = map(int, input().split())
forest = [list(input().strip()) for _ in range(n)]
water = deque([])
visited = [[0]*m for _ in range(n)]
start = 0
end = 0

for i in range(n):
    for j in range(m):
        if forest[i][j] == 'S':
            start = (i, j)
        elif forest[i][j] == 'D':
            end = (i, j)
        elif forest[i][j] == '*':
            water.append((i, j))

print(bfs())