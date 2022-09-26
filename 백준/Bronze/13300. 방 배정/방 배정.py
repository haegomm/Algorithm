n, k = map(int, input().split())

w = [0] * 7
m = [0] * 7
cnt = 0

for _ in range(n):
    s, g = map(int, input().split())
    if s == 0:
        w[g] += 1
    else:
        m[g] += 1

for check in w, m:
    for i in range(1, 7):
        if check[i] % k == 0:
            cnt += check[i] // k
        else:
            cnt += check[i] // k + 1

print(cnt)