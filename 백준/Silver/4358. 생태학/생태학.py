import sys

trees = {}
total = 0

while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    if not trees.get(tree):
        trees[tree] = 1
    else:
        trees[tree] += 1
    total += 1

ordered_trees = sorted(trees.items())
for tree, num in ordered_trees:
    print(f'{tree} {num/total*100:.4f}')