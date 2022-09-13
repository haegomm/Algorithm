def inorder(n):
    if n:
        inorder(L[n])
        print(word[n], end='')
        inorder(R[n])


for tc in range(1, 11):
    v = int(input())

    L = [0] * (v+1)
    R = [0] * (v+1)
    word = [''] * (v+1)

    for _ in range(v):
        info = list(input().split())
        idx, s = int(info[0]), info[1]
        word[idx] = s
        if len(info) == 3:
            L[idx] = int(info[2])
        elif len(info) == 4:
            L[idx] = int(info[2])
            R[idx] = int(info[3])

    print(f'#{tc}', end=' ')
    inorder(1)
    print()