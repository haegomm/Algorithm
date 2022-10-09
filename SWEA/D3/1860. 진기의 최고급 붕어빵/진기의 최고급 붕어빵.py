for t in range(1, int(input()) + 1):
    n, m, k = map(int, input().split())
    guest = sorted(list(map(int, input().split())))
    bung = 0
    result = 'Possible'

    for time in range(0, guest[-1] + 1):
        if time != 0 and time % m == 0:
            bung += k

        if time in guest:
            if bung <= 0:
                result = 'Impossible'
                break
            else:
                while time == guest[0]:
                    bung -= 1
                    guest.remove(guest[0])
                    if not guest:
                        break

    print(f'#{t} {result}')