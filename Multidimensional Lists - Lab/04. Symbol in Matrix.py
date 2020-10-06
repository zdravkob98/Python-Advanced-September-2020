rows = int(input())
flag = False
matrix = []

for i in range(rows):
    matrix.append(input())

symbol = input()

for i in range(rows):
    if flag:
        break
    for j in range(rows):
        if matrix[i][j] == symbol:
            print(f'({i}, {j})')
            flag = True

if not flag:
    print(f'{symbol} does not occur in the matrix')


#------------------------------------------------------------------------------------------------------------------------

rows = int(input())

matrix = []
for i in range(rows):
    matrix.append(input())

symbol = input()

def occurrence (matrix, rows, symbol):
    for i in range(rows):
        for j in range(rows):
            if matrix[i][j] == symbol:
                return i, j

positional = occurrence(matrix,rows,symbol)

if occurrence(matrix,rows,symbol):
    print(positional)
else:
    print(f'{symbol} does not occur in the matrix')