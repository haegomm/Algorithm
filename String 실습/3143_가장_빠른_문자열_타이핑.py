t = int(input())

for tc in range(1, t + 1):

    word, saving_str = input().split()

    word = word.replace(saving_str, '.')
    count_typing = len(word)

    print(f'#{tc} {count_typing}')
