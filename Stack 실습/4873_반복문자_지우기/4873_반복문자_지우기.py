t = int(input())

for tc in range(1, t + 1):

    words = input()

    words_stack = ['']

    for word in words:
        if word == words_stack[-1]:
            words_stack.pop()
        else:
            words_stack.append(word)

    print(f'#{tc} {(len(words_stack)) - 1}')