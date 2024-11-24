import sys

nums = list(map(int, sys.stdin.read().split()))
ans = max(nums)

print(ans, nums.index(ans)+1, sep='\n')