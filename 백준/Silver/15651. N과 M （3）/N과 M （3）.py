N, M = map(int, input().split())
S = []


def dfs():
    if len(S) == M:
        print(' '.join(map(str, S)))
        return

    for i in range(1, N + 1):
        S.append(i)
        dfs()
        S.pop()


dfs()