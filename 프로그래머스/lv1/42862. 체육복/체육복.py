def solution(n, lost, reserve):
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve) - set(lost))
    reserve.sort()
    no = len(lost)
    
    for r in reserve:

        if r - 1 in lost:
            lost.remove(r - 1)
            no -= 1

        else:
            if r + 1 in lost:
                lost.remove(r + 1)
                no -= 1

    answer = n - no

    return answer
