import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if heap:
            print(heappop(heap))
        else:
            print(0)
    else:
        heappush(heap, num)