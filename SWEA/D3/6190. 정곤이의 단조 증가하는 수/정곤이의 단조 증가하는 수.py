for t in range(1, int(input()) + 1):
    n = int(input())
    numbers = sorted(list(map(int, input().split())), reverse=True)
    result = -1

    for i in range(n-1):
        for j in range(i+1, n):
            mul = str(numbers[i] * numbers[j])
            for j in range(len(mul)-1):
                if mul[j] > mul[j+1]:
                    break
            else:
                if int(result) < int(mul):
                    result = mul
                    break

    print(f'#{t} {result}')