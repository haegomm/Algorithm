def solution(participant, completion):
    from collections import Counter

    participant_count = Counter(participant)
    completion_count = Counter(completion)

    answer = participant_count - completion_count

    return list(answer.keys())[0]