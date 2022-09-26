n = int(input())
result = []

for num2 in range(n//2, n+1):
    numbers = [n, num2]
    num1 = n
    while True:
        num3 = num1 - num2
        if num3 >= 0:
            numbers.append(num3)
            num1 = num2
            num2 = num3
        else:
            break

    if len(numbers) > len(result):
        result = numbers

print(len(result))
print(*result)