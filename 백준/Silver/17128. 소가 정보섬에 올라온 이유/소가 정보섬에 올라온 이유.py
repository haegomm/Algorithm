n, q = map(int, input().split())
cows = list(map(int, input().split()))
sticker = list(map(int, input().split()))

products = [(cows[i] * cows[(i+1)%n] * cows[(i+2)%n] * cows[(i+3)%n]) for i in range(n)]
sum_S = sum(products)

for i in sticker:
    for j in range(4):
        k = (i - 1 - j + n) % n
        sum_S -= products[k]
        products[k] *= -1
        sum_S += products[k]

    print(sum_S)