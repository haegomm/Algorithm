def pre_order(node):
    if node != '.':
        print(node, end='')
        pre_order(tree[ord(node)-65][0])
        pre_order(tree[ord(node)-65][1])

def in_order(node):
    if node != '.':
        in_order(tree[ord(node)-65][0])
        print(node, end='')
        in_order(tree[ord(node)-65][1])

def post_order(node):
    if node != '.':
        post_order(tree[ord(node)-65][0])
        post_order(tree[ord(node)-65][1])
        print(node, end='')


v = int(input())
tree = [[0]*3 for _ in range(v)]

for _ in range(v):
    info = list(input().split())

    tree[ord(info[0])-65][0], tree[ord(info[0])-65][1] = info[1], info[2]

pre_order('A')
print()
in_order('A')
print()
post_order('A')