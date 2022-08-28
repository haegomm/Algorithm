def gobang(i, j):
    global result
    gobang_cnt = 1
    direction = 0
    start_i, start_j = i, j

    while True:
        ni = i + dx[direction]
        nj = j + dy[direction]
        if 0 <= ni < n and 0 <= nj < n and board[ni][nj] == 'o':
            i = ni
            j = nj
            gobang_cnt += 1
            if gobang_cnt == 5:
                result = 'YES'
                break
        else:
            direction += 1
            if direction == 4:
                break
            i = start_i
            j = start_j
            ni = 0
            nj = 0
            gobang_cnt = 1

dx = [0, 1, 1, 1]
dy = [1, 0, 1, -1]

t = int(input())

for tc in range(1, t + 1):

    n = int(input())
    board = list(input() for _ in range(n))
    result = 'NO'

    for i in range(n):
        if result == 'YES':
            break
        for j in range(n):
            if board[i][j] == 'o':
                gobang(i, j)

    print(f'#{tc} {result}')