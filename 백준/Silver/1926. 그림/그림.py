from collections import deque

def bfs(i, j):
    paper[i][j] = 0
    queue = deque([(i, j)])
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and paper[nx][ny] == 1:
                paper[nx][ny] = 0
                cnt += 1
                queue.append((nx, ny))

    return cnt


n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

drawing_cnt = 0
max_wide = 0

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1:
            temp_wide = bfs(i, j)
            max_wide = max(max_wide, temp_wide)
            drawing_cnt += 1

print(drawing_cnt)
print(max_wide)
