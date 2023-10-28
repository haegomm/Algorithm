n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
ans = []

def dfs():
    if len(ans) == m:
        print(*ans)
        return
    prev = 0
    for i in range(n):
        if not visited[i] and nums[i] != prev:
            visited[i] = True
            ans.append(nums[i])
            dfs()
            visited[i] = False
            ans.pop()
            prev = nums[i]

dfs()