t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())  # input받는 문자열 갯수 n, 회문 문자 길이 m

    # 입력받아야 할 문자열 갯수 만큼 반복문을 돌면서 한 줄 씩 입력받아 한 줄 씩 확인.
    row_words = [input() for _ in range(n)]

    # 튜플 리스트 # 왜 * 사용해야하지... row_words가 리스트이니깐 리스트를 풀어줘야함.
    col_words = list(map(''.join, zip(*row_words)))  # 튜플을 문자열로 변환

    for r_c_list in row_words, col_words:
        for words in r_c_list:
            for i in range(n - m + 1):
                check_words = words[i: i + m]
                reversed_check = check_words[:: -1]

                if check_words == reversed_check:
                    print(f'#{tc} {check_words}')
                    break

                # else:
                #     break    # 반복문 안에 있어서 구간탐색 다 못해서 쓰면 안됨!

    # for words in col_words:
    #     check_words = words[:m]
    #     reversed_check = check_words[:: -1]

    #     result = ''

    #     for i in range(m):
    #         if check_words[i] == reversed_check[i]:
    #             result += check_words[i]

    #         else:
    #             break

    #     if check_words == result:
    #         print(f'#{tc} {check_words}')
    #         break

    # for _ in range(n):  # 입력받아야 할 문자열 갯수 만큼 반복문을 돌면서 한 줄 씩 입력받아 한 줄 씩 확인.
    #     words = input()

    #     check_words = words[:m]
    #     reversed_check = check_words[:: -1]

    #     row_list = []

    #     for i in range(m):
    #         check_words[i] == reversed_check[i]

    #         # 가로줄에서 못 찾으면 세로 줄 확인을 위해 zip_list로 문자열 이동.
    #         if check_words[i] != reversed_check[i]:
    #             # [['a', 'b', 'c'], ['d', 'e', 'f'], ['a', 'g', 'h']]
    #             row_list += list(map(words))

    #         print(f'#{tc} {check_words}')
    #         exit()  # 제일 위의  for문을 나올 수 있나? 인풋받는 반복문..

    # # [('a', 'd', 'a'), ('b', 'e', 'g'), ('c', 'f', 'h')]
    # col_row_list = zip(*row_list)

    # for _ in range(len(col_row_list) - 1):
