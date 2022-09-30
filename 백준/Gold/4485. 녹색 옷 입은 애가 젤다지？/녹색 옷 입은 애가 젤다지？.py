from heapq import heappop, heappush
import sys
input = sys.stdin.readline

d_r = [0, 0, -1, 1]
d_c = [-1, 1, 0, 0]


def in_range(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    else:
        return False


def dijkstra(size):
    cost[0][0] = board[0][0]
    heap = [(cost[0][0], 0, 0)]

    while heap:
        min_cost, row, col = heappop(heap)

        if min_cost > cost[row][col]:
            continue

        for d in range(4):
            next_row = row + d_r[d]
            next_col = col + d_c[d]

            if in_range(next_row, next_col, size):
                next_cost = min_cost + board[next_row][next_col]

                if next_cost < cost[next_row][next_col]:
                    cost[next_row][next_col] = next_cost
                    heappush(heap, (next_cost, next_row, next_col))
    
    return cost[-1][-1]

INF = 10 * (125 ** 2)
tc = 0

while True:
    tc += 1

    size = int(input())
    if size == 0:
        break

    board = [list(map(int, input().split())) for _ in range(size)]

    
    cost = [[INF] * size for _ in range(size)]

    print(f'Problem {tc}: {dijkstra(size)}')