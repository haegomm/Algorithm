# import sys

# sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t + 1):

    arr = [[0] * 10 for _ in range(10)]

    # 색칠 영역
    n = int(input())

    for _ in range(n):
        violet_count = 0  # 보라색이 몇 개 있는지를 담을 변수
        color_area = list(map(int, input().split()))

        # 색칠하기
        for i in range(color_area[0], color_area[2] + 1):
            for j in range(color_area[1], color_area[3] + 1):
                arr[i][j] += color_area[4]

        # 전체 영역을 돌면서 값이 3인 것을 찾아 +1 해주기
        for i in range(10):
            for j in range(10):
                if arr[i][j] == 3:
                    violet_count += 1

    print(f'#{tc} {violet_count}')
