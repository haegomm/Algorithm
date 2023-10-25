from collections import deque

def move():
    board[0][0] = 1
    deq = deque([(0, 0, 1, 1)])

    while deq:
        x, y, k, d = deq.popleft()
        if x == (n-1) and y == (m-1):
            return d
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] and k > 0 and visited[nx][ny] < k - 1:
                    visited[nx][ny] = k - 1
                    deq.append((nx, ny, k - 1, d + 1))
                if not board[nx][ny] and visited[nx][ny] < k:
                    visited[nx][ny] = k
                    deq.append((nx, ny, k, d + 1))
    return -1




n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

print(move())