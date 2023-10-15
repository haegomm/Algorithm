n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
ans = []


def dfs(start):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(start, n):
        if not visited[i]:
            ans.append(nums[i])
            visited[i] = True
            dfs(i)
            ans.pop()
            visited[i] = False


dfs(0)