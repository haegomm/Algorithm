import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    n, m = map(int, sys.stdin.readline().split())
    documents = list(map(int, sys.stdin.readline().split()))
    que = list(enumerate(documents))
    documents.sort(reverse=True)
    cnt = 0
    for now in documents:
        while que[0][1] != now:
            tmp = que.pop(0)
            que.append(tmp)
        cnt += 1
        if que.pop(0)[0] == m:
            break
    print(cnt)