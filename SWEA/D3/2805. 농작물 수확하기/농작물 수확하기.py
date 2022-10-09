t = int(input())

for tc in range(1, t + 1):

    n = int(input())
    mf = n // 2
    harv = cnt = 0
    breaker = False

    for _ in range(n):
        farm = list(map(int, input()))
        harv += sum(farm[mf - cnt : mf + cnt + 1])
        if cnt == mf:
            breaker = True
        if breaker:
            cnt -= 1
        else:
            cnt += 1

    print(f'#{tc} {harv}')