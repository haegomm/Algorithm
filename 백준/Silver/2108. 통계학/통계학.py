import sys
from collections import Counter

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]

average = round(sum(numbers) / n)

numbers.sort()
median = numbers[n // 2]

frequency = Counter(numbers).most_common()
if len(frequency) > 1 and frequency[0][1] == frequency[1][1]:
    mode = frequency[1][0]
else:
    mode = frequency[0][0]

range_value = numbers[-1] - numbers[0]

print(average)
print(median)
print(mode)
print(range_value)