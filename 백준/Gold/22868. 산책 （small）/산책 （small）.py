from collections import deque

def bfs(start, end, exclude):
    deq = deque([start])
    visited = [False] * (n + 1)
    path = [[] for _ in range(n + 1)]
    path[start] = [start]
    visited[start] = True

    for ex in exclude:
        visited[ex] = True

    while deq:
        now = deq.popleft()
        path.append(now)
        for next_v in route[now]:
            if not visited[next_v]:
                visited[next_v] = True
                path[next_v] = path[now] + [next_v]
                if next_v == end:
                    return path[next_v], len(path[next_v]) - 1
                deq.append(next_v)
    return [], 0


n, m = map(int, input().split())
route = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    route[v1].append(v2)
    route[v2].append(v1)

for r in route:
    r.sort()

s, e = map(int, input().split())

path1, d1 = bfs(s, e, [])
path2, d2 = bfs(e, s, path1[1:])

print(d1+d2)