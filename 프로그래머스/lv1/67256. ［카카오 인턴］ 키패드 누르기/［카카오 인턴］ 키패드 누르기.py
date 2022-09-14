def solution(numbers, hand):
    answer = ''
    l = [1, 4, 7]
    m = [2, 5, 8, 0]
    r = [3, 6, 9]
    l_now = [0, 3]
    r_now = [2, 3]

    for i in numbers:
        if i in l:
            l_now = [0, l.index(i)]
            answer += 'L'
        elif i in r:
            r_now = [2, r.index(i)]
            answer += 'R'
        elif i in m:
            m_l = abs(1 - l_now[0]) + abs(m.index(i) - l_now[1])
            m_r = abs(1 - r_now[0]) + abs(m.index(i) - r_now[1])
            if m_l < m_r:
                l_now = [1, m.index(i)]
                answer += 'L'
            elif m_l > m_r:
                r_now = [1, m.index(i)]
                answer += 'R'
            else:
                if hand == 'left':
                    l_now = [1, m.index(i)]
                    answer += 'L'
                else:
                    r_now = [1, m.index(i)]
                    answer += 'R'
    return answer