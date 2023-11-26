s = list(input())
k = input()
word = []
for i in s:
	if i.isalpha():
		word.append(i)
word = ''.join(word)
if k in word:
	print(1)
else:
	print(0)