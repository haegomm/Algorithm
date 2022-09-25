for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    arr_row = [input().replace(" ", "") for _ in range(n)]
    arr_col = list(map(''.join, zip(*arr_row)))
    cnt = 0

    for arr in arr_row, arr_col:
        for line in arr:
            real = list(line.split('0'))
            for check in real:
                if check == ('1' * k):
                    cnt += 1

    print(f'#{t}', cnt)