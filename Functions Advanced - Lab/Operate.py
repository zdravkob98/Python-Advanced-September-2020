from functools import reduce

def operate (op, *args):
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
    }

    return reduce(operations[op], args)


print(operate("/", 1, 2, 3))
print(operate("/", 3, 4))
