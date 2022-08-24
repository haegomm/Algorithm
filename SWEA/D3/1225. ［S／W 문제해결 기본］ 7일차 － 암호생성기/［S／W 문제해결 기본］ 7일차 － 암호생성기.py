for _ in range(10):
    tc = int(input())

    queue = list(map(int, input().split()))

    find_password = True

    while find_password:
        for minus_num in range(1, 6):
            password_num = (queue.pop(0) - minus_num)
            if password_num <= 0:
                password_num = 0
                queue.append(password_num)
                find_password = False
                break
            queue.append(password_num)

    print(f'#{tc}', *queue)