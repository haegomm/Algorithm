t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    result = -1
    for i in range(1, 10**18):
        if i**3 > n:
            break
        elif n % i == 0 and n == i ** 3:
            result = i
            break

    print(f'#{tc}', result)