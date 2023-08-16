import sys
from heapq import *

input = sys.stdin.readline

N = int(input())
max_heap = []
min_heap = []
check = {}
for _ in range(N):
    p, l = map(int, input().split())
    heappush(max_heap, (-l, -p))
    heappush(min_heap, (l, p))
    check[p] = True

M = int(input())
for _ in range(M):
    command = input()
    if command[0] == 'a':
        command, p, l = command.split()
        p = int(p)
        l = int(l)
        heappush(max_heap, (-l, -p))
        heappush(min_heap, (l, p))
        check[p] = True
    elif command[0] == 'r':
        command, option = command.split()
        if option == '1':
            print(-max_heap[0][1])
        else:
            print(min_heap[0][1])
    else:
        command, p = command.split()
        p = int(p)
        check[p] = False
        while not check[-max_heap[0][1]]:
            heappop(max_heap)
        while not check[min_heap[0][1]]:
            heappop(min_heap)
