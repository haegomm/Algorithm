import sys
sys.stdin = open("sample_input.txt")

t = int(input())

for tc in range(1, t+1):

    n = int(input())
    numbers = list(map(int, input().split()))

    max_num = 0
    min_num = numbers[0]

    for num in numbers:
        if max_num < num:
            max_num = num

        elif min_num > num:
            min_num = num

    max_min = max_num - min_num

    print(f'#{tc} {max_min}')
