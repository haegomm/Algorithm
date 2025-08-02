def solution(topping):
    
    answer = 0
    n = len(topping)
    
    left = [0] * n
    right = [0] * n
    
    seen = set()
    for i in range(n):
        seen.add(topping[i])
        left[i] = len(seen)
    
    seen.clear()
    for i in range(n - 1, -1, -1):
        seen.add(topping[i])
        right[i] = len(seen)
        
    for i in range(n-1):
        if left[i] == right[i+1]:
            answer += 1
    
    return answer