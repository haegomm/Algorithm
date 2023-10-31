def solve():
    now = 0
    for i in range(n):
        now += distance[i]
        if now > k:
            return i + 1

    for i in range(n - 1, -1, -1):
        now += distance[i]
        if now > k:
            return i + 1

n, k = map(int, input().split())
distance = list(map(int, input().split()))

print(solve())