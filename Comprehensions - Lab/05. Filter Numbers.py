print([

    i for i in range(int(input()), int(input()) + 1) if any([i % m == 0  for m in range(2, 11)])
])