# t = int(input())
#
# for tc in range(1, t+1):
#
#     n, m = map(int, input().split())
#     no_task_num = list(map(int, input().split()))
#
#     student = []
#     for i in range(1, n+1):
#         if i not in no_task_num:
#             student += str(i)
#
#     print(f'#{tc} {" ".join(student)}')

t = int(input())

for tc in range(1, t + 1):

    n, m = map(int, input().split())
    no_task_num = list(map(int, input().split()))

    student = []
    for i in range(1, n + 1):
        if i not in no_task_num:
            student.append(i)

    yes_task_student = ' '.join(map(str, student))

    print(f'#{tc} {yes_task_student}')

