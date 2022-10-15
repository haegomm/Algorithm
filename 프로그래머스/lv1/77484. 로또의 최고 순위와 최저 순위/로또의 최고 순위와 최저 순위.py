def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    same = len(set(lottos) & set(win_nums))
    zeo = len(list(filter(lambda x: x == 0, lottos)))
    answer = [rank[same+zeo], rank[same]]
    return answer