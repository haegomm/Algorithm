def tour(curr, cnt, cost):
    global ans
    if cnt == n and costMap[curr][start] != 0:
        ans = min(ans, cost + costMap[curr][start])
        return
    for nextN in range(n):
        if not visited[nextN] and costMap[curr][nextN] != 0:
            visited[nextN] = True
            tour(nextN, cnt + 1, cost + costMap[curr][nextN])
            visited[nextN] = False


n = int(input())
costMap = [list(map(int, input().split())) for _ in range(n)]
ans = float('inf')

for start in range(n):
    visited = [False] * n
    visited[start] = True
    tour(start, 1, 0)

print(ans)