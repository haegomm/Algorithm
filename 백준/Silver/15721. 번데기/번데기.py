people = int(input())
t = int(input())
target = int(input())
bundegi = []
bun = degi = 1
cnt = 0

while True:
    pre = bun
    cnt += 1

    for _ in range(2):
        bundegi.append((bun, 0))
        bun += 1
        bundegi.append((degi, 1))
        degi += 1
    for _ in range(cnt+1):
        bundegi.append((bun, 0))
        bun += 1
    for _ in range(cnt+1):
        bundegi.append((degi, 1))
        degi += 1
    
    if pre < t <= bun:
        print(bundegi.index((t, target)) % people)
        break