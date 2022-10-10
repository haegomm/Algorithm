for t in range(1, int(input()) + 1):
    n = int(input())
    numbers = sorted(list(map(int, input().split())), reverse=True)
    result = -1

    for i in range(n-1):
        for j in range(i+1, n):
            mul = str(numbers[i] * numbers[j])
            for k in range(len(mul)-1):
                if mul[k] > mul[k+1]:
                    break
            else:
                if result < int(mul):
                    result = int(mul)
                    break

    print(f'#{t} {result}')