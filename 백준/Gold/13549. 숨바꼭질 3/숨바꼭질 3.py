import sys
from collections import deque

input = sys.stdin.readline


def bfs(n, k):
    queue = deque([n])
    visited = [-1] * 100001
    visited[n] = 0
    result = float('inf')

    while queue:
        x = queue.popleft()

        if x == k:
            return visited[x]

        for next_x in [(x - 1), (x + 1), (2 * x)]:

            if 0 <= next_x <= 100000 and visited[next_x] == -1:
                if next_x == x * 2:
                    visited[next_x] = visited[x]
                    queue.appendleft(next_x)
                else:
                    visited[next_x] = visited[x] + 1
                    queue.append(next_x)


n, k = map(int, input().split())
if n == k:
    print(0)
else:
    print(bfs(n, k))