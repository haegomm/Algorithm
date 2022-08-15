t = int(input())

for tc in range(1, t + 1):

    arr = list(map(int, input().split()))
    n = len(arr)

    for i in range(1, 1 << n):

        subset_sum = 0

        for j in range(n):
            if i & (1 << j):
                subset_sum += arr[j]

        if subset_sum == 0:
            print(f'#{tc} 1')
            break

    else:
        print(f'#{tc} 0')
