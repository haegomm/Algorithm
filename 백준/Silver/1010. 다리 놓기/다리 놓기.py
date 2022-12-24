import math

for _ in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    print(math.comb(m, n))