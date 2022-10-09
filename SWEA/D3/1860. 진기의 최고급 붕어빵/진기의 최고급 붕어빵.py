for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    times = list(map(int, input().split()))
    times.sort()

    total = 0
    ans = 'Possible'
    for t in range(0, 11111 + 1):
        if t != 0 and t % M == 0:
            total += K

        if t in times:
            if total <= 0:

                ans = 'Impossible'
                break
            else:
                total -= 1

    print(f'#{tc} {ans}')