ans = set()

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            ans.add((i, j))

print(len(ans))