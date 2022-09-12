t = int(input())

for tc in range(1, t + 1):
    p, q, r, s, w = map(int, input().split())
    a = w * p
    if w < r:
        b = q
    else:
        b = q + ((w - r) * s)
    if a < b:
        print(f"#{tc}", a)
    else:
        print(f"#{tc}", b)