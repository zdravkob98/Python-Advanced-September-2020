rows, cows = [int(x) for x in input().split(', ')]

matrix = []

for i in range(rows):
    matrix.append([int(x) for x in input().split(' ')])

for j in range(cows):
    total = 0
    for i in range(rows):
        total += matrix[i][j]
    print(total)