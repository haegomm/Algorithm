# t = 10

# for tc in range(1, t + 1):
n = int(input())
building = list(map(int, input().split()))

result = 0
for i in range(2, n - 2):
    main = building[i]
    if (
        main > building[i + 2]
        and main > building[i + 1]
        and main > building[i - 1]
        and main > building[i - 2]
    ):  # i를 기준으로 좌우 2개씩 비교하여 i가 제일 크다면
        maxidx = 0
        for compare_idx in (
            building[i - 2],
            building[i - 1],
            building[i + 1],
            building[i + 2],  # i 좌우 2개씩 4개의 값중 제일 큰 값을 찾기위해 값을 하나씩 가져와
        ):
            if maxidx < compare_idx:  # 비교하여
                maxidx = compare_idx  # maxidx에 담는다
                result += main - maxidx  # 기준 인덱스i 의 값에서 maxidx의 값을 뺀 것을 결과값에 더한다.

print(result)
