def first_check():
    for i, w in enumerate(words):
        if not w[0] in shortcutKey:
            shortcutKey.add(w[0])
            if w[0].islower():
                shortcutKey.add(w[0].upper())
            else:
                shortcutKey.add(w[0].lower())
            words[i] = '[' + w[0] + ']' + w[1:]
            return (' '.join(words))
    return None

shortcutKey = set()

for _ in range(int(input())):
    words = list(input().split())
    res = first_check()
    if res:
        print(res)
        continue

    flag = False
    for i, w in enumerate(words):
        for j, ww in enumerate(w):
            if not ww in shortcutKey:
                shortcutKey.add(ww)
                if ww.islower():
                    shortcutKey.add(ww.upper())
                else:
                    shortcutKey.add(ww.lower())
                words[i] = w[:j] + '[' + ww + ']' + w[j+1:]
                flag = True
                break
        if flag:
            break
    print(' '.join(words))