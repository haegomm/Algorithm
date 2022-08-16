t = int(input())

for tc in range(1, t + 1):

    search_word = input()
    words = input()

    search_count = words.count(search_word)

    print(f'#{tc} {search_count}')
