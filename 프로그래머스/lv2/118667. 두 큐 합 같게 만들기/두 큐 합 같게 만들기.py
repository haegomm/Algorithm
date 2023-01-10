from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sumq1 = sum(q1)
    mid = (sumq1 + sum(q2)) // 2
    cnt = 0

    while q1 and q2:
        if sumq1 == mid:
            return cnt
        elif sumq1 > mid:
            sumq1 -= q1.popleft()
        else:
            q1.append(q2.popleft())
            sumq1 += q1[-1]

        cnt += 1

    return -1
