def BNP(m):
    b_money = m
    b_cnt = 0
    for i in range(14):
        p = price[i]
        if b_money >= p:
            b_cnt += b_money // p
            b_money %= p
    return b_money + (b_cnt * price[13])


def TIMING(m):
    t_money = m
    t_cnt = 0
    for i in range(3, 14):
        p = price[i]
        if price[i - 3] > price[i - 2] > price[i - 1]:
            if t_money >= p:
                t_cnt += t_money // p
                t_money %= p
        elif price[i - 3] < price[i - 2] < price[i - 1]:
            t_money += t_cnt * p
            t_cnt = 0
    return t_money + (t_cnt * price[13])


m = int(input())
price = list(map(int, input().split()))

bnp_ans = BNP(m)
timing_ans = TIMING(m)

if bnp_ans > timing_ans:
    print('BNP')
elif bnp_ans < timing_ans:
    print('TIMING')
else:
    print("SAMESAME")