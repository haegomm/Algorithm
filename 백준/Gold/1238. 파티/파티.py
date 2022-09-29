from heapq import heappop, heappush
import sys
input = sys.stdin.readline

students, edge_cnt, house = map(int, input().split())

graph = [[] for _ in range(students + 1)]
for _ in range(edge_cnt):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))


def dijkstra(start, target):
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

    return distance[target]

go_back = [0] * (students + 1)

for student in range(1, students + 1):
    go_back[student] += dijkstra(student, house) + dijkstra(house, student)
    
print(max(go_back))