n = int(input())

matrix = [[int(x) for x in input().split(' ')] for _ in range(n)]

while True:
    token = input().split()
    command = token[0]
    if command == 'END':
        break

    row = int(token[1])
    col = int(token[2])
    value = int(token[3])

    if 0 <= row < n and 0 <= col < n:

        if command == 'Subtract':
            matrix[row][col] -= value
        elif command == 'Add':
            matrix[row][col] += value
    else:
        print("Invalid coordinates")

[print(' '.join(map(str, row))) for row in matrix]