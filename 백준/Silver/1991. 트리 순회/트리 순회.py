# 트리 순회

# 노드 개수
node_cnt = int(input())

# 부모 자식 정보
pa = dict()
ch1 = dict()
ch2 = dict()

node_list = []
# 각 노드 정보 받기
for i in range(node_cnt):
    node, sub1, sub2 = input().split()

    node_list.append(node)

    if sub1 != '.':
        pa[sub1] = node
        ch1[node] = sub1

    if sub2 != '.':
        pa[sub2] = node
        ch2[node] = sub2

def find_root(r):
    while pa.get(r, 'no_parent') != 'no_parent':
        r = pa[r]
    return r

root = find_root(node_list[0])

a = ''
def preorder(n):
    global a
    if n:
        a += n
        preorder(ch1.get(n, 0))
        preorder(ch2.get(n, 0))
preorder(root)
print(a)

b = ''
def inorder(n):
    global b
    if n:
        inorder(ch1.get(n, 0))
        b += n
        inorder(ch2.get(n, 0))
inorder(root)
print(b)

c = ''
def postorder(n):
    global c
    if n:
        postorder(ch1.get(n, 0))
        postorder(ch2.get(n, 0))
        c += n
postorder(root)
print(c)