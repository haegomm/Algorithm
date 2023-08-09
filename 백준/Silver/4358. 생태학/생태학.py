import sys
from collections import Counter

trees = Counter(sys.stdin.read().split("\n"))
del trees[""]
total = sum(trees.values())

ordered_trees = sorted(trees.items())
for tree, num in ordered_trees:
    print(f"{tree} {100 * num / total:.4f}")