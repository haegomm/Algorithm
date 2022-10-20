for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    password = input()
    unlock = []
    turn = n // 4

    for _ in range(turn):
        for i in range(0, n, turn):
            unlock.append(int(password[i:i + turn], 16))

        password = password[-1] + password[:n-1]

    result = sorted(set(unlock), reverse=True)

    print(f'#{t} {result[k-1]}')