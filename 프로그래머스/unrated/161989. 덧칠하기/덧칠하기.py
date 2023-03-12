def solution(n, m, section):
    answer = 0
    last_paint_num = 0
    for one_more in section:
        if one_more <= last_paint_num:
            continue
        else:
            answer += 1
            last_paint_num = one_more + m - 1
    return answer