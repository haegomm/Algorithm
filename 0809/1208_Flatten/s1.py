t = 10

for tc in range(1, 11):

    n = int(input())
    numbers = list(map(int, input().split()))
    i = 0

    while i < n:
        numbers.sort()
        numbers[-1] -= 1
        numbers[0] += 1

        i += 1

    numbers.sort()
    result = numbers[-1] - numbers[0]

    print(f'#{tc} {result}')
