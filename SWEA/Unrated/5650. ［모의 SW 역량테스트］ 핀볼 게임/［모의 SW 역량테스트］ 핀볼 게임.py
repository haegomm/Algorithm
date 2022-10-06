dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
wh = {6, 7, 8, 9, 10}

def pinball(x, y):
    global max_score

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        score = 0

        while 0 <= nx < n and 0 <= ny < n and board[nx][ny] != -1 and (nx, ny) != (x, y):
            # print(nx, ny, x, y, d)
            # if nx == 0 or ny == 0 or nx == (n - 1) or ny == (n - 1) or board[nx][ny] == 5:

            if board[nx][ny] == 5:
                score *= 2
                score += 1
                break
                
            elif board[nx][ny] in wh:
                breaker = False
                for i in range(n):
                    if breaker:
                        break
                    for j in range(n):
                        if board[i][j] == board[nx][ny] and (i, j) != (nx, ny):
                            nx = i
                            ny = j
                            breaker = True
                            break

            elif board[nx][ny] in {1, 2, 3, 4}:
                d = block[board[nx][ny]][d]
                score += 1

            nx += dx[d]
            ny += dy[d]
            
        if not (0 <= nx < n and 0 <= ny < n):
            score *= 2
            score += 1
            
        if max_score < score:
            max_score = score


for t in range(1, int(input()) + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    block = [[], [1, 3, 0, 2], [3, 0, 1, 2], [2, 0, 3, 1], [1, 2, 3, 0]]
    max_score = 0
    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                pinball(i, j)

    print(f'#{t} {max_score}')