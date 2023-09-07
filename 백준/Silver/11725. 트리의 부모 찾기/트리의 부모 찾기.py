import sys
from collections import deque

input = sys.stdin.readline

def find_parent(v):
    queue = deque([v])
    while queue:
        current = queue.popleft()
        for next_v in graph[current]:
            if parent[next_v] == 0:
                parent[next_v] = current
                queue.append(next_v)

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

find_parent(1)
print(*parent[2:], sep='\n')