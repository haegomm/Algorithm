n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = []


def dfs(start):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(start, n):
        ans.append(nums[i])
        dfs(i)
        ans.pop()


dfs(0)