def solution(N, stages):
    fail_p = []
    answer = []
    for stage in range(1, N + 1):
        a = 0  # 도착 사용자 수
        n_c = stages.count(stage)  # 도착 but 클리어하지 못한 사용자 수
        for user in stages:
            if user >= stage:
                a += 1
        if a == 0:
            fail_p.append(0)
        else:
            fail_p.append(n_c/a)

    for _ in range(N):
        high_fail = fail_p.index(max(fail_p))
        answer.append(high_fail+1)
        fail_p[high_fail] = -1
        
    return answer