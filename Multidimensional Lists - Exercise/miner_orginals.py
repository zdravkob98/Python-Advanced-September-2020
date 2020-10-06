def active(current_position, n):
    row = current_position[0]
    col = current_position[1]
    return 0 <= row < n and 0 <= col < n

def coal(n):
    count_coal = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'c':
                count_coal += 1
    return count_coal

def find_s(n):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 's':
                return (i, j)

n = int(input())

command = input().split()

matrix = []
for _ in range(n):
    matrix.append(input().split())

count_coal = coal(n)
coals = 0
flag = False

for comm in command:
    if comm == 'left':
        start_position = find_s(n)
        i = start_position[0]
        j = start_position[1]

        current_position = [i, j - 1]
        if active(current_position, n):
            row = current_position[0]
            col = current_position[1]
            if matrix[row][col] == 'c':
                coals += 1
                if count_coal == coals:
                    flag = True
                    break
            elif matrix[row][col] == 'e':
                flag = True
                break
            matrix[row][col] = matrix[i][j]
            matrix[i][j] = '*'

    elif comm == 'right':
        start_position = find_s(n)
        i = start_position[0]
        j = start_position[1]

        current_position = [i, j + 1]
        if active(current_position, n):
            row = current_position[0]
            col = current_position[1]
            if matrix[row][col] == 'c':
                coals += 1
                if count_coal == coals:
                    flag = True
                    break
            elif matrix[row][col] == 'e':
                flag = True
                break
            matrix[row][col] = matrix[i][j]
            matrix[i][j] = '*'


    elif comm == 'up':
        start_position = find_s(n)
        i = start_position[0]
        j = start_position[1]

        current_position = [i - 1, j]
        if active(current_position, n):
            row = current_position[0]
            col = current_position[1]
            if matrix[row][col] == 'c':
                coals += 1
                if count_coal == coals:
                    flag = True
                    break
            elif matrix[row][col] == 'e':
                flag = True
                break
            matrix[row][col] = matrix[i][j]
            matrix[i][j] = '*'
            start_position = matrix[row][col]


    elif comm == 'down':
        start_position = find_s(n)
        i = start_position[0]
        j = start_position[1]

        current_position = [i + 1, j]
        if active(current_position, n):
            row = current_position[0]
            col = current_position[1]
            if matrix[row][col] == 'c':
                coals += 1
                if count_coal == coals:
                    flag = True
                    break
            elif matrix[row][col] == 'e':
                flag = True
                break
            matrix[row][col] = matrix[i][j]
            matrix[i][j] = '*'

if flag == True:
    if count_coal == coals:
        print(f'You collected all coals! ({row}, {col})')
    else:
        print(f'Game over! ({row}, {col})')
else:
    print(f'{count_coal - coals} coals left. ({row}, {col})')