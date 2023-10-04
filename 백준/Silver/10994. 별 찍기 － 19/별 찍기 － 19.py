def draw(n, x, y):
    if n == 1:
        stars[x][y] = '*'
        return

    lens = (4 * n) - 3
    for i in range(lens):
        stars[y][x + i] = '*'
        stars[y + i][x] = '*'
        stars[y + lens - 1][x + i] = '*'
        stars[y + i][x + lens - 1] = '*'

    draw(n - 1, x + 2, y + 2)


N = int(input())
lens = 4 * N - 3
stars = [[' '] * lens for _ in range(lens)]

draw(N, 0, 0)
for s in stars:
    print(''.join(s))