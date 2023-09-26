import sys
from collections import deque

input = sys.stdin.readline


def save():
    gram = 10001
    visited[0][0] = 1
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        if (x, y) == (n - 1, m - 1):
            return min(visited[x][y] - 1, gram)
        elif maze[x][y] == 2:
            gram = visited[x][y] - 1 + (n - 1 - x) + (m - 1 - y)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if maze[x][y] == 0 or maze[x][y] == 2:
                    visited[nx][ny] = visited[x][y] + 1
                    if visited[nx][ny] > t:
                        return gram
                    queue.append((nx, ny))
    return gram


n, m, t = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

result = save()
if result > t:
    print('Fail')
else:
    print(result)