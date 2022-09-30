from collections import deque
import sys
input = sys.stdin.readline


# 입력값 받아오기
node_cnt, edge_cnt, k = map(int, input().split())

# 그래프 그리기
graph = [[] for _ in range(node_cnt + 1)]
for _ in range(edge_cnt):
    a, b, dist = map(int, input().split())
    graph[a].append((b, dist))

INF = 9999999999
distance = [[INF]*k for _ in range(node_cnt + 1)]


def unlucky_dijkstra():
    distance[1][0] = 0
    check_list = deque([(0, 1)])

    while check_list:
        min_dist, min_node = check_list.popleft()

        for next_node, dist in graph[min_node]:
            next_dist = min_dist + dist

            if next_dist > distance[next_node][-1]:
                continue

            distance[next_node][-1] = next_dist
            distance[next_node].sort()
            check_list.append((next_dist, next_node))


unlucky_dijkstra()

for i in range(1, node_cnt + 1):
    result = distance[i][-1]
    if result == INF:
        print(-1)
    else:
        print(result)