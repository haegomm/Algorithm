from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0

for i in range(1, n + 1):
    for com in combinations(nums, i):
        if sum(com) == s:
            ans += 1

print(ans)