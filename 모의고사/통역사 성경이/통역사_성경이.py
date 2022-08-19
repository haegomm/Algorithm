t = int(input())

for tc in range(1, t + 1):

    tc_tc = int(input())
    say = input()
    say = say.replace('!', '.').replace('?', '.')
    say = say.split('.')
    say.remove(say[-1])
    # print(say)

    name_list = []
    for saying in say:
        name = 0
        saying = list(saying.split())
        for word in saying:
            if word.isalpha():
                if sum(s.isupper() for s in word) == 1:
                    if word[0].isupper():
                        name += 1

        name_list.append(name)
    print(f'#{tc} {" ".join(map(str, name_list))}')
