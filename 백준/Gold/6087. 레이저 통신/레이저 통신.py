from collections import deque

def bfs():
    deq = deque() # (x, y, 방향, 거울 갯수)

    # 초기 방향 설정
    for d in range(4):
        visited[start[0]][start[1]][d] = 0
        deq.append((start[0], start[1], d, 0))

    while deq:
        x, y, dir, cnt = deq.popleft()

        if [x, y] == end:
            return cnt

        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != '*':

            # 직진하는 경우
            if visited[nx][ny][dir] > cnt:
                visited[nx][ny][dir] = cnt
                deq.appendleft((nx, ny, dir, cnt))

            # 방향 전환하는 경우
            for nd in range(4):
                if nd != dir and visited[nx][ny][nd] > cnt + 1:
                    visited[nx][ny][nd] = cnt + 1
                    deq.append((nx, ny, nd, cnt + 1))
        
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[[float('inf')] * 4 for _ in range(m)] for _ in range(n)]
start = []
end = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'C':
            if not start:
                start = [i, j]
                continue
            end = [i, j]

print(bfs())