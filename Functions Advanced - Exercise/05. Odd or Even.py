def odd_even(numbers, command):
    even = sum(filter(lambda x: x % 2 == 0 , numbers)) * len(numbers)
    odd = sum(filter(lambda x: x % 2 != 0, numbers)) * len(numbers)

    if command == 'Odd':
        print(odd)
    if command == 'Even':
        print(even)

command = input()
numbers = [int(x) for x in input().split()]

odd_even(numbers, command)