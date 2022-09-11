import datetime

t = int(input())

for tc in range(1, t + 1):
    m1, d1, m2, d2 = map(int, input().split())

    day1 = datetime.date(2022, m1, d1)
    day2 = datetime.date(2022, m2, d2)
    result = day2 - day1

    print(f'#{tc} {result.days + 1}')