from collections import deque

def bfs(i, j):
    queue = deque([(i, j)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and screen[nx][ny] == 255:
                queue.append((nx, ny))
                screen[nx][ny] = 0



n, m = map(int, input().split())
pixel = [list(map(int, input().split())) for _ in range(n)]
t = int(input())
screen = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(0, m*3, 3):
        if sum(pixel[i][j:j+3])//3 >= t:
            screen[i][j//3] = 255

ans = 0
for i in range(n):
    for j in range(m):
        if screen[i][j] == 255:
            bfs(i, j)
            ans += 1

print(ans)