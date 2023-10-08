n, m = map(int, input().split())
train = [[0] * 20 for _ in range(n)]

for _ in range(m):
    command = list(map(int, input().split()))
    num = command[1] - 1
    if len(command) == 3:
        seat = command[2] - 1
    if command[0] == 1:
        if not train[num][seat]:
            train[num][seat] = 1
    elif command[0] == 2:
        if train[num][seat]:
            train[num][seat] = 0
    elif command[0] == 3:
        temp = [0] + train[num][:19]
        train[num] = temp
    elif command[0] == 4:
        temp = train[num][1:] + [0]
        train[num] = temp

res = {tuple(line) for line in train}
print(len(res))