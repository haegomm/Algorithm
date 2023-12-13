from collections import deque

def bfs():
    visited[start[0]][start[1]] = 0
    queue = deque([(start[0], start[1])])

    while queue:
        x, y = queue.popleft()
        if [x, y] == target:
            return visited[x][y]

        for dx, dy in [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

for _ in range(int(input())):
    n = int(input())
    start = list(map(int, input().split()))
    target = list(map(int, input().split()))
    visited = [[-1] * n for _ in range(n)]

    print(bfs())