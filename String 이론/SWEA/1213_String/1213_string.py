for _ in range(1, 11):

    tc = input()
    serch_str = input()
    sentence = input()

    count_str = sentence.count(serch_str)

    print(f'#{tc} {count_str}')
