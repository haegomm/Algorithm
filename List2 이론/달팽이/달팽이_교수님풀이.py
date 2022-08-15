# 1. 델타 값 정의 (우 하 좌 상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

t = int(input())

for tc in range(1, t + 1):

    n = int(input())

    snail = [[0] * n for _ in range(n)]
    x, y = 0, 0  # 출발 위치
    direction = 0  # 처음 출발 방향 오른쪽

    for i in range(1, n * n + 1):
        snail[x][y] = i
        # 다음 위치 이동
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 범위 안에 있어? & 이미 숫자 없어?
        if 0 <= nx < n and 0 <= ny < n and snail[nx][ny] == 0:
            x, y = nx, ny

        else:
            # 방향을 바꿔서 다시 이동하자!
            direction = (direction + 1) % 4  # 여기가 포인트! 우 하 좌 상 -> 여기서 다시 우로 가야하니깐
            # direction 3번째에서 0번째로 가야하니깐~!
            x += dx[direction]
            y += dy[direction]

    print(f'#{tc}')
    # for i in range(n):
    #     for j in range(n):
    #         print(snail[i][j], end = '')
    #     print()
    for line in snail:
        print(*line)
