def dfs(v):
    visited[v] = True

    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)


t = int(input())

for tc in range(1, t+1):

    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    total = 0

    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    for i in range(1, n+1):
        if not visited[i]:
            total += 1
            dfs(i)

    print(f'#{tc} {total}')
