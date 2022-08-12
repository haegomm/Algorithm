t = int(input())

for tc in range(1, t + 1):

    n = int(input())
    numbers = list(map(int, input().split()))

    # numbers 오름차순 정렬
    for i in range(n - 1):
        minidx = i
        for j in range(i + 1, n):
            if numbers[minidx] > numbers[j]:
                minidx = j

                numbers[i], numbers[minidx] = numbers[minidx], numbers[i]

    # 0으로 채워진 1차원 리스트 만들기
    result = [0] * n
    for k in range(n):
        if k % 2 == 0:
            result[k] = numbers[-(k // 2 + 1)]
        else:
            result[k] = numbers[k // 2]

    print(f'#{tc}', *result)  # * 붙여서 언팩킹
