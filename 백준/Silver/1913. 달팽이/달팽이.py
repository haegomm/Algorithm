dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
k = int(input())

snail = [[0]*n for _ in range(n)]
x, y = 0, 0
direction = 0
result_x, result_y = 0, 0

for i in range(n*n, 0, -1):
    snail[x][y] = i
    if i == k:
        result_x, result_y = x, y
    nx = x + dx[direction]
    ny = y + dy[direction]

    if (0 <= nx < n) and (0 <= ny < n) and (snail[nx][ny] == 0):
        x, y = nx, ny
    else:
        direction = (direction + 1) % 4
        x += dx[direction]
        y += dy[direction]

for line in snail:
    print(*line)

print(result_x + 1, result_y + 1)