for t in range(1, int(input()) + 1):
    n, q = map(int, input().split())
    box = [0] * (n + 1)
    
    for i in range(1, q+1):
        l, r = map(int, input().split())

        for k in range(l, r+1):
            box[k] = i

    print(f'#{t}', *box[1:])