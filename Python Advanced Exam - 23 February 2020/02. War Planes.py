rows = int(input())
matrix = [input().split() for _ in range(rows)]
command = int(input())

def p_positoin(matrix, rows):
    for i in range(rows):
        for j in range(rows):
            if matrix[i][j] == 'p':
                return i, j

def is_valid(next_pos, rows):
    flag = False
    row = next_pos[0]
    col = next_pos[1]
    if 0 <= row < rows and 0 <= col < rows:
        flag = True
    return flag

def find_targets(matrix, rows):
    flag = True
    targets_left = 0
    targets = 0
    for i in range(rows):
        for j in range(rows):
            if matrix[i][j] != 'p' and matrix[i][j] != '.' and matrix[i][j] != 'x':
                targets_left += 1
                flag = False
            if matrix[i][j] == 'x':
                targets += 1
    if flag:
        return targets
    else:
        return targets_left

def final_check(matrix,rows):
    flag = True
    for i in range(rows):
        for j in range(rows):
                if matrix[i][j] != 'p' and matrix[i][j] != '.' and matrix[i][j] != 'x':
                    flag = False
    return flag

def performance(matrix, rows):
    if is_valid(next_pos, rows):
        if action == 'shoot':
            matrix[next_pos[0]][next_pos[1]] = 'x'
        elif action == 'move':
            if matrix[next_pos[0]][next_pos[1]] == '.':
                matrix[next_pos[0]][next_pos[1]] = 'p'
                matrix[current_position[0]][current_position[1]] = '.'


for _ in range(command):
    if not final_check(matrix, rows):
        token = input().split()
        action = token[0]
        direction = token[1]
        size = int(token[2])

        current_position = p_positoin(matrix, rows)

        if direction == 'up':
            next_pos = current_position[0] - size, current_position[1]
            performance(matrix, rows)

        elif direction == 'down':
            next_pos = current_position[0] + size, current_position[1]
            performance(matrix, rows)

        elif direction == 'left':
            next_pos = current_position[0], current_position[1] - size
            performance(matrix, rows)

        elif direction == 'right':
            next_pos = current_position[0], current_position[1] + size
            performance(matrix, rows)
    else:
        break

if final_check(matrix,rows):
    print(f'Mission accomplished! All {find_targets(matrix,rows)} targets destroyed.')
else:
    print(f'Mission failed! {find_targets(matrix,rows)} targets left.')

for row in matrix:
    print(' '.join(map(str, row)))