from collections import deque


def bfs(x, y):
    global ans
    arr[x][y] = 1
    deq = deque([(x, y)])

    while deq:
        x, y = deq.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                if nx == n - 1:
                    ans = 'YES'
                    return
                arr[nx][ny] = 1
                deq.append((nx, ny))


n, m = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]
ans = 'NO'

for j in range(m):
    if arr[0][j] == 0:
        bfs(0, j)
        if ans == 'YES':
            print(ans)
            exit()

print(ans)