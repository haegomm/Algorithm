t = int(input())

for tc in range(1, t + 1):

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    sum = 0

    # 상하좌우로 이동하기 위한 리스트를 만들어준다.
    directi = [-1, 1, 0, 0]
    directj = [0, 0, -1, 1]

    for i in range(n):
        for j in range(n):
            for a in range(4):
                di = i + directi[a]
                dj = j + directj[a]
                if di < 0 or di > n - 1 or dj < 0 or dj > n - 1:
                    continue
                sum += abs(arr[i][j] - arr[di][dj])

    print(f'#{tc} {sum}')
