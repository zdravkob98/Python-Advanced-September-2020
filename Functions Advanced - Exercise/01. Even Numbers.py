# def filter_even_number(numbers):
#     result = list(filter(lambda x: x % 2 == 0, numbers))
#     return result
#
# numbers = [int(x) for x in input().split()]
# print(filter_even_number(numbers))

# numbers = [int(x) for x in input().split()]
# result = list(filter(lambda x : x % 2 == 0, numbers))
# print(result)


def filter_even_number(*args):
    result = list(filter(lambda x: x % 2 == 0, numbers))
    return result

numbers = [int(x) for x in input().split()]
print(filter_even_number(numbers))