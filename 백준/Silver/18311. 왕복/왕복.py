n, k = map(int, input().split())
distance = list(map(int, input().split()))
go = [0]
back = []

temp = 0
for d in distance:
    temp += d
    go.append(temp)

for d in distance[::-1]:
    temp += d
    back.append(temp)

flag = False
while True:
    if not flag:
        for i in range(n - 1):
            if go[i] <= k < go[i + 1]:
                print(i + 1)
                exit()
        else:
            flag = True
    else:
        for i in range(n - 1):
            if back[i] < k <= back[i + 1]:
                print((n-1) - i)
                break
        break