from collections import defaultdict


def solution(genres, plays):
    answer = []
    music = defaultdict(list)
    rank = defaultdict(int)
    for idx, g in enumerate(genres):
        music[g].append((plays[idx], idx))
        rank[g] += plays[idx]
    for key in music:
        music[key] = sorted(music[key], key=lambda x: x[0], reverse=True)
    sorted_rank = sorted(rank.items(), key=lambda item: item[1], reverse=True)
    for key, _ in sorted_rank:
        for i in range(min(2, len(music[key]))):
            answer.append(music[key][i][1])
    return answer