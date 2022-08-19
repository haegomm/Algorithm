import sys
sys.setrecursionlimit(100000)
def dfs(x, y):
    global cabbge
    visited[x][y] = True
    cabbge += 1  # 배추가 있다..

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and farm[nx][ny] == 1:
            dfs(nx, ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

for tc in range(1, t+1):

    # 가로m 세로n 배추 위치 개수k
    m, n, k = map(int, input().split())

    # 0으로 만들어진 배추밭
    farm = [[0]*m for _ in range(n)]

    # 배추 위치
    for _ in range(k):
        px, py = map(int, input().split())
        farm[py][px] = 1

    # 방문 처리 리스트
    visited = [[False]*m for _ in range(n)]

    # 지렁이 갯수 세기 위한 변수
    worm = []

    # 배추 단지 찾기
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and farm[i][j] == 1:
                cabbge = 0
                dfs(i, j)
                worm.append(cabbge)

    print(len(worm))