n, k = map(int, input().split())

arr = list(range(1, n + 1))
answer = []
cnt = 0
while arr:
    cnt += k - 1
    if cnt >= len(arr):
        cnt %= len(arr)

    answer.append(arr.pop(cnt))

print('<' + ', '.join(map(str, answer)) + '>')