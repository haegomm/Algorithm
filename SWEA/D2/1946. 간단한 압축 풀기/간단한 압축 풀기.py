t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    words = ''
    for _ in range(n):
        word, num = input().split()
        words += word * int(num)
    print(f'#{tc}')

    for i in range(0, len(words), 10):
        print(words[i : i + 10])