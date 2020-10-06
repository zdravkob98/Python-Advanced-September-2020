from itertools import combinations

names = input().split(', ')
chairs = int(input())

perm = combinations(names, chairs)

for i in list(perm):
    print(', '.join(i))
