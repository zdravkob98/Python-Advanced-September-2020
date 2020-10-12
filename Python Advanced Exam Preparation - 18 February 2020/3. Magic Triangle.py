# def get_magic_triangle(n):
#     triangle = [[1], [1, 1]]
#     for row in range(2, n):
#         new_row = []
#         for col in range(row + 1):
#             if col - 1 < 0:
#                 new_row.append(1)
#             elif col >= len(triangle[row - 1]):
#                 new_row.append(1)
#             else:
#                 left = triangle[row-1][col-1]
#                 right = triangle[row-1][col]
#                 new_value = left + right
#                 new_row.append(new_value)
#         triangle.append(new_row)
#
#     return triangle

def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    for row in range(2, n):
        new_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                new_row.append(1)
            else:
                left = triangle[row-1][col-1]
                right = triangle[row-1][col]
                new_value = left + right
                new_row.append(new_value)
        triangle.append(new_row)

    return triangle
n = int(input())
print(get_magic_triangle(n))