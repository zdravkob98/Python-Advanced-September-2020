from _collections import defaultdict

dict = defaultdict(int)
numbers = map(float, input().split(' '))

for n in numbers:
    dict[n] += 1

for k,v in dict.items():
    print(f'{k} - {v} times')