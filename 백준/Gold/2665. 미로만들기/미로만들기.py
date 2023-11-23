import heapq

def dijkstra(n, maze):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    changes = [[float('inf')] * n for _ in range(n)]
    queue = [(0, 0, 0)]  # 변경 횟수, x, y
    changes[0][0] = 0

    while queue:
        change, x, y = heapq.heappop(queue)
        if x == n - 1 and y == n - 1:
            return change
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                next_change = change + (1 if maze[nx][ny] == '0' else 0)
                if changes[nx][ny] > next_change:
                    changes[nx][ny] = next_change
                    heapq.heappush(queue, (next_change, nx, ny))

n = int(input())
maze = [input().strip() for _ in range(n)]
print(dijkstra(n, maze))
