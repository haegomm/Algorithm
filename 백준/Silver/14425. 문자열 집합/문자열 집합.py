import sys

n, m = map(int, sys.stdin.readline().split())
check = []
words = []
cnt = 0

for _ in range(n):
    check.append(sys.stdin.readline().split())

for _ in range(m):
    words.append(sys.stdin.readline().split())

for w in check:
    cnt += words.count(w)

print(cnt)