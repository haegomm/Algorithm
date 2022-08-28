t = int(input())

for tc in range(1, t + 1):

    n = int(input())
    numbers = list(map(int, input().split()))

    max_ij = -1
    for i in range(n-1):
        for j in range(i+1, n):
            mul_num = numbers[i] * numbers[j]
            if mul_num >= 10:
                mul_num_str = list(str(mul_num))
                for k in range(len(mul_num_str) - 1):
                    if mul_num_str[k] > mul_num_str[k+1]:
                        break
                else:
                    if max_ij < mul_num:
                        max_ij = mul_num

    print(f'#{tc} {max_ij}')