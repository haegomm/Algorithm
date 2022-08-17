t = int(input())

for tc in range(1, t + 1):

    search_word = input()
    words = input()

    if search_word in words:
        result = 1

    else:
        result = 0

    print(f'#{tc} {result}')
