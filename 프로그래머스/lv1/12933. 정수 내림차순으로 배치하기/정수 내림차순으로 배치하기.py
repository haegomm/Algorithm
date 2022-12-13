def solution(n):
    num = sorted((str(n)), reverse=True)
    answer = ''.join(num)
    return int(answer)