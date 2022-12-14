from heapq import heappop, heappush
import sys
input = sys.stdin.readline

students, edge_cnt, house = map(int, input().split())

graph = [[] for _ in range(students + 1)]
graph_reverse = [[] for _ in range(students + 1)]
for _ in range(edge_cnt):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph_reverse[e].append((s, w))

def dijkstra(start, graph):
    INF = 99999999999
    distance = [INF] * (students + 1)
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        min_dist, min_node = heappop(heap)


        if min_dist > distance[min_node]:
            continue

        for next_node, weight in graph[min_node]:
            new_dist = weight + min_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))

    return distance

go = dijkstra(house, graph)
back = dijkstra(house, graph_reverse)

result = 0
for student in range(1, students + 1):
    time = go[student] + back[student]
    if time > result:
        result = time

print(result)