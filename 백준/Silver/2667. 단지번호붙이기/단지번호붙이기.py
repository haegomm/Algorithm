import sys

input = sys.stdin.readline


def dfs(x, y):
    global total
    arr[x][y] = 0
    total += 1

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]:
            dfs(nx, ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input().strip())
arr = [list(map(int, input().strip())) for _ in range(n)]
result = []

for i in range(n):
    for j in range(n):
        if arr[i][j]:
            total = 0
            dfs(i, j)
            result.append(total)

result.sort()

print(len(result))
print(*result, sep='\n')