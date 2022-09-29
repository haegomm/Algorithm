import sys
from heapq import heappop, heappush

input = sys.stdin.readline

node_cnt, edge_cnt = map(int, input().split())
start = int(input())

INF = 999999999
distance = [INF] * (node_cnt + 1)

graph = [[] for _ in range(node_cnt + 1)]
for _ in range(edge_cnt):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]    

    while heap:
        min_dist, min_node = heappop(heap)

        if min_dist > distance[min_node]:
            continue

        for next_node, dist in graph[min_node]:
            new_dist = min_dist + dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heappush(heap, (new_dist, next_node))

dijkstra(start)

for d in distance[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)