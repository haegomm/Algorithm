nums = list(map(int, input().split()))
for i in range(5):
    nums[i] = nums[i] ** 2

print(sum(nums) % 10)