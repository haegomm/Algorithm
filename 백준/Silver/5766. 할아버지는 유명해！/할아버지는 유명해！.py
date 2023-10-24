from collections import defaultdict

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    rank = defaultdict(int)

    for _ in range(n):
        member = list(map(int, input().split()))

        for man in member:
            rank[man] += 1
        
    second = sorted(list(set(rank.values())), reverse=True)[1]

    ans = []
    for man, point in rank.items():
        if point == second:
            ans.append(man)

    print(*sorted(ans))