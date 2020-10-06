n = int(input())
# matrix = [input().split(', ') for _ in range(n)]
# flattened = [num for sublist in matrix for num in sublist]
# print(list(map(int, flattened)))

print([int(e) for _ in range(n) for e in input().split(', ')])