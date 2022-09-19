numbers = []

for _ in range(9):
    numbers.append(int(input()))

sum_numbers = sum(numbers)
k = sum_numbers - 100
breaker = False

for i in range(0, 8):
    if breaker:
        break
    for j in range(i+1, 9):
        if numbers[i] + numbers[j] == k:
            numbers.remove(numbers[i])
            numbers.remove(numbers[j-1])
            breaker = True
            break

numbers = sorted(numbers)
print(*numbers, sep='\n')