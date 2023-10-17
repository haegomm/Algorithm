import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
visit = set()

dq = deque()

for i in n_list:
    dq.append((i, 1))
    visit.add(i)

result = 0
now_build = 0
while dq:
    now, b = dq.popleft()
    for d in [1, -1]:
        nx = now + d
        if nx in visit:
            continue
        visit.add(nx)
        result += b
        now_build += 1
        dq.append((nx, b + 1))
        if now_build == k:
            dq = list()
            break
print(result)