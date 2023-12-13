nums = set(range(1, 10001))
not_self_nums = set()

for num in range(1, 10001):
    for n in str(num):
        num += int(n)
    not_self_nums.add(num)

self_nums = sorted(nums - not_self_nums)
for ans in self_nums:
    print(ans)