t = int(input())

for tc in range(1, t + 1):

    # 버스 에너지, 도착지, 충전소 갯수를 입력받는다.
    k, n, m = map(int, input().split())

    # 충전소 위치를 입력받는다
    charge_list = list(map(int, input().split()))

    # 버스 시작 위치, 충전 횟수 변수 선언
    bus = 0
    charge_count = 0

    for i in range(m - 1):

        if bus + k in charge_list:  # charg_list의 i번째 충전소 까지 갈 수 있어?
            if bus + k >= n:
                break
            elif bus + k >= charge_list[i + 1]:  # i+1번째 충전소도?
                bus = charge_list[i + 1]  # 그러면 i+1번째 충전소로 가면 돼
                charge_count += 1
            else:
                bus = charge_list[i]  # i+1번째까지 못 가는거면 i번째로 가자
                charge_count += 1
        else:
            charge_count = 0  # i번째도 못가는 거면 종착지까지 도착 실패!
            break

        # 최대로 갈 수 있는 거리가 i + 1이 아니라 + 2일수도 더 멀 수도 있어서 안됨.
        # 여기서 어떻게 수정해야할까

    # while bus + k < n:
    #     for max_move in range(k, 0, -1):
    #         if bus + max_move in charge_list:
    #             bus += max_move
    #             charge_count += 1
    #             break

    #     else:
    #         charge_count = 0
    #         break

    print(f'#{tc} {charge_count}')
