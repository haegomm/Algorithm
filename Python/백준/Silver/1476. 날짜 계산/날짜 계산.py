E, S, M = list(map(int, input().split()))
now = 1

e, s, m = 1, 1, 1

while True:
    if e == E and s == S and m == M:
        print(now)
        break
    now += 1
    e = e % 15 + 1
    s = s % 28 + 1  
    m = m % 19 + 1 