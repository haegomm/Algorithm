def rotate_matrix_layer(x1, y1, x2, y2, r):
    queue = []
    x, y = x1, y1
    while x < x2:
        queue.append(arr[x][y])
        x += 1
    x, y = x2, y1
    while y < y2:
        queue.append(arr[x][y])
        y += 1
    x, y = x2, y2
    while x > x1:
        queue.append(arr[x][y])
        x -= 1
    x, y = x1, y2
    while y > y1:
        queue.append(arr[x][y])
        y -= 1

    r %= len(queue)
    queue = queue[-r:] + queue[:-r]

    idx = 0
    x, y = x1, y1
    while x < x2:
        new[x][y] = queue[idx]
        idx += 1
        x += 1
    x, y = x2, y1
    while y < y2:
        new[x][y] = queue[idx]
        idx += 1
        y += 1
    x, y = x2, y2
    while x > x1:
        new[x][y] = queue[idx]
        idx += 1
        x -= 1
    x, y = x1, y2
    while y > y1:
        new[x][y] = queue[idx]
        idx += 1
        y -= 1


n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
new = [[0] * m for _ in range(n)]

for i in range(0, min(n, m) // 2):
    x1, y1 = i, i
    x2, y2 = n - i - 1, m - i - 1
    rotate_matrix_layer(x1, y1, x2, y2, r)

for line in new:
    print(*line)