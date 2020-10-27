def is_valid (check_pos, rows):
    flag = False
    row = check_pos[0]
    col = check_pos[1]
    if 0 <= row < rows and 0 <= col < rows:
        flag = True
    return flag

def find_idx(bomb):
    n_one = ''
    n_two = ''
    for c in bomb[0]:
        if c.isdigit():
            n_one += c
    for c in bomb[1]:
        if c.isdigit():
            n_two += c
    return n_one, n_two

rows = int(input())

matrix = []

for i in range(rows):
    matrix.append([])
    for j in range(rows):
        matrix[i].append(' ')

n = int(input())
for _ in range(n):
    
    bomb = input().split()
    number = find_idx(bomb)
    r = int(number[0])
    c = int(number[1])
    matrix[r][c] = '*'

for i in range(rows):
    for j in range(rows):
        if matrix[i][j] == ' ':
            counter = 0
            #up
            check_pos = (i - 1, j)
            if is_valid(check_pos, rows):
                if matrix[check_pos[0]][check_pos[1]] == '*':
                    counter += 1
            #down
            check_pos = (i + 1, j)
            if is_valid(check_pos, rows):
                if matrix[check_pos[0]][check_pos[1]] == '*':
                    counter += 1
            #left
            check_pos = (i, j - 1)
            if is_valid(check_pos, rows):
                if matrix[check_pos[0]][check_pos[1]] == '*':
                    counter += 1
            #right
            check_pos = (i, j + 1)
            if is_valid(check_pos, rows):
                if matrix[check_pos[0]][check_pos[1]] == '*':
                    counter += 1
            #up left
            check_pos = (i - 1, j - 1)
            if is_valid(check_pos, rows):
                if matrix[check_pos[0]][check_pos[1]] == '*':
                    counter += 1
            #up rigth
            check_pos = (i - 1, j + 1)
            if is_valid(check_pos, rows):
                if matrix[check_pos[0]][check_pos[1]] == '*':
                    counter += 1
            #down left
            check_pos = (i + 1, j - 1)
            if is_valid(check_pos, rows):
                if matrix[check_pos[0]][check_pos[1]] == '*':
                    counter += 1
            #down right
            check_pos = (i + 1, j + 1)
            if is_valid(check_pos, rows):
                if matrix[check_pos[0]][check_pos[1]] == '*':
                    counter += 1

            matrix[i][j] = str(counter)

for r in matrix:
    print(' '.join(r))
