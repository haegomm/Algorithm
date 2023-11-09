import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j):
    
    queue = deque([(i, j)])
    visited[i][j] = True

    puyo = [(i, j)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    puyo.append((nx, ny))
        
    if len(puyo) >= 4:
        boom(puyo)
        return True
    return False



def boom(puyo):
    for px, py in puyo:
        board[px][py] = '.'
    return

def down():
    for j in range(6):
        for i in range(10, -1,  -1):
            for k in range(11, i, -1):
                if board[i][j] != '.' and board[k][j] == '.':
                    board[k][j] = board[i][j]
                    board[i][j] = '.'
    return


board = [list(input().strip()) for _ in range(12)]
ans = 0

while True:
    flag = False
    visited = [[False] * 6 for _ in range(12)]

    for i in range(11, -1, -1):
        for j in range(6):
            if board[i][j] != '.' and not visited[i][j]:
                visited[i][j] = True
                if bfs(i, j):
                    flag = True

    if not flag:
        break

    down()
    ans += 1

print(ans)