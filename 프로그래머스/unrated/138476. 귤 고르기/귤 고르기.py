from collections import Counter
def solution(k, tangerine):
    answer = 0
    tan = Counter(tangerine).most_common()

    for t in tan:
        k -= t[1]
        answer += 1

        if k <= 0:
            break
    return answer