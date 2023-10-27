import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    global ans
    visited[v] = True
    team.append(v)
    next_v = choice[v]          
    if visited[next_v] == True:
        if next_v in team:
            ans -= len(team[team.index(next_v):])
        return
    else:
        dfs(next_v)

for _ in range(int(input())):
    n = int(input())
    choice = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    ans = n

    for i in range(1, n+1):
        if not visited[i]:
            team = []
            dfs(i)
    
    print(ans)