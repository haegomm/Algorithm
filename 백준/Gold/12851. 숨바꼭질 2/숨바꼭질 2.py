import sys
from collections import deque
input = sys.stdin.readline

def bfs(n,k):
    if n == k:
        return 0, 1
    
    queue = deque([n])
    visited = [-1] * 100001 # 시간 기록
    visited[n] = 0
    cnt = 0

    while  queue:
        x = queue.popleft()

        if x == k:
            cnt += 1

        for next_x in [(2 * x), (x - 1), (x + 1)]:
            if 0 <= next_x <= 100000:
                if visited[next_x] == -1 or visited[next_x] >= visited[x] + 1:
                    visited[next_x] = visited[x] + 1
                    queue.append(next_x)
    
    return visited[k], cnt

n, k = map(int, input().split())
print(*bfs(n, k), sep='\n')