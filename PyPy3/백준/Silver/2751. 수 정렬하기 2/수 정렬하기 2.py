import sys

input = sys.stdin.readline

n = int(input())
nums = [int(input()) for __ in range(n)]

nums.sort()

print(*nums, sep='\n')