h, m = map(int, input().split())

tt = h * 60 + m
tt = (tt - 45) % 1440

h = tt // 60
m = tt % 60

print(h, m)