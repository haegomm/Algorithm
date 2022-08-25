def bfs(x, y):
    global find_end
    visited[x][y] = True  # 지나온 곳 표시하기. 돌아가지 않게
    queue = [(x, y)]

    while queue:
        x, y = queue.pop(0)  # 출발~~
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny] and maze[nx][ny] != 1:
                if maze[nx][ny] == 3:
                    find_end = 1
                    break
                visited[nx][ny] = True
                queue.append((nx, ny))

    return


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for _ in range(10):

    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]  # 미로
    visited = [[False] * 16 for _ in range(16)]
    find_end = 0

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                bfs(i, j)

    print(f'#{tc} {find_end}')