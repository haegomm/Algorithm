def solution(citations):
    citations.sort(reverse=True)
    for i, k in enumerate(citations):
        if k >= i + 1:
            continue
        else:
            return i
    return len(citations)
