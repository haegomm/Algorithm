n = int(input())
time_line = [list(map(int, input().split())) for _ in range(n)]

time_line.sort(key=lambda x: x[0])
time_line.sort(key=lambda x: x[1])

answer = 0
end = 0

for i in range(n):
    if time_line[i][0] >= end:
        end = time_line[i][1]
        answer += 1

print(answer)