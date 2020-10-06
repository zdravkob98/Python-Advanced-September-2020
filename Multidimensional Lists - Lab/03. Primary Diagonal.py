n = int(input())

matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split(' ')])

total = sum([matrix[i][i] for i in range(n)])
print(total)


n = int(input())

matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split(' ')])

total = 0
for i in range(n):
    total += matrix[i][i]
print(total)

