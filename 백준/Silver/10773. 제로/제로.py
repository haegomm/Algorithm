import sys
from collections import deque
input = sys.stdin.readline

nums = deque([])

for _ in range(int(input())):
    num = int(input())
    if num != 0:
        nums.append(num)
    else:
        nums.pop()

print(sum(nums))