from collections import deque


def move(i, j):
    global ans
    move = deque([(i, j, k, 0)])

    while move:
        x, y, nk, d = move.popleft()
        if x == (h - 1) and y == (w - 1):
            ans = d
            return
        if nk > 0:
            for dx, dy in [
                (1, 2),
                (1, -2),
                (-1, 2),
                (-1, -2),
                (2, 1),
                (-2, 1),
                (2, -1),
                (-2, -1),
            ]:
                nx = x + dx
                ny = y + dy
                if (
                    0 <= nx < h
                    and 0 <= ny < w
                    and not board[nx][ny]
                    and visited[nx][ny] < nk - 1
                ):
                    visited[nx][ny] = nk - 1
                    move.append((nx, ny, nk - 1, d + 1))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if (
                0 <= nx < h
                and 0 <= ny < w
                and not board[nx][ny]
                and visited[nx][ny] < nk
            ):
                visited[nx][ny] = nk
                move.append((nx, ny, nk, d + 1))


k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
visited = [[-1] * w for _ in range(h)]
visited[0][0] = k  # 시작 위치는 이미 방문한 것으로 처리
ans = -1

move(0, 0)
print(ans)