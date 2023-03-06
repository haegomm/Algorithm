def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    for idx, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            answer[stack.pop()] = num
        stack.append(idx)

    return answer