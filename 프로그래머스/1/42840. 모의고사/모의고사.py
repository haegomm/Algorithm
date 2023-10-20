def solution(answers):
    answer = []
    cnt = [0, 0, 0]
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    for i, a in enumerate(answers):
        if p1[i%5] == a:
            cnt[0] += 1
        if p2[i%8] == a:
            cnt[1] += 1
        if p3[i%10] == a:
            cnt[2] += 1
    
    max_cnt = max(cnt)
    for i, c in enumerate(cnt):
        if c == max_cnt:
            answer.append(i+1)
        
    return answer