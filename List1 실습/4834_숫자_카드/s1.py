t = int(input())

for tc in range(1, t+1):
    n = int(input())
    numbers = list(map(int, input()))

    c = [0] * 10

    for num in numbers:
        c[num] += 1

    max_count = 0
    max_idx = 0
    for i in range(10):
        if max_count <= c[i]:
            max_count = c[i]
            max_idx = i

    print(f'#{tc} {max_idx} {max_count}')
