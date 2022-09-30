import sys
input = sys.stdin.readline

def find_set(parent, x):
    if parent[x] != x:
        parent[x] = find_set(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_set(parent, a)
    b = find_set(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


node_cnt, edge_cnt = map(int, input().split())
graph = list()
for _ in range(edge_cnt):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

graph.sort()
parent = list(range(node_cnt + 1))
result = []
for cost, a, b in graph:
    if find_set(parent, a) != find_set(parent, b):
        union_parent(parent, a, b)
        result.append(cost)

print(sum(result[:-1]))