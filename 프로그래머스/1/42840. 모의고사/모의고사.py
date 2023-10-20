def solution(answers):
    answer = []
    a1, a2, a3 = 0, 0, 0
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    for i, a in enumerate(answers):
        if p1[i%5] == a:
            a1 += 1
        if p2[i%8] == a:
            a2 += 1
        if p3[i%10] == a:
            a3 += 1
    
    cnt = max(a1, a2, a3)
    if a1 == cnt:
        answer.append(1)
    if a2 == cnt:
        answer.append(2)
    if a3 == cnt:
        answer.append(3)
        
    return answer