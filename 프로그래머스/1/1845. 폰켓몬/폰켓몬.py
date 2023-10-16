def solution(nums):
    n = len(nums) // 2
    ponketmons = set(nums)
    if n <= len(ponketmons):
        return n
    else:
        return len(ponketmons)