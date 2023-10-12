import sys

input = sys.stdin.readline
from collections import deque

y, x, n = map(int, input().split())

deq = deque()
array = [list(input().split()) for _ in range(y)]
answer = [[0] * x for _ in range(y)]

loops = min(y, x) // 2

for i in range(loops):
    deq.clear()
    deq.extend(array[i][i : x - i])
    deq.extend([row[x - i - 1] for row in array[i + 1 : y - i - 1]])
    deq.extend(array[y - i - 1][i : x - i][::-1])
    deq.extend([row[i] for row in array[i + 1 : y - i - 1][::-1]])

    deq.rotate(-n)

    for j in range(i, x - i):  # 위쪽
        answer[i][j] = deq.popleft()
    for j in range(i + 1, y - i - 1):  # 오른쪽
        answer[j][x - i - 1] = deq.popleft()
    for j in range(x - i - 1, i - 1, -1):  # 아래쪽
        answer[y - i - 1][j] = deq.popleft()
    for j in range(y - i - 2, i, -1):  # 왼쪽
        answer[j][i] = deq.popleft()

for line in answer:
    print(" ".join(line))