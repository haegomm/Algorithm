word = input()
changes = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for change in changes:
    word = word.replace(change, ".")

print(len(word))