def create_fibonacci(count):
    fibonacci = []
    n1 = 0
    n2 = 1

    fibonacci.append(n1)
    fibonacci.append(n2)
    for _ in range(count - 2):
        result = n1 + n2
        n1 = n2
        n2 = result
        fibonacci.append(n2)

    return fibonacci