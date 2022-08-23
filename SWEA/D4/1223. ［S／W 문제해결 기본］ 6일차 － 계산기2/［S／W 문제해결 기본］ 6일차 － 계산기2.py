for tc in range(1, 11):
    word_len = input()
    word = input()
    result = ''
    stack = []

    for token in word:
        if token in '*+':
            if not stack:
                stack.append(token)
            elif token == '*':
                while stack and stack[-1] in '*':
                    result += stack.pop()
                stack.append(token)
            elif token == '+':
                while stack:
                    result += stack.pop()
                stack.append(token)

        else:
            result += token

    while stack:
        result += stack.pop()

    for char in result:
        if char not in '*+':
            stack.append(int(char))
        else:
            x = stack.pop()
            y = stack.pop()
            if char == '+':
                stack.append(y + x)
            elif char == '*':
                stack.append(y * x)

    print(f'#{tc} {stack.pop()}')