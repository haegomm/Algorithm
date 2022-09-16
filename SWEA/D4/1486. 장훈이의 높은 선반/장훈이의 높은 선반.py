from itertools import combinations

t = int(input())

for tc in range(1, t + 1):
    n, top = map(int, input().split())
    arr = list(map(int, input().split()))
    subsets = []
    s = []

    for i in range(len(arr) + 1):
        subsets = list(combinations(arr, i))
        for i in subsets:
            check = sum(i)
            if check >= top:
                s.append(check)

    print(f'#{tc}', min(s) - top)