n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = []


def dfs():
    for i in range(n):
        if len(ans) == m:
            print(' '.join(map(str, ans)))
            return
        ans.append(nums[i])
        dfs()
        ans.pop()


dfs()