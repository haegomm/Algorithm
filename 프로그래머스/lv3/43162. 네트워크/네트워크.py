from collections import deque

def solution(n, computers):
    def dfs(v):
        visited[v] = True
        
        for next_node in range(n):
            if not visited[next_node] and computers[v][next_node] == 1:
                dfs(next_node)
        
    answer = 0
    visited = [False] * n
    
    for v in range(n):
        if not visited[v]:
            dfs(v)
            answer += 1
    return answer