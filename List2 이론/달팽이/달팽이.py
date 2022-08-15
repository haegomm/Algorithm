t = int(input())

for tc in range(1, t + 1):

    n = int(input())
    arr = [[0] * n for _ in range(n)]

    # 우 하 좌 상 순서의 행열 이동 리스트 만들기
    directi = [0, 1, 0, -1]
    directj = [1, 0, -1, 0]

    arr[0][0] = 1
    for s in range(2, n * n + 1):
        for i in range(n):
            for j in range(n):
                for a in range(4):
                    while  # 다음 값(이 다음 값을 어떻게 말해줘야하지..?)에 0이 있으면 반복...맞나...?
                        di = i + directi[a]
                        dj = j + directj[a]
                        arr[di][dj] = s
                        if (
                            di < 0 or di > n - 1 or dj < 0 or dj > n - 1
                        ):  # 인덱스 범위 밖으로 나가지 않게 예외 처리
                            continue
                        elif (
                            arr[di][dj] != 0
                        ):  # 다음 값(이 다음 값을 어떻게 말해줘야하지..?)에 0이 없으면 for문 위로 돌아간다..
                            a = (a + 1) % 4
							i += di[a]
                            j += dj[a]

    print(arr)