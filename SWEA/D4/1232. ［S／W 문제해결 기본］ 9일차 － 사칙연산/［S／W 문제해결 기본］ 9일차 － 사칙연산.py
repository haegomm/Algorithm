cal = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x // y,
}


def post_order(n):
    if tree[n][1] and tree[n][2]:
        l = post_order(tree[n][1])
        r = post_order(tree[n][2])
        return cal[tree[n][0]](l, r)
    else:
        return tree[n][1]


for tc in range(1, 11):
    v = int(input())
    tree = [[0]*3 for _ in range(v+1)]

    for _ in range(v):
        info = list(input().split())
        idx = int(info[0])

        if len(info) == 4:
            tree[idx][0] = info[1]
            tree[idx][1] = int(info[2])
            tree[idx][2] = int(info[3])

        else:
            tree[idx][1] = int(info[1])

    print(f'#{tc} {post_order(1)}')