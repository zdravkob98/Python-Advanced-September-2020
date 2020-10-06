def find_P(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'P':
                return (i, j)

def active(current, rows, cols):
    current_row = current[0]
    current_col = current[1]
    return 0 <= current_row < rows and 0 <= current_col < cols


def bunnies (cows, rols, matrix):
    changes = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'B':
                possibles = []
                possibles.append([i - 1, j])
                possibles.append([i + 1, j])
                possibles.append([i, j - 1])
                possibles.append([i, j + 1])
                for possible in possibles:
                    if active(possible, rows, cols):
                        r = possible[0]
                        c = possible[1]
                        changes.append([r, c])
    for change in changes:
        change_r = change[0]
        change_c = change[1]
        matrix[change_r][change_c] = 'B'




rows, cols = [int(x) for x in input().split()]

matrix = []
for _ in range(rows):
    matrix.append([x for x in input()])

command = input()


flag = False
black_flag = False

for comm in command:
    # for p_row in matrix:
    #     print(' '.join(map(str, p_row)))

    if comm == 'U':
        start_possition = find_P(rows, cols)
        if start_possition :
            row = start_possition[0]
            col = start_possition[1]
            #must repair
            current = row - 1, col
            if active(current, rows, cols):
                #must repair
                matrix[row -1][col] = matrix[row][col]
                matrix[row][col] = '.'
                bunnies(cols, rows, matrix)

            else:
                matrix[row][col] = '.'
                bunnies(cols, rows, matrix)
                flag = True
                break
        else:
            black_flag = True
            break

    elif comm == 'D':
        start_possition = find_P(rows, cols)
        if start_possition:
            row = start_possition[0]
            col = start_possition[1]
            # must repair
            current = row + 1, col
            if active(current, rows, cols):
                # must repair
                matrix[row + 1][col] = matrix[row][col]
                matrix[row][col] = '.'
                bunnies(cols, rows, matrix)

            else:
                matrix[row][col] = '.'
                bunnies(cols, rows, matrix)
                flag = True
                break
        else:
            black_flag = True
            break

    elif comm == 'L':
        start_possition = find_P(rows, cols)
        if start_possition:
            row = start_possition[0]
            col = start_possition[1]
            # must repair
            current = row , col - 1
            if active(current, rows, cols):
                # must repair
                matrix[row][col - 1] = matrix[row][col]
                matrix[row][col] = '.'
                bunnies(cols, rows, matrix)

            else:
                matrix[row][col] = '.'
                bunnies(cols, rows, matrix)
                flag = True
                break
        else:
            black_flag = True
            break

    elif comm == 'R':
        start_possition = find_P(rows, cols)
        if start_possition:
            row = start_possition[0]
            col = start_possition[1]
            # must repair
            current = row , col + 1
            if active(current, rows, cols):
                # must repair
                matrix[row][col + 1] = matrix[row][col]
                matrix[row][col] = '.'
                bunnies(cols, rows, matrix)

            else:
                matrix[row][col] = '.'
                bunnies(cols, rows, matrix)
                flag = True
                break
        else:
            black_flag = True
            break
    else:
        bunnies(cols, rows, matrix)

for p_row in matrix:
    print(''.join(map(str, p_row)))

if flag:
    print(f'won: {row} {col}')
if black_flag:
    print(f'dead: {current[0]} {current[1]}')