words = input()
chk = [0, 0]

chk[int(words[0])] += 1

for i in range(1, len(words)):
    if words[i] != words[i-1]:
        chk[int(words[i])] += 1

print(min(chk))