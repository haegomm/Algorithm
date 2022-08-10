for tc in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    for i in range(100):
        line_sum = 0 
        for j in range(100):
            line_sum += arr[i][j]
            if max_sum < line_sum:
                max_sum = line_sum

        line_sum = 0
        for j in range(100):
            line_sum += arr[j][i]
            if max_sum < line_sum:
                max_sum = line_sum

        line_sum = 0
        for i in range(100):
            line_sum += arr[i][i]
            if max_sum < line_sum:
                max_sum = line_sum

        line_sum = 0
        for i in range(100):
            line_sum += arr[i][
                99 - i
            ] 
            if max_sum < line_sum:
                max_sum = line_sum

    print(f'#{tc} {max_sum}')