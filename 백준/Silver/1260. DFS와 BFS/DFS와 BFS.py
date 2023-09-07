import sys
from collections import deque

input = sys.stdin.readline


def dfs(v):
    global dfs_result
    dfs_visited[v] = True
    dfs_result.append(v)

    for next_v in graph[v]:
        if not dfs_visited[next_v]:
            dfs(next_v)


def bfs(v):
    global bfs_result
    bfs_visited[v] = True
    bfs_result.append(v)
    queue = deque([v])

    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            if not bfs_visited[next_v]:
                bfs_visited[next_v] = True
                bfs_result.append(next_v)
                queue.append(next_v)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)
dfs_result = []
bfs_result = []

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for temp in graph:
    temp.sort()

dfs(v)
bfs(v)

print(*dfs_result)
print(*bfs_result)