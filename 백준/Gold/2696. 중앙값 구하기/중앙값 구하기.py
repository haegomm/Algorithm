import sys

input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    answer = []
    t = int(input().strip())
    numbers = []
    for _ in range((t + 9) // 10):
        numbers.extend(map(int, input().split()))
    for idx, num in enumerate(numbers):
        idx += 1
        if idx % 2 != 0:
            temp = sorted(numbers[:idx])
            answer.append(temp[(idx - 1) // 2])
    print(len(answer))
    for i in range(0, len(answer), 10):
        print(*answer[i : i + 10])