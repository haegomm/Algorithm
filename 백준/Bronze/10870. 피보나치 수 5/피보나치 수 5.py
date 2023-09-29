n = int(input())

if n == 0:
    print(0)
else:
    d = [0] * (n + 1)
    d[1] = 1

    for k in range(2, n + 1):
        d[k] = d[k - 1] + d[k - 2]

    print(d[n])