import sys
from heapq import heappush, heappop

input = sys.stdin.readline

for _ in range(int(input())):
    m = int(input())
    nums = []
    for _ in range(m // 10 + (m % 10 > 0)):
        nums.extend(map(int, input().split()))
    max_heap = []
    min_heap = []
    answer = []
    for i in range(m):
        if i % 2 == 0:
            if not min_heap or min_heap[0] >= nums[i]:
                heappush(max_heap, (-nums[i]))
            else:
                heappush(min_heap, nums[i])
                heappush(max_heap, -heappop(min_heap))
            answer.append(-max_heap[0])
        else:
            if -max_heap[0] <= nums[i]:
                heappush(min_heap, nums[i])
            else:
                heappush(max_heap, -nums[i])
                heappush(min_heap, -heappop(max_heap))
    out_len = len(answer)
    print(out_len)
    for i in range(out_len // 10):
        print(*answer[i * 10 : (i + 1) * 10])
    if out_len % 10 > 0:
        print(*answer[out_len // 10 * 10 :])