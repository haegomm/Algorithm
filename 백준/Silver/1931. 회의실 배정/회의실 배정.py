import sys
n = int(sys.stdin.readline())
time = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
time.sort(key=lambda x: (x[1], x[0]))

i = 0
j = 1
cnt = 1
while j < n:
    if time[i][1] <= time[j][0]:
        cnt += 1
        i = j
        j += 1
    else:
        j += 1

print(cnt)