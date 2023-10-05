n, k = map(int, input().split())
shuffle = [0] + list(map(int, input().split()))
d = [0] + list(map(int, input().split()))

cnt = 0

while cnt < k:
    temp = [0] * (n + 1)
    for idx in range(1, n + 1):
        temp[d[idx]] = shuffle[idx]
    shuffle = temp
    cnt += 1

print(*shuffle[1:])