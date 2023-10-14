n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
ans = []


def dfs():
    if len(ans) == m:
        print(*ans)
        return
    for i in range(n):
        if not visited[i]:
            ans.append(nums[i])
            visited[i] = True
            dfs()
            ans.pop()
            visited[i] = False


dfs()