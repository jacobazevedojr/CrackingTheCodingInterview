# Write an algorithm such that if an element in an M x N matrix is 0, its entire row and column is set to zero

def zeroMatrix(matrix):
    rows = [False] * len(matrix)
    columns = [False] * len(matrix[0])

    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == 0:
                rows[row] = True
                columns[column] = True

    for i in range(len(rows)):
        if rows[i]:
            matrix[i] = [0] * len(matrix[0])

    for j in range(len(columns)):
        if columns[j]:
            for i in range(len(matrix)):
                matrix[i][j] = 0

matrix = []
N = 4
count = 1

for i in range(N):
    row = []
    for j in range(N):
        row.append(count)
        count += 1
    matrix.append(row)

matrix[0][3] = 0
matrix[2][0] = 0

for i in range(N):
    print(matrix[i])

print()

zeroMatrix(matrix)

for i in range(N):
    print(matrix[i])
