from collections import deque

def bfs():
    visited[n] = 0
    queue = deque([n])

    while queue:
        now = queue.popleft()
        if now == m:
            return visited[now]

        for next_n in [now + 1, now - 1, now + a, now - a, now - b, now + b, now * a, now * b]:
            if 0 <= next_n <= 100000 and visited[next_n] == -1:
                visited[next_n] = visited[now] + 1
                queue.append(next_n)


a, b, n, m = map(int, input().split())
visited = [-1] * 100001

print(bfs())