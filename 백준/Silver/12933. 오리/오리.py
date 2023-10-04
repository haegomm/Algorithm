def find_duck(start):
    global ans
    ori = 'quack'
    ori_idx = 0
    new_ori = True
    for i in range(start, len(words)):
        if words[i] == ori[ori_idx]:
            if words[i] == 'k':
                if new_ori:
                    ans += 1
                    new_ori = False
                words[i] = 0
                ori_idx = 0
                continue
            words[i] = 0
            ori_idx += 1


words = list(input())
ans = 0

if words[0] != "q" or words[-1] != "k" or len(words) % 5:
    print(-1)
    exit()

for idx in range(len(words) - 4):
    if words[idx] == 'q':
        find_duck(idx)

if any(words) or ans == 0:
    print(-1)
else:
    print(ans)