from itertools import combinations, product

N, num = map(int, input().split())
K = list(input().split())
ans = 0

for n in range(1, len(str(N)) + 1):
    for com in list(product(K, repeat=n)):
        temp = int(''.join(com))
        if temp <= N:
            ans = max(ans ,temp)

print(ans)