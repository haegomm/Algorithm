from collections import deque


def bfs():
    global k
    ans = 0

    while k > 0:
        now = deq.popleft()
        for move in [now + 1, now - 1]:
            if move not in visited and k > 0:
                visited[move] = visited[now] + 1
                ans += visited[move]
                k -= 1
                deq.append(move)

    return ans


n, k = map(int, input().split())
water = list(map(int, input().split()))
deq = deque(water)
visited = dict()

for w in water:
    visited[w] = 0

print(bfs())