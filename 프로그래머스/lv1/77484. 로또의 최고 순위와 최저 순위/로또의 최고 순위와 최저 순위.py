def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    same = len(set(lottos) & set(win_nums))
    zeo = lottos.count(0)
    answer = [rank[same+zeo], rank[same]]
    return answer