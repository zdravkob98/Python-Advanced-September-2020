from itertools import chain
rows, cols = [int(x) for x in input().split()]

matrix = [list(map(int, input().split())) for _ in range(rows)]
second_matrix = []

biggest_sum = -999
best_num = []

for i in range(rows - 2):
    for j in range(cols - 2):

        for times in range(3):
            second_matrix.append(matrix[i + times][j:j + 3])
            if times == 2:
                sum_of_second_matrix = sum(chain(*second_matrix))
                if sum_of_second_matrix > biggest_sum:
                    biggest_sum = sum_of_second_matrix
                    best_num = second_matrix.copy()
                second_matrix.clear()


print(f'Sum = {biggest_sum}')
for i in range(len(best_num)):
    print(' '.join(map(str,best_num[i])))

