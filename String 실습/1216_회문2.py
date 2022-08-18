for _ in range(10):

    tc = int(input())

    n = 100

    row_words = [input() for _ in range(n)]

    col_words = list(map(''.join, zip(*row_words)))

    max_palindrome = 0

    breaker = True
    while breaker:
        for idx in range(n):
            for m in range(100, 0, -1):
                for i in range(n - m + 1):
                    check_row = row_words[idx][i: i + m]
                    check_col = col_words[idx][i: i + m]

                    if (check_row == check_row[::-1]) or (check_col == check_col[::-1]):
                        if max_palindrome < len(check_row) or max_palindrome < len(
                            check_col
                        ):
                            max_palindrome = m

        print(f'#{tc} {max_palindrome}')
        breaker = False
        break
