def func_executor (*args):
    result = []
    for el in args:
        fuction = el[0]
        arguents = el[1]
        result.append(fuction(*arguents))
    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2



print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
