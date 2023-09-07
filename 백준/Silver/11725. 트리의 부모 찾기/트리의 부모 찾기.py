import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find_parent(v):
    check[v] = True

    for next_v in graph[v]:
        if not check[next_v]:
            parent[next_v] = v
            check[next_v] = True
            find_parent(next_v)


n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [[] for _ in range(n + 1)]
check = [False] * (n + 1)

for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

find_parent(1)
print(*parent[2:], sep='\n')