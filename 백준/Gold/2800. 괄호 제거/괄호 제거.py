import sys
from itertools import combinations

string = sys.stdin.readline().rstrip()
idx_stack = []
stack = []
answer = set()

for idx, v in enumerate(list(string)):
    if v == '(':
        stack.append(idx)
    elif v == ')':
        start = stack.pop()
        end = idx
        idx_stack.append([start, end])

for i in range(1, len(idx_stack) + 1):
    for j in combinations(idx_stack, i):
        tmp = list(string)
        for k in j:
            start, end = k
            tmp[start] = ''
            tmp[end] = ''
        answer.add(''.join(tmp))
for i in sorted(list(answer)):
    print(i)