n = int(input())
cows = [3] * 11
result = 0

for _ in range(n):
    num, p = map(int, input().split())
    if cows[num] != 3 and cows[num] != p:
        result += 1
    cows[num] = p

print(result)