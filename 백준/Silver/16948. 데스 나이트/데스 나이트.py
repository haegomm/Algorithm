from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    board[r1][c1] = 0
    queue = deque([(r1, c1)])

    while queue:
        r, c = queue.popleft()

        if r == r2 and c == c2:
            return board[r][c]

        for nr, nc in [(r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)]:
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == -1:
                board[nr][nc] = board[r][c] + 1
                queue.append((nr, nc))

    return -1

n = int(input())
r1, c1, r2, c2 = map(int, input().split())

board = [[-1]*n for _ in range(n)]

print(bfs())