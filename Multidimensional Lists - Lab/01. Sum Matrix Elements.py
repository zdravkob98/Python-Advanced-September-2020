# from itertools import chain
#
# rows, cows = [int(x) for x in input().split(', ')]
# matrix = []
# [matrix.append([int(x) for x in input().split(', ')]) for i in range(rows)]
#
# total = sum(chain(*matrix))
# print(total)
# print(matrix)



from itertools import chain

rows, cows = [int(x) for x in input().split(', ')]

matrix = []


for i in range(rows):
    matrix.append([])
    n = [int(x) for x in input().split(', ')]
    for j in range(cows):
        matrix[i].append(n[j])
        #total += n[j]

total = sum(chain(*matrix))
print(total)
print(matrix)