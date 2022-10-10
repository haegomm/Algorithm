for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    s = list(range(1, n+1))
    
    for y in map(int, input().split()):
        s.remove(y)

    print(f'#{t}', *s)