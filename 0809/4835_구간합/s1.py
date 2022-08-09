# t = int(input())

# for tc in range(1, t+1):

#     n, x = map(int, input().split())
#     numbers = list(map(int, input().split()))

#     sum_list = []
#     for i in range(n-x + 1):
#         sum_numbers = numbers[i]
#         for j in range(1, x):
#             sum_numbers += numbers[i + j]

#         sum_list.append(sum_numbers)

#     max_sum = 0
#     min_sum = sum_list[0]
#     for sum_num in sum_list:
#         if max_sum < sum_num:
#             max_sum = sum_num

#         if min_sum > sum_num:
#             min_sum = sum_num

#     result = max_sum - min_sum

#     print(f'#{tc} {result}')


t = int(input())

for tc in range(1, t+1):

    n, x = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    max_sum = 0
    min_sum = 10000 * 100

    for i in range(n-x + 1):
        sum_numbers = numbers[i]
        for j in range(1, x):
            sum_numbers += numbers[i + j]

        if max_sum < sum_numbers:
            max_sum = sum_numbers

        if min_sum > sum_numbers:
            min_sum = sum_numbers

    result = max_sum - min_sum

    print(f'#{tc} {result}')
