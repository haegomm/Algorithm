from collections import defaultdict

def solution(clothes):
    outfit = defaultdict(int)
    
    for _, category in clothes:
        outfit[category] += 1

    answer = 1
    for count in outfit.values():
        answer *= (count + 1)
    
    return answer - 1
