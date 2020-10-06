def sort(*args):
    result = sorted(numbers)
    return result

numbers = [int(x) for x in input().split()]

print(sort(numbers))
