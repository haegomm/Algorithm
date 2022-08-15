t = int(input())

for tc in range(1, t + 1):

    n = int(input())
    numbers = list(map(int, input().split()))

    # numbers 오름차순 버블정렬
    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    # 0으로 채워진 1차원 리스트 만들기
    result = [0] * n
    for k in range(n):
        if k % 2 == 0:
            result[k] = numbers[-(k // 2 + 1)]
        else:
            result[k] = numbers[k // 2]

    print(f'#{tc}', *result[:10])  # * 붙여서 언팩킹 # 10개만 출력해야해서 [:10]으로 슬라이싱
