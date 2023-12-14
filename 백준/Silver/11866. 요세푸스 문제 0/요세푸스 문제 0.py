from collections import deque

n, k = map(int, input().split())
arr = deque(range(1, n+1))
ans = []

while arr:
    arr.rotate(-k+1)
    ans.append(str(arr.popleft()))

print("<" + ', '.join(ans) + ">")