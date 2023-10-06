def solution(begin, target, words):
    # 한 문자만 다른지 확인하는 함수
    def is_one_letter_different(a, b):
        diff_count = sum([1 for x, y in zip(a, b) if x != y])
        return diff_count == 1

    def dfs(cnt, word):
        nonlocal answer
        if word == target:
            answer = cnt
            return
        for idx, w in enumerate(words):
            if not visited[idx] and is_one_letter_different(word, w):
                visited[idx] = True
                dfs(cnt + 1, w)
                visited[idx] = False

    # target이 words에 없으면 변환 불가능
    if target not in words:
        return 0

    answer = float('inf')  # 아주 큰 값으로 초기화
    visited = [False] * len(words)
    dfs(0, begin)

    return answer if answer != float('inf') else 0
