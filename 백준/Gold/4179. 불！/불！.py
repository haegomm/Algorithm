from collections import deque


def move():
    global hun, escape
    move_fire()
    temp = deque([])
    while hun:
        i, j = hun.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni = i + di
            nj = j + dj
            if (
                0 <= ni < n
                and 0 <= nj < m
                and maze[ni][nj] == '.'
                and not visited[ni][nj]
            ):
                visited[ni][nj] = True
                if ni == 0 or ni == n - 1 or nj == 0 or nj == m - 1:
                    escape = True
                    return
                temp.append([ni, nj])
    hun = temp


def move_fire():
    global fire
    temp = deque([])
    while fire:
        x, y = fire.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '.':
                maze[nx][ny] = 'F'
                temp.append([nx, ny])
    fire = temp


n, m = map(int, input().split())
maze = [list(input().strip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
time = 0
hun = deque()
fire = deque()
escape = False

for i in range(n):
    for j in range(m):
        if maze[i][j] == 'J':
            visited[i][j] = True
            hun.append((i, j))
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                print(1)
                exit()
        elif maze[i][j] == 'F':
            fire.append((i, j))

while True:
    move()
    time += 1
    if escape:
        print(time + 1)
        break
    if not hun:
        print('IMPOSSIBLE')
        break