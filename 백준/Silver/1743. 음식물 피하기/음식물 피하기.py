import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]

for i in range(k):
  x, y = map(int, input().split())
  graph[x - 1][y - 1] = 1

count = 0
arr = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  global count
  if x >= n or x < 0 or y >= m or y < 0:
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    count += 1
    for i in range(4):
      dfs(x + dx[i], y + dy[i])
    return True
  return False

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      arr.append(count)
      count = 0
    
print(max(arr))