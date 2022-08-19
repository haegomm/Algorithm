import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    global island
    visited[x][y] = True

    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and island_map[nx][ny] == 1:
            dfs(nx, ny)


# 상, 하, 좌, 우, 좌상향, 우상향, 좌하향, 우하향
dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

# 케이스 반복
while True:
    # w 너비 h 높이
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    # 섬의 지도
    island_map = [list(map(int, input().split())) for _ in range(h)]

    # 방문 처리 리스트
    visited = [[False]*w for _ in range(h)]

    # 섬의 갯수
    island = 0

    # 섬 위치 찾기
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and island_map[i][j] == 1:
                island += 1
                dfs(i, j)

    print(island)