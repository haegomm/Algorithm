import sys

word = list(map(str, sys.stdin.readline().rstrip("\n")))
res = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        one = word[:i]
        two = word[i:j]
        three = word[j:]

        one.reverse()
        two.reverse()
        three.reverse()

        res.append("".join(one + two + three))

print(min(res))