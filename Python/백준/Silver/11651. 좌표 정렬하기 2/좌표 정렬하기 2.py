import sys
input = sys.stdin.readline

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

nums.sort(key= lambda num: (num[1], num[0]))

for num in nums:
    print(*num)