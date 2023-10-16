def check_win(mal):
    for i in range(3):
        if all(board[i][j] == mal for j in range(3)) or all(
            board[j][i] == mal for j in range(3)
        ):
            return True
        if (
            board[0][0] == board[1][1] == board[2][2] == mal
            or board[0][2] == board[1][1] == board[2][0] == mal
        ):
            return True
    return False


while True:
    words = input().strip()
    if words == 'end':
        break

    x_cnt = words.count('X')
    o_cnt = words.count('O')
    board = [list(words[i * 3 : i * 3 + 3]) for i in range(3)]

    x_win = check_win('X')
    o_win = check_win('O')

    if x_cnt < o_cnt or x_cnt > o_cnt + 1:
        print('invalid')
    elif (
        (x_win and x_cnt != o_cnt + 1)
        or (o_win and x_cnt != o_cnt)
        or (x_win and o_win)
    ):
        print('invalid')
    elif not x_win and not o_win and x_cnt + o_cnt != 9:
        print('invalid')
    else:
        print('valid')