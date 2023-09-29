n = int(input())
d = [0, 1]

for k in range(1, n):
    d.append(d[k] + d[k - 1])

print(d[n])