n = int(input())
history = [list(map(int, input().split())) for _ in range(n)]

chk = [0] * n

for i in range(n):
    for k in range(i + 1, n):
            for g in range(5):
                if history[i][g] == history[k][g]:
                    chk[i] += 1
                    chk[k] += 1
                    break

max_chk = max(chk)
candidates = [i for i in range(n) if chk[i] == max_chk]

print(min(candidates) + 1)