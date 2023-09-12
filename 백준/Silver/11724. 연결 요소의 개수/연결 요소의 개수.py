import sys

input = sys.stdin.readline


def dfs(v):
    check[v] = True
    stack = [v]

    while stack:
        current_v = stack.pop()
        for next_v in graph[current_v]:
            if not check[next_v]:
                check[next_v] = True
                stack.append(next_v)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
check = [False] * (n + 1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

result = 0
for i in range(1, n + 1):
    if not check[i]:
        dfs(i)
        result += 1

print(result)