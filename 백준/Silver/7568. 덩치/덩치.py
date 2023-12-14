n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
ans = [1] * n

for i in range(n):
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            ans[i] += 1

print(*ans)