rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]

first_diagonal = 0
second_diagonal = 0

for i in range(rows):
    first_diagonal += matrix[i][i]
    second_diagonal += matrix[i][-i - 1]

# for i in range(rows):
#     first_diagonal += matrix[i][i]
# for i in range(rows, 0, -1):
#     second_diagonal += matrix[i - 1][-i]



print(abs(first_diagonal - second_diagonal))