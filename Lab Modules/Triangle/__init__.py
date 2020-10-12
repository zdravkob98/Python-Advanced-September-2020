def print_Triangle(size_n):
    for i in range(1, size_n + 1):
        print(' '.join(map(str, [p for p in range(1,i + 1)])))

    for i in range(size_n - 1 , 0, -1):
        print(' '.join(map(str, [p for p in range(1,i + 1)])))