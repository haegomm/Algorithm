t = int(input())

for tc in range(1, t + 1):

    n, m = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(n)]

    fly_max = 0
    for k in range(n - m + 1):
        for s in range(n - m + 1):
            fly_sum = 0
            for i in range(k, k + m):
                for j in range(s, s + m):
                    fly_sum += fly[i][j]

            if fly_max < fly_sum:
                fly_max = fly_sum

    print(f'#{tc} {fly_max}')