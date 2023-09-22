import sys
from collections import deque

input = sys.stdin.readline


def bfs(x, y):
    queue = deque()
    union = []
    queue.append((i, j))
    union.append((i, j))

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if (
                0 <= nx < n
                and 0 <= ny < n
                and l <= abs(countries[x][y] - countries[nx][ny]) <= r
                and not visited[nx][ny]
            ):
                visited[nx][ny] = 1
                queue.append((nx, ny))
                union.append((nx, ny))
    return union


n, l, r = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]

days = 0
while True:
    visited = [[0] * n for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                move = bfs(i, j)

                if len(move) > 1:
                    flag = 1
                    people = sum(countries[x][y] for x, y in move) // len(move)
                    for x, y in move:
                        countries[x][y] = people
    if flag == 0:
        print(days)
        break
    days += 1