dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]
    x, y = 0, 0
    direction = 0

    for i in range(1, (n * n) + 1):
        snail[x][y] = i
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < n and 0 <= ny < n and snail[nx][ny] == 0:
            x = nx
            y = ny
        else:
            direction = (direction + 1) % 4
            x += dx[direction]
            y += dy[direction]

    print(f'#{tc}')
    for line in snail:
        print(*line)