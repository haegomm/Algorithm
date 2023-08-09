import sys
from collections import Counter

trees = Counter(sys.stdin.read().split("\n"))
del trees[""]
total = sum(trees.values())
for tree, num in sorted(trees.items()):
    print(f"{tree} {100 * num / total:.4f}")