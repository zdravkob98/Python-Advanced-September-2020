def is_valid(current_pos, n):
    row = current_pos[0]
    col = current_pos[1]
    return 0 <= row < n and 0 <= col < n


def detonate(bomb_row, bomb_col, n, matrix):
    bomb = matrix[bomb_row][bomb_col]
    rows = [-1, -1, -1, 0, 0, 1, 1, 1]
    cols = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        current_pos = [bomb_row + rows[i], bomb_col + cols[i]]
        if is_valid(current_pos, n):
            row = current_pos[0]
            col = current_pos[1]
            if matrix[row][col] <= 0:
                pass
            else:
                matrix[row][col] -= bomb

n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]

bomb_numbers = input().split()

for bomb in bomb_numbers:
    tokens = [int(x) for x in bomb.split(',')]
    bomb_row = tokens[0]
    bomb_col = tokens[1]

    if matrix[bomb_row][bomb_col] <= 0:
        continue
    else:
        detonate(bomb_row, bomb_col, n, matrix)
        matrix[bomb_row][bomb_col] = 0

active = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] > 0:
            active.append(matrix[i][j])

print(f'Alive cells: {len(active)}')
print(f'Sum: {sum(active)}')
for row in matrix:
    print(' '.join(map(str, row)))



