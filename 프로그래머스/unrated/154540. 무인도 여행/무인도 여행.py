import sys
sys.setrecursionlimit(10000)

def solution(maps):

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def bfs(x, y):
        nonlocal survival
        survival += int(maps[x][y])
        maps[x][y] = "X"

        for d in range(4):
            next_x = x + dx[d]
            next_y = y + dy[d]
            if 0 <= next_x < n and 0 <= next_y < m and maps[next_x][next_y] != "X":
                bfs(next_x, next_y)

    answer = []
    n = len(maps)  # 행
    m = len(maps[0])  # 열

    for i in range(len(maps)):
        maps[i] = list(maps[i])

    for i in range(n):
        for j in range(m):
            if maps[i][j] != "X":
                survival = 0
                bfs(i, j)
                answer.append(survival)

    if answer:
        return sorted(answer)

    else:
        return [-1]
