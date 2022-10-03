def lets_go_find_box(x, y):
    row = x
    col = y

    while True:
        if row < n and arr[row][y]:
            row += 1
        else:
            break

    while True:
        if col < n and arr[x][col]:
            col += 1
        else:
            break

    x_box = row - x
    y_box = col - y
    result.append([x_box, y_box])

    for ci in range(x, row):
        for cj in range(y, col):
            arr[ci][cj] = 0


for t in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = []

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                lets_go_find_box(i, j)

    result.sort(key=lambda x: (x[0] * x[1], x[0]))
    print(f'#{t} {len(result)}', end=' ')
    for line in result:
        print(*line, end=' ')
    print()