t = int(input())

for tc in range(1, t+1):
    n = int(input())

    num_sum = 0
    for num in range(1, n+1):
        if not num % 2:
            num_sum -= num
        else:
            num_sum += num

    print(f'#{tc} {num_sum}')