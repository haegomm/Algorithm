import sys, math

input = sys.stdin.readline


def check(arr):
    cnt = 0
    for n in arr:
        if int(n) % 2 != 0:
            cnt += 1
    return cnt


def operation(nums, cnt):
    global max_num, min_num

    if len(nums) == 1:
        min_num = min(min_num, cnt)
        max_num = max(max_num, cnt)
    elif len(nums) == 2:
        temp = str(int(nums[0]) + int(nums[1]))
        operation(temp, cnt + check(temp))
    else:
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                num1 = nums[: i + 1]
                num2 = nums[i + 1 : j + 1]
                num3 = nums[j + 1 :]
                temp = str(int(num1) + int(num2) + int(num3))
                operation(temp, cnt + check(temp))


nums = input().strip()

min_num = math.inf
max_num = 0

operation(nums, check(nums))
print(min_num, max_num)