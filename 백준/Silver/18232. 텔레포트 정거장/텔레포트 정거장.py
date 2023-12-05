from collections import deque

def bfs():
    visited[s] = True
    queue = deque([(s, 0)])

    while queue:
        v, time = queue.popleft()
        
        nxt = [v + 1, v - 1]
        if graph[v]:
            nxt += graph[v]

        for next_v in nxt:
            if next_v == e:
                return time + 1
            if 1 <= next_v <= n and not visited[next_v]:
                visited[next_v] = True
                queue.append((next_v, time + 1))


n, m = map(int, input().split())
s, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs())