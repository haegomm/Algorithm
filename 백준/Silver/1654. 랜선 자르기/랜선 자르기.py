k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]

start, end = 1, max(cables)

ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for cable in cables:
        cnt += cable // mid

    if cnt >= n:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)