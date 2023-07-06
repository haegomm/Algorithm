n = int(input())
stack = []
answer = []
cnt = 1
flag = 0

for _ in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        answer.append("+")
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    print(*answer, sep='\n')