def solution(sizes):
    max_lengths = []
    min_lengths = []
    for card in sizes:
        max_lengths.append(max(card))
        min_lengths.append(min(card))

    wallet_width = max(max_lengths)
    wallet_height = max(min_lengths)

    return wallet_width * wallet_height