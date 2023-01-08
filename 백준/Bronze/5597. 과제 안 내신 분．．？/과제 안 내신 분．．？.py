nums = list(range(1, 31))

for _ in range(28):
    nums.remove(int(input()))

print(*nums, sep='\n')