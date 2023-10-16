schedule = [0] * 366

for _ in range(int(input())):
    s, e = map(int, input().split())
    for i in range(s, e + 1):
        schedule[i] += 1

x, y = 0, 0
res = 0
for day in range(1, 366):
    if schedule[day] != 0:
        x += 1
        y = max(y, schedule[day])
    else:
        res += x * y
        x, y = 0, 0

res += x * y
print(res)