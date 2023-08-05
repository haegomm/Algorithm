import sys

n, m = map(int, sys.stdin.readline().strip().split())
check = set()
cnt = 0

for _ in range(n):
    check.add(sys.stdin.readline().strip())

for _ in range(m):
    word = sys.stdin.readline().strip()
    if word in check:
        cnt += 1

print(cnt)