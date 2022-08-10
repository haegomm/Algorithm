# import sys

# sys.stdin = open("input.txt")

for tc in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # max 초기 값 설정
    max_sum = 0
    for i in range(100):
        # 가로 합을 구한다
        line_sum = 0  # 가로 한 줄의 합계를 구할 때마다 초기화 시켜줘야해서 sum을 i의 for문과 j의 for문 사이에 놓는다.
        for j in range(100):
            line_sum += arr[i][j]
            if max_sum < line_sum:  # 가로 한 줄 끝나고 합계가 최댓값보다 크면
                max_sum = line_sum  # 그 합계를 최댓값에 값을 넣는다.

        # 세로 합을 구한다
        line_sum = 0  # 왜..
        for j in range(100):
            line_sum += arr[j][i]
            if max_sum < line_sum:
                max_sum = line_sum

        # 왼쪽 위 -> 오른쪽 아래 대각선 합을 구한다
        line_sum = 0
        for i in range(100):
            line_sum += arr[i][i]  # 이 방향의 대각선은 인덱스 값이 0,0 1,1 이라서 i 값으로 인덱스에 접근한다.
            if max_sum < line_sum:
                max_sum = line_sum

        # 오른족 위 -> 왼쪽 아래 대각선 합을 구한다.
        line_sum = 0
        for i in range(100):
            line_sum += arr[i][
                99 - i
            ]  # 이 방향의 대각선은 인덱스 값이 99,0 98,1 이라서 j 인덱스 값을 99-i로 설정해준다.
            if max_sum < line_sum:
                max_sum = line_sum

    print(f'#{tc} {max_sum}')
