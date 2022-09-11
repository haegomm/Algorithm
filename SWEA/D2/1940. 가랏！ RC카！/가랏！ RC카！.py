t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    distance = 0
    speed = 0
    for _ in range(n):
        num = input()
        if num == '0':
            distance += speed
        else:
            c, s = map(int, num.split())
            if c == 1:
                speed += s
                distance += speed
            elif c == 2:
                speed -= s
                if speed < 0:
                    speed = 0
                distance += speed

    print(f'#{tc} {distance}')