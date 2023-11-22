from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, k):
    if n == k:
        return 0, [n]

    queue = deque([n])
    visited = [False] * 100001
    visited[n] = True
    parents = [-1] * 100001

    while queue:
        x = queue.popleft()

        for next_x in [(2 * x), (x - 1), (x + 1)]:
            if 0 <= next_x <= 100000 and not visited[next_x]:
                visited[next_x] = True
                parents[next_x] = x
                if next_x == k:
                    route = []
                    while next_x != -1:
                        route.append(next_x)
                        next_x = parents[next_x]
                    return len(route) - 1, route[::-1]
                queue.append(next_x)

n, k = map(int, input().split())
time, route = bfs(n, k)

print(time)
print(*route)