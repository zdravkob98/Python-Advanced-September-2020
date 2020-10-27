def find_s (rows):
    for i in range(rows):
        for j in range(rows):
            if matrix[i][j] == 'S':
                return i, j

def is_valid (next_pos, rows):
    flag = False
    row = next_pos[0]
    col = next_pos[1]
    if 0 <= row < rows and 0 <= col < rows:
        flag = True
    return flag


def find_another_b (rows):
    for i in range(rows):
        for j in range(rows):
            if matrix[i][j] == 'B':
                return i, j

rows = int(input())
matrix = []
food = 0

for i in range(rows):
    matrix.append([x for x in input()])

while True:
    direction = input()
    current_position = find_s(rows)


    if direction == 'up':
        next_pos = (current_position[0] - 1 , current_position[1])
        if is_valid(next_pos, rows):
            if matrix[next_pos[0]][next_pos[1]] == '*':
                food += 1
                matrix[next_pos[0]][next_pos[1]] = 'S'
                matrix[current_position[0]][current_position[1]] = '.'
            elif matrix[next_pos[0]][next_pos[1]] == 'B':
                matrix[current_position[0]][current_position[1]] = '.'
                matrix[next_pos[0]][next_pos[1]] = '.'
                next_B = find_another_b(rows)
                matrix[next_B[0]][next_B[1]] = 'S'
            else:
                matrix[next_pos[0]][next_pos[1]] = 'S'
                matrix[current_position[0]][current_position[1]] = '.'
        else:
            matrix[current_position[0]][current_position[1]] = '.'
            print("Game over!")
            break

    elif direction == 'down':
        next_pos = (current_position[0] + 1, current_position[1])
        if is_valid(next_pos, rows):
            if matrix[next_pos[0]][next_pos[1]] == '*':
                food += 1
                matrix[next_pos[0]][next_pos[1]] = 'S'
                matrix[current_position[0]][current_position[1]] = '.'
            elif matrix[next_pos[0]][next_pos[1]] == 'B':
                matrix[current_position[0]][current_position[1]] = '.'
                matrix[next_pos[0]][next_pos[1]] = '.'
                next_B = find_another_b(rows)
                matrix[next_B[0]][next_B[1]] = 'S'
            else:
                matrix[next_pos[0]][next_pos[1]] = 'S'
                matrix[current_position[0]][current_position[1]] = '.'
        else:
            matrix[current_position[0]][current_position[1]] = '.'
            print("Game over!")
            break

    elif direction == 'left':
        next_pos = (current_position[0], current_position[1] - 1)
        if is_valid(next_pos, rows):
            if matrix[next_pos[0]][next_pos[1]] == '*':
                food += 1
                matrix[next_pos[0]][next_pos[1]] = 'S'
                matrix[current_position[0]][current_position[1]] = '.'
            elif matrix[next_pos[0]][next_pos[1]] == 'B':
                matrix[current_position[0]][current_position[1]] = '.'
                matrix[next_pos[0]][next_pos[1]] = '.'
                next_B = find_another_b(rows)
                matrix[next_B[0]][next_B[1]] = 'S'
            else:
                matrix[next_pos[0]][next_pos[1]] = 'S'
                matrix[current_position[0]][current_position[1]] = '.'
        else:
            matrix[current_position[0]][current_position[1]] = '.'
            print("Game over!")
            break

    elif direction == 'right':
        next_pos = (current_position[0], current_position[1] + 1)
        if is_valid(next_pos, rows):
            if matrix[next_pos[0]][next_pos[1]] == '*':
                food += 1
                matrix[next_pos[0]][next_pos[1]] = 'S'
                matrix[current_position[0]][current_position[1]] = '.'
            elif matrix[next_pos[0]][next_pos[1]] == 'B':
                matrix[current_position[0]][current_position[1]] = '.'
                matrix[next_pos[0]][next_pos[1]] = '.'
                next_B = find_another_b(rows)
                matrix[next_B[0]][next_B[1]] = 'S'
            else:
                matrix[next_pos[0]][next_pos[1]] = 'S'
                matrix[current_position[0]][current_position[1]] = '.'
        else:
            matrix[current_position[0]][current_position[1]] = '.'
            print("Game over!")
            break

    if food == 10:
        print("You won! You fed the snake.")
        break


print(f"Food eaten: {food}")
for r in matrix:
    print(''.join(map(str, r)))