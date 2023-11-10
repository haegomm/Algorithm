from collections import Counter

for _ in range(int(input())):
    text = input()
    counter = Counter([char for char in text if char.isalpha()])

    most_common = counter.most_common()
    if (len(most_common) > 1 and most_common[0][1] == most_common[1][1]):
        print('?')
    else:
        print(most_common[0][0])