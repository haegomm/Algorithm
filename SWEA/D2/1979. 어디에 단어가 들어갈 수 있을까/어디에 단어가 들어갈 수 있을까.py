t = int(input())

for tc in range(1, t + 1):

    n, k = map(int, input().split())

    arr_row = [list(map(int, input().split())) for _ in range(n)]
    arr_col = list(map(list, zip(*arr_row)))

    result = 0
    for arr in arr_row, arr_col:
        for line in arr:
            for i in range(n):
                if line[i] == 1:
                    word_line = sum(line[i:i+k])
                    if word_line == k:  # 1 1 1 1 0 1 1 1
                        if i + k == n or ((i+k < n) and line[i+k] == 0):
                            if i == 0 or (i - 1 >= 0 and line[i-1] == 0):
                                result += 1

    print(f'#{tc} {result}')