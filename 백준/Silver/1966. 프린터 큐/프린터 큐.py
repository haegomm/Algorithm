import sys
from collections import deque
import heapq

tc = int(sys.stdin.readline())

for _ in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    documents = deque(enumerate(map(int, sys.stdin.readline().split())))
    priority_queue = []
    for idx, priority in documents:
        heapq.heappush(priority_queue, -priority)
    cnt = 0
    while documents:
        idx, priority = documents.popleft()
        if priority == -priority_queue[0]:
            heapq.heappop(priority_queue)
            cnt += 1
            if idx == m:
                print(cnt)
                break
        else:
            documents.append((idx, priority))
