n = input()
cnt = [0] * 9
for x in n:
    i = int(x)
    if i == 9:
        i = 6
    cnt[i] += 1
cnt[6] = (cnt[6]+1) // 2
print(max(cnt))