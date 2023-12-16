from collections import deque

def bfs():
    visited[n] = 0
    queue = deque([n])

    while queue:
        now = queue.popleft()

        if now == k:
            return visited[now]

        for move in [now + 1, now - 1, now * 2]:
            if 0 <= move <= 100000 and visited[move] == -1:
                visited[move] = visited[now] + 1
                queue.append(move)
    

n, k = map(int, input().split())
visited = [-1] * 100001

print(bfs())