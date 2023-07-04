from collections import deque

for t in range(int(input())):
    n, m = map(int, input().split())
    document = deque(list(map(int, input().split())))
    cnt = 0
    while document:
        best = max(document)
        now = document.popleft()
        m -= 1

        if best == now:
            cnt += 1
            if m < 0:
                print(cnt)
                break

        else:
            document.append(now)
            if m < 0:
                m = len(document) - 1