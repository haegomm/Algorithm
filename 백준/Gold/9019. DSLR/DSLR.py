from collections import deque

def bfs():
    visited = [False] * 10000
    queue = deque([(a, '')])
    visited[a] = True

    while queue:
        num, path = queue.popleft()
        if num == b:
            return path

        d = (num * 2) % 10000
        if not visited[d]:
            visited[d] = True
            queue.append((d, path+'D'))

        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = True
            queue.append((s, path+'S'))
        
        l = num // 1000 + (num % 1000) * 10
        if not visited[l]:
            visited[l] = True
            queue.append((l, path+'L'))
        
        r = num // 10 + (num % 10) * 1000
        if not visited[r]:
            visited[r] = True
            queue.append((r, path+'R'))



for _ in range(int(input())):
    a, b = map(int, input().split())
    print(bfs())