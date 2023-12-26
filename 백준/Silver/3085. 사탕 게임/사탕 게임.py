def check():
    cnt = 1

    for i in range(n):
        temp = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                temp += 1
                cnt = max(cnt, temp)
            else:
                temp = 1

    for j in range(n):
        temp = 1
        for i in range(1, n):
            if board[i][j] == board[i - 1][j]:
                temp += 1
                cnt = max(cnt, temp)
            else:
                temp = 1
    
    return cnt


n = int(input().strip())
board = [list(input()) for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            ans = max(ans, check())
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        if i + 1 < n:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            ans = max(ans, check())
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(ans)