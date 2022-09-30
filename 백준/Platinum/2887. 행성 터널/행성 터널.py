# 행성 터널
from heapq import heappop, heappush
import sys
input = sys.stdin.readline


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


def union(a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# (cost, a, b) a와 b를 잇는 비용을 heap에 push
def edges_cal(loc, k):
    *c_0, idx_0 = loc.pop()
    while loc:
        *c, idx = loc.pop()
        cost = abs(c[k] - c_0[k])
        heappush(heap, (cost, idx, idx_0))
        idx_0 = idx
        c_0 = c


# 입력받기
node_cnt = int(input())
loc = []
for idx in range(node_cnt):
    x, y, z = map(int, input().split())
    loc.append((x, y, z, idx))

# 힙생성, 각 축을 기준으로 정렬후 간선의 길이를 구해서 heappush
heap = []
for i in range(3):
    loc_0 = sorted(loc, key=lambda c: c[i])
    edges_cal(loc_0, i)


parent = list(range(node_cnt))          # 부모 리스트
result = 0                              # 결과 == cost 합친거
counts = 0                              # counts cost합칠때마다 1씩 증가 while 종료조건


while counts < node_cnt - 1:
    cost, a, b = heappop(heap)

    a_root, b_root = find_set(a), find_set(b)

    if a_root != b_root:
        union(a_root, b_root)
        result += cost
        counts += 1

print(result)