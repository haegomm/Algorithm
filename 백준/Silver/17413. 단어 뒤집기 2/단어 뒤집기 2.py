import sys

words = list(sys.stdin.readline().rstrip())

idx = 0
start = 0

while idx < len(words):
    if words[idx] == '<':
        idx += 1
        while words[idx] != '>':
            idx += 1
        idx += 1
    elif words[idx].isalnum():
        start = idx
        while idx < len(words) and words[idx].isalnum():
            idx += 1
        temp = words[start:idx]
        temp.reverse()
        words[start:idx] = temp
    else:
        idx += 1

print(''.join(words))