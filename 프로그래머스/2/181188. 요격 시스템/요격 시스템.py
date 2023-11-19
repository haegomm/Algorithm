def solution(targets):
    targets.sort(key=lambda x: x[1])
    cnt = 0
    last_end = -1
    
    for start, end in targets:
        if start >= last_end:
            cnt += 1
            last_end = end
    return cnt