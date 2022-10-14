def find_color(b, r):
    global case, result

    for white in range(1, b):
        case += m - flag[white].count('W')

    for blue in range(b, r):
        case += m - flag[blue].count('B')

    for red in range(r, n-1):
        case += m - flag[red].count('R')

    if result > case:
        result = case

    return result

for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    flag = [input() for _ in range(n)]
    result = 50*50

    for i in range(1, n-1):
        for j in range(i+1, n):
            case = 0
            case += m - flag[0].count('W')
            case += m - flag[-1].count('R')
            find_color(i,j)

    print(f'#{t} {result}')