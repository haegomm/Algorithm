import sys
input = sys.stdin.readline


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]


def union_parent(a, b):
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
    a_root, b_root = find_set(a), find_set(b)
    if a_root != b_root:
        union_parent(a_root, b_root)
        result.append(cost)

print(sum(result[:-1]))