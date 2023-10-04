from collections import defaultdict

arrange = defaultdict(int)
for _ in range(int(input())):
    name, extension = input().split('.')
    arrange[extension] += 1

for result in sorted(arrange.items()):
    print(*result)