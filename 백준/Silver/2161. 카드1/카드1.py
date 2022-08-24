card = list(range(1, int(input()) + 1))

result = []
while True:
    if len(card) == 1:
        break
    result.append(card.pop(0))
    card.append(card.pop(0))
result += card

print(*result)