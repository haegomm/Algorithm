import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(v, d):
    global result
    visited[v] = True

    if d == 4:
        result = 1
        return

    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v, d + 1)
    visited[v] = False


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n
result = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for now in range(n):
    dfs(now, 0)
    if result == 1:
        break

print(result)