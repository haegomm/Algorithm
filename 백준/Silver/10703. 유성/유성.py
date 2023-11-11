import sys
input = sys.stdin.readline

def search_distance():
    distance = n-1
    for j in range(m):
        max_meteor = 0
        min_ground = n-1
        flag = False
        for i in range(n):
            if picture[i][j] == 'X':
                max_meteor = max(max_meteor, i)
                flag = True
            elif picture[i][j] == '#':
                min_ground = min(min_ground, i)
                break
        if flag:
            distance = min(distance, min_ground - max_meteor - 1)

    return distance

n, m = map(int, input().split())
picture = [(input().strip()) for _ in range(n)]
result = [['.']*m for _ in range(n)]
down = search_distance()

for j in range(m):
    for i in range(n):
        if picture[i][j] == 'X':
            result[i+down][j] = 'X'
        elif picture[i][j] == '#':
            result[i][j] = '#'

for line in result:
    print(''.join(line))