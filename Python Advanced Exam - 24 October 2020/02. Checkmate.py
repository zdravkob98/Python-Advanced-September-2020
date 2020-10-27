def find_k (rows):
    for i in range(rows):
        for j in range(rows):
            if matrix[i][j] == 'K':
                return i, j

def find_q (rows):
    for i in range(rows):
        for j in range(rows):
            if matrix[i][j] == 'Q':
                return i, j

def q_attack (queen, rows):
    row = queen[0]
    col = queen[1]
    flag = False
    check1 = True
    check2 = True
    check3 = True
    check4 = True
    check5 = True
    check6 = True
    check7 = True
    check8 = True

    for i in range(1, rows):

        #up
        if 0 <= row + i < rows and 0 <= col < rows and check1:
            if matrix[row + i][col] == 'Q':
                check1 = False
            if matrix[row + i][col] == '*':
                check1 = False
            if matrix[row + i][col] == 'K':
                flag = True
                break
        #down
        if 0 <= row - i< rows and 0 <= col < rows and check2:
            if matrix[row - i][col] == 'Q':
                check2 = False
            if matrix[row - i][col] == '*':
                check2 = False
            if matrix[row - i][col] == 'K':
                flag = True
                break
        #right
        if 0 <= row < rows and 0 <= col + i < rows and check3:
            if matrix[row][col + i] == 'Q':
                check3 = False
            if matrix[row][col + i] == '*':
                check3 = False
            if matrix[row][col + i] == 'K':
                flag = True
                break
        # left
        if 0 <= row < rows and 0 <= col - i < rows and check4:
            if matrix[row][col - i] == 'Q':
                check4 = False
            if matrix[row][col - i] == '*':
                check4 = False
            if matrix[row][col - i] == 'K':
                flag = True
                break
        #diagonals up left
        if 0 <= row - i< rows and 0 <= col -i < rows and check5:
            if matrix[row - i][col - i] == 'Q':
                check5 = False
            if matrix[row - i][col - i] == '*':
                check5 = False
            if matrix[row - i][col - i] == 'K':
                flag = True
                break
        #diagonals up right
        if 0 <= row - i< rows and 0 <= col +i < rows and check6:
            if matrix[row - i][col + i] == 'Q':
                check6 = False
            if matrix[row - i][col + i] == '*':
                check6 = False
            if matrix[row - i][col + i] == 'K':
                flag = True
                break
        #diagonals down left
        if 0 <= row + i< rows and 0 <= col -i< rows and check7:
            if matrix[row + i][col - i] == 'Q':
                check7 = False
            if matrix[row + i][col - i] == '*':
                check7 = False
            if matrix[row + i][col - i] == 'K':
                flag = True
                break
        #diagonals down right
        if 0 <= row + i < rows and 0 <= col + i < rows and check8:
            if matrix[row + i][col + i] == 'Q':
                check8 = False
            if matrix[row + i][col + i] == '*':
                check8 = False
            if matrix[row + i][col + i] == 'K':
                flag = True
                break
    return flag

rows = 8
matrix = []

for i in range(rows):
    matrix.append(input().split())

attack = []

while True:
    king = find_k(rows)
    queen = find_q(rows)
    if queen is None:
        break
    elif q_attack(queen, rows):
        attack.append(list(queen))
    matrix[queen[0]][queen[1]] = '*'

if attack:
    for e in attack:
        print(e)
else:
    print("The king is safe!")