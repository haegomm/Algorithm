code_pattern = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    code = [input() for _ in range(n)]

    password = []

    for line in code:
        line = line.strip('0')
        if len(line) != 0:
            line = '0' * (7 - (len(line) % 7)) + line
            break

    for i in range(0, len(line), 7):
        idx = code_pattern.index(line[i:i+7])
        password.append(idx)

    odd = password[1] + password[3] + password[5] + password[7]
    even = password[0] + password[2] + password[4] + password[6]
    if ((even * 3) + odd) % 10 == 0:
        print(f'#{tc}', odd + even)
    else:
        print(f'#{tc}', 0)