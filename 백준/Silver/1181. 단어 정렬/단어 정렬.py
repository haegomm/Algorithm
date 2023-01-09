n = int(input())
words = []

for _ in range(n):
    word = str(input())
    word_count = len(word)
    words.append((word, word_count))

words = list(set(words))

words.sort(key=lambda word: (word[1], word[0]))

for word in words:
    print(word[0])