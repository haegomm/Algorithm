from collections import Counter
def solution(k, tangerine):
    answer = 0
    tan = Counter(tangerine).items()
    s_tan = sorted(tan, reverse=True, key= lambda x : x[1])

    for t in s_tan:
        k -= t[1]
        answer += 1

        if k <= 0:
            break
    return answer