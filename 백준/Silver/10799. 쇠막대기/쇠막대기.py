stick = input()
stick.strip('()')
stack = 0
answer = 0

for i in stick.replace('()', '|'):
    if i == '(':
        stack += 1
    elif i == '|':
        answer += stack
    else:
        answer += 1
        stack -= 1

print(answer)