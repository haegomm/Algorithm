n, target = map(int, input().split())
money_list = [int(input()) for _ in range(n)]

money_cnt = 0

idx = len(money_list) - 1

# while target > 0:
#     if target >= money_list[idx]:
#         target -= money_list[idx]
#         money_cnt += 1
#     else:
#         idx -= 1

# print(money_cnt)

while target > 0:
    n_target = target % money_list[idx]

    if n_target != target:
        money_cnt += target // money_list[idx]
        target = n_target
    idx -= 1

print(money_cnt)