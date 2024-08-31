import sys
input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

nums.sort(key= lambda num: (num[0], num[1]))

for num in nums:
    print(*num)