email_word = input()
remove_word = "CAMBRIDGE"

for i in remove_word:
    email_word = email_word.replace(i, "")

print(email_word)
