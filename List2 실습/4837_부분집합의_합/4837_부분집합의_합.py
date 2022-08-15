set_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
a_len = len(set_a)

t = int(input())

for tc in range(1, t + 1):

    n, k = map(int, input().split())
    result_cnt = 0  # 부분집합의 합이 k이면서 원소 갯수가 n인 경우의 횟수

    # 부분집합 만들기
    for i in range(1 << a_len):
        subset = []  # 부분집합 원소 리스트
        subset_sum = 0  # 부분집합 합의 변수

        for j in range(a_len):
            if i & (1 << j):
                subset.append(set_a[j])  # 부분집합의 원소를 담는다
                subset_sum += set_a[j]  # 부분집합 원소들을 더한다

        if subset_sum == k and len(subset) == n:  # 부분집합의 합이 k이고 원소들의 갯수가 n이면
            result_cnt += 1  # +1 한다

    print(f'#{tc} {result_cnt}')
