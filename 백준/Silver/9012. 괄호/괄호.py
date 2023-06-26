tc = int(input())

for t in range(tc):
    stack = []
    brackets = input()
    for i in brackets:
        if i == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                print('NO')
                break
            else:
                stack.pop()
    else:
        if not stack:
            print('YES')
        else:
            print('NO')
