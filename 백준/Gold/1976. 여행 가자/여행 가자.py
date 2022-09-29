def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


def union_set(x, y):
    if x != y:
        if x < y:
            parent[y] = x
        else:
            parent[x] = y


n = int(input())
m = int(input())
parent = list(range(n+1))

for i in range(n):
    line = input().split()
    for j in range(n):
        if line[j] == '1':
            i_root, j_root = find_set(i + 1), find_set(j + 1)
            union_set(i_root, j_root)

plans = list(map(int, input().split()))
root = find_set(plans[0])
result = 'YES'

for i in range(1, m):
    if root != find_set(plans[i]):
        result = 'NO'
        break

print(result)