from collections import deque

def bfs():
    visited[my_x-1][my_y-1] = True
    queue = deque([(my_x-1, my_y-1, 0)])
    found = set()

    while queue:
        x, y, d = queue.popleft()

        if (x, y) in rival and (x, y) not in found:
            ans[rival.index((x, y))] = d
            found.add((x, y))
            if len(found) == len(rival):
                break

        for nx, ny in [(x-2,y-1), (x-2,y+1), (x-1,y-2), (x-1,y+2), (x+1,y-2), (x+1,y+2), (x+2,y-1), (x+2,y+1)]:
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, d+1))

n, m = map(int, input().split())
my_x, my_y = map(int, input().split())
rival = []
ans = [0] * m
visited = [[False]*n for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    rival.append((x-1, y-1))

bfs()

print(*ans)
