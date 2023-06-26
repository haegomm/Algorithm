tc = int(input())

for t in range(tc):
    stack = []
    brackets = input()
    while '()' in brackets:
        brackets = brackets.replace('()', '')

    if brackets:
        print('NO')
    else:
        print('YES')