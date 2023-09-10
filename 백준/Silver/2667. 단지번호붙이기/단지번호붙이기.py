import sys

input = sys.stdin.readline


def dfs(x, y):
    global total
    visited[x][y] = True
    total += 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == 1:
            dfs(nx, ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input().strip())
arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
result = []

for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j] == 1:
            total = 0
            dfs(i, j)
            result.append(total)

result.sort()

print(len(result))
print(*result, sep='\n')