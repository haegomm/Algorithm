for tc in range(1, 11):
    n, numbers = input().split()

    numbers_stack = []

    for number in numbers:
        if not numbers_stack:
            numbers_stack.append(number)

        else:
            if number == numbers_stack[-1]:
                numbers_stack[-1].pop
            else:
                numbers_stack.append(number)

    print(f'#{tc} {"".join(numbers_stack)}')
