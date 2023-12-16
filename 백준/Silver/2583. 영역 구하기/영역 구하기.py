from collections import deque

def bfs(i, j):
    board[i][j] = 1
    queue = deque([(i, j)])
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                board[nx][ny] = 1
                queue.append((nx, ny))
                cnt += 1

    return cnt


n, m, k = map(int, input().split())
board = [[0] * m for _ in range(n)]

for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            if board[i][j] == 0:
                board[i][j] = 1

cnt = 0
section = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            section.append(bfs(i, j))
            cnt += 1

print(cnt)
print(*sorted(section))