import sys

input = sys.stdin.readline

n, m = map(int, input().split())
check = set()
cnt = 0

for _ in range(n):
    check.add(input().strip())

for _ in range(m):
    if input().strip() in check:
        cnt += 1

print(cnt)