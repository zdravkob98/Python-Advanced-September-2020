rows, cols = [int(x) for x in input().split()]

matrix = [input().split() for i in range(rows)]

command = input()
while command != 'END':
    token = command.split()
    if len(token) == 5:
        swap = token[0]
        row1 = int(token[1])
        col1 = int(token[2])
        row2 = int(token[3])
        col2 = int(token[4])
        if swap == 'swap' and row1 <= rows and col1 <= cols and row2 <= rows and col2 <= cols:
            element = matrix[row1][col1]
            matrix[row1][col1] = matrix[row2][col2]
            matrix[row2][col2] = element
            for i in range(len(matrix)):
                print(' '.join(matrix[i]))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")

    command = input()

