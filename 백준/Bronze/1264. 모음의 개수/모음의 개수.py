while True:
    s = input()
    answer = 0
    if s == '#':
        break

    for k in ('a', 'e', 'i', 'o', 'u','A','E','I','O','U'):
        answer += s.count(k)

    print(answer)