import sys
import heapq as hq

n = int(input())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num:
        hq.heappush(heap, (-num, num))
    else:
        if len(heap) >= 1:
            print(hq.heappop(heap)[1])
        else:
            print(0)