t = int(input())

for tc in range(1, t + 1):

    memory = list(input())
    modi_cnt = 0

    for i in range(len(memory) - 1):
        if memory[i] != memory[i + 1]:
            modi_cnt += 1

    if memory[0] == '1':
        modi_cnt += 1

    print(f'#{tc} {modi_cnt}')