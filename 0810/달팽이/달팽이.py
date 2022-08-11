# t = int(input())
#
# for tc in range(1, t + 1):
#
#     n = int(input())
#     arr = [[0] * n for _ in range(n)]
#
#     # 우 하 좌 상 순서의 행열 이동 리스트 만들기
#     directi = [0, 1, 0, -1]
#     directj = [1, 0, -1, 0]
#
#     arr[0][0] = 1
#     for s in range(2, n * n + 1):
#         for i in range(n):
#             for j in range(n):
#                 for a in range(4):
#                     while  # 다음 값(이 다음 값을 어떻게 말해줘야하지..?)에 0이 있으면 반복...맞나...?
#                         di = i + directi[a]
#                         dj = j + directj[a]
#                         arr[di][dj] = s
#                         if (
#                             di < 0 or di > n - 1 or dj < 0 or dj > n - 1
#                         ):  # 인덱스 범위 밖으로 나가지 않게 예외 처리
#                             continue
#                         elif (
#                             arr[di][dj] != 0
#                         ):  # 다음 값(이 다음 값을 어떻게 말해줘야하지..?)에 0이 없으면 for문 위로 돌아간다..
#                             continue
#
#     print(arr)

# 1. 델타 값 정의 (우 하 좌 상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input())

for tc in range(1, t + 1):

    n = int(input())

    snail = [[0] * n for _ in range(n)]
    x, y = 0, 0 # 출발 위치
    direction = 0 # 처음 출발 방향 오른쪽

    for i in range(1, n*n + 1):
        snail[x][y] = i
        # 다음 위치 이동
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위 안에 있어? & 이미 숫자 없어?
        if 0 <= nx < n and 0 =< ny < n and snail[nx][ny] == 0:
            x, y = nx, ny

        else:
            # 방향을 바꿔서 다시 이동하자!
            direction = (direction + 1) % 4 # 여기가 포인트! 우 하 좌 상 -> 여기서 다시 우로 가야하니깐
                                            # direction 3번째에서 0번째로 가야하니깐~!
            x += dx[direction]
            y += dy[direction]

    print (f'#{tc}')
    # for i in range(n):
    #     for j in range(n):
    #         print(snail[i][j], end = '')
    #     print()
    for line in snail:
        print(*line)