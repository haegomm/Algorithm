from collections import deque
from sys import stdin


def chk():
    stack = deque()
    for start, end in circle:
        while stack and stack[-1] < start:
            stack.pop()
        if stack:
            if start <= stack[-1] <= end:
                return False
        stack.append(end)
    return True


circle = []
n = int(stdin.readline())
for i in range(n):
    center, radius = map(int, stdin.readline().split())
    circle.append((center - radius, center + radius))
circle.sort()

if chk():
    print('YES')
else:
    print('NO')