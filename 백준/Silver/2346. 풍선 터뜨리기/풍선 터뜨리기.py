n = int(input())
balloon = list(range(1, n + 1))
value = list(map(int, input().split()))
idx = 0
result = []

while balloon:
    move = value[idx]
    result.append(balloon.pop(idx))
    value.pop(idx)
    if balloon:
        if move > 0:
            idx = (idx + move - 1) % len(balloon)
        else:
            idx = (idx + move) % len(balloon)

print(*result)