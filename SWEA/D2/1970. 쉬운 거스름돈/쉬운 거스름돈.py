for t in range(1, int(input()) + 1):
    n = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = []

    for m in money:
        change += [n // m]
        n %= m

    print(f'#{t}')
    print(*change)