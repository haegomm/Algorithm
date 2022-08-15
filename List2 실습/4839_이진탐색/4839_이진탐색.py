t = int(input())

for tc in range(1, t + 1):
    # 전체 페이지, a 찾는 페이지, b 찾는 페이지
    p, a, b = map(int, input().split())

    # a와 b의 시작페이지
    a_l = b_l = 1

    # a와 b의 끝페이지
    a_r = b_r = p

    # a와 b의 중간페이지
    a_m = b_m = 0

    # 페이지 찾는 횟수. 어차피 중간 페이지를 찾아야하니깐 초기 횟수를 1로 설정
    a_cnt = b_cnt = 0

    while a != a_m:
        a_m = int((a_l + a_r) / 2)
        a_cnt += 1

        if a_m == a:
            break
        elif a > a_m:
            a_l = a_m

        elif a < a_m:
            a_r = a_m

    while b != b_m:
        b_m = int((b_l + b_r) / 2)
        b_cnt += 1

        if b_m == b:
            break
        elif b > b_m:
            b_l = b_m

        elif b < b_m:
            b_r = b_m

    if a_cnt > b_cnt:
        print(f'#{tc} B')

    elif a_cnt < b_cnt:
        print(f'#{tc} A')

    elif a_cnt == b_cnt:
        print(f'#{tc} 0')
