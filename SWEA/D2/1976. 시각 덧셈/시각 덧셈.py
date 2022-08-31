t = int(input())

for tc in range(1, t+1):
    h1, m1, h2, m2 = list(map(int, input().split()))

    h = h1 + h2
    m = m1 + m2

    if h > 12:
        h = h - 12

    if m == 60:
        h += 1
        m = 0

    elif m > 60:
        h += 1
        m = m - 60

    print(f'#{tc}', h, m)