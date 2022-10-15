def solution(price, money, count):
    mul = 0
    for i in range(1, count + 1):
        mul += price * i
    result = money - mul

    if result > 0:
        answer = 0

    else:
        answer = abs(result)
    
    return answer