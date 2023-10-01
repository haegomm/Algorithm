import sys

input = sys.stdin.readline


def check():
    bingo = 0

    for line in board:
        if sum(line) == 0:
            bingo += 1

    for i in range(5):
        y = 0
        for j in range(5):
            if board[j][i] == 0:
                y += 1
        if y == 5:
            bingo += 1

    d1, d2 = 0, 0
    for i in range(5):
        if board[i][i] == 0:
            d1 += 1
        if board[i][4 - i] == 0:
            d2 += 1
    if d1 == 5:
        bingo += 1
    if d2 == 5:
        bingo += 1

    return bingo


board = [list(map(int, input().split())) for _ in range(5)]
nums = [int(x) for _ in range(5) for x in input().split()]

cnt = 0
for i in range(25):
    for x in range(5):
        for y in range(5):
            if nums[i] == board[x][y]:
                board[x][y] = 0
                cnt += 1

    if cnt >= 12:
        result = check()

        if result >= 3:
            print(i + 1)
            break