n = int(input())
switch = [0] + list(map(int, input().split()))
students = int(input())

for _ in range(students):
    student, s_switch = map(int, input().split())

    if student == 1:
        for i in range(s_switch, n + 1, s_switch):
            switch[i] = int(not switch[i])
    else:
        for j in range(n):
            if s_switch - j >= 1 and s_switch + j <= n and switch[s_switch - j] == switch[s_switch + j]:
                for k in s_switch - j, s_switch + j:
                    switch[k] = int(not switch[k])
            else:
                switch[s_switch] = int(not switch[s_switch])
                break

for r in range(1, n, 20):
    print(*switch[r:r+20])