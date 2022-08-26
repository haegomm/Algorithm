t = int(input())

for tc in range(1, t + 1):
    word = input()
    check_word = word[::-1]

    result = 0
    if word == check_word:
        result = 1

    print(f'#{tc} {result}')