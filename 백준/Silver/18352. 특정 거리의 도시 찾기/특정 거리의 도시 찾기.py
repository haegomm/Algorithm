from collections import deque

def distance(v):
    visited[v] = 0
    queue = deque([v])

    while queue:
        cur_v = queue.popleft()
        if visited[cur_v] == k:
            ans.append(cur_v)
        for next_v in city[cur_v]:
            if visited[next_v] == -1:
                visited[next_v] = visited[cur_v] + 1
                queue.append(next_v)


n, m, k, s = map(int, input().split())
city = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
ans = []

for _ in range(m):
    c1, c2 = map(int, input().split())
    city[c1].append(c2)

distance(s)
ans.sort()
if not ans:
    print(-1)
else:
    print(*ans, sep='\n')
