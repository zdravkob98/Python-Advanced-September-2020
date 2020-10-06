rows, cols = [int(x) for x in input().split()]

matrix = []
best_sum = -9999
best_matrix = []

for _ in range(rows):
    line = [int(x) for x in input().split()]
    matrix.append(line)

for i in range(rows-2):
    for j in range(cols-2):
        sub_matrix = []
        current_sum = 0
        row_counter = 0

        for r in range(i, i + 3):
            sub_matrix.append([])
            for c in range(j, j + 3):
                sub_matrix[row_counter].append(matrix[r][c])
                current_sum += matrix[r][c]
            row_counter += 1

        if current_sum > best_sum:
            best_sum = current_sum
            best_matrix = sub_matrix

print(f'Sum = {best_sum}')
for row in best_matrix:
    print(' '.join(map(str,row)))