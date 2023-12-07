import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
icecream = [[False] * n for _ in range(n)]
res = 0

for _ in range(m):
    num1, num2 = map(int, input().split())
    icecream[num1 - 1][num2 - 1] = True
    icecream[num2 - 1][num1 - 1] = True

for comb in combinations(range(n), 3):
    if icecream[comb[0]][comb[1]] or icecream[comb[0]][comb[2]] or icecream[comb[1]][comb[2]]:
        continue
    res += 1

print(res)