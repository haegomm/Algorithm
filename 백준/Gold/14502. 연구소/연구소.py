import sys, copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline


def bfs():
    global ans

    for wallCombi in combinations(empty, 3):
        temp = copy.deepcopy(institute)
        for wx, wy in wallCombi:
            temp[wx][wy] = 1

        virus = deque([(x, y) for x in range(n) for y in range(m) if temp[x][y] == 2])

        while virus:
            x, y = virus.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                    temp[nx][ny] = 2
                    virus.append((nx, ny))

        safe = 0
        for line in temp:
            safe += line.count(0)
        ans = max(ans, safe)


n, m = map(int, input().split())
institute = [list(map(int, input().split())) for _ in range(n)]
empty = [(x, y) for x in range(n) for y in range(m) if institute[x][y] == 0]
ans = 0
bfs()
print(ans)