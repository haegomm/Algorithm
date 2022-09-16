from itertools import combinations

t = int(input())

for tc in range(1, t + 1):
    n, top = map(int, input().split())
    arr = list(map(int, input().split()))
    subsets = []
    m = 1000000000

    for i in range(len(arr) + 1):
        subsets = subsets + list(combinations(arr, i))
        for i in subsets:
            check = sum(i)
            if check >= top:
                result = check - top
                if result < m:
                    m = result
                    
    print(f'#{tc}', m)