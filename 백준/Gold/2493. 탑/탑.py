n = int(input())
tops = list(map(int, input().split()))
stack = []
answer = []

for i in range(n):

    while stack and stack[-1][1] < tops[i]:
        stack.pop()

    if not stack:
        answer.append(0)

    else:
        answer.append(stack[-1][0] + 1)

    stack.append((i, tops[i]))

print(*answer)