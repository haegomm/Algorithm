def solution(n, m, section):
    answer = 0
    last_paint_num = 0
    for start_paint_num in section:
        if start_paint_num <= last_paint_num:
            continue
        else:
            answer += 1
            last_paint_num = start_paint_num + m - 1
    return answer