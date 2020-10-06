from _collections import deque

rows, cols = [int(x) for x in input().split()]

text = deque(input())

matrix = []

for i in range(rows):
    matrix.append(deque())
    for j in range(cols):
        element = text.popleft()
        if i % 2 == 0:
            matrix[i].append(element)
        else:
            matrix[i].appendleft(element)
        text.append(element)


for i in range(len(matrix)):
    print(''.join(matrix[i]))