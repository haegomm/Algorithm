from itertools import permutations

n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]
result = set()

for case in permutations(nums, m):
    temp = tuple(sorted(case))
    result.add(temp)

for ans in sorted(result):
    print(*ans)