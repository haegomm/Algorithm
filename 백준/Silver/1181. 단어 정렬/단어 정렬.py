import sys

n = int(sys.stdin.readline())
words = []

for _ in range(n):
    word = str(sys.stdin.readline().strip())
    word_count = len(word)
    words.append((word, word_count))

words = list(set(words))

words.sort(key=lambda word: (word[1], word[0]))

for word in words:
    print(word[0])