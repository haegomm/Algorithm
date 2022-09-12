t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    sheep = [0] * 10
    breaker = True
    while breaker:
        for i in range(1, 100):
            cnt = n * i
            cnt_list = list(map(int, str(cnt)))
            for j in cnt_list:
                if sheep[j] == 0:
                    sheep[j] = 1
            if sheep == [1] * 10:
                breaker = False
                break
    print(f'#{tc} {cnt}')