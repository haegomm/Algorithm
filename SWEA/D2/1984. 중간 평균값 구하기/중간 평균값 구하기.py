t = int(input())

for tc in range(1, t+1):

    numbers = list(map(int, input().split()))
    numbers.sort()

    average = sum(numbers[1:-1]) / (len(numbers) - 2)

    print(f'#{tc}', round(average))