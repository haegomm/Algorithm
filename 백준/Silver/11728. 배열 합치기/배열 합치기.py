temp = input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
res = sorted(a + b)

print(*res)