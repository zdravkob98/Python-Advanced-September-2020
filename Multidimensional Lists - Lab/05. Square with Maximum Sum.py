rols, cows = [int(x) for x in input().split(', ')]

matrix = []
for i in range(rols):
    matrix.append(list(map(int, input().split(', '))))
#def for make matrix

biggest_sum = 0
a = ()
b = ()

for i in range(rols - 1):
    for j in range(cows - 1):
        sum = matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
        if sum > biggest_sum:
            biggest_sum = sum

            a = (matrix[i][j], matrix[i][j + 1] )
            b = (matrix[i + 1][j], matrix[i + 1][j + 1])
        #def for find the biggest


print(f'{a[0]} {a[1]}')
print(f'{b[0]} {b[1]}')
print(biggest_sum)
#def print
