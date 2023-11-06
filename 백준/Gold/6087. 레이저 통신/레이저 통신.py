from collections import deque

W, H = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

start_end = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == 'C']
start, end = start_end

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visited = [[[float('inf')]*4 for _ in range(W)] for _ in range(H)]

queue = deque()

for d in range(4):
    visited[start[0]][start[1]][d] = 0
    queue.append((start[0], start[1], d, 0))

while queue:
    x, y, dir, mirrors = queue.popleft()
    
    if (x, y) == end:
        continue

    dx, dy = directions[dir]
    nx, ny = x + dx, y + dy

    if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '*':

        if visited[nx][ny][dir] > mirrors:
            visited[nx][ny][dir] = mirrors
            queue.appendleft((nx, ny, dir, mirrors))

        for nd in range(4):
            if nd != dir and visited[nx][ny][nd] > mirrors + 1:
                visited[nx][ny][nd] = mirrors + 1
                queue.append((nx, ny, nd, mirrors + 1))

min_mirrors = min(visited[end[0]][end[1]])

print(min_mirrors)
