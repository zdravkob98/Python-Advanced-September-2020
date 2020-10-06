def find_biggest(numbers):
    positive = sum(filter(lambda x: x >= 0, numbers))
    negative = sum(filter(lambda x: x <= 0, numbers))

    print(negative)
    print(positive)

    if abs(positive) > abs(negative):
        print("The positives are stronger than the negatives")

    else:
        print("The negatives are stronger than the positives")



numbers = [int(x) for x in input().split()]

find_biggest(numbers)