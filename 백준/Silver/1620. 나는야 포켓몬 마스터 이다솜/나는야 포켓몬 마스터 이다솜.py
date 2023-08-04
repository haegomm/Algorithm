import sys

n, m = map(int, sys.stdin.readline().split())
pokemon = {}

for idx in range(1, n + 1):
    temp = sys.stdin.readline().strip()
    pokemon[idx] = temp
    pokemon[temp] = idx

for _ in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        print(pokemon[int(q)])
    else:
        print(pokemon[q])