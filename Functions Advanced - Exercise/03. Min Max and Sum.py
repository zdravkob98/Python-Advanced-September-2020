def min_res(*args):
    min_result = min(*args)
    return min_result


def max_res(*args):
    max_result = max(*args)
    return max_result


def sum_res(*args):
    sum_result = sum(*args)
    return sum_result


n = [int(x) for x in input().split()]

print(f'The minimum number is {min_res(n)}')
print(f'The maximum number is {max_res(n)}')
print(f'The sum number is: {sum_res(n)}')