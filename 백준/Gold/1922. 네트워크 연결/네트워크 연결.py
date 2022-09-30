def prim(start):
    visited = [False] * (n + 1)
    distance = [inf] * (n + 1)
    distance[start] = 0
    cost= 0

    for _ in range(n):
        min_dist = inf
        for i, dist in enumerate(distance):
            if not visited[i] and dist < min_dist:
                min_node = i
                min_dist = dist

        visited[min_node] = True
        cost += min_dist

        for next_node, dist in graph[min_node]:
            if not visited[next_node] and dist < distance[next_node]:
                distance[next_node] = dist
    return cost


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
inf = 99999999

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

print(prim(1))