t = int(input())

for tc in range(1, t + 1):

    search_word = input()
    words = input()

    cnt_max = 0

    for i in search_word:
        cnt = words.count(i)

        if cnt_max < cnt:
            cnt_max = cnt

    print(f'#{tc} {cnt_max}')


# count 사용 안하고

t = int(input())

for tc in range(1, t + 1):

    search_word = input()
    words = input()

    cnt_max = 0

    for i in search_word:
        cnt = 0
        for j in words:
            if i == j:
                cnt += 1
                if cnt_max < cnt:
                    cnt_max = cnt

    print(f'#{tc} {cnt_max}')
