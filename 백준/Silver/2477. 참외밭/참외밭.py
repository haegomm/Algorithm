m = int(input())
arr = []

for i in range(6):
    d, v = map(int, input().split())
    arr.append(v)

big = 0
small = 0

for i in range(6):
    tmp = arr[i] * arr[(i + 1) % 6]
    if big < tmp:
        big = tmp
        idx = i

small = arr[(idx + 3) % 6] * arr[(idx + 4) % 6]

print(m * (big - small))