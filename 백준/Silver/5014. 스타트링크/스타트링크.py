from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    visited[s] = 0
    queue = deque([s])

    while queue:
        now = queue.popleft()

        if now == g:
            return visited[now]

        for move in [now + u, now - d]:
            if 1 <= move <= f and visited[move] == -1:
                visited[move] = visited[now] + 1
                queue.append(move)
                
    return "use the stairs"

f, s, g, u, d = map(int, input().split())
visited = [-1] * (f+1)

print(bfs())