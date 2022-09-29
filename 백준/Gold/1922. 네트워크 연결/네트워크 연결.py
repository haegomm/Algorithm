def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


computer_cnt = int(input())
edges_cnt = int(input())

parent = list(range(computer_cnt + 1))

edges = []
for _ in range(edges_cnt):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()        # 리스트 안 튜플은 맨앞 cost를 기준으로 정렬한다! 밑에서 작은 cost부터 불러오게 됨
connect_cnt = 0     # 연결횟수
cost_sum = 0        # cost합

for cost, a, b in edges:
    a_root, b_root = find_set(a), find_set(b)   # 대표원소 찾기

    if a_root != b_root:                        # 루트가 다르다 == 다른 집합이다(서로소) == 컴퓨터 연결이 아직 안되어있다!
        parent[b_root] = a_root                 # 합쳐주고
        connect_cnt += 1                        # 연결수 +1
        cost_sum += cost                        # cost 더해주기
        
        if connect_cnt >= computer_cnt - 1:     # 컴퓨터 개수 - 1 == 연결횟수 가 가장 적게 연결되면서 전부 연결되는 경우이다!
            break
        
print(cost_sum)