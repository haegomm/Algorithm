import sys
from collections import deque

input = sys.stdin.readline


def dfs(v, depth):
    if v == p2:
        return depth

    check[v] = True

    for next_v in family[v]:
        if not check[next_v]:
            result = dfs(next_v, depth + 1)
            if result != -1:
                return result
    return -1


n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
family = [[] for _ in range(n + 1)]
check = [False] * (n + 1)

for _ in range(m):
    v1, v2 = map(int, input().split())
    family[v1].append(v2)
    family[v2].append(v1)

print(dfs(p1, 0))