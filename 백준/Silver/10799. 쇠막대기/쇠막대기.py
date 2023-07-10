stick = input()
stick.strip('()')
stack = []
cnt = 0
answer = 0

for i in range(len(stick)):
    if stick[i] == '(':
        cnt += 1
    else:
        if stick[i - 1] == '(':
            cnt -= 1
            answer += cnt
        else:
            answer += 1
            cnt -= 1

print(answer)