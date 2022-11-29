def solution(x):
    num = str(x)
    ha = 0
    for i in range(len(num)):
        ha += int(num[i])
        
    if x % ha == 0:
        answer = True
    else:
        answer = False
    return answer