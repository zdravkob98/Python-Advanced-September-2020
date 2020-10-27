words = input()

try:
    times = int(input())
    print(words * times)
except ValueError:
    print('Variable times must be an integer')