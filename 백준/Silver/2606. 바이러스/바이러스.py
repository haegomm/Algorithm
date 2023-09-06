import sys
from collections import deque


def bfs(v):
    result = 0
    infected[v] = True
    queue = deque([v])

    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            if not infected[next_v]:
                infected[next_v] = True
                result += 1
                queue.append(next_v)

    return result


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n + 1)]
infected = [False] * (n + 1)

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(bfs(1))