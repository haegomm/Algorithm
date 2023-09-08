import sys
from collections import deque

input = sys.stdin.readline


def bfs(v):
    cnt = 1
    infected = [0] * (n + 1)
    infected[v] = 1
    queue = deque([v])

    while queue:
        v = queue.popleft()
        for next in graph[v]:
            if not infected[next]:
                infected[next] = 1
                cnt += 1
                queue.append(next)
    return cnt


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
maxCnt = 1
ans = []

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v2].append(v1)

for i in range(1, n + 1):
    cnt = bfs(i)
    if cnt > maxCnt:
        maxCnt = cnt
        ans.clear()
        ans.append(i)
    elif cnt == maxCnt:
        ans.append(i)

print(*ans)