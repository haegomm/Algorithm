left, right = input().split('(^0^)')

left_count = 0
right_count = 0

for i in left:
    if i == '@':
        left_count += 1

for j in right:
    if j == '@':
        right_count += 1


print(left_count, right_count)

#################

left, right = input().split('(^0^)')

left_count = left.count('@')
right_count = right.count('@')

print(left_count, right_count)
