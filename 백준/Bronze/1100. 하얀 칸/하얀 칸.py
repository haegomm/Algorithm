board = [list(input()) for _ in range(8)]

white_cnt = 0
for i in range(8):
    for j in range(8):
        if board[i][j] == 'F':
            if (i % 2 == 0) and (j % 2 == 0):
                white_cnt += 1
            elif (i % 2 == 1) and (j % 2 == 1):
                white_cnt += 1
            else:
                continue

print(white_cnt)