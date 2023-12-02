from collections import Counter

n = int(input())
first_letters = [input()[0] for _ in range(n)]
counter = Counter(first_letters)

result = [char for char, count in counter.items() if count >= 5]
result.sort()

if result:
    print(''.join(result))
else:
    print("PREDAJA")
