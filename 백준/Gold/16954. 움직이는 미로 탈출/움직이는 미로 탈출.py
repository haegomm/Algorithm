from collections import deque


def move():
    global wall
    visited = set()
    deq = deque([(7, 0)])

    while deq:
        for _ in range(len(deq)):
            x, y = deq.popleft()
            if x == 0:
                return 1
            if (x, y) in wall:
                continue
            for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < 8 and 0 <= ny < 8 and not (nx, ny) in wall and not (nx, ny) in visited:
                    visited.add((nx, ny))
                    deq.append((nx, ny))
        temp = set()
        if wall:
            visited = set()
        for wx, wy in wall:
            if wx < 7:
                temp.add((wx+1, wy))
        wall = temp
    return 0


maze = [list(input().strip()) for _ in range(8)]
wall = set()

for i in range(8):
    for j in range(8):
        if maze[i][j] == '#':
            wall.add((i, j))

print(move())