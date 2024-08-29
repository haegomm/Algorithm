from datetime import date

sy, sm, sd = map(int, input().split())
ey, em, ed = map(int, input().split())

start = date(sy, sm, sd)
end = date(ey, em, ed)

ans = (end - start).days

if ey - sy > 1000 or (ey - sy == 1000 and (em > sm or (em == sm and ed >= sd))):
    print('gg')
else:
    print(f'D-{ans}')