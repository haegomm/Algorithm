from itertools import permutations
def primenumber(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = set()
    
    for n in range(1, len(numbers)+1):
        for com in permutations(list(numbers), n):
            nums.add(int(''.join(com)))
    for num in nums:
        if primenumber(num):
            answer += 1
    return answer