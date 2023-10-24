from collections import deque


def move():
    global wall
    visited = [[False] * 8 for _ in range(8)]
    deq = deque([(7, 0)])

    while deq:
        for _ in range(len(deq)):
            x, y = deq.popleft()
            visited[x][y] = False
            if x == 0:
                return 1
            if maze[x][y] == '#':
                continue
            for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < 8 and 0 <= ny < 8 and not visited[nx][ny] and maze[nx][ny] == '.':
                    visited[nx][ny] = True
                    deq.append((nx, ny))
        temp = []
        for wx, wy in wall[::-1]:
            maze[wx][wy] = '.'
            nwx = wx + 1
            if nwx == 8:
                continue
            maze[nwx][wy] = '#'
            temp.append((nwx, wy))
        wall = temp[::-1]
        for wx, wy in wall:
            visited[wx][wy] = False
    return 0


maze = [list(input().strip()) for _ in range(8)]
wall = []

for i in range(8):
    for j in range(8):
        if maze[i][j] == '#':
            wall.append((i, j))

print(move())