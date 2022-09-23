# 2117. [모의 SW 역량테스트] 홈 방범 서비스

'''
운영 비용 = K * K + (K - 1) * (K - 1)
중앙과의 거리가 k 보다 작으면 방범 범위에 포함된다! 

하나의 집이 지불할 수 있는 금액이 pay
'''


def operation_cost(k):
    '''
    :param k: 범위
    :return: 운영비용
    '''
    return k * k + (k - 1) * (k - 1)


def distance(a, b):
    '''
    :param a: 점 a (r, c)
    :param b: 점 b (r, c)
    :return: 두 점 사이 거리
    '''
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def can_connect(a, k):
    '''
    :param a: distance_investigate 의 한 좌표, 각 집과의 거리가 적혀있다.
    :param k: 거리 k
    :return: k 보다 작은 곳의 수를 출력
    '''
    answer = 0
    for distance in a:
        if distance < k:
            answer += 1
    return answer


for case in range(1, int(input()) + 1):
    city_size, pay = map(int, input().split())
    city_map = [list(map(int, input().split())) for _ in range(city_size)]

    # 집 주소 적기
    home_cnt = 0
    home_address = []
    for row in range(city_size):
        for col in range(city_size):
            if city_map[row][col]:
                home_address.append((row, col))
                home_cnt += 1

    # k 최대값 구해보기
    k_max = 0
    k_0 = 0
    pay_max = home_cnt * pay
    while pay_max - k_max >= 0:
        k_0 += 1
        k_max = operation_cost(k_0)

    # 각 좌표에다가 집들과의 거리 적기
    distance_investigate = [[[] for _ in range(city_size)] for _ in range(city_size)]
    for row in range(city_size):
        for col in range(city_size):
            for home in home_address:
                distance_investigate[row][col].append(distance((row, col), home))

    # k를 바꿔가며 찾기
    result = 0
    for k in range(1, k_0 + 1):
        # k일때 가장 많이 연결되는 거 찾기
        connect_max = 0

        for row in range(city_size):
            for col in range(city_size):
                rc = can_connect(distance_investigate[row][col], k)
                if rc > connect_max:
                    connect_max = rc

        best_way = pay * connect_max - operation_cost(k)

        # 손해보지 않고 기존 최댓값보다 크면 갱신!
        if best_way >= 0 and connect_max > result:
            result = connect_max

    print(f'#{case} {result}')