def command(num, l, r):
    if num == 1:
        bulbs[l] = r
    else:
        for k in range(l, r + 1):
            if num == 2:
                bulbs[k] = int(not bulbs[k])
            elif num == 3:
                bulbs[k] = 0
            elif num == 4:
                bulbs[k] = 1


n, m = map(int, input().split())
bulbs = [0] + list(map(int, input().split()))

for _ in range(m):
    a, b, c = map(int, input().split())
    command(a, b, c)

print(*bulbs[1:])