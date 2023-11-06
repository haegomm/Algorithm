def operation_1(matrix):
    return matrix[::-1]

def operation_2(matrix):
    return [row[::-1] for row in matrix]

def operation_3(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def operation_4(matrix):
    return [list(col) for col in zip(*matrix)][::-1]

def operation_5(matrix):
    n, m = len(matrix), len(matrix[0])
    new_matrix = [[0] * m for _ in range(n)]
    mid_n, mid_m = n // 2, m // 2

    for i in range(mid_n):
        for j in range(mid_m):
            new_matrix[i][j + mid_m] = matrix[i][j]
            new_matrix[i + mid_n][j + mid_m] = matrix[i][j + mid_m]
            new_matrix[i + mid_n][j] = matrix[i + mid_n][j + mid_m]
            new_matrix[i][j] = matrix[i + mid_n][j]

    return new_matrix

def operation_6(matrix):
    n, m = len(matrix), len(matrix[0])
    new_matrix = [[0] * m for _ in range(n)]
    mid_n, mid_m = n // 2, m // 2

    for i in range(mid_n):
        for j in range(mid_m):
            new_matrix[i + mid_n][j] = matrix[i][j]
            new_matrix[i][j] = matrix[i][j + mid_m]
            new_matrix[i][j + mid_m] = matrix[i + mid_n][j + mid_m]
            new_matrix[i + mid_n][j + mid_m] = matrix[i + mid_n][j]

    return new_matrix

N, M, R = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
operations = list(map(int, input().split()))

for op in operations:
    if op == 1:
        matrix = operation_1(matrix)
    elif op == 2:
        matrix = operation_2(matrix)
    elif op == 3:
        matrix = operation_3(matrix)
    elif op == 4:
        matrix = operation_4(matrix)
    elif op == 5:
        matrix = operation_5(matrix)
    elif op == 6:
        matrix = operation_6(matrix)

for row in matrix:
    print(' '.join(map(str, row)))