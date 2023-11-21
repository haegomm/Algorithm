from itertools import zip_longest

words = []
for _ in range(5):
    words.append(input())

zipped_words = zip_longest(*words, fillvalue='')
cul_words = ''.join(''.join(w) for w in zipped_words)

print(cul_words)