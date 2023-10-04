def move(p, x, y):
    global cnt
    px = abs(p[0] - x)
    py = abs(p[1] - y)
    cnt += px + py

    return (x, y)


keyboard = ['qwertyuiop', 'asdfghjkl0', 'zxcvbnm000']

l, r = input().split()
words = input()
cnt = 0

for i in range(3):
    for j in range(10):
        if keyboard[i][j] == l:
            l = (i, j)
        elif keyboard[i][j] == r:
            r = (i, j)

for w in words:
    cnt += 1
    for i in range(3):
        for j in range(10):
            if keyboard[i][j] == w:
                if (i != 2 and j < 5) or (i == 2 and j < 4):
                    l = move(l, i, j)
                    break
                else:
                    r = move(r, i, j)
                    break

print(cnt)