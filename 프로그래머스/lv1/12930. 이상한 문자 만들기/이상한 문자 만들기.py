def solution(s):
    words = s.split(' ')
    answer = []

    for word in words:
        word = list(word)
        for i, values in enumerate(word):
            if i % 2 == 0:
                word[i] = values.upper()
            else:
                word[i] = values.lower()
        word = "".join(word)
        answer += [word]
    answer = " ".join(answer)

    return answer