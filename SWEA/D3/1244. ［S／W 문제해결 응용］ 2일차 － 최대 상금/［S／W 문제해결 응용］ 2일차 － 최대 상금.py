# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금



def check(num, k, memo=''):
    global result

    # 재귀 종료 조건
    if k == 0:
        memo += num
        if int(memo) > result:
            result = int(memo)
        return
            
    # 큰 숫자들은 앞으로 옮기고 2개만 남았는데 바꿔야할 횟수가 남아있을 때
    if len(num) == 2:
        next_num = num[1] + num[0]
        check(next_num, k - 1, memo)

    else:
        max_num = max(list(map(int, num)))
        idx_list = []
        for idx, i in enumerate(num):
            if int(i) == max_num:
                idx_list.append(idx)
        
        for idx in idx_list:

            if idx == 0:
                cut_num = num[1:]
                check(cut_num, k, memo + num[0])

            else:
                cut_num = num[1:idx] + num[0] + num[idx+1:]
                check(cut_num, k - 1, memo + num[idx])

                


for case in range(1, int(input()) + 1):
    num, k = input().split()

    # test용 체크해볼 케이스 번호
    # test = 6
    # if case != test:
    #     continue


    result = 0
    check(num, int(k))
    print(f'#{case} {result}')
