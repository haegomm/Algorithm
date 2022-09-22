import sys
# sys.stdin = open('input.txt')

# t = int(input())
#
# for tc in range(1, t+1):
#     n = int(input())
#     time = [list(map(int, input().split())) for _ in range(n)]
#
#     # 종료시간 기준으로 정렬하기
#     time = sorted(time, key= lambda x : x[1])
#
#     # 시작 조건
#     i = 0
#     j = 1
#     cnt = 1 # 리스트의 0번째는 시작시간이 제일 빨리 끝나는 경우이므로 일단 화물을 옮기는 것
#     while j < n:
#         if time[i][1] <= time[j][0]:
#             cnt += 1
#             i = j
#             j += 1
#         else:
#             j += 1
#
#     print(f'#{tc} {cnt}')


n = int(sys.stdin.readline())
time = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

time = sorted(time, key= lambda x : x[0])
time = sorted(time, key= lambda x : x[1])

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