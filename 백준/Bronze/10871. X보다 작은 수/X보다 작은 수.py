n, x = map(int, input().split())
nums = list(map(int, input().split()))
result = []

for i in range(n):
    if nums[i] < x:
        result.append(nums[i])

print(*result, sep=' ')