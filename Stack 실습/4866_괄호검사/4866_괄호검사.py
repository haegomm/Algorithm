t = int(input())

for tc in range(1, t + 1):
    check = input()

    bracket = []

    for i in check:
        if i != '{' and i != '(' and i != ')' and i != '}':
            continue

        elif i == '{' or i == '(':
            bracket.append(i)

        elif i == '}':
            if not bracket:
                print(f'#{tc} 0')
                break
            elif bracket[-1] == '{':
                bracket.pop()
            else:
                print(f'#{tc} 0')
                break

        elif i == ')':
            if not bracket:
                print(f'#{tc} 0')
                break
            elif bracket[-1] == '(':
                bracket.pop()
            else:
                print(f'#{tc} 0')
                break

    else:
        if not bracket:
            print(f'#{tc} 1')

        elif len(bracket) >= 1:
            print(f'#{tc} 0')
