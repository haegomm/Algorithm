n = int(input())
graph = [[float('inf')] * n for _ in range(n)]

for i in range(n):
    line = input()
    for j, char in enumerate(line):
        if char == 'Y':
            graph[i][j] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

max_friends = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if i != j and graph[i][j] <= 2:
            cnt += 1
    max_friends = max(max_friends, cnt)

print(max_friends)