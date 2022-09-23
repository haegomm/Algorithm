# 우상, 우하, 좌하 좌상
d_r = [-1, 1, 1, -1]
d_c = [1, 1, -1, -1]

# 회전했을때 다음 방향 r_d: [다음방향]
d_sheet = {
    1: [1, 2, 3, 0],
    -1: [3, 0, 1, 2],
}


def tour(row, col, direction, rotate_cnt=0, memo=tuple([0])):
    '''
    :param direction: 현재 진행 방향
    :param r_d: 회전하는 방향(rotate_direction), 시계방향인지 반시계방향인지
    :param rotate_cnt: 방향 회전한 횟수
    :param memo: 이동경로 메모메모
    '''
    global result

    # 나 여기 등장
    here = board[row][col]

    # @@ 종료조건 @@
    # 여기가 출발점이고, memo가 1보다 크다 == 투어 다녀 왔다
    if (row, col) == start_rc and len(memo) > 1:
        eat = len(memo) - 1
        if eat > result:
            result = eat
            # print(memo)
        return
    # 여기 디저트가 memo에 있다면 버려!, 왔던길 더가는거 방지도 가능
    if here in memo:
        return

    memo = *memo, here

    # @@ tour @@
    next_r = row + d_r[direction]
    next_c = col + d_c[direction]

    # 범위 벗어나는 경우? 버리기
    if next_r < 0 or next_r >= board_size or next_c < 0 or next_c >= board_size:
        return

    # 가장자리에 도착할 경우: 방향 회전
    if (rotate_cnt < 3) and (next_r == board_size - 1 or next_c == board_size - 1):
        tour(next_r, next_c, d_sheet[1]
             [direction], rotate_cnt + 1, memo)
    # 다 아니면 그냥 가던방향 유지, 회전하기
    else:
        tour(next_r, next_c, direction, rotate_cnt, memo)
        if rotate_cnt < 3:
            tour(next_r, next_c, d_sheet[1]
                 [direction], rotate_cnt + 1, memo)


for case in range(1, int(input()) + 1):
    board_size = int(input())
    board = [list(map(int, input().split())) for _ in range(board_size)]

    board[0][0] = board[0][board_size - 1] = board[board_size -
                                                   1][0] = board[board_size - 1][board_size - 1] = 0

    result = -1
    for row in range(board_size):
        for col in range(board_size):
            start_rc = (row, col)
            for direction in range(4):
                tour(row, col, direction)

    print(f'#{case} {result}')
