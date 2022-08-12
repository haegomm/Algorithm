# replace 사용
word = input()
changes = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for change in changes:
    word = word.replace(change, ".")
    # 변경된 문자열을 . 1개로 바꿔서 하나의 갯수로 세어지게 만든다.

print(len(word))


# count 사용
word = input()
changes = ['=', '-', 'lj', 'nj', 'dz=']  # 문자열
total = len(word)

for change in changes:
    total -= word.count(change)

print(total)
