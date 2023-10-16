schedule = [0] * 367

for _ in range(int(input())):
    s, e = map(int, input().split())
    schedule[s] += 1
    schedule[e + 1] -= 1

x, y = 0, 0
res = 0

for i in range(1, 367):
    schedule[i] += schedule[i - 1]
    if schedule[i] != 0:
        x += 1
        y = max(y, schedule[i])
    else:
        res += x * y
        x, y = 0, 0

print(res)