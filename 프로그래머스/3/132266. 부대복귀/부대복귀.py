from collections import deque

def bfs(graph, destination, n):
    distance = [-1] * (n + 1)
    queue = deque([destination])
    distance[destination] = 0

    while queue:
        current = queue.popleft()

        for next_node in graph[current]:
            if distance[next_node] == -1:
                distance[next_node] = distance[current] + 1
                queue.append(next_node)

    return distance

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in roads:
        graph[v1].append(v2)
        graph[v2].append(v1)

    distance = bfs(graph, destination, n)
    return [distance[start] for start in sources]