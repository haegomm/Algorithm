arr = [list(map(int, input().split())) for _ in range(9)]

arr_max = 0
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if arr_max < arr[i][j]:
            arr_max = arr[i][j]
            x, y = i, j

print(arr_max)
print(x+1, y+1)