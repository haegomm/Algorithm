from heapq import heappop, heappush
import sys
input = sys.stdin.readline

# 정점, 간선 개수 입력
node_cnt, edge_cnt = map(int, input().split())

# graph생성, 정점의 번호는 1 ~ node_cnt 까지, 양방향
graph = [[] for _ in range(node_cnt + 1)]
for _ in range(edge_cnt):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))
    graph[b].append((a, dist))

# 반드시 지나야할 정점의 번호 v1, v2
v1, v2 = map(int, input().split())

'''
두가지 경로가 있다. 
start -> v1 -> v2 -> end, 
start -> v2 -> v1 -> end
다익스트라로 v1 부터 나머지로, v2 부터 나머지로 최소거리를 구하고 위 경우를 확인해보자!
'''
INF = 1000 * 801
distance_12 = [INF] * (node_cnt + 1)
distance_21 = [INF] * (node_cnt + 1)


def dijkstra(start, distance):
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


dijkstra(v1, distance_12)
dijkstra(v2, distance_21)

d_1_v1 = distance_12[1]
d_v1_v2 = distance_12[v2]
d_v2_n = distance_21[node_cnt]
d_1_v2 = distance_21[1]
d_v1_n = distance_12[node_cnt]

if d_1_v1 < INF and d_v1_v2 < INF and d_v2_n < INF:
    way1 = d_1_v1 + d_v1_v2 + d_v2_n
else:
    way1 = -1

if d_1_v2 < INF and d_v1_v2 < INF and d_v1_n < INF:
    way2 = d_1_v2 + d_v1_v2 + d_v1_n
else:
    way2 = -1

print(min(way1, way2))