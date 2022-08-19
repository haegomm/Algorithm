t = int(input())

for tc in range(1, t+1):

    n = int(input())
    card = list(input().split())

    if n % 2 == 0:
        card1 = card[:int(n/2)]
        card2 = card[int(n/2):]

    else:
        card1 = card[:int(n / 2) + 1]
        card2 = card[int(n / 2) + 1:]

    perpect = [0] * n

    for i in range(n):
        if i % 2 == 0:
            perpect[i] = card1[int(i / 2)]
        else:
            perpect[i] = card2[int(i / 2)]

    print(f'#{tc} {" ".join(perpect)}')