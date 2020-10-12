def find_p(matrix, rows):
    for i in range(rows):
        for j in range(rows):
            if matrix[i][j] == 'P':
                return i, j


def is_valid(rows, next_pos):
    flag = False
    row = next_pos[0]
    col = next_pos[1]
    if 0 <= row < rows and 0 <= col < rows:
        flag = True
    else:
        flag = False
    return flag


def move(valid, matrix, next_pos, string, i, j):
    if valid:
        if matrix[next_pos[0]][next_pos[1]] != '-':
            string += matrix[next_pos[0]][next_pos[1]]
        matrix[next_pos[0]][next_pos[1]] = 'P'
        matrix[i][j] = '-'
    else:
        string = string[:-1]
    return string


string = input()
rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([x for x in input()])

count_command = int(input())

for _ in range(count_command):
    command = input()
    current_position = find_p(matrix, rows)
    i = current_position[0]
    j = current_position[1]

    if command == 'up':
        next_pos = (i - 1, j)
        valid = is_valid(rows, next_pos)
        string = move(valid, matrix, next_pos, string, i, j)

    elif command == 'down':
        next_pos = (i + 1, j)
        valid = is_valid(rows, next_pos)
        string = move(valid, matrix, next_pos, string, i, j)

    elif command == 'left':
        next_pos = (i, j - 1)
        valid = is_valid(rows, next_pos)
        string = move(valid, matrix, next_pos, string, i, j)

    elif command == 'right':
        next_pos = (i, j + 1)
        valid = is_valid(rows, next_pos)
        string = move(valid, matrix, next_pos, string, i, j)

print(string)
for row in matrix:
    print(''.join(map(str, row)))
