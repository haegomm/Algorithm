import sys


def canPlaceFence():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "W":
                for k in range(4):
                    x, y = i + dx[k], j + dy[k]

                    if x < 0 or x >= r or y < 0 or y >= c:
                        continue

                    if graph[x][y] == "S":
                        return False
    return True


r, c = map(int, sys.stdin.readline().split())

graph = [list(input().strip()) for _ in range(r)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

if canPlaceFence():
    print(1)
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '.':
                graph[i][j] = "D"
    for row in graph:
        print(''.join(row))
else:
    print(0)