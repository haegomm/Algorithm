def solution(array, commands):
    answer = []
    for command in commands:
        new = sorted(array[command[0] - 1:command[1]])
        answer.append(new[command[2]-1])
    return answer